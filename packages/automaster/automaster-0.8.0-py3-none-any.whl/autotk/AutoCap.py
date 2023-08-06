import gzip
import hashlib
import os
import pickle
import re
import sys
import threading
import time
import tkinter as tk

import cv2
import numpy as np
from autotk.AutoCoreLite import logger, atom, _load_ico
from comtypes import GUID
from comtypes.persist import IPropertyBag
from pygrabber.dshow_graph import FilterGraph

import types


class VisionBase():
    # 把视觉算法类化,目前暂用于HDMI的算法汇集,未来迁移到AutoVision模块
    def __init__(self) -> None:
        super().__init__()

    def hash_func(self, hash_type="PHash"):
        if "AverageHash" == hash_type:
            hashFun = cv2.img_hash.AverageHash_create()
        elif "MarrHildrethHash" == hash_type:
            hashFun = cv2.img_hash.MarrHildrethHash_create()
        elif "RadialVarianceHash" == hash_type:
            hashFun = cv2.img_hash.RadialVarianceHash_create()
        elif "BlockMeanHash" == hash_type:
            hashFun = cv2.img_hash.BlockMeanHash_create()
        elif "ColorMomentHash" == hash_type:
            hashFun = cv2.img_hash.ColorMomentHash_create()
        elif "PHash" == hash_type:
            hashFun = cv2.img_hash.PHash_create()
        else:
            hashFun = cv2.img_hash.PHash_create()
        return hashFun

    def img_blur(self, img):
        img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        score = cv2.Laplacian(img2gray, cv2.CV_64F).var()
        return score


class Detect(VisionBase):
    def __init__(self) -> None:
        self.resize_appshow = 1
        self.InfoDict = {"ver": 1.0}  # version
        super().__init__()

    def init_data(self):
        self.hashFun = self.hash_func("PHash")  # hash函数初始化
        self.pkl_detect_exclude = {}  # set_pkl_detect() 检测不允许存在的特征,用于特征排除,例如是厂测画面 "./factory.pkl"
        self.pkl_detect = {}  # set_pkl_detect() 检测的特征
        self.pkl_black = {}  # get_pkl_black() 空载特征 BlackTag.pkl
        self.resize_tuple = None  # 因为仅是显示,固定resize的大小

        self.roi_conf = []  # 定义roi算法的截取参数,例如左上角的frame[0:50,0:200]
        self.roi_delmask = []  # 定义mask去除的区域截取参数,例如右上角的frame[0:40,-100:-1]
        self.load_other = {}  # 载入附件的other字典,用于auto_detect自驱动

    def read(self):
        print("Detect Class Base..")
        return False, None

    def frame_resize(self, frame, resize=None):
        if resize:
            img_h, img_w, _ = frame.shape
            resize_tuple = (int(img_w * resize), int(img_h * resize))
            frame = cv2.resize(frame, resize_tuple)
            return frame
        if not self.resize_tuple:
            img_h, img_w, _ = frame.shape
            self.resize_tuple = (int(img_w * 0.5), int(img_h * 0.5))
        frame = cv2.resize(frame, self.resize_tuple)
        return frame

    def jpg_load_check(self, fpath):
        if not os.path.exists(fpath):
            return False, f"NoFound [{fpath}]"
        try:
            _appendix = self.get_appendix(fpath)
            if _appendix:
                logger.debug(f"[tagfile]{fpath}")
                # print(_appendix)        # 开发调试用
                _ver = _appendix.pop("ver")
                _verlimit = self.InfoDict.get("ver", 0.0) + 1
                print(f"Version {_ver}[{_verlimit}]")
                if _ver > _verlimit:
                    return False, f"Version Error {_ver}[{_verlimit}]"
                _time = _appendix.pop("time")
                if time.time() <= _time:
                    return False, f"Feature Error \r\n[time]{_time}"
                self.pkl_detect = _appendix.pop("hash")
                self.load_other = _appendix
                if self.load_other:
                    logger.debug(f"Detect Addtion {list(self.load_other.keys())}")

                codestr = _appendix.get("code", "")
                try:
                    exec(codestr)
                except Exception as e:
                    print(f"[code]{e}")
                    return False, f"Feature Error \r\n[code]{e}"
                return True, ""
        except Exception as e:
            print(e)
        return False, f"Feature Error [{fpath}]"

    def set_pkl_detect(self, pkl_file, pkl_exclude=""):
        with open(pkl_file, 'rb') as l:
            self.pkl_detect = pickle.load(l)
        if pkl_exclude:
            _exclude_pkl_file = "./factory.pkl"
            if (os.path.exists(_exclude_pkl_file)):
                with open(_exclude_pkl_file, 'rb') as l:
                    self.pkl_detect_exclude = pickle.load(l)
        else:
            self.pkl_detect_exclude = {}

    def get_pkl_black(self, black_pkl="./BlackTag.pkl"):
        if not (os.path.exists(black_pkl)):
            logger.debug(f"NoFound {black_pkl} Auto..")
            sampledict = {"Black_0_0_0_0_0_0_0_0": np.zeros((1, 8), dtype=np.uint8)}
            with open(black_pkl, 'wb') as s:
                pickle.dump(sampledict, s, pickle.HIGHEST_PROTOCOL)
        if not self.pkl_black:
            with open(black_pkl, 'rb') as l:
                self.pkl_black = pickle.load(l)
        return self.pkl_black

    def auto_detect(self, dlimit=1, sample_pkl=None, exclude_pkl=None):
        result, frame, showframe = self.cap_detect_hash(dlimit, sample_pkl, exclude_pkl)
        if self.load_other and result:
            # print(self.load_other)
            if "roihash" in self.load_other:
                for r, s in self.load_other["roihash"].items():
                    result = False  # ROI 各个区的结果是And的逻辑
                    hashA = self.roihash(frame, r)
                    for name, hashB in s.items():
                        cmpValue = self.hashFun.compare(hashA, hashB)
                        if (cmpValue <= dlimit):
                            result = True
                            # print(name,cmpValue)
                            break
                    # print(r, s, result,hashA,cmpValue,dlimit)
                    if not result:  # ROI 各个区的结果是And的逻辑
                        break

        return result, frame, showframe

    def cap_detect_hash(self, dlimit=1, sample_pkl=None, exclude_pkl=None, debug=True):
        if not sample_pkl:
            sample_pkl = self.pkl_detect
        if not exclude_pkl:
            exclude_pkl = self.pkl_detect_exclude
        ret, frame = self.read()
        result = False
        showframe = self.frame_resize(frame, self.resize_appshow)
        if ret:
            if "delmask" in self.load_other:
                delmask = self.load_other["delmask"]
                frame = cv2.bitwise_and(frame, delmask)  # 附加的全局去除mask
                # cv2.imwrite("tmp.jpg", frame)
            hashA = self.hashFun.compute(frame)
            _min = 9999
            for name, hashB in sample_pkl.items():
                cmpValue = self.hashFun.compare(hashA, hashB)
                if cmpValue < _min:
                    _min = cmpValue
                if (cmpValue <= dlimit):
                    result = True
                    break
            msg = f"Min:{_min}"
            if exclude_pkl:
                for exname, exhashB in exclude_pkl.items():
                    excmpValue = self.hashFun.compare(hashA, exhashB)
                    if not excmpValue:
                        result = False
                        msg += " [exclude]"
                        break
            if debug:
                msg = f"{frame.shape} {msg}"
                if result:
                    cv2.putText(showframe, msg, (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                else:
                    cv2.putText(showframe, msg, (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        return result, frame, showframe

    def compute_taghash(self, img, sample_pkl, dlimit=3):
        try:
            hashA = self.hashFun.compute(img)
            for name, hashB in sample_pkl.items():
                cmpValue = self.hashFun.compare(hashA, hashB)
                if (cmpValue <= dlimit):
                    return True
        except:
            pass
        return False

    def isnot_black(self):
        ret, frame = self.read()
        if ret:
            if not self.compute_taghash(frame, self.pkl_black, 3):
                return True, frame
        return False, frame

    def frame_is_black(self, frame):
        return self.compute_taghash(frame, self.pkl_black, 3)

    def loop_time_pkl(self, gen_pkl, timelen=30):
        '''
        固定时长的特征制作
        '''
        self.get_pkl_black()  # 刷新 self.pkl_black
        frames = {}
        other_dict = {}
        _sample = {}
        logger.debug(f"Start Feature {gen_pkl}..")
        btime = time.time()
        etime = 0
        while etime < timelen:
            ret, frame = self.read()
            isblack = self.frame_is_black(frame)
            if isblack:
                print("Capture Black 检测到非法画面")
            else:
                if not _sample:
                    frames["start"] = frame
                else:
                    frames["end"] = frame
                self.sample_add(_sample, frame, "Factory", other_dict)
            cv2.waitKey(100)
            etime = time.time() - btime
            print(f"Elptime:{etime:.2f}")
        etime = time.time() - btime
        # with open(gen_pkl, 'wb') as s:
        #     pickle.dump(_sample, s, pickle.HIGHEST_PROTOCOL)
        # logger.debug(f"Elptime:{etime:.2f} {gen_pkl}")
        self.make_sample_jpg(frames, _sample, gen_pkl.replace(".pkl", ".jpg"), other_dict)
        logger.debug(f"Elptime:{etime:.2f}")

    def loop_generate_pkl(self, gen_pkl, timeout=30):
        '''
        在播放特征的循环中,制作特征,特征不新增的时候自动停止,超时也停止
        '''
        self.get_pkl_black()  # 刷新 self.pkl_black
        other_dict = {}
        _sample = {}
        _log = []
        frames = {}
        logger.debug(f"Start Feature {gen_pkl}..")
        btime = time.time()
        while len(_log) < 20:
            ret, frame = self.read()
            isblack = self.frame_is_black(frame)
            if isblack:
                print("Capture Black 检测到非法画面")
            else:
                if not _sample:
                    frames["start"] = frame
                self.sample_add(_sample, frame, "Feature", other_dict)
                _log.append(len(_sample))
            cv2.waitKey(100)
        etime = time.time() - btime
        while etime < timeout:
            ret, frame = self.read()
            isblack = self.frame_is_black(frame)
            if isblack:
                print("Capture Black 检测到非法画面")
            else:
                frames["end"] = frame
                self.sample_add(_sample, frame, "Feature", other_dict)
                _log.append(len(_sample))
                _log.pop(0)
            cv2.waitKey(100)
            etime = time.time() - btime
            if _log[0] == _log[-1]:
                break
            print(f"Feature[{_log[-1]}]")
        etime = time.time() - btime
        # with open(gen_pkl, 'wb') as s:
        #     pickle.dump(_sample, s, pickle.HIGHEST_PROTOCOL)
        # logger.debug(f"Elptime:{etime:.2f} Feature[{_log[-1]}] {gen_pkl} ")
        # print(f"Elptime:{etime:.2f} Feature[{_log[-1]}] {gen_pkl} ")
        self.make_sample_jpg(frames, _sample, gen_pkl.replace(".pkl", ".jpg"), other_dict)
        print(f"Elptime:{etime:.2f} Feature[{_log[-1]}]")

    def loop_black_add(self, black_pkl="BlackTag.pkl", ):
        '''
        在播放特征的循环中,制作特征,特征不新增的时候自动停止
        '''
        _sample = self.get_pkl_black(black_pkl)
        _log = []
        frames = {}
        other_dict = {}
        logger.debug(f"Start Sample {black_pkl}..")
        while len(_log) < 10:
            ret, frame = self.read()
            self.sample_add(_sample, frame, "Black", other_dict)
            _log.append(len(_sample))
            frames[_log[-1]] = frame
            cv2.waitKey(100)
        while not _log[0] == _log[-1]:
            ret, frame = self.read()
            self.sample_add(_sample, frame, "Black", other_dict)
            _log.append(len(_sample))
            frames[_log[-1]] = frame
            _log.pop(0)
            cv2.waitKey(100)
        # with open(black_pkl, 'wb') as s:
        #     pickle.dump(_sample, s, pickle.HIGHEST_PROTOCOL)
        # logger.debug(f"Finish Sample[{_log[-1]}] {black_pkl}")
        self.make_sample_jpg(frames, _sample, black_pkl.replace(".pkl", ".jpg"), other_dict)
        logger.debug(f"Finish Sample[{_log[-1]}]")

    def add_roihash(self, frame, other_dict):
        if not "roihash" in other_dict:
            other_dict["roihash"] = {}  # 调用是设定算法名称,并初始化相关参数
            for r in self.roi_conf:
                other_dict["roihash"][r] = {}
        _dict = other_dict["roihash"]
        for r, s in _dict.items():
            _hash = self.roihash(frame, r)
            tip = "ROI"
            for v in _hash[0]:
                tip += "_%03d" % v
            s[tip] = _hash

    def roihash(self, frame, r):
        _roi = [int(i) for i in r.split(",")]
        roi_frame = frame[_roi[0]:_roi[1], _roi[2]:_roi[3]]
        _hash = self.hashFun.compute(roi_frame)
        return _hash

    def sample_add(self, sampledict, frame, tip, other_dict):
        if self.roi_delmask:
            mask = self.make_delmask(frame)
            if not isinstance(mask, bool):
                frame = cv2.bitwise_and(frame, mask)  # 附加的全局去除mask
                other_dict["delmask"] = mask
        hashA = self.hashFun.compute(frame)
        for v in hashA[0]:
            tip += "_%03d" % v
        # print(hashA)
        sampledict[tip] = hashA
        if self.roi_conf:
            self.add_roihash(frame, other_dict)  # 附加的算法.........
        return sampledict

    def load_codepatch(self, fpath=None):
        if fpath:
            self.fcodepath = fpath
        if os.path.exists(self.fcodepath):
            print(f"[CodePath]{self.fcodepath}")
            with open(self.fcodepath, "r", encoding="utf-8") as f:
                self.InfoDict["code"] = f.read()

    def data_combine(self, sampledict, other_dict):
        self.load_codepatch()
        self.InfoDict["hash"] = sampledict
        self.InfoDict["time"] = time.time()
        all_dict = dict(self.InfoDict, **other_dict)
        print(f"[Combine]{all_dict.keys()}")
        return all_dict

    def make_sample_jpg(self, frames, sampledict, fname, other_dict):
        showframe = self.img_combine(frames)
        # all_dict = dict({"hash": sampledict}, **other_dict)
        all_dict = self.data_combine(sampledict, other_dict)
        ret = self.set_appendix(all_dict, showframe, fname)
        msg = f"JPG Sample {fname} {ret}"
        print(msg)
        logger.debug(msg)

    def make_delmask(self, frame):
        if self.roi_delmask:
            mask = np.ones(frame.shape, np.uint8) * 255
            for r in self.roi_delmask:
                _roi = [int(i) for i in r.split(",")]
                mask[_roi[0]:_roi[1], _roi[2]:_roi[3]] = 0
            return mask
        return False

    def set_appendix(self, datadict, frame, fname, ftype=".jpg"):
        try:
            ret, img_byte = cv2.imencode(ftype, frame)
            if ret:
                if not ftype in fname:
                    fname += ftype
                data_byte = gzip.compress(pickle.dumps(datadict))
                img_len = len(img_byte)
                len_byte = int(img_len).to_bytes(length=8, byteorder='big', signed=True)
                f_byte = img_byte.tobytes() + data_byte + len_byte
                md5_byte = hashlib.md5(f_byte).digest()
                with open(fname, "wb") as f:
                    f.write(f_byte + md5_byte)
                return True
        except Exception as e:
            print(e)
        return False

    def get_appendix(self, fimg):
        with open(fimg, "rb") as f:
            all_byte = f.read()
        f_byte = all_byte[:-16]
        md5_now = hashlib.md5(f_byte).digest()
        md5_byte = all_byte[-16:]
        if md5_byte == md5_now:
            len_byte = f_byte[-8:]
            img_len = int().from_bytes(len_byte, byteorder='big', signed=True)
            if img_len > 0:
                img_byte = f_byte[:img_len]
                data_byte = f_byte[img_len:-8]
                datadict = pickle.loads(gzip.decompress(data_byte))
                return datadict
        return ""

    def _appendix_change(self, fimg, update_dict, remove=[]):
        with open(fimg, "rb") as f:
            all_byte = f.read()
        f_byte = all_byte[:-16]
        md5_now = hashlib.md5(f_byte).digest()
        md5_byte = all_byte[-16:]
        if md5_byte == md5_now:
            len_byte = f_byte[-8:]
            img_len = int().from_bytes(len_byte, byteorder='big', signed=True)
            if img_len > 0:
                data_byte = f_byte[img_len:-8]
                datadict = pickle.loads(gzip.decompress(data_byte))
                print(datadict)
                datadict = dict(datadict, **update_dict)
                if remove:
                    for r in remove:
                        datadict.pop(r)
                print(datadict)
                data_byte = gzip.compress(pickle.dumps(datadict))
                f_byte = f_byte[:img_len] + data_byte + len_byte
                md5_byte = hashlib.md5(f_byte).digest()
                with open(fimg, "wb") as f:
                    f.write(f_byte + md5_byte)
                return True
        return ""

    def img_combine(self, imgs={}, type=1):
        h_max = 0
        w_list = []
        w_start = []
        w_combine = 0
        f_list = []
        tips = []
        for n, f in imgs.items():
            tips.append(n)
            h, w = f.shape[:2]
            if h > h_max:
                h_max = h
            w_start.append(w_combine)
            w_combine += w
            w_list.append(w_combine)
            f_list.append(f)
        # print(tips)
        combine_frame = np.zeros((h_max, w_combine, 3), dtype="uint8")
        for i, frame in enumerate(f_list):
            combine_frame[0:h_max, w_start[i]:w_list[i]] = frame
        return combine_frame


# 本来建立来做launcher检测的,但发觉CapClase能够适配小USB普通采集卡,暂不使用.................
# class CapClassCV(Detect):
#
#     def __init__(self, capId, capSet=None) -> None:
#         '''
#         capId : int or str(int) or VID&PID eg:VEN_8888&DEV_8581
#         capSet :height_width  cap.set(3, 1280), cap.set(4, 720)
#         '''
#         try:
#             if isinstance(capId, str):
#                 if "&" in capId:
#                     capId = self.get_first_vpid(capId)
#                 else:
#                     capId = int(capId)
#             self.capId = capId
#             print(f"CapId={self.capId}")
#
#             self.capSet = capSet.upper() if capSet else ""
#             self.init_data()
#         except Exception as e:
#             print(e.__traceback__.tb_lineno)
#             print(e)
#
#         super().__init__()
#
#     def get_first_vpid(self, vpid):
#         pattern = re.compile(r"#(\w+_\w+&\w+_\w+)&")
#         filter_enumerator = FilterGraph().system_device_enum.system_device_enum.CreateClassEnumerator(
#             GUID("{860BB310-5D01-11d0-BD3B-00A0C911CE86}"), 0)
#         moniker, count = filter_enumerator.Next(1)
#         _idx = 0
#         while count > 0:
#             property_bag = moniker.BindToStorage(0, 0, IPropertyBag._iid_).QueryInterface(IPropertyBag)
#             _devpath = property_bag.Read("DevicePath", pErrorLog=None)
#             _name = property_bag.Read("FriendlyName", pErrorLog=None)
#             _vpid = None
#             list = pattern.findall(_devpath)
#             if list:
#                 _vpid = list[0].upper()
#                 if _vpid == vpid:
#                     logger.debug(f'[AutoID]{_name}')
#                     return _idx
#             moniker, count = filter_enumerator.Next(1)
#             _idx += 1
#         return 0
#
#     def init_data(self):
#         super().init_data()
#         self.cvcap = cv2.VideoCapture(self.capId, cv2.CAP_DSHOW)
#         self.resize_appshow = None  # APP主界面显示的缩放尺寸
#         self.resize_tuple = None  # 因为仅是显示,固定resize的大小
#         if self.capSet:
#             _w = 1280
#             _h = 720
#             self.cvcap.set(3, _w)
#             self.cvcap.set(4, _h)
#             self.resize_tuple = (1280, 720)
#
#     def grab(self):
#         return self.cvcap.grab()
#
#     def isOpened(self):
#         return self.cvcap.isOpened()
#
#     def read(self):
#         return self.cvcap.read()
#
#     def release(self):
#         return self.cvcap.release()
#
#     def cap_resize(self):
#         ret, frame = self.read()
#         self.frame_resize(frame)
#
#     def frame_resize(self, frame, resize=None):
#         if resize:
#             img_h, img_w, _ = frame.shape
#             resize_tuple = (int(img_w * resize), int(img_h * resize))
#             frame = cv2.resize(frame, resize_tuple)
#             return frame
#         if not self.resize_tuple:
#             img_h, img_w, _ = frame.shape
#             self.resize_tuple = (int(img_w * 0.5), int(img_h * 0.5))
#         frame = cv2.resize(frame, self.resize_tuple)
#         return frame


class CapClass(Detect):

    def __init__(self, capId, capSet=None, tagfile="") -> None:
        '''
        capId : int or str(int) or VID&PID eg:VEN_8888&DEV_8581
        capSet : f'4K_width_rate_tpye' eg: 4K_4096_60_YUY2
        capSet : f'2K_width_rate_tpye' eg: 4K_4096_60_YUY2
        para_dict : eg:{"roihash":[0,50,0,200]}
        '''
        super().__init__()

        if tagfile and os.path.exists(tagfile):
            _appendix = self.get_appendix(tagfile)
            capId = _appendix.get("capId", capId)
            capSet = _appendix.get("capSet", capSet)
            # print(capId)
            # self._appendix_change(tagfile,{"time":time.time()},["capId"])
        self.InfoDict = {"ver": 1.0}  # auto cap config,+verlimit
        self.graph = FilterGraph()
        self.devs_info = self.get_devs()
        self.exsit_vpid=False
        if isinstance(capId, str):
            if "&" in capId:
                self.InfoDict["capId"] = capId
                capId = self.get_first_vpid(capId)
            else:
                capId = int(capId)
        self.capId = capId
        print(f"CapId={self.capId}")
        self.graph.add_video_input_device(self.capId)
        self.dev = self.graph.get_input_device()
        self.graph.add_sample_grabber(self.img_capback)
        self.graph.add_null_render()
        self.capSet = capSet.upper() if capSet else ""
        if "4K" in self.capSet:
            self.InfoDict["capSet"] = self.capSet
            self.dev.set_format(self.get_4k_format(self.capSet))
            self.resize_appshow = 0.25  # APP主界面显示的缩放尺寸
        elif "2K" in self.capSet:
            self.InfoDict["capSet"] = self.capSet
            self.dev.set_format(self.get_2k_format(self.capSet))
            self.resize_appshow = 0.25  # APP主界面显示的缩放尺寸
        elif "1K" in self.capSet:
            self.InfoDict["capSet"] = self.capSet
            self.dev.set_format(self.get_1k_format(self.capSet))
            self.resize_appshow = 0.5  # APP主界面显示的缩放尺寸
        else:
            self.format_str = "Auto"
            self.dev.set_format(0)
        self.graph.prepare_preview_graph()
        self.init_data()

    def get_4k_format(self, my4k=""):
        formats = self.dev.get_formats()
        now_idx = 0
        for f in formats:
            # print(f)
            _w = f.get('width', 0)
            if _w >= 3840:
                _info = f"4K_{int(_w)}_{int(f.get('min_framerate', ''))}_{f.get('media_type_str', '')}"
                if my4k:
                    cmplen = len(my4k)
                    if _info[:cmplen] == my4k:
                        now_idx = f.get("index", 0)
                        logger.debug(f"[Format]{_info}[{my4k}]={now_idx}")
                        self.format_str = f"[Format]{_info}[{my4k}]={now_idx}"
                        break
                else:
                    now_idx = f.get("index", 0)
                    break
        return now_idx

    def get_2k_format(self, my4k=""):
        formats = self.dev.get_formats()
        now_idx = 0
        for f in formats:
            _w = f.get('width', 0)
            if 3840 > _w >= 2560:
                _info = f"2K_{int(f.get('height', 0))}_{int(f.get('min_framerate', ''))}_{f.get('media_type_str', '')}"
                if my4k:
                    cmplen = len(my4k)
                    if _info[:cmplen] == my4k:
                        now_idx = f.get("index", 0)
                        logger.debug(f"[Format]{_info}[{my4k}]={now_idx}")
                        self.format_str = f"[Format]{_info}[{my4k}]={now_idx}"
                        break
                else:
                    now_idx = f.get("index", 0)
                    break
        return now_idx

    def get_1k_format(self, my4k=""):
        formats = self.dev.get_formats()
        now_idx = 0
        for f in formats:
            _w = f.get('width', 0)
            if 2560 > _w >= 1024:
                _info = f"1K_{int(f.get('height', 0))}_{int(f.get('min_framerate', ''))}_{f.get('media_type_str', '')}"
                print(_info)
                if my4k:
                    cmplen = len(my4k)
                    if _info[:cmplen] == my4k:
                        now_idx = f.get("index", 0)
                        logger.debug(f"[Format]{_info}[{my4k}]={now_idx}")
                        self.format_str = f"[Format]{_info}[{my4k}]={now_idx}"
                        break
                else:
                    now_idx = f.get("index", 0)
                    break
        return now_idx

    def get_first_vpid(self, vpid):
        for i, d in self.devs_info.items():
            if d.get("ID", "") == vpid:
                logger.debug(f'[AutoID]{d.get("Name", "")}')
                self.exsit_vpid=True
                return i
        return 0

    def get_devs(self):
        pattern = re.compile(r"#(\w+_\w+&\w+_\w+)&")
        filter_enumerator = self.graph.system_device_enum.system_device_enum.CreateClassEnumerator(
            GUID("{860BB310-5D01-11d0-BD3B-00A0C911CE86}"), 0)
        moniker, count = filter_enumerator.Next(1)
        dev_info = {}
        _idx = 0
        while count > 0:
            try:
                property_bag = moniker.BindToStorage(0, 0, IPropertyBag._iid_).QueryInterface(IPropertyBag)
                _devpath = property_bag.Read("DevicePath", pErrorLog=None)
                _name = property_bag.Read("FriendlyName", pErrorLog=None)
                _vpid = None
                list = pattern.findall(_devpath)
                if list:
                    _vpid = list[0].upper()
                dev_info[_idx] = {"ID": _vpid, "DevicePath": _devpath, "Name": _name}
            except:
                pass
            moniker, count = filter_enumerator.Next(1)
            _idx += 1
        return dev_info

    def get_formats(self):
        formats = self.dev.get_formats()
        _show = {}
        for f in formats:
            # print(f)
            _w = f.get('width', 0)
            if _w:
                _info = f"({_w},{f.get('height', 0)}) Rate[{f.get('min_framerate', 0 - 1)},{f.get('max_framerate', -1)}]{f.get('media_type_str', '')}"
                _show[f.get("index", None)] = _info
                print(f.get("index", None), _info)
        return _show

    def set_roihash_list(self, roi, add=True):  # 制作特征的时候使用的roi设定
        if roi in self.roi_conf:
            if not add:
                self.roi_conf.remove(roi)
        else:
            if add:
                self.roi_conf.append(roi)

    def set_roimask_list(self, roi, add=True):  # 制作特征的时候使用的roi设定
        if roi in self.roi_delmask:
            if not add:
                self.roi_delmask.remove(roi)
        else:
            if add:
                self.roi_delmask.append(roi)

    def init_data(self):
        super().init_data()
        self.fcodepath = "./code_patch.py"
        self.resize_tuple = None  # 因为仅是显示,固定resize的大小
        # if self.capSet:
        #     self.resize_tuple =
        self.graph.run()
        self.image_grabbed = None
        self.image_done = threading.Event()

    def imshow_float(self, tip, frame, resize=None):
        if not resize:
            resize = self.resize_appshow
        frame = self.frame_resize(frame, resize)
        cv2.imshow(tip, frame)

    def img_capback(self, image):
        self.image_grabbed = np.flip(image, 2)
        # self.image_grabbed = cv2.flip(image, 0)
        self.image_grabbed = cv2.cvtColor(self.image_grabbed, cv2.COLOR_RGB2BGR)
        self.image_done.set()

    def grab(self):
        pass

    def isOpened(self):
        return True

    def read(self):
        try:
            self.graph.grab_frame()
            self.image_done.wait(1000)
        except:
            return False, None
        return True, self.image_grabbed

    def release(self):
        # self.graph.stop()
        pass

    def cap_resize(self):
        ret, frame = self.read()
        self.frame_resize(frame)

    def frame_resize(self, frame, resize=None):
        if resize:
            img_h, img_w, _ = frame.shape
            resize_tuple = (int(img_w * resize), int(img_h * resize))
            frame = cv2.resize(frame, resize_tuple)
            return frame
        if not self.resize_tuple:
            img_h, img_w, _ = frame.shape
            self.resize_tuple = (int(img_w * 0.5), int(img_h * 0.5))
        frame = cv2.resize(frame, self.resize_tuple)
        return frame


class CapGUI():
    def initdata(self):
        sys.stdout = self
        self.fdir = "./"
        self.do_case = 0  # 切Case
        self.debug_print = {}  # 用于去除重复打印

    def __init__(self, master):
        self.initdata()
        self.mainwin = master
        self.init_gui(master)
        sys.stdout = self
        self.debug_print = {}  # 用于去除重复打印
        # self.CapC = CapClassCV("VID_534D&PID_2109", "4k")
        self.CapC = CapClass("VID_534D&PID_2109", "1k")
        # self.CapC = CapClass("VEN_8888&DEV_8581", "4k")
        # print(self.CapC.devs_info)

        self.loop()

    def flush(self):
        pass

    def write(self, line):
        self.text.insert(0.0, f"{line}")
        self.text.update()

    def do_auto(self):
        fpkl = self.str_name.get()
        tlen = self.int_time.get()
        if fpkl and tlen > 0:
            self.b_doauto["state"] = "disabled"
            self.b_dotime["state"] = "disabled"
            self.do_case = 1
            print(f"开始循环特征制作(超时{tlen}秒): {fpkl}")

    def do_timelen(self):
        fpkl = self.str_name.get()
        tlen = self.int_time.get()
        if fpkl and tlen > 0:
            self.b_doauto["state"] = "disabled"
            self.b_dotime["state"] = "disabled"
            self.do_case = 2
            print(f"开始固定时长({tlen}秒)制作: {fpkl}")

    def loop(self):
        if self.do_case:
            cv2.destroyAllWindows()
            fname = f"{self.fdir}{self.str_name.get()}.pkl"
            flen = self.int_time.get()
            if self.do_case == 1:
                self.CapC.loop_generate_pkl(gen_pkl=fname, timeout=flen)
            elif self.do_case == 2:
                self.CapC.loop_time_pkl(gen_pkl=fname, timelen=flen)
            else:
                pass
            print(f"完成特征文件制作: {self.fdir}{self.str_name.get()}.jpg")
            self.do_case = 0
            self.b_doauto["state"] = "normal"
            self.b_dotime["state"] = "normal"
        else:
            if self.CapC.isOpened():
                ret, frame = self.CapC.read()
                tip = f"Viewer[{self.CapC.capId}] {frame.shape} Resize:{self.CapC.resize_appshow}"
                self.CapC.imshow_float(tip, frame)
                # frame = self.CapC.frame_resize(frame,resize=0.25)
                # showframe = self.CapC.frame_resize(frame, resize=0.5)
                # cv2.imshow(tip, showframe)
                if self.CapC.roi_conf:
                    for r in self.CapC.roi_conf:
                        _roi = [int(i) for i in r.split(",")]
                        roi_frame = frame[_roi[0]:_roi[1], _roi[2]:_roi[3]]
                        self.CapC.imshow_float(r, roi_frame)
                        # cv2.imshow(r, roi_frame)
                if self.CapC.roi_delmask:
                    for r in self.CapC.roi_delmask:
                        _roi = [int(i) for i in r.split(",")]
                        roi_frame = frame[_roi[0]:_roi[1], _roi[2]:_roi[3]]
                        self.CapC.imshow_float(r, roi_frame)
                        # cv2.imshow(r, roi_frame)
                self.debug_real(frame)
        self.mainwin.after(100, self.loop)

    def debug_real(self, frame, switch=0):
        pass

    def print(self, tag, value):
        if not tag in self.debug_print:
            self.debug_print[tag] = value
            print(f"[{tag}]{value}")

    def debug_get_jpg(self, fjpg):
        _appendix = self.CapC.get_appendix(fjpg)
        self.print("_appendix", _appendix.keys())
        if "roihash" in _appendix:
            # _mask=self.CapC.make_delmask(frame)
            self.print("roihash", _appendix["roihash"].keys())
        if "delmask" in _appendix:
            delmask = _appendix["delmask"]
            # self.CapC.imshow_float("delmask",delmask)
            # frame = cv2.bitwise_and(frame, delmask)
            # self.CapC.imshow_float("roi", frame)

    def init_gui(self, win):
        gui = tk.Frame(win)
        gui.pack(expand=1, fill=tk.BOTH)
        tools = tk.Frame(gui)
        self.str_name = tk.StringVar(value="feature")
        tk.Label(tools, text="特征文件名称:").pack(fill=tk.X, side=tk.LEFT, padx=3, pady=1)
        tk.Entry(tools, textvariable=self.str_name, width=20, relief="solid", justify=tk.RIGHT).pack(fill=tk.X,
                                                                                                     side=tk.LEFT,
                                                                                                     pady=1)
        tk.Label(tools, text=".jpg").pack(fill=tk.X, side=tk.LEFT, pady=1)
        self.b_doauto = tk.Button(tools, text="循环特征录制", command=self.do_auto)
        self.b_doauto.pack(fill=tk.X, side=tk.RIGHT, padx=1, pady=1)
        tools.pack(fill=tk.X, padx=1, pady=1)
        tools2 = tk.Frame(gui)
        tools2.pack(fill=tk.X, padx=1, pady=1)
        self.int_time = tk.IntVar(value=30)
        tk.Label(tools2, text="设定(循环超时)固定时长:").pack(fill=tk.X, side=tk.LEFT, padx=3, pady=1)
        tk.Entry(tools2, textvariable=self.int_time, width=10, relief="solid", justify=tk.RIGHT).pack(fill=tk.X,
                                                                                                      side=tk.LEFT,
                                                                                                      pady=1)
        tk.Label(tools2, text="秒").pack(fill=tk.X, side=tk.LEFT, pady=1)
        self.b_dotime = tk.Button(tools2, text="固定时长录制", command=self.do_timelen)
        self.b_dotime.pack(fill=tk.X, side=tk.RIGHT, padx=1, pady=1)

        self.int_logo = tk.IntVar()
        tk.Checkbutton(gui, text="增加ROI:左上角logo[0:80,0:400]", variable=self.int_logo, anchor="w", bg="#e0e0e0",
                       command=self.set_roi_logo).pack(fill=tk.X, padx=1, pady=1)

        self.int_del_mask = tk.IntVar()
        tk.Checkbutton(gui, text="去除ROI:右上角时间[0:80,-150:-1]", variable=self.int_del_mask, anchor="w", bg="#e0e0e0",
                       command=self.set_roi_del).pack(fill=tk.X, padx=1, pady=1)

        self.text = tk.Text(gui, wrap=tk.WORD, width=30)
        self.text.pack(fill=tk.X, padx=1, pady=1)

        # 修改默认选项
        self.int_logo.set(1)
        win.after(1000, self.set_roi_logo)
        self.int_del_mask.set(1)
        win.after(1000, self.set_roi_del)

    def set_roi_logo(self):
        self.CapC.set_roihash_list("0,80,0,400", bool(self.int_logo.get()))
        cv2.destroyAllWindows()

    def set_roi_del(self):
        self.CapC.set_roimask_list("0,80,-150,-1", bool(self.int_del_mask.get()))
        cv2.destroyAllWindows()


def _debug():
    frame1 = cv2.imread("./ok.bmp")
    frame2 = cv2.imread("./fail.bmp")
    print("P", VisionBase().img_blur(frame1))
    print("F", VisionBase().img_blur(frame2))


def _debug_cap():
    cap = cv2.VideoCapture(6, cv2.CAP_DSHOW)
    cap.grab()
    print(cap.set(3, 1280), cap.set(4, 720))  # 1280*720分辨率下,potplay的截图与实时采集同hash特征
    # print(cap.set(3,1920),cap.set(4,1080)) # 1280*720分辨率下,potplay的截图与实时采集同hash特征
    print(cap.get(3), cap.get(4))
    hashFun = VisionBase().hash_func("PHash")
    btime = time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        ret, frame = cap.read()
        # print(frame.shape)
        hashA = hashFun.compute(frame)
        print(hashA)  # [[130  29  60 131 131  60  24 139]] [[130  61  60 131 131  60  24 155]]
        cv2.imshow("show_result", frame)
        _key = cv2.waitKey(100) & 0xff
        if _key in [27]:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # _debug_hash()
    # CapC = CapClass(6)
    # print(CapC.get_formats())
    # print(CapC.dev.get_current_format())
    # _debug_cap()

    app_title = "SEI_GenerateFeature_V2.0.0"
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    ispass_atom = atom('GenerateFeature')
    if (not ispass_atom):
        sys.exit()
    root = tk.Tk()
    root.title(app_title)
    _load_ico(root)
    dev_class = CapGUI(root)
    root.mainloop()
