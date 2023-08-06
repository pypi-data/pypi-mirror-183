import os
import pickle
import time

import cv2
import matplotlib.pyplot as plt
import numpy as np
from autotk.AutoCoreLite import logger
from interval import Interval


class DetectBase():
    def __init__(self, mode, conf_dict={}, update_conf={}) -> None:
        self.para_update = update_conf
        self.detect_mode = mode  # ASS_freebox,PCB_freebox,PCB_800DT,ASS_800DT
        self.conf_dict = {}
        self.json_file = "./Detect.json"
        self.init_data(conf_dict)

    def dict_update(self, new):
        for k, v in new.items():
            if k in self.conf_dict:
                self.conf_dict[k].update(new[k])
            else:
                self.conf_dict[k] = new[k]

    def init_data(self, new_dict):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding='utf-8') as f:
                conf_json = eval(f.read())
                # print(conf_json)
                self.dict_update(conf_json)  # 仅支持2级参数更新
        if new_dict:
            self.dict_update(new_dict)
        self.debug_conf=self.conf_dict.get("DebugShow",{})
        self.detect_conf = self.conf_dict.get(self.detect_mode, {})
        self.detect_func_dict = {}  # 检测LED的主函数入口注册
        self.detect_func_reg()
        self.detect_func = self.detect_func_dict[self.detect_mode]
        # 循环检测公共参数
        self.retry = self.detect_conf.get("retry", 1)
        self.dute_time = self.detect_conf.get("dute_time", 1)
        self.cmd_values = self.detect_conf.get("cmd_values", "").split(",")
        self.exposures = self.detect_conf.get("exposures", "").split(",")
        if len(self.exposures) < len(self.cmd_values):  # 自动补全曝光参数数量
            self.exposures += [self.exposures[-1]] * (len(self.cmd_values) - len(self.exposures))
        self.para_prefix = self.detect_conf.get("para_prefix", "")
        # 执行分支参数
        self.para_dicts = []
        for cmd in self.cmd_values:
            tag = f'{self.para_prefix}{cmd}'
            if tag in self.conf_dict:
                self.para_dicts.append(self.conf_dict[tag])
            else:
                if len(self.para_dicts) > 0:
                    logger.debug(f'Config [{tag}] duplicate copy')
                    self.para_dicts.append(self.para_dicts[-1])
                else:
                    logger.error(f'NoFound Detect Config [{tag}]')
                    self.para_dicts.append({})
        # 处理双配置,以工具配置为准并全部分子参数值相同,因工具ini配置key为小写,Detect.json需切全局控制的定义为全小写
        if self.para_update:
            for k, v in self.para_update.items():
                if k in self.detect_conf:
                    old_value = self.detect_conf[k]
                    new_value = type(old_value)(v)
                    if not new_value == old_value:
                        logger.debug(f"Update Config [{self.detect_mode}][{k}]{old_value} -> {new_value}")
                        self.detect_conf[k] = new_value
                elif k in self.para_dicts[0]:
                    for j, pd in enumerate(self.para_dicts):
                        if k in pd:
                            old_value = pd[k]
                            new_value = type(old_value)(v)
                            if not new_value == old_value:
                                tag = f'{self.para_prefix}{self.cmd_values[j]}'
                                logger.debug(f"Update Config[{tag}][{k}]{old_value} -> {new_value}")
                                self.conf_dict[tag][k] = new_value
    def set_cap_para(self, cap, idx):
        cap.set(cv2.CAP_PROP_EXPOSURE, int(self.exposures[idx]))
        _cap_str = self.para_dicts[idx].get("CAP", "")
        _set_cap = {}
        if _cap_str:
            _set_cap = eval(_cap_str)
        for k, v in _set_cap.items():
            print(f"[CAP]set{k}({v})", cap.set(k, v))

    def detect_func_reg(self):
        pass  # 注册检测函数(规范输入,输出,自动配置内参)

    def debug_cvshow(self, tip="debug show", img=None, switch=1):
        switch = self.debug_conf.get("Show", switch)
        if switch:
            _skip_tip_list=self.debug_conf.get("ShowSkip", [])
            if not tip in _skip_tip_list:
                cv2.imshow(tip, img)

    def debug_pltshow(self, tip,imgs, switch=0):
        switch = self.debug_conf.get("PltShow", switch)
        if switch:
            _skip_tip_list=self.debug_conf.get("PltShowSkip", [])
            if not tip in _skip_tip_list:
                plt.suptitle(f"{tip}")
                if isinstance(imgs,list):
                    num=len(imgs)
                else:
                    num=1
                if num==1:
                    plt.imshow(imgs)
                elif num==2:
                    for i in range(num):
                        plt.subplot(121+i)
                        plt.imshow(imgs[i])
                elif num==3:
                    for i in range(num):
                        plt.subplot(131+i)
                        plt.imshow(imgs[i])
                elif num==4:
                    for i in range(num):
                        plt.subplot(221+i)
                        plt.imshow(imgs[i])
                elif 7>num>=5:
                    for i in range(num):
                        plt.subplot(231+i)
                        plt.imshow(imgs[i])
                else:
                    print("[debug_pltshow] Mort imgs..")
                    return
                plt.show()
    def debug_show_hist(self,plot_dict,switch=1):
        switch = self.debug_conf.get("PltHist", switch)
        if switch:
            # plt show
            showframe=cv2.merge([plot_dict["R"],plot_dict["G"],plot_dict['B']])
            plt.suptitle(f"{plot_dict['msg']} {plot_dict['result']}")
            plt.subplot(221)
            plt.imshow(showframe)
            plt.subplot(222)
            plt.plot(plot_dict['histb'])
            plt.subplot(223)
            plt.plot(plot_dict['histg'])
            plt.subplot(224)
            plt.plot(plot_dict['histr'])
            plt.show()
    def debug_show_split(self, frame, B, G, R, switch=1, tips=None):
        switch = self.debug_conf.get("PltBGR", switch)
        if switch:
            show_frame = frame[:, :, (2, 1, 0)]
            plt.suptitle(f"{tips}")
            plt.subplot(221)
            plt.imshow(B, plt.cm.gray)
            plt.subplot(222)
            plt.imshow(G, plt.cm.gray)
            plt.subplot(223)
            plt.imshow(R, plt.cm.gray)
            plt.subplot(224)
            plt.imshow(show_frame)
            plt.show()
    def debug_split(self, frame,switch=0):
        switch=self.debug_conf.get("PltSplit",switch)
        if switch:
            # 色调（H）、饱和度（S）和明度（V）
            hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            (H, S, V) = cv2.split(hsvframe)
            (B, G, R) = cv2.split(frame)
            plt.suptitle(f"H,S,V ; B,G,R")
            plt.subplot(231)
            plt.imshow(H, plt.cm.gray)
            plt.subplot(232)
            plt.imshow(S, plt.cm.gray)
            plt.subplot(233)
            plt.imshow(V, plt.cm.gray)

            plt.subplot(234)
            plt.imshow(B, plt.cm.gray)
            plt.subplot(235)
            plt.imshow(G, plt.cm.gray)
            plt.subplot(236)
            plt.imshow(R, plt.cm.gray)
            plt.show()

    def show_conf(self, conf):
        msg = f"show config para for debug"
        return msg

    def debug_led_test(self, cap, i):
        if i == None:
            ret, frame = cap.read()
            ret, frame = cap.read()
            return ret, frame
        self.set_cap_para(cap, i)
        ret, frame = cap.read()
        ret, frame = cap.read()
        if (ret):
            result, msg = self.detect_func(frame, self.para_dicts[i])
            logger.debug(f'Debug LED[{result}] {msg}')
            print(f'Debug LED[{result}] {msg}')
        else:
            logger.debug("Cap read Error")
        return ret, frame

    def auto_led_test(self, cap, func_led, name, func_saveerr, pane_id):
        # func_led=adb.ledtest ; func_saveerr=self.save_img_err  固定的上层传递参数
        result = True
        msg = ""
        frames = {}
        for i, t in enumerate(self.cmd_values):
            self.set_cap_para(cap, i)
            func_led(t)
            time.sleep(self.dute_time)
            for n in range(self.retry):
                ret, frame = cap.read()
                ret, frame = cap.read()
                if (ret):
                    frames[t] = frame
                    result, msg = self.detect_func(frame, self.para_dicts[i])
                    logger.debug(f'{name} LED {t}[{n}] {msg} {result}')
                    print(f'{name} LED {t}[{n}] {msg} {result}')
                    if result:
                        break  # 有PASS就break
                    else:
                        func_saveerr(frame, pane_id, t, i)
                else:
                    logger.debug("Cap read Error")
            if not result:
                logger.error(f'{name} {msg}')
                break  # 有FAIL就break
        showframe = self.img_combine(frames)
        return result, showframe

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

    def get_color_name(self, frame):
        hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        (H, S, V) = cv2.split(hsvframe)
        hvalue = np.argmax(np.bincount(H.flatten()))
        svalue = np.argmax(np.bincount(S.flatten()))
        vvalue = np.argmax(np.bincount(V.flatten()))
        name, color = self.hvs2colorname(hvalue, svalue, vvalue)
        # print(name,hvalue, svalue, vvalue)
        return name, color

    def hvs2colorname(self, h, s, v):
        if (0 <= h <= 180 and 0 <= s <= 255 and 0 <= v <= 46):
            name = "黑"
            color = "black"
        elif (0 <= h <= 180 and 0 <= s <= 43 and 46 <= v <= 220):
            name = "灰"
            color = "gray"
        elif (0 <= h <= 180 and 0 <= s <= 30 and 221 <= v <= 255):
            name = "白"
            color = "white"
        elif ((0 <= h <= 10 or 156 <= h <= 180) and 43 <= s <= 255 and 46 <= v <= 255):
            name = "红"
            color = "red"
        elif (11 <= h <= 25 and 43 <= s <= 255 and 46 <= v <= 255):
            name = "橙"
            color = "orange"
        elif (26 <= h <= 34 and 43 <= s <= 255 and 46 <= v <= 255):
            name = "黄"
            color = "yellow"
        elif (35 <= h <= 77 and 43 <= s <= 255 and 46 <= v <= 255):
            name = "绿"
            color = "green"
        elif (78 <= h <= 99 and 43 <= s <= 255 and 46 <= v <= 255):
            name = "青"
            color = "cyan"
        elif (100 <= h <= 124 and 43 <= s <= 255 and 46 <= v <= 255):
            name = "蓝"
            color = "blue"
        elif (125 <= h <= 155 and 43 <= s <= 255 and 46 <= v <= 255):
            name = "紫"
            color = "purple"
        else:
            name = None
            color = None
        return name, color


class LEDDetect(DetectBase):

    def detect_func_reg(self):
        # 当前支持的检测方案 # ASS_freebox,PCB_freebox,PCB_800DT,ASS_800DT
        self.detect_func_dict["ASS_freebox"] = self.ass_freebox
        self.detect_func_dict["ASS_800DT"] = self.ass_800DT

    def ass_freebox(self, frame, fb_conf, debug=False):
        '''
            cv2.HoughCircles(src,method,dp,minDist,circles = None,param1 = None,param2 = None,minRadius = None,maxRadius = None)
            src: 8位，单通道图像。如果使用彩色图像，需要先转换为灰度图像。
            method：定义检测图像中圆的方法。目前唯一实现的方法是cv2.HOUGH_GRADIENT
            dp：累加器分辨率与图像分辨率的反比。dp获取越大，累加器数组越小
            minDist：检测到的圆的中心(x,y)坐标之间的最小距离。如果minDist太小，则可能导致检测到多个相邻的圆。如果minDist太大，则可能导致很多圆检测不到
            param1：用于处理边缘检测的梯度值方法。
            param2：cv2.HOUGH_GRADIENT方法的累加器阈值。阈值越小，检测到的圈子越多
            minRadius：半径的最小大小(以像素为单位)
            maxRadius：半径的最大大小(以像素为单位)
        '''
        detect_color = fb_conf.get("detect_color", "off")
        minDist = fb_conf.get("minDist", 200)
        edgeGredient = fb_conf.get("edgeGredient", 40)
        tagCounter = fb_conf.get("tagCounter", 30)
        minRadius = fb_conf.get("minRadius", 70)
        maxRadius = fb_conf.get("maxRadius", 100)
        try:
            S_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            circles = cv2.HoughCircles(S_img, cv2.HOUGH_GRADIENT, 1, minDist, param1=edgeGredient, param2=tagCounter,
                                       minRadius=minRadius, maxRadius=maxRadius)
        except Exception as e:
            logger.critical(e)
            circles = None
        _roi = []
        if (circles is not None):
            for i, circle in enumerate(circles[0]):  # 圆的基本信息
                x = int(circle[0])  # 坐标行列(就是圆心)
                y = int(circle[1])
                r = int(circle[2])  # 半径
                r_sqrt = int(circle[2] / 1.414)  # 内接正方形
                # data.append((x, y, r, r_sqrt))
                _roi.append((y - r_sqrt, y + r_sqrt, x - r_sqrt, x + r_sqrt))
                if (len(circles[0]) == 1):
                    c_color = (0, 200, 0)
                else:
                    c_color = (0, 0, 200)
                if debug:
                    frame = cv2.circle(frame, (x, y), r, c_color, 2, 20, 0)  # 在原图用指定颜色圈出圆，参数设定为int所以圈画存在误差
        if (_roi and len(_roi) == 1):
            tag_img = frame[_roi[0]:_roi[1], _roi[2]:_roi[3]]
            msg, ret = self.get_color_name(tag_img)
        else:
            msg, ret = "灭", 'off'
        result = ret == detect_color.lower()  # 仅支持全小写英文颜色配置,freebox对应cmd配置是0,1,2
        return result, f"Detect Color:{msg}"
    def load_led_sample(self,fname="./led_.pkl"):
        sampledict = {}
        if os.path.exists(fname):
            with open(fname, 'rb') as l:
                sampledict = pickle.load(l)
        return sampledict
    def save_led_sample(self,hist_dict,fname="./led_.pkl"):
        with open(fname, 'wb') as s:
            pickle.dump(hist_dict, s, pickle.HIGHEST_PROTOCOL)
    def led_Hist(self,frame,tag="",cmplimit=0.9,hist_min=50,hist_size=256,mask=None):
        (B, G, R) = cv2.split(frame)
        histb=cv2.calcHist([B],[0],mask,[hist_size],[hist_min,256])
        histg=cv2.calcHist([G],[0],mask,[hist_size],[hist_min,256])
        histr=cv2.calcHist([R],[0],mask,[hist_size],[hist_min,256])
        histr = cv2.normalize(histr, histr, 0, 1, cv2.NORM_MINMAX, -1)
        histg = cv2.normalize(histg, histg, 0, 1, cv2.NORM_MINMAX, -1)
        histb = cv2.normalize(histb, histb, 0, 1, cv2.NORM_MINMAX, -1)

        pkl_fname=f"./led_{tag}_{hist_size}.pkl"
        sampledict = self.load_led_sample(fname=pkl_fname)
        if sampledict:
            cmp_r=cv2.compareHist(sampledict["R"],histr,cv2.HISTCMP_CORREL)
            cmp_g=cv2.compareHist(sampledict["G"],histg,cv2.HISTCMP_CORREL)
            cmp_b=cv2.compareHist(sampledict["B"],histb,cv2.HISTCMP_CORREL)
            msg=f"Cmp[{tag}]RGB({round(cmp_r,2)},{round(cmp_g,2)},{round(cmp_b,2)})[{cmplimit}]"
            result=cmp_r >=cmplimit and cmp_g >=cmplimit and cmp_b >=cmplimit
        else:
            self.save_led_sample({"R":histr,"G":histg,"B":histb},fname=pkl_fname)
            msg="NoFound Sample Auto save.."
            result=True
        self.debug_show_hist({"R":R,"G":G,"B":B,"result":result,"msg":msg,"histr":histr,"histg":histg,"histb":histb})
        return result,msg

    def ass_800DT(self, frame, conf_800, debug=False):
        len_limit = conf_800.get("len_limit", 250)
        debug = bool(conf_800.get("debug", debug))
        cmp_limit=conf_800.get("similarity", 0)
        result = False
        msg = []
        try:
            hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            rgb_tag = conf_800.get("detect_color", "")
            (H, S, V) = cv2.split(hsvframe)
            (B, G, R) = cv2.split(frame)
            self.debug_split(frame,switch=0)  # 调试用
            tag_dict={"red":R,"green":G,"blue":B,"user":H}
            if cmp_limit>0:
                _histMin=conf_800.get("hist_min", "")
                _histSize=conf_800.get("hist_size", 128)
                cmp_result,cmp_msg=self.led_Hist(frame,rgb_tag,cmplimit=cmp_limit,hist_min=_histMin,hist_size=_histSize)
                msg.append(cmp_msg)
            if rgb_tag in tag_dict:
                contours, hierarchy = self.led_F_contours(tag_dict[rgb_tag], conf_800)  # 分量>过滤灰度范围[FMin,FMax]>取目标轮廓
            else:
                contours, hierarchy = self.led_F_contours(V, conf_800)  # V分量>过滤亮度[VMin,VMax]>取目标轮廓
            if (len(contours) == 1):
                if rgb_tag in tag_dict:
                    tag_dict[rgb_tag] = self.mask_and_contours(tag_dict[rgb_tag], contours)  # 通过轮廓>Mask截取>H分量的ROI区域
                    # self.debug_show_split(frame,H, S, V,tips="ROI")  # 调试用
                    frame = self.cut_by_contours(frame, contours)
                    tag_dict[rgb_tag] = self.cut_by_contours(tag_dict[rgb_tag], contours)
                    # H分量>过滤[HMin,HMax]>len_limit检测头尾坏灯
                    ispass_len, detect_l = self.led_L_len(frame, tag_dict[rgb_tag], conf_800, debug=debug)
                else:
                    H = self.mask_and_contours(H, contours)  # 通过轮廓>Mask截取>H分量的ROI区域
                    # self.debug_show_split(frame,H, S, V,tips="ROI")  # 调试用
                    frame = self.cut_by_contours(frame, contours)
                    H = self.cut_by_contours(H, contours)
                    # H分量>过滤[HMin,HMax]>len_limit检测头尾坏灯
                    ispass_len, detect_l = self.led_H_len(frame, H, conf_800, debug=debug)
                if (not ispass_len):
                    msg.append("Detect Length %s[%s] Fail" % (detect_l, len_limit))
                V = self.cut_by_contours(V, contours)
                # V分量>过滤亮度[VMin,VMax]>median[BlurSize]>允许断裂[BreakLimit]
                ispass_break, msg_break = self.led_break(frame, V, conf_800, debug=debug)
                if msg_break:
                    msg.append(msg_break)
                if (debug):
                    try:
                        showtext1 = f"{self.show_conf(conf_800)} Len:{detect_l}"
                        cv2.putText(frame, showtext1, (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    except:
                        pass
                self.debug_cvshow("Show", frame)
                if cmp_limit > 0:
                    result = ispass_len and ispass_break and cmp_result
                else:
                    result = ispass_len and ispass_break
            elif len(contours) < 1:
                self.debug_cvshow("ShowNoFound", frame)
                msg.append("No Detect Contours")
            else:
                if (debug):
                    try:
                        showtext1 = f"{self.show_conf(conf_800)}"
                        cv2.putText(frame, showtext1, (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    except:
                        pass
                cv2.drawContours(frame, contours, -1, (255, 255, 255), 1)
                self.debug_cvshow("ShowMore", frame)
                msg.append("Detect More Contours")
        except Exception as e:
            print("L--Error", e.__traceback__.tb_lineno)
            msg.append("%s" % e)
        print(msg)
        return result, ";".join(msg)

    def led_L_len(self, frame, Himg, conf, debug=False):
        h_min = conf.get("LMin", 125)
        h_max = conf.get("LMax", 155)
        len_limit = conf.get("len_limit", 250)
        Himg = cv2.GaussianBlur(Himg, (3, 3), 0)
        retvalue, Himg = cv2.threshold(Himg, h_min, h_max, cv2.THRESH_BINARY)  # 二值化 蓝色区间 100 <= h <= 124
        detect_l = self.led_len(frame, Himg, debug=debug)
        ispass_len = detect_l >= len_limit
        return ispass_len, detect_l
    def led_H_len(self, frame, Himg, conf, debug=False):
        h_min = conf.get("HMin", 125)
        h_max = conf.get("HMax", 155)
        len_limit = conf.get("len_limit", 250)
        Himg = cv2.GaussianBlur(Himg, (3, 3), 0)
        retvalue, Himg = cv2.threshold(Himg, h_min, h_max, cv2.THRESH_BINARY)  # 二值化 蓝色区间 100 <= h <= 124
        detect_l = self.led_len(frame, Himg, debug=debug)
        ispass_len = detect_l >= len_limit
        return ispass_len, detect_l
    def led_len(self, frame, detect_frame, debug=False):
        contours, hierarchy = cv2.findContours(detect_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 轮廓
        if (len(contours)):
            max_idx = self.coutours_maxidx(contours)
            rect = cv2.minAreaRect(contours[max_idx])  # 得到最小外接矩形的: 中心(x,y), (宽,高), 旋转角度
            if (debug):
                # print(rect)
                # _l=max(rect[1])*0.8
                # _w=min(rect[1])*0.5
                # print(_l,_w)
                # rect_tag=(rect[0],(_l,_w),rect[2])
                self.debug_cvshow("DetectLen", detect_frame)
                box = cv2.boxPoints(rect)
                # box = cv2.boxPoints(rect_tag)
                box = np.int0(box)
                cv2.drawContours(frame, [box], 0, (255, 255, 255), 1)
            return round(max(rect[1]), 1)
        return 0

    def led_break(self, frame, Vimg, conf, debug=False):
        Vmin = conf.get("VMin", 140)
        Vmax = conf.get("VMax", 255)
        BlurSize = conf.get("BlurSize", 7)
        breaklimit = conf.get("BreakLimit", 20)
        msg = ""
        result = False
        try:
            v_gamma = np.power(Vimg / 255.0, 1.5) * 255.0  # 调整对比度
            Vimg = v_gamma.astype(np.uint8)
            self.debug_pltshow("BreakGamma",Vimg)
            retvalue, V = cv2.threshold(Vimg, Vmin, Vmax, cv2.THRESH_BINARY)  # 二值化
            V = cv2.medianBlur(V, BlurSize)
            break_lines = self.find_break_lines(frame, V, debug=debug)
            break_num = len(break_lines)
            result = not break_num
            for p in break_lines:
                start, end = p
                if (end - start) > breaklimit:
                    result = False
                    break
            if (not result):
                msg = f"Detect ({break_num})Break Part"
        except Exception as e:
            print(e)
            print("b--Error", e.__traceback__.tb_lineno)
        return result, msg

    def find_break_lines(self, frame, detect_frame, show=True, debug=False):
        try:
            lines = cv2.HoughLinesP(detect_frame, 20, np.pi / 180, 50, 100, 10)
            if not len(lines):
                print("NoFound HoughLinesP")
                return []
            _lx = []
            _ly = []
            for x1, y1, x2, y2 in lines[:, 0]:
                if (debug):
                    self.debug_cvshow("DetectBreak", detect_frame)
                    cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 255), 1)
                _zoom_x = Interval(x1, x2)
                if (len(_lx)):
                    isjoin = False
                    for i, z in enumerate(_lx):
                        if (z.overlaps(_zoom_x)):
                            _lx[i] = z.join(_zoom_x)
                            isjoin = True
                    if (not isjoin):
                        _lx.append(_zoom_x)
                else:
                    _lx.append(_zoom_x)
                _ly.append(y1)
                _ly.append(y2)
            lx = []
            lx_num = len(_lx)
            for i in range(lx_num):
                if (len(_lx) < 2):
                    break
                new_lx = _lx.pop(0)
                isjoin = False
                for i, z in enumerate(_lx):
                    if (z.overlaps(new_lx)):
                        _lx[i] = z.join(new_lx)
                        isjoin = True
                if (not isjoin):
                    lx.append(new_lx)
            showL = []
            showR = []
            for l in lx + _lx:
                showL.append(l.lower_bound)
                showR.append(l.upper_bound)
            showL.remove(min(showL))
            showR.remove(max(showR))
            showL.sort()
            showR.sort()
            break_lines = []
            for i, end in enumerate(showL):
                start = showR[i]
                break_lines.append((start, end))
                # print("len",end-start)
                if (show):
                    cv2.line(frame, (start, max(_ly)), (end, max(_ly)), (255, 255, 255), 1)
        except Exception as e:
            print(e)
            print("l--Error", e.__traceback__.tb_lineno)
        return break_lines

    def coutours_maxidx(self, contours):
        area = []
        # 找到最大的轮廓
        for k in range(len(contours)):
            area.append(cv2.contourArea(contours[k]))
        max_idx = np.argmax(np.array(area))
        return max_idx

    def gen_offset(self, frame, rect):
        r_cpoint, r_hw, r_r = rect
        # print(rect, top, bottom)
        if (r_hw[0] >= r_hw[1]):
            roi_hw = (220, 50)
        else:
            roi_hw = (50, 220)
        # box = cv2.boxPoints(((314.5-110,253.7-75), (220, 50), 0.5208563208580017))
        box = cv2.boxPoints(((r_cpoint[0] - 110, r_cpoint[1] - 75), roi_hw, r_r))
        box2 = cv2.boxPoints(((r_cpoint[0] + 110, r_cpoint[1] + 75), roi_hw, r_r))
        box = np.int0(box)
        box2 = np.int0(box2)
        mask = np.zeros(frame.shape, np.uint8)
        fillmask = cv2.drawContours(mask, [box], 0, (255, 0, 0), -1)
        ROI = cv2.bitwise_and(mask, frame)
        cv2.drawContours(frame, [box2], 0, (255, 0, 0), 1)

    def mask_and_contours(self, Bimg, contours):
        max_idx = self.coutours_maxidx(contours)
        rect = cv2.minAreaRect(contours[max_idx])
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        mask = np.zeros(Bimg.shape, np.uint8)
        cv2.drawContours(mask, [box], 0, (255, 255, 255), -1)
        ROI = cv2.bitwise_and(Bimg, mask)
        self.debug_cvshow("MaskAnd", ROI)
        return ROI

    def cut_by_contours(self, img, contours, switch=False):
        if switch:
            max_idx = self.coutours_maxidx(contours)
            rect = cv2.minAreaRect(contours[max_idx])
            top = int(rect[0][1] - 100)  # 大概100便宜 忽略了角度
            bottom = int(rect[0][1] + 100)
            img = img[top:bottom, :]
        return img

    def led_F_contours(self, Vimg, conf):
        v_min = conf.get("FMin", 140)
        v_max = conf.get("FMax", 255)
        _Oimg=Vimg
        Vimg = cv2.GaussianBlur(Vimg, (3, 3), 0)
        self.debug_pltshow("FBlur",[_Oimg,Vimg])
        cv2.threshold(Vimg, v_min, v_max, cv2.THRESH_BINARY)
        retvalue, Vimg = cv2.threshold(Vimg, v_min, v_max, cv2.THRESH_BINARY)  # 二值化 蓝色区间 100 <= h <= 124
        # Vimg = cv2.Canny(Vimg, v_min, v_max)
        contours, hierarchy = cv2.findContours(Vimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 外部轮廓 区分环境轮廓
        self.debug_cvshow("led_F_contours", Vimg)
        return contours, hierarchy

    def show_conf(self, conf):
        f_min = conf.get("FMin", 125)
        f_max = conf.get("FMax", 255)
        l_min = conf.get("LMin", 125)
        l_max = conf.get("LMax", 125)
        h_min = conf.get("HMin", 125)
        h_max = conf.get("HMax", 155)
        v_min = conf.get("VMin", 140)
        v_max = conf.get("VMax", 255)
        blur_size = conf.get("BlurSize", 7)
        msg = f"F[{f_min},{f_max}] L[{l_min},{l_max}] H[{h_min},{h_max}] V[{v_min},{v_max}] VBlur[{blur_size}] "
        return msg

    def led_600TID(self, frame, debug=False):
        result = False
        msg = []
        try:
            h_min = self.conf_3box.get("HMin", Hmin)
            h_max = self.conf_3box.get("HMax", Hmax)
            hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            (H, S, V) = cv2.split(hsvframe)
            self.debug_show_split(frame, H, S, V)  # 调试用
            contours, hierarchy = cv2.findContours(V, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 外部轮廓 区分环境轮廓
            if (len(contours) == 1):
                rect = cv2.minAreaRect(contours[0])
                top = int(rect[0][1] - 100)
                bottom = int(rect[0][1] + 100)
                self.gen_offset(frame, rect)
                frame = frame[top:bottom, :]
                # 检测蓝色灯条长度 区分边缘坏灯
                H = H[top:bottom, :]
                retvalue, H = cv2.threshold(H, Hmin, Hmax, cv2.THRESH_BINARY)  # 二值化 蓝色区间 100 <= h <= 124
                detect_l = self.led_len(frame, H, debug=debug)
                ispass_len = detect_l >= lenlimit
                if (not ispass_len):
                    msg.append("Detect Length %s(%s) Fail" % (detect_l, lenlimit))
                # 识别断线位置
                V = V[top:bottom, :]
                ispass_break, msg_break = self.led_break(V, self.conf_3box, debug=debug)
                if msg_break:
                    msg.append(msg_break)
                if (debug):
                    try:
                        showtext1 = "H[%s , %s] Vmin[%s] VBlur[%s] Length %s" % (h_min, h_max, Vmin, BlurSize, detect_l)
                        cv2.putText(frame, showtext1, (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                    except:
                        pass
                # frame = frame[top:bottom, :]
                self.debug_cvshow("Show", frame)
                result = ispass_len and ispass_break

            else:
                cv2.drawContours(frame, contours, -1, (0, 0, 255), 1)
                rect = cv2.minAreaRect(contours[0])
                top = int(rect[0][1] - 100)
                bottom = int(rect[0][1] + 100)
                # ((314.5252685546875, 253.71841430664062), (589.0938110351562, 18.717409133911133), 0.5208563208580017) 153 353
                r_cpoint, r_hw, r_r = rect
                print(rect, top, bottom)
                # box = cv2.boxPoints(((314.5-110,253.7-75), (220, 50), 0.5208563208580017))
                # box = cv2.boxPoints(((r_cpoint[0]-110,r_cpoint[1]-75), (220, 50), r_r))
                # box=np.int0(box)
                # cv2.drawContours(frame, [box], 0, (255, 0, 0), 1)
                # frame = frame[top:bottom, :]
                self.debug_cvshow("ShowAll", frame)
                msg.append("Detect More Contours")
        except Exception as e:
            msg.append("%s" % e)
        return result, ";".join(msg)


def _func_none(*args):
    pass


def _get_all_cap_para(cap):
    # print(cap.set(37, 1))  # 弹出属性参数调节窗口
    _set_cap = {}
    for i in range(50):
        va = cap.get(i)
        if not va == -1.0:
            _set_cap[i] = va
    print(_set_cap)


if __name__ == '__main__':
    cap = cv2.VideoCapture(4, cv2.CAP_DSHOW)
    cap.grab()
    # print(cap.set(37, 1))  # 弹出属性参数调节窗口
    # _get_all_cap_para(cap)
    # ret,frame=cap.read()
    # if ret:
    #     cv2.imwrite("./LED.jpg",frame)

    btime = time.time()
    if cap.isOpened():
        while 1:
            DD = LEDDetect("ASS_800DT")
            elptime = time.time() - btime
            # result, frame = DD.debug_led_test(cap,None)
            result, frame = DD.debug_led_test(cap,0)
            # cv2.imshow("show_result", frame)
            _key = cv2.waitKey(100) & 0xff
            if _key in [27]:
                break
    cap.release()
    cv2.destroyAllWindows()
