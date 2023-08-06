import os, json, sys, time, logging, configparser
import threading
import pickle
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import PhotoImage
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import asksaveasfilename
import tkinter.messagebox as mbox
import queue
from ftplib import FTP

from autotk.AutoCoreLite import runmain, license_name, logger, getnewdir, atom, config_auto
from autotk.AutoCore import UIForm, Box
from autotk.AutoMES import Mes
from autotk.AutoDB import log2db
from autotk.AutoLang import lolang, lang_append

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageTk
from ttkwidgets import CheckboxTreeview, DebugWindow
import win32event
import win32api
import win32com.client

try:
    import cv2
except:
    pass
try:
    from autotk.AutoAudio import Sound_Man, directsound, Modal_PSD_Real
except:
    pass
try:
    from autotk.AutoSerial import scan_com, ir_com, volt_com
except:
    pass
try:
    from autotk.AutoOSS import RemoteConfig
except:
    pass


class BoxData(tk.Toplevel):
    def __init__(self, master=None, cnf={}, setting={}, result={}, **kw):
        self.setting = setting
        self.result = result
        super().__init__(master, cnf, **kw)
        if ("geometry" in self.setting):
            self.geometry(self.setting["geometry"])
        if ("title" in self.setting):
            self.title(self.setting["title"])
        self.textdata = setting.get("data", "None")
        self.transient(master)  # 调用这个函数就会将Toplevel注册成master的临时窗口,临时窗口简化最大最小按钮
        # self.resizable(height=False, width=False)  # 禁止调整大小
        self.grab_set()  # 将此应用程序的所有事件路由到此窗口小部件
        self.init_ui()
        self.bind("<Escape>", self.destroy)
        self.focus_force()  #

    def destroy(self, *args) -> None:
        super().destroy()

    def init_ui(self):
        try:
            if (self.textdata):
                if isinstance(self.textdata[0], list):
                    _cols = ["D%s" % (i + 1) for i, j in enumerate(self.textdata[0])]
                    # _cols=tuple(self.setting.get("columns",_cols))
                    _cols = self.setting.get("columns", _cols)
                    showtable = ttk.Treeview(self, show="headings", columns=_cols)
                    for d in self.textdata:
                        showtable.insert("", "end", values=d)
                else:
                    _cols = ["D%s" % (i + 1) for i, j in enumerate(self.textdata)]
                    _cols = tuple(self.setting.get("columns", _cols))
                    showtable = ttk.Treeview(self, show="headings", columns=_cols)
                    showtable.insert("", "end", values=self.textdata)
                for c in _cols:
                    showtable.column(c, width=5)
            showtable.pack(expand=1, fill=tk.BOTH)
        except Exception as e:
            print(e)


class BoxText(tk.Toplevel):
    def __init__(self, master=None, cnf={}, setting={}, result={}, **kw):
        self.setting = setting
        self.result = result
        super().__init__(master, cnf, **kw)
        if ("geometry" in self.setting):
            self.geometry(self.setting["geometry"])
            pass  # 自动尺寸
        if ("title" in self.setting):
            self.title(self.setting["title"])
        self.textdata = setting.get("data", "None")
        self.transient(master)  # 调用这个函数就会将Toplevel注册成master的临时窗口,临时窗口简化最大最小按钮
        # self.resizable(height=False, width=False)  # 禁止调整大小
        self.grab_set()  # 将此应用程序的所有事件路由到此窗口小部件
        self.init_ui()
        self.bind("<Escape>", self.destroy)
        self.focus_force()  #

    def destroy(self, *args) -> None:
        super().destroy()

    def init_ui(self):
        try:
            textinfo = ScrolledText(self)
            textinfo.insert(tk.INSERT, self.textdata)
            textinfo.configure(state='disabled')
            textinfo.pack(expand=1, fill=tk.BOTH)
        except Exception as e:
            print(e)


class BoxFrame(tk.Toplevel):
    def __init__(self, master=None, cnf={}, setting={}, result={}, **kw):
        self.setting = setting
        self.result = result
        super().__init__(master, cnf, **kw)
        if ("geometry" in self.setting):
            # self.geometry(self.setting["geometry"])
            pass  # 自动尺寸
        if ("title" in self.setting):
            self.title(self.setting["title"])
        self.resizeframe = setting.get("resize", None)
        self.frame = setting.get("frame", None)
        # self.iconbitmap("./ico.ico")      # iconphoto(True 继承图标
        self.transient(master)  # 调用这个函数就会将Toplevel注册成master的临时窗口,临时窗口简化最大最小按钮
        self.resizable(height=False, width=False)  # 禁止调整大小
        self.grab_set()  # 将此应用程序的所有事件路由到此窗口小部件
        self.init_ui()
        self.bind("<Escape>", self.destroy)
        self.focus_force()  #

    def destroy(self, *args) -> None:
        super().destroy()

    def init_ui(self):
        try:
            panel = Label(self)
            panel.pack()
            if (self.resizeframe):
                img_h, img_w, _ = self.frame.shape
                self.frame = cv2.resize(self.frame, (int(img_w * 0.5), int(img_h * 0.5)))
            cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)  # 转换颜色从BGR到RGBA
            current_image = Image.fromarray(cv2image)  # 将图像转换成Image对象
            imgtk = ImageTk.PhotoImage(image=current_image)
            panel.imgtk = imgtk
            panel.config(image=imgtk)
        except Exception as e:
            print(e)


class Func_Loop_Box(tk.Toplevel):
    def __init__(self, master=None, cnf={}, setting={}, result={}, **kw):
        self.setting = setting
        self.result = result
        super().__init__(master, cnf, **kw)
        if ("func" in self.setting):
            self.func = self.setting["func"]
        if ("keycodes" in self.setting):
            self.tags = self.setting["keycodes"]
        if ("geometry" in self.setting):
            self.geometry(self.setting["geometry"])
        if ("title" in self.setting):
            self.showname = self.setting["title"]
            self.title(self.showname)
        self.dute = 200
        self.timeout = 100
        if ("dute" in self.setting):
            self.dute = self.setting["dute"]
        self.dute_count = self.dute / 1000
        if ("timeout" in self.setting):
            self.timeout = self.setting["timeout"]
        self.count = self.timeout if self.timeout > 0 else 0
        # self.iconbitmap("./ico.ico")      # iconphoto(True 继承图标
        self.transient(master)  # 调用这个函数就会将Toplevel注册成master的临时窗口,临时窗口简化最大最小按钮
        self.resizable(height=False, width=False)  # 禁止调整大小
        self.grab_set()  # 模态 2022.01.26 注释按钮检测偶现不弹窗问题好像能解决但偶现主界面刷新问题
        self.init_ui()
        self.focus_force()  # 2022.01.27使用模特增加focus 避免不弹窗问题
        self.refresh_data()

    def loop(self, *args, **kwargs):
        ret, data = self.func()
        self.result['Data'] = data
        if (ret):
            allpass = True
            for k in self.tags.split(','):
                if (not k in data):
                    allpass = False
                    self.set_tips(k)
                    break
            if (allpass):
                self.result['Result'] = True
                self.destroy()

    def refresh_data(self, *args, **kwargs):
        if (self.timeout > 0):
            self.count -= self.dute_count
            self.title("{} {}".format(self.showname, int(self.count)))
        else:
            self.title("{}".format(self.showname))
        try:
            self.loop()
        except Exception as e:
            logger.critical(e)
            self.destroy()
        if (self.count < 0):
            self.destroy()
        else:
            self.after(self.dute, self.refresh_data)

    def destroy(self, *args, **kwargs):
        super().destroy()

    def set_tips(self, msg=None):
        try:
            if ("keycodes" in self.setting):
                if msg:
                    self.msgtip.set(f"请按键：{msg}")
                else:
                    self.msgtip.set(f"请按键：{self.tags}")
        except:
            pass

    def init_ui(self):
        self.msgtip = tk.StringVar(value="请按键：")
        self.set_tips()
        tip = Label(self, textvariable=self.msgtip, anchor='w', font=('宋体', 18), background="yellow")
        tip.place(relx=0.02, rely=0.04, relwidth=0.97, relheight=0.4)
        self.b_fail = Button(self, text='FAIL [故障]', command=self.destroy, style='TButton')
        self.b_fail.place(relx=0.02, rely=0.5, relwidth=0.97, relheight=0.4)


class MForm(UIForm):

    def show_debug(self, *args):
        DebugWindow(self.master)

    def show_view(self, pane_id, img, resize=None):
        try:
            LabelView = self.pane_all[pane_id]["LabelView"]
            if (resize):
                img_h, img_w, _ = img.shape
                img = cv2.resize(img, (int(img_w * resize), int(img_h * resize)))
            cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)  # 转换颜色从BGR到RGBA
            current_image = Image.fromarray(cv2image)  # 将图像转换成Image对象
            imgtk = ImageTk.PhotoImage(image=current_image)
            LabelView.imgtk = imgtk
            LabelView.config(image=imgtk)
        except:
            pass

    def isRemove(self, pane_id):
        return self.pane_all[pane_id]["Tid"] == ""

    def babort_click(self, item, pane_id):
        try:
            self.pane_all[pane_id]["Abort"] = True
        except:
            pass

    def show_plot_class(self, BoxClass, setting={}, result={"Result": False, "Data": ""}):
        # show_plot_class 可重入前替换参数,使用matplotlib.pyplot显示曲线,默认BoxClass=BoxData
        self.show_box_class(BoxClass, setting, result)

    def blist_click(self, item, pane_id):
        super().blist_click(item, pane_id)
        try:
            data = self.pane_item_dict[pane_id][item]["Data"]
            if (self.plan[item] in self.planClickFrame):
                if (isinstance(data, str)):
                    mbox.showinfo(self.pane_sn[pane_id].get(), data)
                else:
                    frame, msg = data
                    show_title = "%s %s" % (self.pane_sn[pane_id].get(), msg)
                    self.show_box_class(BoxFrame, setting={'title': show_title, "frame": frame, "resize": 0.5})
                return
            if (self.plan[item] in self.planClickPlot):
                if (isinstance(data, str)):
                    mbox.showinfo(self.pane_sn[pane_id].get(), data)
                else:
                    show_title = "%s" % (self.pane_sn[pane_id].get())
                    scwidth = self.master.winfo_screenwidth()
                    scheight = self.master.winfo_screenheight()
                    width = 600
                    height = 400
                    size = '%dx%d+%d+%d' % (width, height, (scwidth - width) / 2, (scheight - height) / 2)
                    self.show_plot_class(BoxData, setting={'title': show_title, "data": data, "geometry": size})
                return
            if (self.plan[item] in self.planClickInfo):
                if (data):
                    if (len(data) > 2000):  # 2000字以上
                        scwidth = self.master.winfo_screenwidth()
                        scheight = self.master.winfo_screenheight()
                        width = 800
                        height = 600
                        size = '%dx%d+%d+%d' % (width, height, (scwidth - width) / 2, (scheight - height) / 2)
                        show_title = "%s" % (self.pane_sn[pane_id].get())
                        self.show_box_class(BoxText, setting={'title': show_title, "data": data, "geometry": size})
                    else:
                        mbox.showinfo(self.pane_sn[pane_id].get(), data)
                else:
                    print("No Data..", data)
                return
            print("blist_click[planClickFrame/planClickPlot/planClickInfo] Undefined", self.plan[item])
            # 重测执行代码段
            # logger.info("Retest {}".format(self.plan[item]))
            # name = self.pane_sn[pane_id].get()
            # self.plan_todo[self.plan[item]](name, pane_id)
        except:
            pass

    def loadconfig(self):
        super().loadconfig()
        # log和report的dir子路径可配置
        self.dir_log = getnewdir(f'../Log/{self.conf_dict.get("SETTING", {}).get("log_dir", "Factory")}/')
        self.dir_report = getnewdir(f'../Report/{self.conf_dict.get("SETTING", {}).get("report_dir", "Factory")}/')
        # 标志adb模式,mode为双数使用usb模式,mode为单数使用exe模式,mode=0为默认usb模式
        self.adb_is_exe = bool(int(self.conf_dict["SETTING"].get("mode", "0")) % 2)
        # 颜色 默认初始值为 黑：-16777216
        self.color_dict = {"indx": ["红", "绿", "蓝", "白", "黄", "紫", "青", "灰", "黑", ], "红": -65536, "绿": -16711936,
                           "蓝": -16776961, "白": -1, "黑": -16777216, "灰": -7829368, "黄": -256, "紫": -65281,
                           "青": -16711681}
        self.show_log_heigth = 8  # 重置LOG的显示高度
        # 注册执行线程                                                                                 Plan注册>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.plan_todo = {"HDMI_VIDEO": self.todo_VIDEO, "HDMI_AUDIO": self.todo_AUDIO, "DECODE_H264": self.todo_VIDEO,
                          "DECODE_AV1": self.todo_VIDEO, "DECODE_VP9": self.todo_VIDEO,
                          "WRITE_BOXID": self.todo_WRITE_BOXID,
                          "WIFI_COUPLE": self.todo_WIFI_COUPLE, "ROUTER_COUPLE": self.todo_ROUTER_COUPLE,
                          'BURN_KEY': self.todo_BURN_KEY, 'HDMI_VOLT': self.todo_HDMI_VOLT,
                          "PRETREATMENT": self.todo_PRETREATMENT,
                          "ADB_CLOSE": self.todo_ADB_CLOSE, "IPERF_LAN": self.todo_IPERF_LAN,
                          'CHECK_KEYS': self.todo_CHECK_KEYS, 'ROUTER_TELNET': self.todo_ROUTER_TELNET,
                          'DVB_VOLT': self.todo_DVB_VOLT, 'BT_TEST': self.todo_BT_TEST, 'READ_KEY': self.todo_READ_KEY,
                          "ETH_TEST": self.todo_ETH_TEST, "MES": self.todo_MES, "DVB": self.todo_DVB,
                          'WIFI_24': self.todo_WIFI_24, 'WIFI_5': self.todo_WIFI_5, 'FTP': self.todo_FTP,
                          "RESET": self.todo_RESET, "BASIC_TEST": self.todo_BASIC_TEST, "SCANNER": self.todo_SCANNER,
                          'BUTTON_TEST': self.todo_BUTTON_TEST, 'AGING_TEST': self.todo_AGING_TEST,
                          "RESOLUTION": self.todo_RESOLUTION, "USB_TEST": self.todo_USB_TEST,
                          "VISION_DETECT": self.todo_VISION_DETECT, "LEDS_DETECT": self.todo_LEDS_DETECT,
                          "SD_TEST": self.todo_SD_TEST, "IR_TEST": self.todo_IR_TEST, 'LED_TEST': self.todo_LED_TEST,
                          "SPDIF_AUDIO": self.todo_AUDIO, "ADB_IPERF": self.todo_ADB_IPERF}
        self.planAllowAbort = ["VISION_DETECT", "LEDS_DETECT"]
        self.planClickFrame = ["HDMI_VIDEO", "AV_VIDEO", "DVB", "LED_TEST", "DECODE_AV1", "DECODE_VP9", "DECODE_H264"]
        self.planClickPlot = ["HDMI_AUDIO", "SPDIF_AUDIO", "AV_AUDIO"]
        self.planClickInfo = ["RESOLUTION", "USB_TEST", "SD_TEST", "ETH_TEST", "IR_TEST", "BASIC_TEST", "MES",
                              "SCANNER", "BURN_KEY", "READ_KEY", "CHECK_KEYS", "WIFI_COUPLE", "ROUTER_COUPLE",
                              "BUTTON_TEST", "HDMI_VOLT", "DVB_VOLT", "AGING_TEST", "WIFI_5", "WIFI_24",
                              "ROUTER_TELNET", "ADB_CLOSE", "LEDS_DETECT", "IPERF_24", "IPERF_5", "IPERF_LAN",
                              "BT_TEST", "WRITE_BOXID"]
        self.scanlock = threading.Semaphore(1)  # 资源锁

    def initdata(self):
        super().initdata()
        for i, p in enumerate(self.pane_sn):
            self.pane_all[i] = {"Ready": True, "Run": False, "HDMI": 0, "Boxid": "", "BoxidVstr": p, "Tid": "",
                                "Class": "", "Abort": False,
                                }
        # 参数定义最多有几个线程可以同时使用资源
        self.pane_all["DeviceNum"] = 0  # 记录ADB的搜索数量
        self.pane_all["Overflow"] = []  # 超出治具数量的设备记录
        self.pane_all["Abort"] = {}  # 中断的设备记录,中断的判断为Fail
        if ("HDMI_VIDEO" in self.plan):
            if (os.path.isfile("./hdmi.jpg")):
                img = cv2.imread("./hdmi.jpg")
                self.samplehash = self.aHash(img)  # 1111100010100100100111101111011001100000000001000101010100011110
            else:
                logger.info("Read the Default hdmi sample ahash value")
                self.samplehash = "1111100010100100100111101111011001100000000001000101010100011110"
        # MES
        try:
            logger.debug("MES Connnetting..")
            mes_id = int(self.conf_dict["MES"]["id"])
            mes_wsdl = self.conf_dict["MES"]["wsdl"]
            mes_station = self.conf_dict["MES"]["station"]
            mes_scanner = self.conf_dict["MES"]["scanner"]
            self.mes = Mes(mes_wsdl, mes_station, mes_scanner, not mes_id, self.conf_dict["MES"])
        except:
            logger.debug("MES Connect Error")
        #
        self.pane_dict_report = {"PASSCount": 0, "FAILCount": 0, "ItemFailCount": {i: 0 for i in self.plan}}
        #
        self.pane_port = {}

    def t_plan(self, dut, sn_ctl, pane_id):
        try:
            btime = time.time()
            if dut.checkready():
                name = dut.boxid
                sn_ctl.set(name)
                self.pane_all[pane_id]["Boxid"] = name
                self.pane_all[pane_id]["Class"] = dut
                logger.info("Start Test Device {}".format(name))

                self.pane_all[pane_id]["BeginTime"] = btime
                self.pane_dict_report[pane_id] = {"SN": name}
                for i, p in enumerate(self.plan):
                    if (not self.main_run): return
                    _btime = time.time()
                    self.pane_item_dict[pane_id][i]["Data"] = None  # 清空数据
                    self.pane_item_dict[pane_id][i]["running"]()
                    self.pane_dict_report[pane_id]["TestItem"] = i + 1
                    try:
                        self.pane_dict_report[pane_id][p] = {}
                        self.log_db.plan(name, p)
                        result, show_tips = self.plan_todo[p](name, pane_id, i, p, self.pane_dict_report[pane_id][p])
                    except Exception as e:
                        result = False
                        show_tips = ""
                        logger.critical("[Error]t_plan %s pane %s" % (name, pane_id))
                        logger.critical(str(e))
                    finally:
                        elpstime = round(time.time() - _btime, 3)
                        self.pane_dict_report[pane_id][p]['elpstime'] = elpstime
                        self.pane_dict_report[pane_id][p]['result'] = result
                        if (result):
                            logger.warning("%s %s %s PASS" % (name, self.lo(p), show_tips))
                        else:
                            logger.error("%s %s %s FAIL" % (name, self.lo(p), show_tips))
                        logger.info("Elapsed Time: %.3f s" % (elpstime))  # 统一计算耗时
                    self.log_db.add_report(name, p, elpstime, result, self.pane_dict_report[pane_id][p])
                    if (pane_id in self.pane_all["Abort"]):
                        pass
                        # self.pane_all["Abort"].pop(pane_id)
                        # break
                    if (self.isRemove(pane_id)):  # 设备已移除
                        break
                    if (not result):
                        self.pane_item_dict[pane_id][i]["fail"]()
                        break
                    self.pane_item_dict[pane_id][i]["pass"]()
                self.log_db.plan(name, report=result)
                # adb = self.pane_all[pane_id]["Class"]
                # if (not adb.error):   #20210715 adb错误 更换成移除与执行关闭 更新界面
                # print(self.main_run,self.pane_all)
                if (self.main_run and not self.isRemove(pane_id)):
                    self.update_report(pane_id)
                # 由执行中 转存 到 完成
                self.pane_all[pane_id]["Abort"] = False
                self.pane_all[pane_id]["Run"] = False
                logger.info("Test Device {} Finish (Elapsed: {:.1f} s)".format(name, time.time() - btime))
                if (not 'FTP' in self.plan):  # 去重
                    self.save_report(pane_id, result)
                if ("a" in self.conf_dict["SETTING"]["debug"]):
                    self.pane_all[pane_id]["Class"].adb_close()  # DUT 自动关闭adb
                elif ("l" in self.conf_dict["SETTING"]["debug"]):
                    if ("e" in self.conf_dict["SETTING"]["debug"]):
                        if (result):
                            self.debug_remove(pane_id)
                    else:
                        self.debug_remove(pane_id)
                # adb.dev_finish()  # DUT 完成
            else:
                logger.error(f'DUT未就绪 {dut.errormsg[dut.error]}')
        except Exception as e:
            print(e)
            logger.critical("[t_plan]Error: %s" % e)

    def update_report(self, pane_id):
        try:
            dict_report = self.pane_dict_report[pane_id]
            if (dict_report):
                result = False
                usetime = 0
                for i in self.plan:
                    if ("result" in dict_report[i].keys()):
                        result = dict_report[i]["result"]
                        usetime += dict_report[i]["elpstime"]
                        if (not result):
                            self.pane_dict_report["ItemFailCount"][i] += 1  # 统计错误Item
                            break
                    else:
                        self.pane_dict_report["ItemFailCount"][i] += 1  # 统计错误Item
                        break  # 未执行完 result没有
                self.pane_dict_report[pane_id]["elpstime"] = usetime
                if (result):
                    self.pane_dict_report["PASSCount"] += 1
                    self.pane_result[pane_id]["text"] = "PASS"
                    self.pane_result[pane_id]["background"] = "green"
                else:
                    self.pane_dict_report["FAILCount"] += 1
                    self.pane_result[pane_id]["text"] = "FAIL"
                    self.pane_result[pane_id]["background"] = "red"
            else:
                self.pane_result[pane_id]["text"] = "Result"
                self.pane_result[pane_id]["background"] = "gray"
            self.refresh_info()
        except Exception as e:
            logger.warning("[Warn] update_report")
            logger.warning(e)

    def save_img_report(self, frame, itemname, sn, result):
        self.save_img(frame, f'{"PASS" if result else "FAIL"} {itemname} {sn}', self.dir_report)

    def save_img_log(self, frame, pane_id, itemname, value):
        self.save_img(frame, f'{pane_id + 1} {itemname} {value}', self.dir_log)

    def save_img_err(self, frame, pane_id, itemname, value):
        self.save_img(frame, f'Err[Sta{pane_id + 1}]{itemname} {value}', self.dir_log)

    def save_img(self, frame, name, dirpath):
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        cv2.imwrite(f"{dirpath}{name} {timestr}.jpg", frame)

    def save_report(self, pane_id, result):
        loadsn = self.pane_all[pane_id]["BoxidVstr"].get()
        reportjson = self.pane_dict_report[pane_id]
        app_json = json.dumps(reportjson, indent=4, sort_keys=True)
        self.mes.SaveJson(loadsn, result, reportjson)
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        filename = f'{self.dir_report}{loadsn}_{timestr}_{"PASS" if result else "FAIL"}.json'
        with open(filename, "w+") as jsonf:
            jsonf.write(app_json)
        if ("csv" in self.conf_dict["SETTING"]["debug"]):  # 保存结果汇总到本地csv
            with open("ReportCollect.csv", 'a+') as f:
                content = "%s,%s\n" % (loadsn, reportjson)
                f.write(content)
        return filename

    def todo_ADB_CLOSE(self, name, pane_id, item, tagid, report_dict, msg=[], *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            mode = self.conf_dict[tagid]["mode"]
            dhcp = int(self.conf_dict[tagid]["dhcp"])
            if "door" in self.conf_dict[tagid]:
                open_door = int(self.conf_dict[tagid]["door"])
            else:
                open_door = True  # 兼容旧版本,无该配置
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        # 临时ADB指令
        '''
        cmd0 = pm install /storage/%s/Nes_SetNetHdcp_v1.0.apk
        delay0 = 2
        match0 = Success
        cmd1 = am start -n com.nes.sethdcp/com.nes.sethdcp.MainActivity
        delay1 = 2
        match1 = cmp=com.nes.sethdcp/.MainActivity
        cmd2 = dumpsys activity com.nes.sethdcp/com.nes.sethdcp.MainActivity getHdcpState
        delay2 = 3
        match2 = getHdcpState_SUCCESS
        '''
        result = True
        try:
            for i in range(10):
                if (not "cmd%d" % i in self.conf_dict[tagid]): break
                cmd = self.conf_dict[tagid]["cmd%d" % i]
                if ("%" in cmd):
                    # if("storage/%s" in cmd):
                    cmd = cmd % (adb.sendshell("ls /storage ")[:9])  # 变量变换
                logger.debug("[CMD%d] %s" % (i, cmd))
                if (cmd):
                    ret = adb.sendshell(cmd)
                    logger.debug("[RECV%d] %s" % (i, ret.strip()))
                    delay = self.conf_dict[tagid]["delay%d" % i]
                    if (delay):
                        time.sleep(int(delay))
                    match = self.conf_dict[tagid]["match%d" % i]
                    if (match):
                        if (not match in ret):
                            logger.error("[CMD%s]Match:%s Fail" % (i, match))
                            msg.append("[RECV%d] %s" % (i, ret.strip()))
                            result = False
                            break
        except Exception as e:
            logger.critical(e)
            result = False
        if (result and dhcp):
            result = adb.setDhcp()
            msg.append("[HDCP]%s" % result)
            logger.debug("%s %s [DHCP]%s" % (name, self.lo(tagid), result))
        self.pane_item_dict[pane_id][item]["Data"] = "\r\n".join(msg)
        # 临时增加治具门打开
        if (result):
            if (mode == "0"):
                adb.adb_close_next()
            else:
                adb.adb_close()
                # 临时增加治具门打开
                if (result and open_door):
                    try:
                        auto = int(self.conf_dict["BUTTON_TEST"]["auto"])
                    except:
                        logger.critical("Config BUTTON_TEST temp Para %s" % self.lo("Error"))
                        # self.pane_dict_report[pane_id][tagid] = {"result": False}
                        return False
                    if (auto == 1):
                        try:
                            # 控制自动按键,波特率9600打开串口，发送“BUTTON_ON” 按键开启 ，串口返回“OK”；发送“BUTTON_OF”F 按键关闭，串口返回“OK
                            ports = self.conf_dict["BUTTON_TEST"]["ports"].split(',')
                            ctl_m = control_com(ports[pane_id])
                            ctl_m.open()
                            ctl_m.open_door()
                            logger.debug("Open the Door")
                        except:
                            logger.critical("Temp Control COM Error")
                        finally:
                            ctl_m.close()
        return result, ""

    def todo_MES(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            id = int(self.conf_dict[tagid]["id"])
            keywords = self.conf_dict[tagid]["keyword"].split(',')
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        if ("SCANNER" in self.pane_dict_report[pane_id] and "scan" in self.pane_dict_report[pane_id]["SCANNER"]):
            sn = self.pane_dict_report[pane_id]["SCANNER"]["scan"]
        else:
            sn = self.pane_dict_report[pane_id]["SN"]
        msg = []
        result = True
        for k, v in self.pane_dict_report[pane_id].items():
            if (k == tagid): break
            if (k == "SN"):
                k = "Boxid"  # 当前工具使用的主键名称为Boxid AutoHDMI需要替换Report中的SN为对应的Boxid>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            result = self.mes.Uploaditem(sn, k, v)
            msg.append("%s>> %s" % (k, v))
            if (keywords != [""] and isinstance(v, dict)):
                for w in keywords:
                    if (w in v and bool(v[w])):
                        result = self.mes.Uploaditem(sn, w, v[w])  # 特殊上传
                        msg.append("%s+> %s" % (w, v[w]))
            if (not result): break
        self.pane_item_dict[pane_id][item]["Data"] = "\r\n".join(msg)
        result = self.mes.Result(sn, True)
        if (result):
            result = adb.adb_patch(self.conf_dict[tagid])
        return result, ''

    def todo_AUDIO(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        if (not adb.palystate): adb.hdmiPlay(self.hdmi_sour, self.hdmi_delay)
        try:
            vmax_limit = self.conf_dict[tagid]["vmax_limit"]
            loudness_limit = self.conf_dict[tagid]["loudness_limit"]
            len = float(self.conf_dict[tagid]["len"])
            psd_enable = int(self.conf_dict[tagid]["psd_enable"])
            p_limit1 = float(self.conf_dict[tagid]["p_limit1"])
            judge1 = list(map(float, [i for i in self.conf_dict[tagid]["judge1"].split(',')]))
            p_limit2 = float(self.conf_dict[tagid]["p_limit2"])
            judge2 = list(map(float, [i for i in self.conf_dict[tagid]["judge1"].split(',')]))
            judge_offset = float(self.conf_dict[tagid]["offset"])
            savewave = int(self.conf_dict[tagid]["save"])
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        try:
            ret_name, rec_dev = self.get_rec(pane_id, tagid)
            if (not ret_name):
                logger.critical("%s %s Deploy[%d] Read Error" % (name, self.lo(tagid), pane_id))
                return False, "RecNotFound"
            self.reclock.acquire()
            try:
                time.sleep(0.2)
                logger.debug("%s Reclock Lock." % self.lo(tagid))
                sound_class = Sound_Man(rec_dev, len)
                result = sound_class.sound_rec()
            except Exception as e:
                logger.critical(e)
                print(e)
            finally:
                self.reclock.release()
                logger.debug("%s Reclock Release." % self.lo(tagid))
            msg = []
            if (result):
                # 最大值判断
                if (vmax_limit):
                    result, vmax, retmsg = sound_class.check_max(vmax_limit)
                    msg.append(retmsg)
                    report_dict["Vmax"] = vmax
                if (result and loudness_limit):
                    result, loudness, retmsg = sound_class.check_loudness(loudness_limit)
                    msg.append(retmsg)
                    report_dict["Loudness"] = loudness
                self.pane_item_dict[pane_id][item]["Data"] = "\r\n".join(msg)
                if (result):
                    if (psd_enable):
                        result, showinfo = sound_class.check_wave(p_limit1, judge1, p_limit2, judge2, judge_offset)
                        # self.pane_item_dict[pane_id][item]["Data"] = tuple(showdata)  # psd显示 def show_plot_class 重入
                    else:
                        msg.append("PSD:Off")
                        self.pane_item_dict[pane_id][item]["Data"] = "\r\n".join(msg)
                if (savewave):
                    sound_class.save_wavefile(f"{tagid} {name}", self.dir_report)
            else:
                msg.append("Record 采集异常")
        except Exception as e:
            logger.critical(e)
            result = False
        return result, " ".join(msg)

    def todo_VIDEO(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            limit = float(self.conf_dict[tagid]["limit"])
            hitlimit = int(self.conf_dict[tagid]["hit_limit"])
            caplen = int(self.conf_dict[tagid]["len"])
            quality = int(self.conf_dict[tagid]["quality"])
            set2k = bool(self.conf_dict[tagid].get("set2k", "1"))  # 兼容旧配置,实际已不使用,hdmi_open采集卡固定分辨率
            savejpg = int(self.conf.getboolean(tagid, "save"))
            sour_str = self.conf_dict[tagid].get("source_id", "")  # 兼容其他视频源配置
            loudness_limit = self.conf_dict[tagid].get("loudness_limit", "")  # 兼容响度一起测试
            if sour_str:
                sour_num = int(sour_str)
                hdmi_delay = int(self.conf_dict["SETTING"]["hdmi_delay"])
                adb.hdmiPlay(sour_num, hdmi_delay)
            else:
                sour_num = int(self.conf_dict["SETTING"]["hdmi_source"])
                hdmi_delay = int(self.conf_dict["SETTING"]["hdmi_delay"])
                if (not adb.palystate): adb.hdmiPlay(sour_num, hdmi_delay)
            samplefile = "Sample%d.pkl" % (sour_num)
        except Exception as e:
            print(e.__traceback__.tb_lineno)
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        if (not os.path.exists(samplefile)):
            logger.critical("Config Sample Not Found %s" % self.lo("Error"))
            return False, ''
        self.hdmilock.acquire()
        try:
            logger.debug("Start Frame Match [Sta%d]%s" % (pane_id + 1, name))
            result = False
            cap = self.hdmi_open(pane_id, set2k)
            showframe = None
            showmsg = []
            # cap = cv2.VideoCapture("./eEver USB Video Device_20210414_164008.avi")
            if cap.isOpened():
                try:
                    ret, frame, msg, frames = self.sample_match(cap, caplen, samplefile, quality, hitlimit)
                    result = ret >= limit
                    showmsg.append("%s MatchRate: %.2f[%s] %s" % (name, ret, limit, msg))
                    logger.info("%s MatchRate: %.2f[%s] %s" % (name, ret, limit, msg))
                    if (not ret):
                        self.save_img_err(frame, pane_id, name, ret)
                    h, w = frame.shape[:2]
                    showframe = np.zeros((h, w * 2, 3), dtype="uint8")
                    showframe[0:h, 0:w] = frames[0]
                    showframe[0:h, w:w * 2] = frame
                    if (savejpg):
                        self.save_img_report(showframe, tagid, name, result)
                except Exception as e:
                    logger.critical(e)
                    print(e)
                finally:
                    cap.release()  # CHJ 20210119
            else:
                logger.critical("Open VideoCapture Error[%d]" % (pane_id + 1))
        except Exception as e:
            logger.critical(e)
            print(e)
        finally:
            self.hdmilock.release()
        if (result and loudness_limit):  # 需同一项中测试音频
            ret_name, rec_dev = self.get_rec(pane_id, "HDMI_AUDIO")
            if ret_name:
                self.reclock.acquire()
                try:
                    logger.debug("HDMI Reclock Lock.")
                    sound_class = Sound_Man(rec_dev, caplen)
                    ret = sound_class.sound_rec()
                    if ret:
                        result, loudness, retmsg = sound_class.check_loudness(loudness_limit)
                        showmsg.append(retmsg)
                        if result:
                            logger.info("%s %s %s" % (name, self.lo(tagid), retmsg))
                        else:
                            logger.error("%s %s %s" % (name, self.lo(tagid), retmsg))
                    else:
                        logger.critical("%s %s Rec Fail") % (name, self.lo(tagid))
                        result = False
                except Exception as e:
                    logger.critical(e)
                    print(e)
                finally:
                    self.reclock.release()
                    logger.debug("HDMI Reclock Release.")
            else:
                logger.critical("%s %s Deploy[%d] Read Error" % (name, self.lo(tagid), pane_id))
                result = False
        if not sour_num == 4:
            adb.hdmiStop()  # 非HDMI采集 测试完关闭
        self.pane_item_dict[pane_id][item]["Data"] = [showframe, " ".join(showmsg)]
        report_dict['Message'] = ";".join(showmsg)
        return result, " ".join(showmsg)

    def todo_IPERF_LAN(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            dhcp = int(self.conf_dict[tagid]["dhcp"])
            close_wifi = int(self.conf_dict[tagid]["close_wifi"])
            timeout = int(self.conf_dict[tagid]["timeout"])
            iperf_para = self.conf_dict[tagid]["para"]
            port = int(self.conf_dict[tagid]["port"])
            iperf_t = int(self.conf_dict[tagid]["count"])
            iperf_retry = int(self.conf_dict[tagid]["iperf_retry"])
            mean_min = float(self.conf_dict[tagid]["mean_min"])
            mean_max = float(self.conf_dict[tagid]["mean_max"])
            peak_min = float(self.conf_dict[tagid]["peak_min"])
            peak_max = float(self.conf_dict[tagid]["peak_max"])
            tx_enable = int(self.conf_dict[tagid]["tx_enable"])
            tx_delay = float(self.conf_dict[tagid]["tx_delay"])
            txmean_min = float(self.conf_dict[tagid]["tx_mean_min"])
            txmean_max = float(self.conf_dict[tagid]["tx_mean_max"])
            txpeak_min = float(self.conf_dict[tagid]["tx_peak_min"])
            txpeak_max = float(self.conf_dict[tagid]["tx_peak_max"])
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        resultmsg = []
        if close_wifi:
            logger.debug("Clear WIFI %s" % adb.sendcmd_recv1("conf"))
        if dhcp:
            logger.debug("Set DHCP %s" % adb.setDhcp())
        # ret = adb.sendcmd_recv1("closeEth", "1")  # 0表示关闭 1表示打开
        # if not ret:
        #     logger.error("%s Enable Eth Error" % (name))
        for i in range(timeout):
            # if (self.pane_all[pane_id]["Abort"]):
            #     return False, "Abort Clicked"
            ret, ip = adb.sendcmd_recv2("getEthIp")
            # ret, ip = adb.sendcmd_recv2("getwifiip")  # 未接网线使用WiFi调试
            if (ret or adb.error or not self.main_run):
                break
            else:
                logger.debug("Check LAN IP Again %d/%d sec" % (i, timeout))
                time.sleep(1)
        if (ret):
            ret = adb.myiperf(ip, port)  # 集成版本iperf2=myIperf
            # ret=adb.runiperf(ip,port)
            if (ret):
                # Rx
                for r in range(iperf_retry + 1):
                    # if (self.pane_all[pane_id]["Abort"]):
                    #     return False, "Abort Clicked"
                    if r:
                        logger.debug("[RxMean]%s [RxPeak]%s Retry again %s" % (mean, peak, r))
                    mean, peak, sec_data, retinfo = self.loop_iperf(ret, ip, port, iperf_t, iperf_para)
                    if (sec_data):
                        logger.debug("%s Rx 吞吐量Mbits/sec %s" % (name, sec_data[:-1]))
                        result = mean_min < mean <= mean_max and peak_min < peak <= peak_max
                    else:
                        result = False
                        logger.error("%s Rx 吞吐量读取数据出错" % (name))
                        _show_log = retinfo.get("log", "")
                        if _show_log:
                            logger.debug(_show_log)
                    if result:
                        break
                resultmsg.append("RxPeak:%s[%s,%s]" % (peak, peak_min, peak_max))
                resultmsg.append("RxMean:%s[%s,%s]" % (mean, mean_min, mean_max))
                report_dict["rxpeak"] = peak
                report_dict["rxmean"] = mean
                # Tx
                if tx_enable and result:
                    _host = retinfo.get("local", "")
                    if (_host):
                        _ser_cmd = "%s.exe -s -p %s -D" % (ret, port)
                        logger.debug("Start %s for %s Tx Delay %ss.." % (_ser_cmd, _host, tx_delay))
                        subprocess.Popen(_ser_cmd, shell=True, stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)  # kill in destroy
                        time.sleep(tx_delay)
                        for r in range(iperf_retry + 1):
                            if r:
                                logger.debug("[TxMean]%s [TxPeak]%s Retry again %s" % (txmean, txpeak, r))
                            txmean, txpeak, txsec_data, txretinfo = adb.myiperf_client(_host, port, iperf_t,
                                                                                       iperf_para)
                            if (txsec_data):
                                logger.debug("%s Tx 吞吐量Mbits/sec %s" % (name, txsec_data[:-1]))
                                result = txmean_min < txmean <= txmean_max and txpeak_min < txpeak <= txpeak_max
                            else:
                                result = False
                                logger.error("%s Tx 吞吐量读取数据出错" % (name))
                                _show_log = txretinfo.get("log", "")
                                if _show_log:
                                    logger.debug(_show_log)
                            if result:
                                break
                        resultmsg.append("TxPeak:%s[%s,%s]" % (txpeak, txpeak_min, txpeak_max))
                        resultmsg.append("TxMean:%s[%s,%s]" % (txmean, txmean_min, txmean_max))
                        report_dict["txpeak"] = txpeak
                        report_dict["txmean"] = txmean
                    else:
                        logger.error("Get PC LAN host Error" % ret)
                        result = False
            else:
                logger.error("Run %s Server Error" % ret)
                result = False
            self.pane_item_dict[pane_id][item]["Data"] = "IP: %s \r\n%s" % (ip, "\r\n".join(resultmsg))
        else:
            logger.error("%s Get LAN IP Timeout" % (name))
            result = False
        if result:
            adb.casePass("ETH_IPERF")
        return result, " ".join(resultmsg)

    def todo_USB_TEST(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            num_limit = self.conf_dict[tagid]["limit"]
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        ret, count = adb.getUsbNum()
        if ret:
            result = int(count) >= int(num_limit)
            logger.debug("%s Detect Count %s" % (name, count))
            self.pane_item_dict[pane_id][item]["Data"] = "Detect Count: %s [Limit:%s]" % (count, num_limit)
            report_dict['count'] = count
            return result, '%s[%s]' % (count, num_limit)
        else:
            return False, "getUsbNum"

    def todo_RESOLUTION(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            num_limit = self.conf_dict[tagid]["limit"]
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        ret, ls = adb.getResolution()
        _count= len(ls)
        result = _count>= int(num_limit)
        logger.debug("%s %s" % (name, ls))
        # logger.info("%s %s %s[%s]"%(name,self.lo(tagid),len(ls),num_limit))
        self.pane_item_dict[pane_id][item]["Data"] = "%s\r\n\r\nSUM:%d [Limit:%s]" % (ls, len(ls), num_limit)
        report_dict['resolution'] = ";".join(ls)
        report_dict['count'] = _count
        return result, '%s[%s]' % (len(ls), num_limit)

    def todo_LED_TEST(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # tagid = "LED_TEST"
        # btime = time.time()
        try:
            auto = int(self.conf_dict[tagid]["auto"])
            timeout = int(self.conf_dict[tagid]["timeout"])
            dute_time = float(self.conf_dict[tagid]["dute_time"])
            exposures = self.conf_dict[tagid]["exposure"].split(",")
            values = self.conf_dict[tagid]["values"].split(",")
            tags = self.conf_dict[tagid]["colors"].lower().split(",")
            savejpg = int(self.conf.getboolean(tagid, "save"))
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        if (auto == 1):
            # 读取识别结果并比较
            result = True
            cap = self.led_cap_open(pane_id)
            if (cap.isOpened()):
                for i, t in enumerate(values):
                    cap.set(15, int(exposures[i]))
                    adb.ledtest(t)
                    time.sleep(dute_time)
                    ret, frame, tagframe, tagdata, = self.led_circle_roi(cap, True, circle_para=(200, 40, 30, 70, 100))
                    if (ret):
                        get, color = self.get_color_name(tagframe)
                    else:
                        get, color = "灭", 'off'
                    judge = color == tags[i]  # 仅支持英文颜色配置
                    result = result and judge
                    if (judge):
                        logger.debug("%s %s %s(%s):%s" % (name, self.lo(tagid), tags[i], t, judge))
                    else:
                        logger.debug("%s %s %s(%s):%s [%s]" % (name, self.lo(tagid), tags[i], t, judge, get))
                        self.save_img_err(frame, pane_id, t, i)
                        break
                show_msg = "%s %s %s(%s):%s" % (name, self.lo(tagid), tags[i], t, judge)
                self.pane_item_dict[pane_id][item]["Data"] = [frame, show_msg]
                if (savejpg):
                    self.save_img_report(frame, tagid, name, result)
            else:
                result = False
                logger.critical("Capture Open Error")
        else:
            askret = {"PASS": False, 'FAIL': False}
            self.blist_ask(item, pane_id, askret)
            while self.main_run and not adb.error and not (askret["PASS"] or askret['FAIL']):
                for v in values:
                    adb.ledtest(v)
                    time.sleep(dute_time)
            result = askret["PASS"]
        # self.pane_item_dict[pane_id][item]["Data"] = "Detect :%s\r\n Require :%s"%(data,keycodes)
        adb.ledfinish()
        # if (result):
        #     logger.warning("%s %s PASS" % (name, self.lo(tagid)))
        # else:
        #     logger.error("%s %s FAIL" % (name, self.lo(tagid)))
        # elpstime = round(time.time() - btime, 3)
        # logger.info("Elapsed Time: %.3f s" % (elpstime))
        # self.pane_dict_report[pane_id][tagid] = {"result": result, "elpstime": elpstime}
        return result, ''

    def todo_BUTTON_TEST(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # tagid = "BUTTON_TEST"
        btime = time.time()
        try:
            auto = int(self.conf_dict[tagid]["auto"])
            dute = float(self.conf_dict[tagid]["dute"])
            timeout = int(self.conf_dict[tagid]["timeout"])
            keycodes = self.conf_dict[tagid]["keycodes"]
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        if (auto == 1):
            try:
                # 控制自动按键,波特率9600打开串口，发送“BUTTON_ON” 按键开启 ，串口返回“OK”；发送“BUTTON_OF”F 按键关闭，串口返回“OK
                ports = self.conf_dict[tagid]["ports"].split(',')
                ctl_m = control_com(ports[pane_id])
                ctl_m.open()
                time.sleep(dute)
                ctl_m.click()
            except:
                logger.critical("Button Control COM Error")
            finally:
                ctl_m.close()
            result, data = adb.buttontest()  # buttonResult_SUCCESS_19,20,21,22,8,9,10,11
            if (result):
                for k in keycodes.split(','):  # 有一个要求的按键不存在即FAIL
                    if not k in data:
                        result = False
                        break
        elif (auto == 2):
            result, data = adb.buttontest()  # buttonResult_SUCCESS_19,20,21,22,8,9,10,11
            if (result):
                for k in keycodes.split(','):  # 有一个要求的按键不存在即FAIL
                    if not k in data:
                        result = False
                        break
            if (not result):
                # screenwidth = self.master.winfo_screenwidth()
                # screenheight = self.master.winfo_screenheight()
                # width = 300
                # height = 100
                # size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                # _set = {"title":name,"geometry": size,"func":adb.buttontest,"keycodes":keycodes,"timeout":timeout}
                _set = {"title": name, "func": adb.buttontest, "keycodes": keycodes, "timeout": timeout}
                boxresult = {"Result": False, "Data": ""}
                result, data = self.show_box_class(Func_Loop_Box, setting=_set, result=boxresult)
                # wait_box=Func_Loop_Box(self.master,setting=_set, result=boxresult)
                # self.master.wait_window(wait_box)  # 停止执行 阻塞 该行代码
                # result = boxresult["Result"]
                # data = boxresult["Data"]
        else:
            elpstime = round(time.time() - btime, 3)
            while self.main_run and elpstime < timeout:
                result, data = adb.buttontest()  # buttonResult_SUCCESS_19,20,21,22,8,9,10,11
                if (result):
                    for k in keycodes.split(','):  # 有一个要求的按键不存在即FAIL
                        if not k in data:
                            result = False
                            break
                if (result):
                    break
                else:
                    time.sleep(0.5)
                    # elpstime = round(time.time() - btime, 3)
                    # self.blist_msg(item,pane_id,"等待按钮%d"%(timeout-elpstime))  # 动态显示
            # self.blist_msg(item,pane_id,self.lo(tagid))  # 动态显示
        self.pane_item_dict[pane_id][item]["Data"] = "Keycode Detect :%s\r\n Require :%s" % (data, keycodes)
        # if (result):
        #     logger.warning("%s %s %s PASS" % (name, self.lo(tagid), data))
        # else:
        #     logger.error("%s %s %s[%s] FAIL" % (name, self.lo(tagid), data, keycodes))
        # elpstime = round(time.time() - btime, 3)
        # logger.info("Elapsed Time: %.3f s" % (elpstime))
        # self.pane_dict_report[pane_id][tagid] = {"result": result, "elpstime": elpstime}
        return result, '%s' % data if result else '%s[%s]' % (data, keycodes)

    def todo_BASIC_TEST(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # tagid = "BASIC_TEST"
        # btime = time.time()
        try:
            cpu_type_match = self.conf_dict[tagid]["cpu_type_match"]
            cpu_temp_min = self.conf_dict[tagid]["cpu_temp_min"]
            cpu_temp_max = self.conf_dict[tagid]["cpu_temp_max"]
            ddr_size_limit = self.conf_dict[tagid]["ddr_size_limit"]
            emmc_size_limit = self.conf_dict[tagid]["emmc_size_limit"]
            hw_id_match = self.conf_dict[tagid]["hw_id_match"]
            hw_ver_match = self.conf_dict[tagid]["ver_match"]
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        msg = []
        err = []
        result = True
        if cpu_type_match:
            ret, data = adb.getCpuType()
            report_dict["CPU"] = data
            if ret and cpu_type_match in data:
                msg.append("CPU:%s" % data)
            else:
                result = False
                msg.append("CPU:%s[%s]" % (data, cpu_type_match))
                err.append("CPU:%s[%s]" % (data, cpu_type_match))
        if cpu_temp_min and cpu_temp_max:
            ret, data = adb.getCpuTemp()
            report_dict["Temp"] = data
            if ret and float(cpu_temp_max) >= float(data) >= float(cpu_temp_min):
                msg.append("Temp:%s" % data)
            else:
                result = False
                msg.append("Temp:%s[%s,%s]" % (data, cpu_temp_min, cpu_temp_max))
                err.append("Temp:%s[%s,%s]" % (data, cpu_temp_min, cpu_temp_max))
        if ddr_size_limit:
            ret, data = adb.getDDR()
            report_dict["DDR"] = data
            if ret and int(data) >= int(ddr_size_limit):
                msg.append("DDR:%s" % data)
            else:
                result = False
                msg.append("DDR:%s[%s]" % (data, ddr_size_limit))
                err.append("DDR:%s[%s]" % (data, ddr_size_limit))
        if emmc_size_limit:
            ret, data = adb.getEMMC()
            report_dict["EMMC"] = data
            if ret and int(data) >= int(emmc_size_limit):
                msg.append("EMMC:%s" % data)
            else:
                result = False
                msg.append("EMMC:%s[%s]" % (data, emmc_size_limit))
                err.append("EMMC:%s[%s]" % (data, emmc_size_limit))
        if hw_id_match:
            ret, data = adb.gethwid()
            report_dict["ID"] = data
            if ret and hw_id_match in data:
                msg.append("ID:%s" % data)
            else:
                result = False
                msg.append("ID:%s[%s]" % (data, hw_id_match))
                err.append("ID:%s[%s]" % (data, hw_id_match))
        if hw_ver_match:
            ret, data = adb.gethwver()
            report_dict["VER"] = data
            if ret and hw_ver_match in data:
                msg.append("VER:%s" % data)
            else:
                result = False
                msg.append("VER:%s[%s]" % (data, hw_ver_match))
                err.append("VER:%s[%s]" % (data, hw_ver_match))

        logger.debug("%s %s" % (name, " ".join(msg)))

        self.pane_item_dict[pane_id][item]["Data"] = "\r\n".join(msg)
        # if (result):
        #     logger.warning("%s %s PASS" % (name, self.lo(tagid)))
        # else:
        #     logger.error("%s %s %s FAIL" % (name, self.lo(tagid), " ".join(err)))

        # elpstime = round(time.time() - btime, 3)
        # logger.info("Elapsed Time: %.3f s" % (elpstime))
        # report["result"] = result
        # report["elpstime"] = elpstime
        # self.pane_dict_report[pane_id][tagid] = report
        return result, "" if result else " ".join(err)

    def todo_SCANNER(self, name, pane_id, item, tagid, report_dict, *args):
        showsn = self.pane_all[pane_id]["BoxidVstr"]
        adb = self.pane_all[pane_id]["Class"]
        scan_now = ''  # 界面sn显示,checksn统一为扫入字符串
        _msg = []  # 测试项内容显示
        try:
            mode = self.conf_dict["SCANNER"]["mode"]
            getkeys = self.conf_dict["SCANNER"]["getkeys"].upper()
            retry = int(self.conf_dict["SCANNER"]["retry"])
            len_limit = int(self.conf_dict["SCANNER"]["len"])
            match = self.conf_dict[tagid]["match"]
            sn_match = self.conf_dict[tagid]["sn_match"]
            boxid_match = self.conf_dict[tagid]["boxid_match"]
            emac_match = self.conf_dict[tagid]["emac_match"]
            wmac_match = self.conf_dict[tagid]["wmac_match"]
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        # 开始录入模式(match在该处处理)
        if (mode in ["usid", "mac", "wmac", "fbxserial", "oem"]):  # unifykey的其他值读取,目前用于调试
            judge, scan_now = adb.sendcmd_recv2("readKeyValue", mode)
            logger.debug("Read %s=%s %s" % (mode, scan_now, judge))
            logger.warning("[DUT]%s %s %s" % (
                scan_now, adb.sendcmd_recv2("readKeyValue", 'mac'), adb.sendcmd_recv2("readKeyValue", 'wmac')))
        elif (mode == "sboxid"):  # unifykey的读取sboxid
            judge, scan_now = adb.sendcmd_recv2("readKeyValue", mode)
            logger.debug("Read %s=%s %s" % (mode, scan_now, judge))
            report_dict["BOXID"] = scan_now
        elif (mode == 'SN.txt'):  # 读取临时SN.txt
            scan_now = adb.getTempSN()
        elif (mode == 'InputSN'):  # 弹窗输入SN
            tip = "%s USB_%s" % (self.lo(tagid), self.pane_all[pane_id]["Tid"])
            self.scanlock.acquire()
            self.set_guide("WaitScan", "SN %s [%s]" % (tip, name))  # 带顶部向导指示
            scan_now = self.show_box(name + " SN", tip)
            if (scan_now):
                for r in range(retry):
                    logger.debug("[Scan]%s" % scan_now)
                    if len(scan_now) == len_limit:
                        report_dict["SN"] = scan_now
                        break
                    else:
                        scan_now = self.show_box(name + " SN", tip)  # 增加重试扫码
            self.set_guide()  # 带顶部向导指示
            self.scanlock.release()
        elif (mode == 'InputBoxid'):  # 弹窗输入Boxid
            tip = "%s USB_%s" % (self.lo(tagid), self.pane_all[pane_id]["Tid"])
            self.scanlock.acquire()
            self.set_guide("WaitScan", "Boxid %s [%s]" % (tip, name))
            scan_now = self.show_box(name + " Boxid", tip)
            if (scan_now):
                for r in range(retry):
                    logger.debug("[Scan]%s" % scan_now)
                    if len(scan_now) == len_limit:
                        report_dict["BOXID"] = scan_now
                        break
                    else:
                        scan_now = self.show_box(name + " Boxid", tip)  # 增加重试扫码
            self.set_guide()
            self.scanlock.release()
        elif (mode == "2"):  # 模式2 流程需要重新扫码 串口接收 AutoBurnKey使用
            self.scanlock.acquire()
            if (self.isRemove(pane_id) or not self.main_run):  # 强制中断
                logger.debug("[Abort]SCANNER %s" % name)
                self.scanlock.release()
                return False, ''
            try:
                portname = self.pane_all[pane_id]["Tid"]
                self.set_guide("WaitScan", "USB_%s [%s]" % (portname, name))
                port = self.conf_dict["SCANNER"]["port"]
                scanner = scan_com(port)
                if (scanner.open()):
                    ret = False
                    while not ret:
                        ret, value = scanner.scan(3)
                        if (ret):
                            break
                        if (self.isRemove(pane_id) or not self.main_run):  # 强制中断
                            value = b""
                            logger.debug("[Abort]Scanning %s" % name)
                            break
                    scan_now = value.decode().strip()
                    scanner.close()
                else:
                    logger.critical("Scanner Open Error 扫码设备错误")
                    scan_now = None
            except Exception as e:
                scan_now = None
                print(e)
            finally:
                self.set_guide()
                self.scanlock.release()
        elif (mode == "ScanBoxid"):  # 使用扫码模组扫入Boxid
            ret, port = self.get_com(pane_id, tagid)  # COM scan
            if (not ret):
                logger.critical("%s %s Deploy[%d] Read Error" % (name, self.lo(tagid), pane_id))
                return False, ''
            scanner = scan_com(port)
            if (scanner.open()):
                for i in range(retry):
                    value = scanner.trig_recv()
                    if (len(value) >= len_limit):
                        if (match):
                            if (match in value):
                                break
                        else:
                            break
                scan_now = value
                scanner.close()
                if (scan_now):
                    report_dict["BOXID"] = scan_now
            else:
                logger.critical("Scanner Open Error 扫码设备错误")
                scan_now = None
        elif (mode == "ScanSN"):  # 使用扫码模组扫入SN
            ret, port = self.get_com(pane_id, tagid)  # COM scan
            if (not ret):
                logger.critical("%s %s Deploy[%d] Read Error" % (name, self.lo(tagid), pane_id))
                return False, ''
            scanner = scan_com(port)
            if (scanner.open()):
                for i in range(retry):
                    value = scanner.trig_recv()
                    if (len(value) >= len_limit):
                        if (match):
                            if (match in value):
                                break
                        else:
                            break
                scan_now = value
                scanner.close()
            else:
                logger.critical("Scanner Open Error 扫码设备错误")
                scan_now = None
        elif (mode == "6"):  # 模式6 流程需要重新扫码  AutoRouterCouple从路由板子读取SN
            for i in range(retry):
                scan_now = adb.telnet_gpon140_cmd("prolinecmd xponsn display")
                logger.debug("[Router]xponsn:%s" % scan_now)
                judge = bool(scan_now)
                if (judge): break
        elif (mode == "77"):  # freebox通过boxid获取emac,然后仍然使用emac过站
            scan_now = self.mes.GetByboxid(name)
        elif (mode == "7"):  # 模式7 使用GetKeys切换过站SN
            scan_now = self.mes.GetKeys(name, 1)  # freebox 使用emac过站
        else:  # 其他模式=模式0
            scan_now = name
            logger.error("%s %s mode=%s" % (name, self.lo(tagid), mode))
        # 界面显示
        scan_now = scan_now.strip()
        showsn.set(scan_now)
        # 按模式读取扫码记录,对比sn,mac
        mesjudge = self.mes.CheckSN(scan_now)
        report_dict['scan'] = scan_now  # MES使用录入进行数据上传与过站
        if (getkeys == "SN"):
            _sn, _emac, _wmac = self.mes.GetMac(scan_now, 1)
            report_dict["SN"] = _emac
            report_dict["EMAC"] = _sn
        elif (getkeys == "EMAC"):
            _sn, _emac, _wmac = self.mes.GetMac(scan_now, 1)
            report_dict["EMAC"] = _emac
        elif (getkeys == "WMAC"):
            _sn, _emac, _wmac = self.mes.GetMac(scan_now, 2)
            report_dict["WMAC"] = _wmac
        elif (getkeys == "EMAC,WMAC"):
            _sn, _emac, _wmac = self.mes.GetMac(scan_now, 3)
            report_dict["EMAC"] = _emac
            report_dict["WMAC"] = _wmac
        #
        result = bool(scan_now) and mesjudge
        _msg.append("Scanner: %s" % scan_now)
        _msg.append("Load : %s " % name)
        _msg.append("MES: %s" % mesjudge)
        # 最后的默认兼容处理
        if not "BOXID" in report_dict:
            report_dict['BOXID'] = name  # 默认adb读取name为BOXID
        if not "SN" in report_dict:  # 默认scan_now录入为SN
            report_dict['SN'] = scan_now
        # 配置match校验
        conf_match = {"SN": sn_match, "BOXID": boxid_match, "EMAC": emac_match, "WMAC": wmac_match}
        for nk, _m in conf_match.items():
            if (result and nk in report_dict):  # 配置xx_match的校验
                if (_m):
                    result = sn_match in report_dict[nk]
                    _msg.append("%s:%s [%s] %s" % (nk, report_dict[nk], _m, result))
                    if (not result):
                        logger.error("%s %s %s:%s[%s] Not Match" % (name, self.lo(tagid), nk, report_dict[nk], _m))
                        break
                else:
                    _msg.append("%s:%s" % (nk, report_dict[nk]))
        self.pane_item_dict[pane_id][item]["Data"] = "\r\n".join(_msg)  # 详细内容显示
        # 提前自动执行预触发,混合产测APK的多线程
        for p in self.plan:
            if (p == "BT_TEST"):
                try:
                    btname = self.conf_dict["BT_TEST"]["name"]
                    if (" " in btname):
                        btname = "'%s'" % btname
                    connect = int(self.conf_dict["BT_TEST"]["connect"])
                    ret = adb.bt_begin(btname, connect)
                    logger.debug("%s %s Begin..%s" % (name, self.lo("BT_TEST"), ret))
                except Exception as e:
                    print(e)
            if (p == "WIFI_5"):
                try:
                    ssid = self.conf_dict["WIFI_5"]["ssid"]
                    key = self.conf_dict["WIFI_5"]["key"]
                    type = self.conf_dict["WIFI_5"]["type"]
                    connect = int(self.conf_dict["WIFI_5"]["connect"])
                    ret = adb.wifi_begin(ssid, key, type, connect)
                    logger.debug("%s %s Begin..%s" % (name, self.lo("WIFI_5"), ret))
                except Exception as e:
                    print(e)
            if (p == "WIFI_24"):
                try:
                    ssid = self.conf_dict["WIFI_24"]["ssid"]
                    key = self.conf_dict["WIFI_24"]["key"]
                    type = self.conf_dict["WIFI_24"]["type"]
                    connect = int(self.conf_dict["WIFI_24"]["connect"])
                    ret = adb.wifi_begin(ssid, key, type, connect)
                    logger.debug("%s %s Begin..%s" % (name, self.lo("WIFI_24"), ret))
                except Exception as e:
                    print(e)
        # print(report_dict)
        return result, '%s[%s]' % (scan_now, name)

    def todo_WRITE_BOXID(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            pass
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        if not "SCANNER" in self.pane_dict_report[pane_id]:
            return False, 'Config 未配置%s' % (self.lo("SCANNER"))
        # result = True
        _msg = []
        _show_msg = []
        if ("BOXID" in self.pane_dict_report[pane_id]["SCANNER"]):
            _boxid = self.pane_dict_report[pane_id]["SCANNER"]["BOXID"]
            result = adb.setBoxid(_boxid, check=True)
            _msg.append("[BOXID]%s %s" % (_boxid, result))
            if not result:
                _show_msg.append("Illegal 非法条码或写入错误")
        else:
            logger.warning("NotFound Boxid..")
            result = False
            _show_msg.append("NotFound")
        self.pane_item_dict[pane_id][item]["Data"] = "\r\n".join(_msg)  # 详细内容显示
        return result, " ".join(_show_msg)

    def todo_FTP(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # tagid = "FTP"
        # btime = time.time()
        try:
            host = self.conf_dict[tagid]["host"]
            port = int(self.conf_dict[tagid]["port"])
            timeout = int(self.conf_dict[tagid]["timeout"])
            user = self.conf_dict[tagid]["user"]
            key = self.conf_dict[tagid]["key"]
            sub_dir = self.conf_dict[tagid]["sub_dir"]
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        try:
            local_path = self.save_report(pane_id, True)  # 在测试序列中,FAIL的流程无法跑到FTP测试项
            ftp = FTP()
            # ftp.encoding="utf-8"
            ftp.connect(host, port, timeout=timeout)  # 第一个参数可以是ftp服务器的ip或者域名，第二个参数为ftp服务器的连接端口，默认为21
            ftp.login(user, key)  # 匿名登录直接使用ftp.login()
            # ftp.set_pasv(False)
            ftp.cwd("./%s" % sub_dir)  # 切换目录
            _path, filename = os.path.split(local_path)
            logger.debug("%s %s Ready for upload.." % (name, self.lo(tagid)))
            try:
                with open(local_path, "rb") as fp:
                    ftp.storbinary("STOR {}".format(filename), fp)
                result = True
            except Exception as e:
                logger.critical("Upload Files Error")
                logger.critical(e)
                result = False
            logger.debug("%s %s Upload Finish" % (name, self.lo(tagid)))
            ftp.quit()
        except Exception as e:
            logger.critical(e)
            result = False
        # self.pane_item_dict[pane_id][item]["Data"] = " SN: %s\r\nMAC: %s" % (getsn, getmac)
        # if (result):
        #     logger.warning("%s %s PASS" % (name, self.lo(tagid)))
        # else:
        #     logger.error("%s %s FAIL" % (name, self.lo(tagid)))
        # elpstime = round(time.time() - btime, 3)
        # logger.info("Elapsed Time: %.3f s" % (elpstime))
        # self.pane_dict_report[pane_id][tagid] = {"result": result, "elpstime": elpstime}
        return result, ''

    def todo_HDMI_VOLT(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # tagid = "HDMI_VOLT"
        # btime = time.time()
        try:
            # portlist = self.conf_dict[tagid]["portlist"]
            # port = portlist.split(',')[pane_id]
            volt_min = float(self.conf_dict[tagid]["volt_min"])
            volt_max = float(self.conf_dict[tagid]["volt_max"])
            cec_retry = int(self.conf_dict[tagid]["cec_retry"])
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        try:
            # 检测电压
            ret, port = self.get_com(pane_id, tagid)  # COM scan
            if (not ret):
                logger.critical("%s %s Deploy[%d] Read Error" % (name, self.lo(tagid), pane_id))
                return False, ''
            volt_m = volt_com(port)
            volt_m.open()
            time.sleep(0.2)
            value = volt_m.getVolt_H()
            if (value == None):
                pass
            else:
                time.sleep(0.2)
                value = volt_m.getVolt_H()
            # CEC信号测试
            cec_judge = False
            for r in range(cec_retry):
                adb.cecTest()  # 底层有2秒延时后发出信号,产测APK5.0.34.2以后更新1.5秒
                time.sleep(1)
                volt_m.ser.write("C".encode())
                time.sleep(1)
                ret = volt_m.ser.readline().strip()
                if (b"" == ret):
                    time.sleep(1)
                    ret = volt_m.ser.readline().strip()
                out = ret.decode()
                logger.debug(out.strip())
                if ("CEC" in out):
                    cec_judge = "_P" in out
                    if (cec_judge):
                        break
            volt_m.close()
            result = cec_judge and volt_min <= value <= volt_max
            logger.info("%s %s Voltage:%s[%s,%s] CEC:%s" % (name, self.lo(tagid), value, volt_min, volt_max, cec_judge))
        except Exception as e:
            value = None
            result = False
            logger.critical(e)
        self.pane_item_dict[pane_id][item]["Data"] = "Voltage:%s[%s,%s]\r\nCEC:%s" % (
            value, volt_min, volt_max, cec_judge)
        report_dict['voltage'] = value
        report_dict['cec'] = cec_judge
        # if (result):
        #     logger.warning("%s %s Voltage:%s CEC:%s PASS" % (name, self.lo(tagid), value, cec_judge))
        # else:
        #     logger.error(
        #         "%s %s Voltage:%s[%s,%s] CEC:%s FAIL" % (name, self.lo(tagid), value, volt_min, volt_max, cec_judge))
        # elpstime = round(time.time() - btime, 3)
        # logger.info("Elapsed Time: %.3f s" % (elpstime))
        # self.pane_dict_report[pane_id][tagid] = {"result": result, "elpstime": elpstime, 'voltage': value,
        #                                          "cec": cec_judge}
        return result, 'Voltage:%s CEC:%s' % (value, cec_judge) if result else "Voltage:%s[%s,%s] CEC:%s" % (
            value, volt_min, volt_max, cec_judge)

    def todo_DVB_VOLT(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # tagid = "DVB_VOLT"
        # btime = time.time()
        try:
            # portlist = self.conf_dict[tagid]["portlist"]
            # port = portlist.split(',')[pane_id]
            cmd_list = self.conf_dict[tagid]["cmd_list"].split(',')
            volt_retry = int(self.conf_dict[tagid]["volt_retry"])
            dute_delay = float(self.conf_dict[tagid]["dute_delay"])
            enable_22k = int(self.conf_dict[tagid]["enable_22k"])
            volt_min_list = self.conf_dict[tagid]["volt_min_list"].split(',')
            volt_max_list = self.conf_dict[tagid]["volt_max_list"].split(',')
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        msg = []
        result = True
        try:
            self.dvblock.acquire()  # dvb电压加资源锁,优化效果好像不明显
            if (cmd_list and len(cmd_list) > 1):
                ret, port = self.get_com(pane_id, tagid)  # COM scan
                if (not ret):
                    logger.critical("%s %s Deploy[%d] Read Error" % (name, self.lo(tagid), pane_id))
                    return False, ''
                volt_m = volt_com(port)
                volt_m.open()
                time.sleep(0.2)
                for i, cmd in enumerate(cmd_list):
                    # 输出电压
                    adb.dvb_volt(cmd)
                    # 检测电压
                    volt_min = float(volt_min_list[i])
                    volt_max = float(volt_max_list[i])
                    for j in range(volt_retry):
                        time.sleep(dute_delay)
                        value = volt_m.getVolt_D()
                        if (value == None):
                            pass
                        else:
                            judge = volt_min <= value <= volt_max
                            if (judge):
                                break
                    msg.append("%s[%s,%s]" % (value, volt_min, volt_max))
                    result = result and judge
                    logger.info(
                        "%s %s CMD:%s Voltage:%s[%s,%s]" % (name, self.lo(tagid), cmd, value, volt_min, volt_max))
                    if (enable_22k and 12 <= value <= 14):  # DVB输出13v的时候同时检测22k
                        check22k = volt_m.getK()
                        result = result and check22k
                        logger.info("%s %s 22K:%s" % (name, self.lo(tagid), check22k))
                        msg.append("22K[%s]" % check22k)
                volt_m.close()
            else:
                result = False
                logger.critical("DVB_VOLT Config cmd_list Not Match")
        except Exception as e:
            result = False
            logger.critical(e)
        finally:
            pass
            self.dvblock.release()
        self.pane_item_dict[pane_id][item]["Data"] = "\r\n".join(msg)
        report_dict['Message'] = ",".join(msg)
        # if (result):
        #     logger.warning("%s %s Voltage:%s PASS" % (name, self.lo(tagid), ",".join(msg)))
        # else:
        #     logger.error("%s %s Voltage:%s FAIL" % (name, self.lo(tagid), ",".join(msg)))
        # elpstime = round(time.time() - btime, 3)
        # logger.info("Elapsed Time: %.3f s" % (elpstime))
        # self.pane_dict_report[pane_id][tagid] = {"result": result, "elpstime": elpstime, 'msg': ",".join(msg)}
        return result, "Voltage:%s" % (",".join(msg))

    def todo_DVB(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            playlist = self.conf_dict[tagid]["playlist"].split(",")
            sampletag = self.conf_dict[tagid]["sampletag"]
            samplefile = "SampleDVB%s.pkl" % sampletag
            cap_delay = float(self.conf_dict[tagid]["cap_delay"])
            timeout = int(self.conf_dict[tagid]["timeout"])
            timelen = int(self.conf_dict[tagid]["len"])
            limit = float(self.conf_dict[tagid]["limit"])
            hitlimit = int(self.conf_dict[tagid]["hit_limit"])
            quality = int(self.conf_dict[tagid]["quality"])
            savejpg = int(self.conf.getboolean(tagid, "save"))
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        if (not os.path.exists(samplefile)):
            logger.critical("Config Sample Not Found %s" % self.lo("Error"))
            return False, ''
        result = False
        # 检测视频播放
        try:
            if (adb.dvb_open()):
                time.sleep(1)
                for i in playlist:
                    logger.debug("%s %s DVB[%s] Play.." % (name, self.lo(tagid), i))
                    if (adb.dvb_play(i)):
                        time.sleep(cap_delay)
                        logger.debug("%s %s DVB[%s] Start Capture.." % (name, self.lo(tagid), i))
                        self.hdmilock.acquire()
                        logger.debug("Start Frame Match [Sta%d]%s" % (pane_id + 1, name))
                        result = False
                        cap = self.hdmi_open(pane_id)
                        showmsg = []
                        if cap.isOpened():
                            try:
                                ret, frame, msg, frames = self.sample_match(cap, timelen, samplefile, quality, hitlimit)
                                result = ret >= limit
                                showmsg.append("%s MatchRate: %.2f[%s] %s" % (name, ret, limit, msg))
                                logger.info("%s MatchRate: %.2f[%s] %s" % (name, ret, limit, msg))
                                if (not ret):
                                    self.save_img_err(frame, pane_id, name, ret)
                                h, w = frame.shape[:2]
                                showframe = np.zeros((h, w * 2, 3), dtype="uint8")
                                showframe[0:h, 0:w] = frames[0]
                                showframe[0:h, w:w * 2] = frame
                                if (savejpg):
                                    self.save_img_report(showframe, tagid, name, result)
                                self.pane_item_dict[pane_id][item]["Data"] = [showframe, " ".join(showmsg)]
                            except Exception as e:
                                logger.critical(e)
                                print(e)
                            finally:
                                cap.release()  # CHJ 20210119
                        else:
                            logger.critical("Open VideoCapture Error[%d]" % (pane_id + 1))
                        self.hdmilock.release()
                        if (result):
                            for j in range(timeout):
                                result = adb.dvb_result(i)
                                if (result):
                                    logger.debug("%s %s DVB[%s] Return PASS" % (name, self.lo(tagid), i))
                                    break
                                else:
                                    time.sleep(1)
                            if (not result):
                                logger.critical("%s %s DVB[%s] Return FAIL" % (name, self.lo(tagid), i))
                        else:
                            break
                        report_dict[f"DVB{i}"] = " ".join(showmsg)
            else:
                logger.critical("%s %s DVB Open Error" % (name, self.lo(tagid)))
            # adb.dvb_close()  # DVB测试项由发2次close指令修改为只发1次指令,由厂测APK确保dvb关闭(需测稳定性) 2022.10.19
        except Exception as e:
            logger.critical(e)
        finally:
            adb.dvb_close()
        return result, ''

    def todo_IR_TEST(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # tagid = "IR_TEST"
        # btime = time.time()
        try:
            # portlist = self.conf_dict[tagid]["portlist"]
            retry = int(self.conf_dict[tagid]["retry"])
            # if (portlist):
            #     port = portlist.split(',')[pane_id]
            timeout = self.conf_dict[tagid]["timeout"]
            match = self.conf_dict[tagid]["match"]
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        # if (portlist):  # 启用外部模块
        try:
            ret, port = self.get_com(pane_id, tagid)  # COM scan
            if (not ret):
                logger.critical("%s %s Deploy[%d] Read Error" % (name, self.lo(tagid), pane_id))
                return False, ''
            ir = ir_com(port)
            ir.open()
            logger.debug("IR Module %s Send:%s" % (port, match))
            for i in range(retry):
                ir.sendkey(match)
                time.sleep(0.2)
                ret, code = adb.getIrKeyEvent(timeout=int(timeout))
                result = match in code
                if (result):
                    break
                else:
                    logger.debug("IR Module %s Send:%s Again[%d]" % (port, match, i + 2))
                    time.sleep(0.5)
            ir.close()
        except Exception as e:
            logger.critical(e)
        ret, code = adb.getIrKeyEvent(timeout=int(timeout))
        result = match in code
        logger.debug("%s KeyCode %s [%s]" % (name, code, match))
        # logger.info("%s %s %s[%s]"%(name,self.lo(tagid),len(ls),num_limit))
        self.pane_item_dict[pane_id][item]["Data"] = "KeyCode: %s        \r\n Match : %s" % (code, match)
        report_dict['keycode'] = code
        # if (result):
        #     logger.warning("%s %s %s[%s] PASS" % (name, self.lo(tagid), code, match))
        # else:
        #     logger.error("%s %s %s[%s] FAIL" % (name, self.lo(tagid), code, match))
        # elpstime = round(time.time() - btime, 3)
        # logger.info("Elapsed Time: %.3f s" % (elpstime))
        # self.pane_dict_report[pane_id][tagid] = {"result": result, "elpstime": elpstime, 'keycode': code}
        return result, '%s[%s]' % (code, match)

    def todo_BT_TEST(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # tagid = "BT_TEST"
        # btime = time.time()
        try:
            btname = self.conf_dict[tagid]["name"]
            if (" " in btname):
                btname = "'%s'" % btname
            retry = int(self.conf_dict[tagid]["retry"])
            rssi_min = float(self.conf_dict[tagid]["rssi_min"])
            rssi_max = float(self.conf_dict[tagid]["rssi_max"])
            timeout = int(self.conf_dict[tagid]["timeout"])
            connect = int(self.conf_dict[tagid]["connect"])
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        rssi = ''
        if (connect):
            logger.debug("%s Buletooth:%s Connect.." % (name, btname))
            ret = adb.bttest(btname)
            if (ret):
                ret, rssi = adb.getbttestres(timeout)
                if (ret):
                    logger.debug("%s Name:%s RSSI:%s[%s,%s]" % (name, btname, rssi, rssi_min, rssi_max))
                    result = rssi_min <= float(rssi) <= rssi_max
                    if (not result):
                        ret, rssi = adb.getwifirssi()
                        logger.debug("%s Name:%s RSSI:%s[%s,%s] Again" % (name, btname, rssi, rssi_min, rssi_max))
                        result = rssi_min <= float(rssi) <= rssi_max
                else:
                    logger.error("%s Get %s RSSI Error" % (name, btname))
                    result = False
                self.pane_item_dict[pane_id][item]["Data"] = "Name: %s \r\n RSSI : %s [%s,%s]" % (
                    btname, rssi, rssi_min, rssi_max)
            else:
                logger.error("%s Get IP[%s] Timeout" % (name, btname))
                result = False
        else:
            logger.debug("%s Scan:%s .." % (name, btname))
            for r in range(retry):
                ret, rssi = adb.btscan(btname, timeout)
                if (ret):
                    logger.debug("%s Scan %s RSSI:%s[%s,%s]" % (name, btname, rssi, rssi_min, rssi_max))
                    result = rssi_min <= float(rssi) <= rssi_max
                    if (result):
                        break
                else:
                    result = False
            self.pane_item_dict[pane_id][item]["Data"] = " Name: %s \r\n RSSI : %s [%s,%s]" % (
                btname, rssi, rssi_min, rssi_max)
        report_dict['rssi'] = rssi
        # if (result):
        #     logger.warning("%s %s RSSI:%s PASS" % (name, self.lo(tagid), rssi))
        # else:
        #     logger.error("%s %s RSSI:%s[%s,%s] FAIL" % (name, self.lo(tagid), rssi, rssi_min, rssi_max))
        # elpstime = round(time.time() - btime, 3)
        # logger.info("Elapsed Time: %.3f s" % (elpstime))
        # self.pane_dict_report[pane_id][tagid] = {"result": result, "elpstime": elpstime, 'rssi': rssi}
        return result, "RSSI:%s" % rssi if result else "RSSI:%s[%s,%s]" % (rssi, rssi_min, rssi_max)

    def todo_WIFI_5(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            ssid = self.conf_dict[tagid]["ssid"]
            key = self.conf_dict[tagid]["key"]
            type = self.conf_dict[tagid]["type"]
            retry = int(self.conf_dict[tagid]["retry"])
            rssi_min = float(self.conf_dict[tagid]["rssi_min"])
            rssi_max = float(self.conf_dict[tagid]["rssi_max"])
            timeout = int(self.conf_dict[tagid]["timeout"])
            connect = int(self.conf_dict[tagid]["connect"])
            iswifi6 = int(self.conf_dict[tagid].get("is_wifi6", 0))
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        rssi = ''
        if (connect):
            ret = adb.conwifi(ssid, key, type)
            if (ret):
                ret, ip = adb.again(adb.getwifiip, retry, timeout)
                if (ret):
                    ret, rssi = adb.getwifirssi()
                    if (ret):
                        logger.debug("%s IP:%s RSSI:%s[%s,%s]" % (name, ip, rssi, rssi_min, rssi_max))
                        result = rssi_min <= float(rssi) <= rssi_max
                        if (not result):
                            ret, rssi = adb.getwifirssi()
                            logger.debug("%s IP:%s RSSI:%s[%s,%s] Again" % (name, ip, rssi, rssi_min, rssi_max))
                            result = rssi_min <= float(rssi) <= rssi_max
                    else:
                        logger.error("%s Get %s[%s] RSSI Error" % (name, ssid, ip))
                        result = False
                    self.pane_item_dict[pane_id][item]["Data"] = "IP: %s \r\n RSSI : %s [%s,%s]" % (
                        ip, rssi, rssi_min, rssi_max)
                else:
                    logger.error("%s Get IP[%s] Timeout" % (name, ssid))
                    result = False

            else:
                logger.error("%s Connect Error [%s]%s" % (name, ssid, key))
                result = False
        else:
            for r in range(retry):
                ret, rssi = adb.wifiscan(ssid, timeout)
                if (ret):
                    logger.debug("%s Scan %s RSSI:%s[%s,%s]" % (name, ssid, rssi, rssi_min, rssi_max))
                    result = rssi_min <= float(rssi) <= rssi_max
                    if (result):
                        break
                else:
                    result = False
            self.pane_item_dict[pane_id][item]["Data"] = " SSID: %s \r\n RSSI : %s [%s,%s]" % (
                ssid, rssi, rssi_min, rssi_max)
        report_dict['rssi'] = rssi
        return result, 'RSSI:%s' % rssi if result else "RSSI:%s[%s,%s]" % (rssi, rssi_min, rssi_max)

    def todo_WIFI_24(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            ssid = self.conf_dict[tagid]["ssid"]
            key = self.conf_dict[tagid]["key"]
            type = self.conf_dict[tagid]["type"]
            retry = int(self.conf_dict[tagid]["retry"])
            rssi_min = float(self.conf_dict[tagid]["rssi_min"])
            rssi_max = float(self.conf_dict[tagid]["rssi_max"])
            timeout = int(self.conf_dict[tagid]["timeout"])
            connect = int(self.conf_dict[tagid]["connect"])
            iswifi6 = int(self.conf_dict[tagid].get("is_wifi6",0))
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        rssi = ''
        if (connect):
            ret = adb.conwifi(ssid, key, type)
            if (ret):
                ret, ip = adb.again(adb.getwifiip, retry, timeout)
                if (ret):
                    ret, rssi = adb.getwifirssi()
                    if (ret):
                        logger.debug("%s IP:%s RSSI:%s[%s,%s]" % (name, ip, rssi, rssi_min, rssi_max))
                        result = rssi_min <= float(rssi) <= rssi_max
                        if (not result):
                            ret, rssi = adb.getwifirssi()
                            logger.debug("%s IP:%s RSSI:%s[%s,%s] Again" % (name, ip, rssi, rssi_min, rssi_max))
                            result = rssi_min <= float(rssi) <= rssi_max
                    else:
                        logger.error("%s Get %s[%s] RSSI Error" % (name, ssid, ip))
                        result = False
                    self.pane_item_dict[pane_id][item]["Data"] = "IP: %s \r\n RSSI : %s [%s,%s]" % (
                        ip, rssi, rssi_min, rssi_max)
                else:
                    logger.error("%s Get IP[%s] Timeout" % (name, ssid))
                    result = False

            else:
                logger.error("%s Connect Error [%s]%s" % (name, ssid, key))
                result = False
        else:
            for r in range(retry):
                ret, rssi = adb.wifiscan(ssid, timeout)
                if (ret):
                    logger.debug("%s Scan %s RSSI:%s[%s,%s]" % (name, ssid, rssi, rssi_min, rssi_max))
                    result = rssi_min <= float(rssi) <= rssi_max
                    if (result):
                        break
                else:
                    result = False
            self.pane_item_dict[pane_id][item]["Data"] = " SSID: %s \r\n RSSI : %s [%s,%s]" % (
                ssid, rssi, rssi_min, rssi_max)
        report_dict['rssi'] = rssi
        return result, 'RSSI:%s' % rssi if result else "RSSI:%s[%s,%s]" % (rssi, rssi_min, rssi_max)

    def todo_CHECK_KEYS(self, name, pane_id, item, tagid, report_dict, *args):  # AutoBurnKey 读KEY校验
        adb = self.pane_all[pane_id]["Class"]
        msg = ""
        try:
            retry = int(self.conf_dict[tagid]["retry"])
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        for r in range(retry):
            result, msg = adb.keys_read()
            if (result): break
        if (not result):
            logger.error("%s %s %s" % (name, self.lo(tagid), msg))
        self.pane_item_dict[pane_id][item]["Data"] = "Check Keys: %s" % (msg)
        report_dict["Message"] = msg
        return result, ''

    def todo_READ_KEY(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # tagid = "READ_KEY"
        # btime = time.time()
        msg = ""
        try:
            timeout = int(self.conf_dict[tagid]["timeout"])
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        result = adb.readKey()
        if (result):
            time.sleep(0.5)
            ret, msg = adb.readKeyResult()
            for i in range(timeout):
                if (ret):
                    result = "PCPASS" in msg
                    break
                else:
                    time.sleep(1)
                    result = False
                ret, msg = adb.readKeyResult()
                logger.debug("%s %s %s" % (name, self.lo(tagid), msg))
        else:
            logger.debug("Error Start ReadKey!")
        self.pane_item_dict[pane_id][item]["Data"] = "Message: %s" % (msg)
        report_dict["Message"] = msg
        # if (result):
        #     logger.warning("%s %s PASS" % (name, self.lo(tagid)))
        # else:
        #     logger.error("%s %s FAIL" % (name, self.lo(tagid)))
        # # elpstime = round(time.time() - btime, 3)
        # logger.info("Elapsed Time: %.3f s" % (elpstime))
        # self.pane_dict_report[pane_id][tagid] = {"result": result, "elpstime": elpstime, "msg": msg}
        return result, ''

    def todo_BURN_KEY(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # tagid = "BURN_KEY"
        msg = ""
        # btime = time.time()
        try:
            mode = int(self.conf_dict[tagid]["mode"])
            sn_match = self.conf_dict[tagid]["sn_match"]
            emac_match = self.conf_dict[tagid]["emac_match"]
            wmac_match = self.conf_dict[tagid]["wmac_match"]
            timeout = int(self.conf_dict[tagid]["timeout"])
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        # 通过MES获取sn,emac,wmac
        # scan_now = name  # 临时sn
        if (4 > mode > 0):
            scan_now = self.pane_sn[pane_id].get()  # 使用显示条码从MES读取emac和wmac
            sn, emac, wmac = self.mes.GetMac(scan_now, mode)
            logger.debug("%s %s SN:%s EMAC:%s WMAC:%s " % (name, self.lo(tagid), sn, emac, wmac))
        else:
            # 使用扫码校验的测试项的记录结果作为sn
            if ("SCANNER" in self.pane_dict_report[pane_id] and "SN" in self.pane_dict_report[pane_id]["SCANNER"]):
                sn = self.pane_dict_report[pane_id]["SCANNER"]["SN"]
                if ("EMAC" in self.pane_dict_report[pane_id]["SCANNER"]):
                    emac = self.pane_dict_report[pane_id]["SCANNER"]["EMAC"]
                    logger.debug("%s %s eMAC:%s" % (name, self.lo(tagid), emac))
                else:
                    emac = "null"
                if ("WMAC" in self.pane_dict_report[pane_id]["SCANNER"]):
                    wmac = self.pane_dict_report[pane_id]["SCANNER"]["WMAC"]
                    logger.debug("%s %s wMAC:%s" % (name, self.lo(tagid), wmac))
                else:
                    wmac = "null"
            else:  # 使用显示条码作为SN
                sn = self.pane_dict_report[pane_id]["SN"]
                emac = "null"
                wmac = "null"
            logger.debug("%s %s SN:%s" % (name, self.lo(tagid), sn))
        result = True
        if (result and sn_match):
            result = sn_match in sn
            if (not result): logger.error("%s %s SN:%s[%s] Not Match" % (name, self.lo(tagid), sn, sn_match))
        if (result and emac_match):
            result = emac_match in emac
            if (not result): logger.error("%s %s eMAC:%s[%s] Not Match" % (name, self.lo(tagid), emac, emac_match))
        if (result and wmac_match):
            result = wmac_match in wmac
            if (not result): logger.error("%s %s wMAC:%s[%s] Not Match" % (name, self.lo(tagid), wmac, wmac_match))
        if (result):
            if (mode == 4):  # 定义为PC烧录模式
                try:
                    result, msg = adb.keys_burn(sn, emac, wmac)  # AutoBurnKey 使用
                    if (result):
                        adb.sendcmd_recv1("casePass", "WRITE_KEY")  # 回传结果
                    else:
                        logger.error("%s %s %s" % (name, self.lo(tagid), msg))
                        adb.sendcmd_recv1("caseFail", "WRITE_KEY")  # 回传结果
                except Exception as e:
                    result = False
                    logger.critical("%s" % e)
            else:
                result = adb.burnKey(sn, emac, wmac)
                if (result):
                    time.sleep(1)
                    logger.debug("burnKey..")
                    ret, msg = adb.burnKeyResult()
                    for i in range(timeout):
                        if (ret or adb.error):
                            result = "PCPASS" in msg
                            break
                        else:
                            time.sleep(1)
                            result = False
                        ret, msg = adb.burnKeyResult()
                        logger.debug("%s %s %s" % (name, self.lo(tagid), msg))
        self.pane_item_dict[pane_id][item]["Data"] = "SN: %s \r\neMAC: %s \r\nwMAC : %s \r\nMessage: %s" % (
            sn, emac, wmac, msg)
        report_dict['sn'] = sn
        report_dict['emac'] = emac
        report_dict['wmac'] = wmac
        report_dict['Message'] = msg
        # if (result):
        #     logger.warning("%s %s [%s,%s,%s] PASS" % (name, self.lo(tagid), sn, emac, wmac))
        # else:
        #     logger.error("%s %s [%s,%s,%s] %s FAIL" % (name, self.lo(tagid), sn, emac, wmac, msg))
        # elpstime = round(time.time() - btime, 3)
        # logger.info("Elapsed Time: %.3f s" % (elpstime))
        # self.pane_dict_report[pane_id][tagid] = {"result": result, "elpstime": elpstime, "sn": sn, "emac": emac,
        #                                          "wmac": wmac, "Message": msg}
        return result, "[%s,%s,%s]" % (sn, emac, wmac)

    def todo_AGING_TEST(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # try:
        #     limit = self.conf_dict[tagid].get("limit","")
        # except:
        #     logger.critical("Config Para %s" % self.lo("Error"))
        #     report_dict["result"] = False
        #     return False, 'Config'
        msg = ""
        logger.info("Aging Start")
        result, msg = adb.agingTest()  # 使用厂测配置模板的设定老化时长      # 2022/09/27 进入老化指令,增加msg返回
        if not result:
            logger.error(f"{name} {msg}")
        self.pane_item_dict[pane_id][item]["Data"] = msg
        return result, msg

    def todo_ETH_TEST(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # tagid = "ETH_TEST"
        # btime = time.time()
        try:
            timeout = self.conf_dict[tagid]["timeout"]
            match = self.conf_dict[tagid]["match"]
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        ret, ip = adb.getEthIp(timeout=int(timeout))
        result = match in ip
        logger.debug("%s IP %s [%s]" % (name, ip, match))
        # logger.info("%s %s %s[%s]"%(name,self.lo(tagid),len(ls),num_limit))
        self.pane_item_dict[pane_id][item]["Data"] = "Ether IP: %s \r\n Match : %s" % (ip, match)
        report_dict['ip'] = ip
        # if (result):
        #     logger.warning("%s %s %s[%s] PASS" % (name, self.lo(tagid), ip, match))
        # else:
        #     logger.error("%s %s %s[%s] FAIL" % (name, self.lo(tagid), ip, match))
        # elpstime = round(time.time() - btime, 3)
        # logger.info("Elapsed Time: %.3f s" % (elpstime))
        # self.pane_dict_report[pane_id][tagid] = {"result": result, "elpstime": elpstime, 'ip': ip}
        return result, '%s[%s]' % (ip, match)

    def todo_PRETREATMENT(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            pfiles = self.conf_dict[tagid]["push_file"]
            installapk = self.conf_dict[tagid]["install_apk"]
            if not "apk" in os.path.splitext(installapk)[-1]:
                return False, 'install_apk Config'
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        result = True
        try:
            # push文件到sdcard
            if pfiles:
                ret, plist = adb.push_files(pfiles)
                if not ret:
                    return False, "Push Files"
            # install -r 安装厂测apk
            if installapk:
                ret = adb.apk_install(installapk)
                if not ret:
                    return False, "Install APK"
            # 自动化cmd
            for i in range(10):
                if (not "cmd%d" % i in self.conf_dict[tagid]): break
                cmd = self.conf_dict[tagid]["cmd%d" % i]
                if ("%" in cmd):
                    # if("storage/%s" in cmd):
                    cmd = cmd % (adb.sendshell("ls /storage ")[:9])  # 变量变换
                logger.debug("[CMD%d] %s" % (i, cmd))
                if (cmd):
                    ret = adb.sendshell(cmd)
                    logger.debug("[RECV%d] %s" % (i, ret.strip()))
                    delay = self.conf_dict[tagid]["delay%d" % i]
                    if (delay):
                        time.sleep(int(delay))
                    match = self.conf_dict[tagid]["match%d" % i]
                    if (match):
                        if (not match in ret):
                            logger.error("[CMD%s]Match:%s Fail" % (i, match))
                            # msg.append("[RECV%d] %s" % (i, ret.strip()))
                            result = False
                            break
        except Exception as e:
            logger.critical(e)
            result = False
        return result, ''

    def todo_VISION_DETECT(self, name, pane_id, item, tagid, report_dict, *args):
        cap = self.pane_all[pane_id]["Camera"]
        try:
            tagfile = self.conf_dict[tagid]["tagfile"]
            limit = int(self.conf_dict[tagid]["limit"])
            timeout = int(self.conf_dict[tagid]["timeout"])
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        factoryfile = "./factory.pkl"
        if (os.path.exists(factoryfile)):
            with open(factoryfile, 'rb') as l:
                factorydict = pickle.load(l)
        if (os.path.exists(tagfile)):
            with open(tagfile, 'rb') as l:
                sampledict = pickle.load(l)
        else:
            return False, 'NotFound tagfile(%s)' % tagfile
        btime = time.time()
        result = False
        msg = ""
        # print(sampledict)
        hashFun = cv2.img_hash.PHash_create()
        while self.main_run and cap.isOpened():
            try:
                if (time.time() - btime) > timeout:
                    msg = "TimeOut"
                    break
                if (self.pane_all[pane_id]["Abort"]):
                    msg = "Abort Clicked"
                    break
                ret, frame = cap.read()
                hashA = hashFun.compute(frame)
                minvalue = 99999
                for name, hashB in sampledict.items():
                    cmpValue = hashFun.compare(hashA, hashB)
                    if cmpValue < minvalue:
                        minvalue = cmpValue
                    result = minvalue <= limit
                    if result: break
                showtext = str(minvalue)
                cv2.putText(frame, showtext, (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                # result = self.compute_taghash(frame, sampledict, limit)
                if (os.path.exists(factoryfile)):
                    err = self.compute_taghash(frame, factorydict)
                    if (err):
                        result = False
                        msg = "Detect Factory"
                        break
                self.show_view(pane_id, frame)
                if (result):
                    break
                else:
                    cv2.waitKey(200)
            except Exception as e:
                logger.warning("Detect Error:%s" % e)
        # self.pane_item_dict[pane_id][item]["Data"] = msg
        # report_dict['Message'] = msg.replace('\n', '')
        return result, msg

    def todo_LEDS_DETECT(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            camid_list = [int(i) for i in self.conf_dict[tagid]["id"].split(",")]
            if (not len(camid_list) == 3):
                return False, "Camera config not enough"
            tagfile = self.conf_dict[tagid]["tagfile"]
            htag = cv2.imread("./%s" % tagfile, 0)
            htagvalue = cv2.calcHist([htag], [0], None, [64], [1, 255])
            len_limit = int(self.conf_dict[tagid]["len_limit"])
            hist_limit = float(self.conf_dict[tagid]["hist_limit"])
            timeout = int(self.conf_dict[tagid]["timeout"])
            delaytime = int(self.conf_dict[tagid]["delay"])
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'

        btime = time.time()
        result = False
        msg = ""
        ROI_led_h = 30
        try:
            logger.debug("Delay %s sec and Start..." % delaytime)
            cap_list = []
            adb.leds_change(1)
            time.sleep(delaytime)
            btime = time.time()
            for id in camid_list:
                cap = cv2.VideoCapture(id, cv2.CAP_DSHOW)
                cap.set(cv2.CAP_PROP_EXPOSURE, -7)
                if (not cap.grab()):
                    msg = "Open Camera %s Error" % id
                else:
                    cap_list.append(cap)
        except:
            pass
        if (not len(cap_list) == 3):
            return False, "Camera init not enough"
        while self.main_run:
            try:
                if (time.time() - btime) > timeout:
                    break
                if (self.pane_all[pane_id]["Abort"]):
                    msg = "Abort Clicked"
                    break
                adb.leds_change(1)
                if (time.time() - btime > 5):  # debug
                    adb.leds_change(4)
                for cap in cap_list:
                    cap.set(cv2.CAP_PROP_EXPOSURE, -7)
                cv2.waitKey(50)
                cap_list_result = []
                ispass = 0
                for i, cap in enumerate(cap_list):
                    for a in range(3):
                        ret, frame = cap.read()
                        ret, frame = cap.read()
                        if (ret):
                            _result, _msg, _frame, _rect = self.detect_ledbox(frame, lenlimit=len_limit, ROIw=ROI_led_h,
                                                                              debug=True)
                            cap_list_result.append((cap, _frame, _rect))
                            if (_result):
                                ispass += 1
                            else:
                                logger.debug("[%s]%s" % (i, _msg))
                                msg = "[%s]%s" % (i, _msg)
                            break
                        # cv2.waitKey(50)
                if (ispass >= len(cap_list)):
                    adb.leds_change(3)
                    hist_list = {}
                    for cap, oldframe, rect in cap_list_result:
                        cap.set(cv2.CAP_PROP_EXPOSURE, -5)
                        cv2.waitKey(50)
                        ret, frame = cap.read()
                        ret, frame = cap.read()
                        d_hist, frame = self.detect_ledflag(frame, htagvalue, rect, oldframe, debug=False)
                        hist_list[d_hist] = (frame, oldframe)
                    judge_hist = min(hist_list.keys())
                    if (judge_hist <= hist_limit):
                        result = True
                    msg = "Hist:%.2f(%s)" % (judge_hist, hist_limit)
                    centre_show = hist_list.pop(judge_hist)[0]
                    if (result):
                        cv2.putText(centre_show, msg, (5, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1)
                    else:
                        logger.debug(msg)
                        cv2.putText(centre_show, msg, (5, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)
                    h2, w = centre_show.shape[:2]
                    show_make = np.zeros((ROI_led_h * 4 + h2, w, 3), dtype="uint8")
                    show_make[0:h2, :] = centre_show
                    _key, (_new, old) = hist_list.popitem()
                    show_make[h2:h2 + ROI_led_h * 2, :] = old
                    _key, (_new, old) = hist_list.popitem()
                    show_make[h2 + ROI_led_h * 2:h2 + ROI_led_h * 4, :] = old
                else:
                    h2, w = frame.shape[:2]
                    show_make = np.zeros((ROI_led_h * 6, w, 3), dtype="uint8")
                    _cap, old, _rect = cap_list_result.pop(0)
                    show_make[0:ROI_led_h * 2] = old
                    _cap, old, _rect = cap_list_result.pop(0)
                    show_make[ROI_led_h * 2:ROI_led_h * 4] = old
                    _cap, old, _rect = cap_list_result.pop(0)
                    show_make[ROI_led_h * 4:ROI_led_h * 6] = old
                self.show_view(pane_id, show_make)
                if (result):
                    break
                else:
                    cv2.waitKey(200)
            except Exception as e:
                logger.warning("Detect Error:%s" % e)
        self.pane_item_dict[pane_id][item]["Data"] = msg.replace(";", "\n").replace(":", ": ")
        report_dict['Message'] = msg
        return result, msg

    def todo_WIFI_COUPLE(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # tagid = "WIFI_COUPLE"
        # btime = time.time()
        try:
            _txchain = self.conf_dict[tagid]["txchain"].split(',')
            _minlist = [float(i) for i in self.conf_dict[tagid]["min"].split(',')]
            _maxlist = [float(i) for i in self.conf_dict[tagid]["max"].split(',')]
            dute = float(self.conf_dict[tagid]["dute"])
            num = int(self.conf_dict[tagid]["num"])
            fw_file = self.conf_dict[tagid]["fw_file"]
            nvram = self.conf_dict[tagid]["nvram"]
            num_limit = float(self.conf_dict[tagid]["limit"])
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        _channel = 1
        data = []
        msg = "Couple: %s Min: %s Max: %s Limit: %s Num: %s" % (_channel, _minlist, _maxlist, num_limit, num)
        result = adb.push_fw(fw_file, nvram)
        if (result):
            for i, c in enumerate(_txchain):
                if (i < len(_minlist)):
                    _min = _minlist[i]
                    _max = _maxlist[i]
                else:
                    _min = _minlist[-1]
                    _max = _maxlist[-1]
                logger.debug("%s Start WIFI txchain %s" % (name, c))
                result = adb.wifi_fw_start(c)
                if (result):
                    RF = RFmode()
                    logger.debug("%s Begin Couple [%s]2412 MHz" % (name, _channel))
                    data = RF.get_power_list(_channel, 2412, num, dute)
                    _pass = 0
                    for d in data:
                        if (_min <= d <= _max):
                            _pass += 1
                    result = _pass / num >= num_limit
                    logger.debug("%s TxChain[%s] Powers %s Pass:%s" % (name, c, data, _pass))
                    msg += "\n[%s]Pass %s Powers:\n%s" % (c, _pass, data)
                    if (not result):
                        break
        self.pane_item_dict[pane_id][item]["Data"] = msg
        report_dict['Message'] = msg.replace('\n', '')
        # if (result):
        #     logger.warning("%s %s %s[%s] PASS" % (name, self.lo(tagid), data, num_limit))
        # else:
        #     logger.error("%s %s %s[%s] FAIL" % (name, self.lo(tagid), data, num_limit))
        # elpstime = round(time.time() - btime, 3)
        # logger.info("Elapsed Time: %.3f s" % (elpstime))
        # self.pane_dict_report[pane_id][tagid] = {"result": result, "elpstime": elpstime, 'msg': msg.replace('\n', '')}
        return result, '%s[%s]' % (data, num_limit)

    def todo_ROUTER_TELNET(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            _ip = self.conf_dict[tagid]["ip"]
            _static = self.conf_dict[tagid]["static"]
            static_ip = ".".join(_ip.split(".")[:-1] + [_static])  # 生成同网段静态IP
            _user = self.conf_dict[tagid]["user"]
            _password = self.conf_dict[tagid]["password"]
            _wait = int(self.conf_dict[tagid]["wait"])
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        if (_static):
            ret = adb.setEthIp(static_ip, _ip)  # 设置静态IP
        result, value = adb.sendcmd_recv2("getEthIp")
        for a in range(_wait):
            if (result): break
            time.sleep(1)
            if (_static and not ret):
                ret = adb.setEthIp(static_ip, _ip)  # 设置静态IP
            result, value = adb.sendcmd_recv2("getEthIp")
            if (adb.has_error()):
                logger.critical("[ADB_ERROR]%s %s" % (name, adb.errormsg[adb.error]))
                # break
        if (not result):
            return False, 'Wait(%s) Ethernet' % (a)
        logger.debug("[Wait %s]%s" % (a, value))
        result = adb.telnet_router(_ip, _user, _password)
        self.pane_item_dict[pane_id][item]["Data"] = "Host:%s (%s/%s) \nLocal:%s\nWait:%s" % (
            _ip, _user, _password, value, a)
        return result, ''

    def todo_ROUTER_COUPLE(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        try:
            with open("./CoupleCmd", "r", encoding='utf-8') as f:
                cmd_dict = eval(f.read())
            _txchain = cmd_dict.keys()
            if (not _txchain):
                return False, "CoupleCmd"
            _freqlist = [int(i) for i in self.conf_dict[tagid]["freq"].split(',')]
            _minlist = [float(i) for i in self.conf_dict[tagid]["min"].split(',')]
            _maxlist = [float(i) for i in self.conf_dict[tagid]["max"].split(',')]
            dute = float(self.conf_dict[tagid]["dute"])
            num = int(self.conf_dict[tagid]["num"])
            num_limit = float(self.conf_dict[tagid]["limit"])
            _channel = None
            for i in range(8):
                usb_tid = self.conf_dict[tagid]['bind%d' % (i + 1)]
                if (usb_tid == self.pane_all[pane_id]["Tid"]):
                    _channel = i + 1
                    bind_offset = self.conf_dict[tagid]['bind%d_offset' % (i + 1)]
                    if (bind_offset):
                        _offset_list = [float(i) for i in bind_offset.split(',')]
                    else:
                        _offset_list = [0]
                    break
            if (_channel == None):
                logger.critical("Bind Couple Channel %s" % self.lo("Error"))
                report_dict["result"] = False
                return False, 'Config'
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        data = []
        max_data = []
        msg = "Couple: %s FREQ:%s Min: %s Max: %s Limit: %s Num: %s Offset: %s" % (
            _channel, _freqlist, _minlist, _maxlist, num_limit, num, _offset_list)
        result = adb.telnet_state
        if (result):
            for i, c in enumerate(_txchain):
                _min = self.get_one_value(_minlist, i)
                _max = self.get_one_value(_maxlist, i)
                _freq = self.get_one_value(_freqlist, i)
                _offset = self.get_one_value(_offset_list, i)
                logger.debug("%s Start Router TxChain(%s)" % (name, c))
                result = adb.telnet_cmdlist(cmd_dict[c])
                if (result):
                    RF = RFmode()
                    logger.debug("%s Begin Couple(%s)%s MHz" % (name, _channel, _freq))
                    data = RF.get_power_list(_channel, _freq, num, dute, _offset)
                    max_data.append(max(data))
                    _pass = 0
                    for d in data:
                        if (_min <= d <= _max):
                            _pass += 1
                    result = _pass / num >= num_limit
                    logger.debug("%s Powers(%s)Pass(%s)%s" % (name, c, _pass, data))
                    msg += "\nPowers(%s)Pass(%s)\n%s" % (c, _pass, data)
                    if (not result):
                        break
                else:
                    logger.error("Couple(%s) Control TxChain(%s) Fail" % (_channel, c))
        self.pane_item_dict[pane_id][item]["Data"] = msg
        report_dict['Message'] = msg.replace('\n', '')
        report_dict['Data'] = "%s" % (max_data)
        return result, "%s" % (max_data)

    def todo_SD_TEST(self, name, pane_id, item, tagid, report_dict, *args):
        adb = self.pane_all[pane_id]["Class"]
        # tagid = "SD_TEST"
        # btime = time.time()
        try:
            num_limit = self.conf_dict[tagid]["limit"]
        except:
            logger.critical("Config Para %s" % self.lo("Error"))
            report_dict["result"] = False
            return False, 'Config'
        ret, count = adb.getSdNum()
        result = int(count) >= int(num_limit)
        logger.debug("%s Detect Count %s" % (name, count))
        # logger.info("%s %s %s[%s]"%(name,self.lo(tagid),len(ls),num_limit))
        self.pane_item_dict[pane_id][item]["Data"] = "Detect Count: %s [Limit:%s]" % (count, num_limit)
        report_dict['count'] = count
        # if (result):
        #     logger.warning("%s %s %s[%s] PASS" % (name, self.lo(tagid), count, num_limit))
        # else:
        #     logger.error("%s %s %s[%s] FAIL" % (name, self.lo(tagid), count, num_limit))
        # elpstime = round(time.time() - btime, 3)
        # logger.info("Elapsed Time: %.3f s" % (elpstime))
        # self.pane_dict_report[pane_id][tagid] = {"result": result, "elpstime": elpstime, 'count': count}
        return result, '%s[%s]' % (count, num_limit)

    def todo_RESET(self, name, pane_id, item, tagid, report_dict, *args):
        pass  # 清除厂测数据?

    def todo_ADB_IPERF(self, name, pane_id, item, tagid, report_dict, *args):
        pass  # iperf 吞吐量测试


def init_logo(text1="LED视觉检测", pos1=(52, 3), text2="LED Vision Detect", pos2=(56, 19)):
    image = Image.open("./SEI.png")
    draw = ImageDraw.Draw(image)
    setFont1 = ImageFont.truetype('C:/windows/fonts/simhei.ttf', 15)
    # setFont1 = ImageFont.truetype('C:/windows/fonts/STXINWEI.ttf', 15)
    setFont2 = ImageFont.truetype('C:/windows/fonts/STXINWEI.ttf', 10)
    draw.text(pos1, text1, font=setFont1, fill="#000000", direction=None)
    draw.text(pos2, text2, font=setFont2, fill="#000000", direction=None)
    image.show()
    image.save("./SEI_logo.png")


if __name__ == '__main__':
    # init_logo()
    os.remove('./English')
    os.remove('./Chinese')
    os.remove('./Config.ini')
