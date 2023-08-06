# 基于usb的adb集成
import logging
import os, time
import re
import base64
import requests, json
import usb1
from adb_shell.adb_device import AdbDeviceUsb, _AdbTransactionInfo, _FileSyncTransactionInfo, constants
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.auth.keygen import keygen
from autotk.AutoCoreLite import logger
import threading


def get_adb_devices(isexe=False):
    if (isexe):
        out = os.popen("adb.exe devices -l").read()  # os.popen支持读取操作
        pattern = re.compile(r"device.*id:(\d+)")
        list = pattern.findall(out)
        return list, list, list
    else:
        adb_names = []
        adb_devices = []
        adb_devices_info = []
        adb_interface = (255, 66, 1)  # From adb.h
        btime=time.time()
        try:
            with usb1.USBContext() as context:
                for device in context.getDeviceList(skip_on_error=True):
                    vid = "%04X" % device.getVendorID()
                    bus = device.getBusNumber()
                    portpath = [bus] + device.getPortNumberList()
                    portname = ".".join([str(i) for i in portpath])
                    info = {"PORTNAME": portname, "PORTPATH": portpath, "BUS": bus,"VID":vid}
                    if vid in ["18D1"]:   # 过滤指定生产商ID
                        # print(time.time()-btime)
                        for setting in device.iterSettings():
                            get_inter = (setting.getClass(), setting.getSubClass(), setting.getProtocol())
                            # print(get_inter)
                            if (get_inter == adb_interface):
                                adb_names.append(portname)
                                adb_devices.append(portpath)
                                adb_devices_info.append(info)
                                # print(info)
                                break
        except Exception as e:
            print(e)
        return adb_names, adb_devices, adb_devices_info


class adbClass():
    def __init__(self, port, versionlimit=2021111101, skipboxid=False, skipapk=False,tryroot=False):
        self.verlimit = versionlimit
        self.boxid = None
        self.btstart = False
        self.wifistart = {}
        self.skipboxid = skipboxid
        self.skipApk = skipapk  # skipApk
        if (skipboxid):
            self.skipboxid = port
        self.ver = 0
        self.root_once=tryroot     # root一次,需要root 设定为true 不需要 设定为false 执行一次后设定为false 
        self.palystate = False
        self.iperfver = None
        self.errormsg = ["NoError", "Command Error", "APK Version_limit:%s Unsupported" % versionlimit,
                         "Not Found Return", "ConnectError",
                         "Device Not Found", "Tid Change"]
        self.error = 0
        if (isinstance(port, str)):
            if ("." in port):
                self.portpath = [int(i) for i in port.split('.')]
            else:
                self.portpath = port  # 与tid共用变量,可以通过port区分exe还是usb
        else:
            self.portpath = port
        self.initdev()
        self.connect()
        # self.initcheck = self.checkready()
        self.telnet_state = False  # 路由telnet状态

    def apk_install(self, apkpath, delay=7):
        ret, apks = self.push_files(apkpath, "/data/data/com.utsmta.app")
        for a in apks:
            logger.debug("[Install]%s" % a)
            self.sendshell("pm install -r %s" % a, onlysend=True)
            time.sleep(delay)
            self.reconnect()
            return True
        return False

    def push_files(self, pfiles, remote="/sdcard"):
        push_files = []
        sdcard_files = []
        if pfiles:
            _files = pfiles.split(",")
            for f in _files:
                f = f.strip()
                if f:
                    if os.path.exists("./%s" % f):
                        push_files.append("./%s" % f)
                    elif (os.path.exists(f)):
                        push_files.append(f)
                    else:
                        logger.debug("NotFound %s" % f)
                        return False, []
        if push_files:
            for p in push_files:
                tag = "%s/%s" % (remote, os.path.basename(p))
                ret = self.adbpush(p, tag)
                if ret:
                    sdcard_files.append(tag)
                    logger.debug("[Push]%s" % p)
                else:
                    logger.error("[Push]%s Error" % p)
        return len(push_files) == len(sdcard_files), sdcard_files

    def screencap_frame(self):
        ret = self.sendshell("screencap -p | base64")  # 约用时1s
        return base64.b64decode(ret)

    def check_port(self, timeout=5):
        '''
        Had port return True
        '''
        for t in range(timeout):
            time.sleep(0.5)  # 防止盒子上电状态的ADB服务刷新
            tid_list, adb_paths, adb_info = get_adb_devices(isinstance(self.portpath, str))
            # print(adb_paths,self.portpath)
            if (self.portpath in adb_paths):
                return True
            time.sleep(0.5)
        return False

    def check_serport(self, ip, port):
        f = os.popen("tcping %s %s" % (ip, port))  # 需配合tcping.exe 使用
        for i in range(3):
            r = f.readline()
            # print(r)
            if ("Port is open" in r):
                return True
        return False

    def iperf_loop(self, host, port=None, count=None, otherpara="-w 2M -P 3 -t 3",iperfx=None):
        _info = {}
        # /data/data/com.utsmta.app/files
        # cmdfile = "/data/data/com.utsmta.app/files/myIperf"
        if not iperfx:
            iperfx=self.iperf_cmd
        if (port):
            portstr = " -p %s" % port
        else:
            portstr = " "
        if (count):
            countstr = " -t %s" % count
            set_time = count
        else:
            countstr = " "
            set_time = 10
        if "perf3" in iperfx and "-w" in otherpara:
            logger.debug("[ADB]Iperf3 window skip")
            w_start = otherpara.index("-w")
            if "-" in otherpara[w_start:]:
                w_end = otherpara.index("-", w_start + 1)
                otherpara = otherpara[:w_start] + otherpara[w_end:]
            else:
                otherpara = otherpara[:w_start]
        cmdline=f"{iperfx} -c {host}{portstr}{countstr} {otherpara}"
        logger.debug("[ADB]%s"%cmdline)
        ret = self.sendshell(cmdline,addtimeout=set_time + 10)
        judge_num = count
        if (" -i " in cmdline):
            pattern = re.compile(r'.+-i\s+(\d+)')
            dute = int(pattern.findall(cmdline)[-1])
            judge_num = count / dute
        if ("-P" in otherpara):
            pattern = re.compile(r'\[.+U.+Bytes\D+(\S+)\s+Mbits/sec')
        else:
            pattern = re.compile(r'\[.+Bytes\D+(\S+)\s+Mbits/sec')
        sec_data = []
        last_data = 0.0
        max_data = 0.0
        try:
            _info["log"] = ret
            data = ret.split("\n")
            for l in data:
                if ("local" in l.lower()):
                    local_ip = re.compile(r"local ([0-9.]+)").findall(l)
                    if local_ip:
                        _info["local"] = local_ip[0]
                # list = pattern.findall(l.decode())
                list = pattern.findall(l)
                if (list):
                    last_data = round(float(list[0]), 1)
                    sec_data.append(last_data)
            if len(sec_data) >= judge_num:
                max_data = max(sec_data)
            else:
                logger.debug("".join(_info.get("log", [])))
        except Exception as e:
            logger.critical(e)
        return last_data, max_data, sec_data, _info

    def runiperf(self,ip=None,port=None):
        iperf_dict={"iperf2":"iperf2","iperf3":"iperf3","myIperf3":"iperf3","iperf":"iperf"}
        iperf_match={"iperf2":"iperf version 2","iperf3":"iperf 3","iperf":"iperf"}
        retry=3
        if port:
            portstr=f" -p {port}"
        else:
            portstr=""
        try:
            for n,v in iperf_dict.items():
                # if n in ["iperf2","iperf3"]:continue # 调试用
                ret=self.sendshell(f"which {n}")
                if n in ret:
                    ret = self.sendshell(f"{n} -v")
                    _ver=ret.split("\n")[0].strip()
                    logger.debug(f'[{n}]{_ver}')
                    if "iperf version 2" in ret:
                        if not v=="iperf2":
                            logger.warning(f"Check {n} match Version2")
                            v="iperf2"     # 版本修正
                    elif "iperf 3" in ret:
                        if not v=="iperf3":
                            logger.warning(f"Check {n} match Version3")
                            v = "iperf3"     # 版本修正
                    else:
                        if not v=="iperf":
                            logger.warning(f"Check {n} match Version1")
                            v = "iperf"     # 版本修正
                    # if v=="iperf2":continue  # 用于调试跳过
                    for r in range(retry):  # 可重试
                        # kill 旧线程 是否可提高数据 kill 没有用 futex_wait_queue_me 的线程无法连接connect failed: Connection refused
                        # out = self.sendshell(f"ps -e|grep {n}")
                        # if out:
                        #     for o in out.split("\n"):
                        #         pattern = re.compile("\w+\s+(\d+).+(%s)$" % n)
                        #         list = pattern.findall(o)
                        #         for k,n in list:
                        #             print(k,n)
                        #             self.sendshell(f"kill {k}")
                        #     time.sleep(1)

                        # self.sendcmd_recv1("runTask '%s -s%s'"%(n,portstr))
                        self.sendshell(f"{n} -s{portstr} -D",onlysend=True)  # iperf -D 参数为后台运行(手动新增改权限也无法调起)
                        # self.sendshell(f"{n} -s -D",onlysend=True)  # iperf -D 参数为后台运行(手动新增改权限也无法调起)
                        out = self.sendshell(f"ps -e|grep {n}")
                        # print(out)
                        pattern = re.compile("\w+\s+(\d+).+(%s)$" % n)
                        list = pattern.findall(out)
                        if (list):
                            logger.debug(f"Running {n}[{v}] Server")
                            self.iperf_cmd=n
                            return v
                        else:
                            logger.debug(f"Retry {n} {retry-r}")
                            time.sleep(1)
                            # print(self.sendshell("ps -e|grep perf"))
        except Exception as e:
            logger.error(e)
        return ""

    def initdev(self):
        if (isinstance(self.portpath, str)): return True  # exe模式没有dev初始化
        p_exist=True
        for i in range(3):
            try:
                if (p_exist):
                    self.dev = AdbDeviceUsb(port_path=self.portpath, default_transport_timeout_s=5 + i)
                    return True
                else:
                    p_exist= self.check_port()
            except Exception as e:
                print("[USB]Port Break", self.portpath, e)
        logger.error("[USB]Port Break")
        self.error = 5
        return False

    def checkapk(self, name="com.utsmta.app", topmost=True):
        if (self.skipApk):
            logger.debug("Skip Apk Check.")
            name = "com.android.tv.settings"
            out = self.sendshell('ps -e|grep %s' % name)
            pattern = re.compile(r"%s" % name)
            list = pattern.findall(out)
            if (list):
                return True
        out = self.sendshell('ps -e|grep %s' % name)
        pattern = re.compile(r"%s" % name)
        list = pattern.findall(out)
        if (list):
            if topmost:
                time.sleep(1)
                # out=self.sendshell("dumpsys window windows | grep mFocus")
                out = self.sendshell("dumpsys window windows | grep name=%s" % name)  # 获取最前面的APP
                # print(out)
                # print(time.time(),'checkapk',self.sendshell("getprop sys.nes.opening.factory"))
                result = name in out
            else:
                result = True
        else:
            result = False
            time.sleep(1)
        return result

    def sendcmd(self, cmd, *para):
        _cmd = "dumpsys activity com.utsmta.app/com.nes.factorytest.ui.activity.Main2Activity "
        if (isinstance(self.portpath, str), str):
            ret = self.sendshell("%s%s %s" % (_cmd, cmd, " ".join(para)))
        else:
            ret = self.dev.shell("%s%s %s" % (_cmd, cmd, " ".join(para)))
        print(ret)
        return ret

    def sendcmd_recv1(self, cmd, *para):
        if (self.has_error()): return False
        try:
            ret = self.sendcmd(cmd, *para)
            if (not ret): self.error = 3
            pattern = re.compile(r"%s_(\w+)" % cmd)  # 识别命令放回
            list = pattern.findall(ret)
            if (list):
                result = list[0]
                judge = True if ("SUCCESS" in result) else False
                return judge
            else:
                return False
        except Exception as e:
            logger.critical(e)
            self.error = 1  # 指令错误
            return False

    def sendcmd_recv2_data(self, cmd, *para):
        if (self.error): return False, ""
        try:
            ret = self.sendcmd(cmd, *para)
            if (not ret): self.error = 3
            _tag = "%s_SUCCESS" % cmd
            if (_tag in ret):
                value = ret.split("%s_SUCCESS_" % cmd)[-1]
                return True, value
            else:
                value = ret.split("%s_FAILED_" % cmd)[-1]
            return False, value
        except Exception as e:
            # logger.critical(ret)
            logger.critical("[ADB]%s" % e)
            self.error = 1  # 指令错误
            return False, ""

    def sendcmd_recv2(self, cmd, *para):
        if (self.has_error()): return False, ""
        try:
            ret = self.sendcmd(cmd, *para)
            if (not ret): self.error = 3
            # logger.debug("cmd ret:%s" % ret)
            # print(":::::\n%s" % ret)
            pattern = re.compile(r"%s_(\w+)_([^_]+)" % cmd)  # 识别命令放回
            list = pattern.findall(ret)
            # print(list)
            if (list):
                result, value = list[0]
                judge = True if ("SUCCESS" in result) else False
                return judge, value
            else:
                pattern = re.compile(r"%s_(\w+)" % cmd)  # 识别命令放回
                list = pattern.findall(ret)
                if (list):
                    result = list[0]
                    judge = True if ("SUCCESS" in result) else False
                    return judge, ""
                else:
                    return False, ""
        except Exception as e:
            # logger.critical(ret)
            logger.critical("[ADB]%s" % e)
            self.error = 1  # 指令错误
            return False, ""

    def getBoxid(self, timeout=2):
        if self.skipApk:  # 没有产测APK直接获取Boxid
            ret = self.sendshell("cd /sys/class/unifykeys/ && echo sboxid>name | cat read").strip()
            if ret:
                return ret
            return False
        else:
            time.sleep(1)  # 等待厂测拉起完成
            for i in range(timeout * 2):
                result, value = self.sendcmd_recv2("getBoxid")
                if (result):
                    return value
                else:
                    if (not self.check_port(1)): return False
                    time.sleep(0.5)
            return False

    def reboot(self):
        # print("[ADB]Reboot %s" % self.boxid)
        self.sendshell('reboot')
        pass

    def set_selinux(self, permissive=True):
        set = "permissive" if permissive else "enforcing"  # 设置后都需重启生效
        ret, msg = self.sendcmd_recv2("getEnvValue", "ubootenv.var.EnableSelinux")
        if ret and set == msg.lower():
            logger.debug("[Selinux]%s" % msg)
            # self.sendcmd_recv2("setEnvValue", "ubootenv.var.EnableSelinux","enforcing")  # debug
            return True
        else:
            ret, msg = self.sendcmd_recv2("setEnvValue", "ubootenv.var.EnableSelinux", set)
            ret, msg = self.sendcmd_recv2("getEnvValue", "ubootenv.var.EnableSelinux")
            logger.debug("[Selinux]Set %s" % msg)
            if permissive:
                self.reboot()  # 恢复enforcing下次开机生效即可
            if ret and set == msg.lower():
                return True
        return False

    def dev_init(self):
        # print("[ADB]Ready %s" % self.boxid)
        pass

    def dev_finish(self):
        self.close()
        pass

    def runapk(self, apk="com.utsmta.app.showapp"):
        if self.skipApk: return
        out = self.sendshell("am start -a %s" % apk)

    def adbroot(self):
        try:
            if self.root_once:
                if (isinstance(self.portpath, str)):  # exe模式 push文件
                    os.popen("adb -d -t %s root" % (self.portpath))
                else:
                    self.dev.root(10, 10)
                    self.reconnect()
                ret = self.sendshell("whoami")
                self.root_once=False
                logger.debug(f'Try ROOT {"root" in ret.lower()}')
        except:
            logger.debug("Try ROOT Error")
            pass

    def get_one_id(self):
        ret = self.sendshell("cd /sys/class/unifykeys/ && echo usid>name | cat read").strip()
        if "Permission" in ret:
            logging.warning(ret)
            ret = self.sendshell("getprop ro.serialno").strip()  # release版本可通过getprop获取sn
        if ret:
            logger.debug("Get SN %s" % ret)
            return ret
        ret = self.sendshell("cd /sys/class/unifykeys/ && echo sboxid>name | cat read").strip()
        if ret:
            logger.debug("Get Boxid %s" % ret)
            return ret
        ret = self.sendshell("ifconfig | grep lan").lower()
        if "wlan" in ret and "hwaddr" in ret:
            pattern = re.compile(r"wlan.+hwaddr\W+(([a-f0-9]{2}:){5}[a-f0-9]{2})")
            list = pattern.findall(ret)
            if list:
                _wmac = list[0][0].replace(":", "").upper()
                logger.debug("Get WMAC %s" % _wmac)
                return _wmac
        else:
            logger.debug(ret)
        return False

    def boot_ready(self, name="com.android.tv.settings", bootdelay=10):
        out = self.sendshell("ps -Ao pid,Name,etime|grep %s" % name)
        if out:
            list_etime = re.compile(r"(\d+(:\d+)+)").findall(out)
            if list_etime:
                etime, _ = list_etime[0]
                e_list = etime.split(":")
                logger.debug("[Check]%s elptime %s[%s]" % (self.portpath, etime, bootdelay))
                if len(e_list) > 2:
                    return True
                else:
                    e_min = int(e_list[0])
                    if e_min:
                        return True
                    else:
                        return int(e_list[-1]) >= bootdelay  # 10秒以上
        else:
            if not (isinstance(self.portpath, str)):
                self.error = 4  # ADB模式下 启动时的错误 判断为4 允许重连处理
        # logger.debug("[Check]%s waitting %s.." % (self.portpath, name))  # 放循环外记录i
        return False

    def checkready(self):
        logger.debug(f"Check Device.. {self.portpath}")
        if (self.has_error()):
            return False
        for b in range(20):  # 20秒内的启动检测
            _boot = self.boot_ready(bootdelay=6)  # setting 启动后8秒再开始通信
            if _boot:
                break
            else:
                time.sleep(1)
        if not self.check_port(1):
            return False  # 启动时间等待过后仍没有ADB连接 直接Fail
        for c in range(10):
            self.ver = self.getver()
            # print(self.ver)
            if (self.ver):
                self.adbroot()  # 提升权限
                if (self.ver >= self.verlimit):  # 限定APK版本
                    self.runapk("com.utsmta.app.showapp")  # 首次启动,拉起产测APK
                    for a in range(10):
                        check = self.checkapk("com.utsmta.app")  # 检测是否启动
                        if (check):
                            if (self.skipboxid):
                                _oneid = self.get_one_id()  # 使用wmac
                                if _oneid:
                                    bid = _oneid
                                else:
                                    bid = "USB_%s" % self.skipboxid
                            else:
                                bid = self.getBoxid(timeout=5)
                            if (bid):
                                self.boxid = bid
                                self.dev_init()
                                return True
                            else:
                                return False
                        else:
                            if (isinstance(self.portpath, str)):  # exe模式
                                logger.debug("Run Apk %d Again" % a)
                            else:  # usb模式
                                logger.debug("Run Apk And Check %d Again" % a)
                                if (self.check_port(1)):
                                    self.reconnect()
                                    if (a > 3):  # USB模式的检测超时时间
                                        break
                            self.runapk("com.utsmta.app.showapp")
                            time.sleep(1)
                        if (isinstance(self.portpath, str)):
                            if (not self.check_port(1)):  # exe模式特有 tid change
                                self.error = 6
                                break
                    logger.warning("APK Run Error")
                    return False
                else:
                    self.error = 2  # 版本不兼容
                    logger.warning(f"{self.portpath} APK Version Unsupported {self.ver}[{self.verlimit}]")
                    return False
            else:
                time.sleep(1)
            if (isinstance(self.portpath, str)):
                if (not self.check_port(1)):  # exe模式特有 tid change
                    self.error = 6
                    break

    def has_error(self):
        if (self.error == 0):
            return False
        elif (self.error == 4):
            self.error = 0
            self.initdev()
            self.connect()
        else:
            logger.debug("[HasError](%d)%s" % (self.error, self.errormsg[self.error]))
            return True

    def close(self):
        # print("closed")
        self.error = 0
        if (not isinstance(self.portpath, str)):
            os.popen("taskkill /f /im adb.exe")  # kill adb.exe服务 USB模式独占
            self.dev.close()

    def reconnect(self):
        self.close()
        if (self.has_error()): return False
        for i in range(2):
            try:
                self.signer = PythonRSASigner.FromRSAKeyPath(os.path.expanduser('~/.android/adbkey'))
                if (self.dev.connect(rsa_keys=[self.signer], transport_timeout_s=10, auth_timeout_s=6 + i)):
                    self.error = 0
                    return self.error
                else:
                    time.sleep(0.5)
                    self.initdev()
            except Exception as e:
                print(e)
        self.error = 4
        return self.error

    def connect(self):
        if (isinstance(self.portpath, str)): return True  # exe模式下没有connect
        if (self.has_error()): return False
        for i in range(3):
            try:
                _keypath = os.path.expanduser('~/.android/adbkey')
                if not (os.path.exists(_keypath + ".pub")):
                    _keypath = "./adbkey"
                    if not (os.path.exists(_keypath + ".pub")):
                        keygen(_keypath)
                self.signer = PythonRSASigner.FromRSAKeyPath(_keypath)
                if (self.dev.connect(rsa_keys=[self.signer], transport_timeout_s=10, auth_timeout_s=6 + i)):
                    self.error = 0
                    return self.error
                else:
                    time.sleep(0.5)
                    self.initdev()
            except Exception as e:
                logger.error("[ADBConnect]%s" % e)
        logger.error("[ADBConnect]Fail")
        self.error = 4
        return self.error

    def sendshell(self, cmdline, onlysend=False, addtimeout=0):
        print("-> ",cmdline)
        if (self.has_error()): return ""
        if (isinstance(self.portpath, str)):  # exe模式
            try:
                if ("|" in cmdline):
                    if (not '"' in cmdline):
                        cmdline = '"%s"' % cmdline
                    else:
                        print("[sendshell]", cmdline)
                if (onlysend):
                    os.popen('adb -d -t %s shell %s' % (self.portpath, cmdline))
                    # subprocess.Popen(["adb",'-d','-t',self.portpath])
                    return True
                else:
                    ret = os.popen('adb -d -t %s shell %s' % (self.portpath, cmdline)).read()
                    return ret
            except Exception as e:
                logger.critical(e)
                self.error = 1  # 指令错误
                return ""
        else:
            try:
                if onlysend:
                    try:
                        self.dev.shell(cmdline, 1, 1, 1)  # usb模式
                    except:
                        pass
                    return self.reconnect()
                elif addtimeout:  # 仅USB模式专用
                    self.dev._default_transport_timeout_s += addtimeout
                    ret = self.dev.shell(cmdline)  # usb模式
                    self.dev._default_transport_timeout_s -= addtimeout
                    return ret
                else:
                    return self.dev.shell(cmdline)  # usb模式
            except Exception as e:
                logger.debug("[Error]" + cmdline)
                if (not cmdline in ["ps -e|grep com.utsmta.app"]):  # 跳过错误打印
                    logger.critical(e)
                self.error = 1  # 指令错误
                return ""

    def getver(self):
        if self.skipApk: return 9999999999  # 跳过版本检测
        out = self.sendshell("dumpsys package com.utsmta.app|grep versionCode")
        pattern = re.compile(r"versionCode=(\d{9}\d+)")  # 长度10以上
        list = pattern.findall(out)
        if (list):
            return int(list[0])
        else:
            return False

    def audio_play(self, filename):
        return self.sendcmd_recv1("playAudio", filename)  # ？

    def rec_start(self, filename):
        return self.sendcmd_recv1("recordAudio", filename)  # ？

    def rec_stop(self, filename):
        return self.sendcmd_recv1("stopRecord", filename)  # ？

    def setBoxid(self, value, check=False):
        if check:
            _token, _json, isnew = self.get_token_json()
            if (isnew):
                strmin = _json["startSeiBoxId"]
                strmax = _json["endSeiBoxId"]
            else:
                strmin = _json["start_seiboxid"]
                strmax = _json["end_seiboxid"]
            if (len(strmin) == len(value) and strmin <= value <= strmax):
                logger.debug("%s [%s,%s]" % (value, strmin, strmax))
                return self.sendcmd_recv1("setBoxid", str(value))
            else:
                logger.error("%s [%s,%s] Illegal 非法条码" % (value, strmin, strmax))
                return False
        else:
            return self.sendcmd_recv1("setBoxid", str(value))

    def setSN(self, value):
        return self.sendcmd_recv1("setSN", str(value))

    def ledtest(self, value):
        return self.sendcmd_recv1("testled", str(value))

    def ledfinish(self):
        return self.sendcmd_recv1("ledTestFinish")

    def cecTest(self):
        return self.sendcmd_recv1("cecTest")

    def agingTest(self, value=None):
        # value单位为分钟 value暂不支持(以产测配置为准)
        if (value == None):
            return self.sendcmd_recv2("agingTest")      # 2022/09/27 进入老化指令,增加msg返回
        return self.sendcmd_recv2("agingTest", str(value))

    def agingResult(self):
        # 获取当前老化结果
        return self.sendcmd_recv2("agingTime")

    def cecResult(self):
        # 获取当前老化结果
        return self.sendcmd_recv2("cecResult")

    def hdmiPlay(self, value, delay=1):
        self.dvb_close()
        self.palystate = True
        logger.debug("[ADB]HDMI Play %s" % value)
        ret = self.sendcmd_recv1("hdmiPlay", str(value))
        time.sleep(int(delay))
        return ret

    def getTempSN(self, tempfile="SN.txt"):
        # self.sendshell('echo "%s" > /sdcard/%s' % ("QASEI5300000406", tempfile))  # 写文件
        out = self.sendshell("cat /sdcard/%s" % tempfile)
        if (tempfile in out):  # cat: /sdcard/SN.txt: No such file or directory
            return ""
        return out.strip()

    def setNodeValue(self, key, value):
        return self.sendcmd_recv1("setNodeValue", key, str(value))

    def getNodeValue(self, key):
        return self.sendcmd_recv2("getNodeValue", key)

    def getUsbNum(self):
        return self.sendcmd_recv2("getUsbNum")

    def getCpuType(self):
        return self.sendcmd_recv2("cpuType")

    def getCpuTemp(self):
        return self.sendcmd_recv2("cpuTemp")  # 单位摄氏度

    def gethwid(self):
        return self.sendcmd_recv2("hwId")

    def gethwver(self):
        return self.sendcmd_recv2("fwVersion")

    def setDhcp(self):
        return self.sendcmd_recv1("setDhcp")

    def readKey(self):
        return self.sendcmd_recv1("readKey")

    def readKeyResult(self):
        return self.sendcmd_recv2("readKeyResult")

    def burnKey(self, sn, emac="null", wmac="null"):
        # burnKeyResult 1221212 null daaaa 若不烧emac或wmac，则传null
        return self.sendcmd_recv1("burnKey", sn, emac, wmac)

    def burnKeyResult(self):
        # msg 0=未烧KEY 1=正在烧录 2=烧Key成功 3=烧录失败
        return self.sendcmd_recv2("burnKeyResult")

    def getDDRType(self):
        return self.sendcmd_recv2("getDDRType")  # 单位Byte

    def getDDR(self):
        return self.sendcmd_recv2("ddrSize")  # 单位Byte

    def getEMMC(self):
        return self.sendcmd_recv2("emmcSize")  # 单位Byte

    def getResolution(self):
        ret, out = self.sendcmd_recv2("getHdmiImple")
        pattern = re.compile(r"(\w*-\w*)")
        list = pattern.findall(out)
        return ret, list

    def getSdNum(self):
        return self.sendcmd_recv2("getSdNum")

    def setVideoColor(self, value):
        # adb shell dumpsys activity com.utsmta.app/com.nes.factorytest.ui.activity.Main2Activity set_video_color [value]
        return self.sendcmd_recv1("setVideoColor", str(value))

    def conwifi(self, ssid, key, type="1"):
        # disable ETH..
        ret = self.sendcmd_recv1("closeEth", "0")  # 0表示关闭 1表示打开 (系统插入网线会自动用网口,该接口部分系统无效)
        if (ret):
            return self.sendcmd_recv1("conwifi", ssid, key, type)
        else:
            return ret

    def diswifi(self):
        # 断开WIIF，暂未使用
        return self.sendcmd_recv1("diswifi")

    def buttontest(self):
        return self.sendcmd_recv2("buttonResult")  # buttonResult_SUCCESS_19,20,21,22,8,9,10,11

    def wifitest(self):
        return self.sendcmd_recv1("wifitest")

    def conf(self):
        # 清空WIFI连接记录,暂未使用
        return self.sendcmd_recv1("conf")

    def wifi_begin(self, name, key, type="1", connect=0):
        if (self.ver <= 2021120203 and self.wifistart):  # 使用版本信息 兼容旧APK接口
            return False  # 仅能提前触发一个WIFI测试
        if (not connect):
            # self.wifistart=self.sendcmd_recv1("wifiScan", name)
            self.wifistart[name] = self.sendcmd_recv1("wifiScan", name)
            return self.wifistart[name]
        return False

    def wifiscan(self, name, timeout=5):
        ret = name in self.wifistart and self.wifistart[name]
        if (not ret):
            ret = self.sendcmd_recv1("wifiScan", name)
        if (ret):
            ret, value = self.sendcmd_recv2("wifiScanResult", name)
            for a in range(timeout):
                if (ret): break
                time.sleep(1)
                ret, value = self.sendcmd_recv2("wifiScanResult", name)
            self.wifistart[name] = False
        else:
            value = None
        return ret, value

    def bt_begin(self, name, connect):
        if (connect):
            self.btstart = self.sendcmd_recv1("bttest", name)
        else:
            self.btstart = self.sendcmd_recv1("btScan", name)
        return self.btstart

    def btscan(self, name, timeout=3):
        ret = self.btstart
        if (not ret):
            ret = self.sendcmd_recv1("btScan", name)
        if (ret):
            ret, value = self.getbttestres(timeout)
            self.btstart = False
        else:
            value = None
        return ret, value

    def bttest(self, name):
        return self.sendcmd_recv1("bttest", name)

    def stopbttest(self):
        return self.sendcmd_recv1("stopbttest")

    def casePass(self, casename, *para):
        # casename=[
        # MICROP_TEST麦克风,MEDIA音视频,DVBDVB,LNB_22KLNB/22K,LNB_22K_TAntennaPower,CLEAR_DATA清除厂测数据,ADD_SBOXID扫入SBOXID,
        # ADD_SN扫入SN,OPEN_ADB打开adb,TEMP_HUMID温湿度,CECCEC测试,KEY_PRESS按键测试,KEY_SEND_IR红外发射测试,HDMI_INHDMI_IN,
        # CHECK_TEST_RESULT校验测试结果,ZIG_BEEZigbee,GSM2G模块,FOUR_G4G模块,ROUTER_4G路由-4G测试,WIFI_4G4G_WIFI_天线,
        # WAN_TO_LAN更新4G路由配置,HMDI_IMPLEHDMI硬件接口,SDSD卡,CACA卡,CICI卡,USBUSB存储,BLUETOOTH蓝牙,
        # WIFIWIFI,ETHERNET以太网,WRITE_KEY烧key,READ_KEY读key,REST_SYSTEM恢复出厂设置,]
        return self.sendcmd_recv1("casePass", casename, *para)

    def caseFail(self, casename, *para):
        # casename=[
        # MICROP_TEST麦克风,MEDIA音视频,DVBDVB,LNB_22KLNB/22K,LNB_22K_TAntennaPower,CLEAR_DATA清除厂测数据,ADD_SBOXID扫入SBOXID,
        # ADD_SN扫入SN,OPEN_ADB打开adb,TEMP_HUMID温湿度,CECCEC测试,KEY_PRESS按键测试,KEY_SEND_IR红外发射测试,HDMI_INHDMI_IN,
        # CHECK_TEST_RESULT校验测试结果,ZIG_BEEZigbee,GSM2G模块,FOUR_G4G模块,ROUTER_4G路由-4G测试,WIFI_4G4G_WIFI_天线,
        # WAN_TO_LAN更新4G路由配置,HMDI_IMPLEHDMI硬件接口,SDSD卡,CACA卡,CICI卡,USBUSB存储,BLUETOOTH蓝牙,
        # WIFIWIFI,ETHERNET以太网,WRITE_KEY烧key,READ_KEY读key,REST_SYSTEM恢复出厂设置,]
        return self.sendcmd_recv1("caseFail", casename, *para)

    def getbttestres(self, timeout=15):
        result, value = self.sendcmd_recv2("getbttestres")
        for a in range(timeout):
            if (result): break
            time.sleep(1)
            logger.debug("getbttestres %d" % a)
            result, value = self.sendcmd_recv2("getbttestres")
        return result, value

    def getwifirssi(self, timeout=15):
        result, value = self.sendcmd_recv2("getwifirssi")
        for a in range(timeout):
            if (result): break
            time.sleep(1)
            logger.debug("getwifirssi %d" % a)
            result, ip = self.sendcmd_recv2("getwifirssi")
        return result, value

    def getIrKeyEvent(self, timeout=3):
        result, value = self.sendcmd_recv2("getIrKeyEvent")
        for a in range(timeout):
            if (result): break
            time.sleep(1)
            logger.debug("getIrKeyEvent %d" % a)
            result, value = self.sendcmd_recv2("getIrKeyEvent")
        return result, value

    def setEthIp(self, ip="192.168.1.148", gateway="192.168.1.1", dns1="8.8.8.8", dns2="4.4.4.4", prefixlen="24"):
        return self.sendcmd_recv2("setStaticIp", ip, gateway, dns1, dns2, prefixlen)

    def getEthIp(self, timeout=15):
        # enable Eth..
        ret = self.sendcmd_recv1("closeEth", "1")  # 0表示关闭 1表示打开
        if (ret):
            result, value = self.sendcmd_recv2("getEthIp")
            for a in range(timeout):
                if (self.error): break
                if (result): break
                time.sleep(1)
                logger.debug("getEthIp %d" % a)
                result, value = self.sendcmd_recv2("getEthIp")
            return result, value
        else:
            return ret, ""

    def getwifiip(self, timeout=15):
        result, value = self.sendcmd_recv2("getwifiip")
        for a in range(timeout):
            if (result): break
            time.sleep(1)
            logger.debug("getwifiip %d" % a)
            result, value = self.sendcmd_recv2("getwifiip")
        return result, value

    def again(self, func, againnum, *funcpara):
        result, *vulue = func(*funcpara)
        for a in range(againnum):
            if (result): break
            time.sleep(1)
            logger.debug("Again %d" % a)
            result, *vulue = func(*funcpara)
        return result, *vulue

    def hdmiStop(self):
        self.palystate = False
        logger.debug("[ADB]HDMI Stop")
        return self.sendcmd_recv1("hdmiStop")

    def avPlay(self):
        return self.sendcmd_recv1("avPlay")

    def dvb_open(self):
        self.hdmiStop()
        return self.sendcmd_recv1("startDvb")

    def dvb_volt(self, value: str):
        # 00：tuner1 0V # 11：tuner1 5V # 22：tuner1 13V/22K # 33：tuner1 18V
        # 0：tuner1 0V # 1：tuner1 5V # 2：tuner1 13V/22K # 3：tuner1 18V
        # 4：tuner2 0V # 5：tuner2 5V # 6：tuner2 13V/22K # 7：tuner2 18V
        return self.sendcmd_recv1("setVoltage", value)

    def dvb_play(self, value=0):
        # 0=播放tuner1清流; 1=播放tuner2清流; 2=播放tuner1加扰流(Irdeto IFCP); 3=播放tuner1加扰流(Irdeto MSR)
        return self.sendcmd_recv1("dvbTestPlay", str(value))

    def dvb_result(self, value=0):
        return self.sendcmd_recv1("dvbTestPlayResult", str(value))

    def dvb_close(self):
        # self.sendshell('am broadcast -a com.nes.intent.action.dvbtest --es playProgram "stop"')       # 2020.10.20
        logger.debug("[ADB]DVB Close")
        return self.sendcmd_recv1("stopDvbTestPlay")

    def adb_close_next(self):
        return self.sendcmd_recv1("closeAdbNextStation")

    def adb_close(self):
        self.sendshell('am broadcast -a com.nes.intent.action.NES_DISABLE_USB_DEBUGGING')

    def adb_patch(self,conf_dict,total=10):
        result=True
        for i in range(total):
            cmd=conf_dict.get(f"cmd{i}","")
            if (cmd):
                if ("%" in cmd):
                    storage=self.sendshell("ls /storage ")[:9]
                    logger.debug(f"{self.boxid} [Replace%] {storage}")
                    cmd = cmd % (storage)  # 变量变换
                logger.debug(f"{self.boxid} [CMD{i}] {cmd}")
                ret = self.sendshell(cmd)
                logger.debug(f"{self.boxid} [RECV{i}] {ret.strip()}")
                delay = int(conf_dict.get(f"delay{i}",0))
                if (delay):
                    time.sleep(delay)
                match = conf_dict.get(f"match{i}","")
                if (match):
                    if (not match in ret):
                        logger.error(f"{self.boxid} [Not Match{i}] {match}")
                        result = False
                        break
            else:
                break
        return result
    def get_token(self):
        old_token = self.sendshell('ls /sdcard |grep sen5config_').strip()
        new_token = self.sendshell('ls /sdcard |grep SEI_token_').strip()
        if (old_token and new_token):
            logger.error("Token Found 2 Files")
            return False, None
        elif (old_token):
            logger.debug("old token[%s]" % old_token)
            out = self.sendshell('cat /sdcard/%s' % old_token)
            token = json.loads(out)["token"]
            return token, False
        elif (new_token):
            logger.debug("new token[%s]" % new_token)
            token = self.sendshell('cat /sdcard/%s' % new_token)
            return token, True
        else:
            logger.error("Not found token")
            return False, None

    def get_tag_keys(self, _json, isnew, conf_keys):
        # print(_json)
        # print()
        print(conf_keys)
        skip_keys = ["hdcp2_key", "otp", "acsdata", "skywaykey", "vmx", "uuid", "orderId", "fbkey",
                     "irdeto",'provisionEfuseMode', 'audioEfuseMode','provisionEfuse', 'audioEfuse']  # 过期或未使用的以及不需校验的,20221008跳过efuse对比
        tags = []  # 需要读取的unifykeys节点
        unifykeys = {'did': ["DID", "IOT_CERT", "IOT_PRIV"], 'netflix': ["netflix_mgkid"],
                     'widevine': ["widevinekeybox"], "otp": ["OTP"], "acsdata": ["acsdata"], "orderId": ["OrderId"],
                     'playready': ["prpubkeybox", "prprivkeybox"], 'hdcp1_key': ["hdcp"],
                     'hdcp2_key': ["hdcp2lc128", "hdcp2key"], "uuid": ["UUID"],
                     'hdcp22_key': ["hdcp22_fw_private"], 'attestationkey': ["attestationkeybox"],
                     'attestation_v2': ["attestationkeybox"],
                     'skywaykey': ["skywaykey"], 'emac': ["mac"],
                     'sn': ["usid"], 'wmac': ['wmac'], 'oem': ["oem"], 'ssn': ["ssn"], 'skey': ["skey"],
                     'fbkey': ["fbxserial"]}
        if (conf_keys):
            if (isnew):
                require_keys = _json["requiredPublicKey"] + _json["requiredUploadKey"]  # 新token
                # print(require_keys, "hdcp22" in require_keys)
                for k, b in conf_keys.items():
                    if (not k in skip_keys):
                        if (k == "sn"):
                            token_sta = not _json["assignSn"] == 2
                        elif (k == "emac"):
                            token_sta = not _json["assignMac"] == 2
                        elif (k == "wmac"):
                            token_sta = not _json["assignWmac"] == 2
                        elif (k == "oem"):
                            token_sta = not _json["oemKey"] == ""
                            # print(_json["oemKey"] == "", _json["oemKey"])
                        elif (k == "attestationkey"):
                            token_sta = k in require_keys or "attestation_v2" in require_keys
                        else:
                            token_sta = k in require_keys
                            if (k == "playready"):
                                if (b):
                                    token_sta = "public_playready" in require_keys and "playready" in require_keys  # new
                                    # token_sta = "prpubkeybox" in require_keys and "prprivkeybox" in require_keys
                                else:
                                    token_sta = "public_playready" in require_keys or "playready" in require_keys  # new
                                    # token_sta ="prpubkeybox" in require_keys or "prprivkeybox" in require_keys
                            if (k == "hdcp22_key"):
                                token_sta = "hdcp22" in require_keys  # new
                                # token_sta = "hdcp22_fw_private" in require_keys
                            if (k == "skey"):
                                token_sta = "tivo_skey" in require_keys
                        cmp = b == token_sta
                    if (not cmp):
                        logger.error("Comparison config Fail [%s]%s" % (k, b))
                        return False
                    if (b):
                        tags += unifykeys.get(k,[])     # 20221008跳过efuse对比,并log为空
                return tags
            else:

                require_keys = _json["require_keys"]  # 旧token
                for k, b in conf_keys.items():
                    if (not k in skip_keys):
                        if (k == "sn"):
                            # token_sta = not _json["assign_Sn"]==2
                            token_sta = not _json["assign_sn"] == 2
                        elif (k == "emac"):
                            # token_sta = not _json["assign_Mac"] == 2
                            token_sta = not _json["assign_mac"] == 2
                        elif (k == "wmac"):
                            # token_sta = not _json["assign_Wmac"] == 2
                            token_sta = not _json["assign_wmac"] == 2
                        elif (k == "oem"):
                            # token_sta = not _json["oem_Key"] == 2
                            token_sta = not _json["oem_key"] == ""
                            # print(_json["oem_key"] == "",_json["oem_key"])
                        elif (k == "attestationkey"):
                            token_sta = k in require_keys or "attestation_v2" in require_keys
                        else:
                            token_sta = k in _json["require_keys"]
                            if (k == "playready"):
                                if (b):
                                    token_sta = "prpubkeybox" in require_keys and "prprivkeybox" in require_keys
                                else:
                                    token_sta = "prpubkeybox" in require_keys or "prprivkeybox" in require_keys
                            if (k == "hdcp22_key"):
                                token_sta = "hdcp22_fw_private" in require_keys
                            if (k == "skey"):
                                token_sta = "tivo_skey" in require_keys
                        cmp = b == token_sta
                    if (not cmp):
                        logger.error("Comparison[%s] Config Fail" % k)  # 显示错误配置的key名
                        return False
                    if (b):
                        tags += unifykeys.get(k,[])     # 20221008跳过efuse对比,并log为空
                return tags
        return False

    def get_fb_token(self):
        fb_token = self.sendshell('ls /sdcard |grep pms_config_').strip()
        if (fb_token):
            out = self.sendshell('cat /sdcard/%s' % fb_token)
            return out
        else:
            logger.error("Not found fb_token")
        return False

    def get_apkconfig(self):
        configefile = self.sendshell('ls /sdcard |grep SEI_CaseParmConfig').strip()
        if (configefile):
            logger.debug("Apk config[%s]" % configefile)
            out = self.sendshell('cat /sdcard/%s' % configefile)
            conf_json = self.token2json(out)
            if ("writeKey" in conf_json):
                _json = conf_json["writeKey"]
                _json.pop("testState")
                return _json, conf_json
        else:
            logger.error("Not found apk config")
        return False, {}

    def get_token_json(self):
        token, isnew = self.get_token()
        if (token):
            _json = self.token2json(token)
            return token, _json, isnew
        else:
            token, isnew = self.get_token()
            if (token):
                _json = self.token2json(token)
                return token, _json, isnew
            else:
                return False, {}, isnew

    def url_get(self, token, url):
        payload = {}
        headers = {'Authorization': 'Bearer %s' % token}
        # requests.packages.urllib3.disable_warnings()
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        response_dict = json.loads(response.text)
        return response.text, response_dict

    def url_put(self, token, url, payload={}, Bearer=True):
        if (Bearer):
            headers = {'Authorization': 'Bearer %s' % token, 'Content-Type': 'application/json'}
        else:
            headers = {'Authorization': '%s' % token, 'Content-Type': 'application/json'}
        response = requests.request("PUT", url, headers=headers, data=payload, verify=False)
        response_dict = json.loads(response.text)
        return response.text, response_dict

    def url_post(self, token, url, dict={}, Bearer=True):
        payload = json.dumps(dict)
        if (Bearer):
            headers = {'Authorization': 'Bearer %s' % token, 'Content-Type': 'application/json'}
        else:
            headers = {'Authorization': '%s' % token, 'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        response_dict = json.loads(response.text)
        return response.text, response_dict

    def echo_file(self, base64str, remote):
        for j in range(2):
            if (isinstance(self.portpath, str)):
                n = 7000  # exe命令窗 长度限制
                for i in range(0, len(base64str), n):
                    con = base64str[i:i + n]
                    if (i):
                        self.sendshell('"echo %s >> /sdcard/%s"' % (con.strip(), remote))  # 传入文件的方式传递添加模式
                    else:
                        self.sendshell('"echo %s > /sdcard/%s"' % (con.strip(), remote))  # 传入文件的方式传递
            else:
                self.sendshell('echo "%s" > /sdcard/%s' % (base64str, remote))  # 传入文件的方式传递
            check = len(self.sendshell('cat /sdcard/%s' % (remote))) >= len(base64str)
            if check:
                return True
            else:
                self.sendshell('rm /sdcard/%s' % (remote))
                logger.debug("[echo_file]%s Remove and Again" % remote)

    def set_pms_keys(self, _token, _json, file_name="require_keys.txt"):
        if ("server_url_key_batch" in _json):
            logger.debug(f"[{self.boxid}] 请求..")
            url = "%s/%s" % (_json["server_url_key_batch"], self.boxid)
            pname = self.sendshell("getprop ro.product.device").strip()
            if ('require_keys' in _json and "attestationkey" in _json['require_keys']):  # 默认返回token配置的attestationkey
                url = "%s/%s?replaceKeys=attestationkey.%s" % (
                    _json["server_url_key_batch"], self.boxid, pname)  # 使用盒子的device名称获取keys(比默认的优先)
            response, response_dict = self.url_get(_token, url)
            if ("key_batch" in response_dict):
                replace_res = base64.b64encode(response.encode()).decode()
                ret = self.echo_file(replace_res, file_name)
                if not ret:
                    logger.error("[echo_file]%s Fail" % file_name)
                return ret, pname
            else:
                pname = self.sendshell("getprop ro.product.name").strip()
                if ('require_keys' in _json and "attestationkey" in _json[
                    'require_keys']):  # 默认返回token配置的attestationkey
                    url = "%s/%s?replaceKeys=attestationkey.%s" % (_json["server_url_key_batch"], self.boxid, pname)
                response, response_dict = self.url_get(_token, url)
                if ("key_batch" in response_dict):
                    replace_res = base64.b64encode(response.encode()).decode()
                    ret = self.echo_file(replace_res, file_name)
                    if not ret:
                        logger.error("[echo_file]%s Fail" % file_name)
                    return ret, pname
                else:
                    logger.error(response_dict)
                    return False, response
        else:
            logger.error("Token Config Error")
            return False, "Token Config Error"
        # return False, "Get pms Fail"

    def token2json(self, token):
        if ("." in token):
            token = token.split('.')[1]
        for i in range(5):
            if (len(token) % 4):
                token += "="
            else:
                break
        _json = json.loads(base64.b64decode(token).decode())
        return _json

    def push_steam(self, stream, filename="pc_fbkey"):
        # adb_info = _AdbTransactionInfo(None, None, None, 10,timeout_s=10)     # 20221008 AdbDevice.push 变成使用self.dev._open(b'sync:' 返回了
        filesync_info = _FileSyncTransactionInfo(constants.FILESYNC_PUSH_FORMAT, maxdata=self.dev._maxdata)
        if not self.dev.available:
            return False
        adb_info=self.dev._open(b'sync:',None,constants.DEFAULT_READ_TIMEOUT_S,None)
        # self.dev._push(stream, '/sdcard/English', constants.DEFAULT_PUSH_MODE, 0, None, adb_info, filesync_info)
        fileinfo = ('{},{}'.format('/sdcard/%s' % filename, int(constants.DEFAULT_PUSH_MODE))).encode('utf-8')
        self.dev._filesync_send(constants.SEND, adb_info, filesync_info, data=fileinfo)
        data_size = self.dev.max_chunk_size
        for data in stream(data_size):
            if data:
                self.dev._filesync_send(constants.DATA, adb_info, filesync_info, data=data)
            else:
                break
            mtime = int(time.time())
        self.dev._filesync_send(constants.DONE, adb_info, filesync_info, size=mtime)
        for cmd_id, _, data in self.dev._filesync_read_until([], [constants.OKAY, constants.FAIL], adb_info,
                                                             filesync_info):
            if cmd_id == constants.OKAY:
                return True
        self.dev._close(adb_info)
        return False

    def adbpull(self, remote, local):
        if (self.has_error()):
            return False
        try:
            if (isinstance(self.portpath, str)):  # exe模式 push文件
                ret = os.popen("adb -d -t %s pull %s %s" % (self.portpath, remote, local)).read()
                return ret
            else:
                ret = self.dev.pull(remote, local)
                return True
        except Exception as e:
            print("[adbpull]", e)
            self.error = 1  # 指令错误
            return False

    def adbpush(self, local, remote):
        if (self.has_error()):
            return False
        try:
            if (isinstance(self.portpath, str)):  # exe模式 push文件
                ret = os.popen("adb -d -t %s push %s %s" % (self.portpath, local, remote)).read()
                return ret
            else:
                ret = self.dev.push(local, remote)
                return True
        except Exception as e:
            print("[adbpush]", e)
            self.error = 1  # 指令错误
            return False

    def fbkey_push(self, mac, filename="pc_fbkey"):
        if (':' in mac):
            mac = mac.replace(":", "")
        token = self.get_fb_token()
        if (token):
            _json = self.token2json(token)
            _url = "%s/factory/fbKeys/installCertificate" % _json['host']
            retstr, retjson = self.url_post(token, _url, {"mac": mac, "chipId": self.boxid}, False)
            print(retstr)
            if ('body' in retjson and "certUrl" in retjson['body']):
                file_url = retjson['body']['certUrl']
                response = requests.request("GET", file_url, headers={}, data={})
                print(response)
                fbpwd = retjson['body']['password']
                fbpwd = base64.b64encode(fbpwd.encode()).decode()
                if (isinstance(self.portpath, str)):  # exe模式 push文件
                    tmpfile = str(uuid.uuid1())
                    with open(tmpfile, 'wb') as f:
                        data = b''
                        for chunk in response.iter_content(chunk_size=512):
                            f.write(chunk)
                            data += chunk
                    tmp_md5 = hashlib.md5(data).hexdigest()
                    out = self.adbpush(tmpfile, "/sdcard/%s" % filename)
                    out = self.sendshell("md5sum /sdcard/%s" % filename)
                    md5_send = out.split(" ")[0].strip()
                    # print(tmp_md5, tmpfile)
                    # print(md5_send, "pc_fbkey")
                    os.remove(tmpfile)
                    if (md5_send == tmp_md5):
                        logger.info("fbkey push Finish")
                        return True, fbpwd
                    else:
                        logger.error("Push fbkey File Error")
                        return False, fbpwd
                else:  # usb使用stream流模式push文件
                    return self.push_steam(response.iter_content, filename), fbpwd
        return False, ''

    def keys_burn(self, sn, emac="null", wmac="null", file_name="require_keys.txt"):
        if (not sn):
            return False, "Input SN[%s] Fail" % sn
        if (not emac == 'null'):
            if (':' in emac):
                pattern = re.compile(r"^\s*([0-9a-fA-F]{2,2}:){5,5}[0-9a-fA-F]{2,2}\s*$")
            else:
                pattern = re.compile(r"^\s*([0-9a-fA-F]{2,2}){6,6}\s*$")
            if (not pattern.match(emac)):
                return False, "Input EMAC[%s] Fail" % emac
        if (not wmac == 'null'):
            if (':' in wmac):
                pattern = re.compile(r"^\s*([0-9a-fA-F]{2,2}:){5,5}[0-9a-fA-F]{2,2}\s*$")
            else:
                pattern = re.compile(r"^\s*([0-9a-fA-F]{2,2}){6,6}\s*$")
            if (not pattern.match(wmac)):
                return False, "Input WMAC[%s] Fail" % wmac
        logger.debug("[%s]Start Burn Keys.." % self.boxid)
        msg = ""
        _token, _json, isnew = self.get_token_json()
        if (not _token):
            return False, "Read Token Error"
        conf_keys, conf = self.get_apkconfig()
        if (not conf_keys):
            conf_keys, conf = self.get_apkconfig()
        if (not conf_keys):
            return False, "Read APK config Fail"
        print(conf_keys)
        if (isnew):
            if ('host' in _json):
                _url = "%s/factory/device/operation/batchConf" % _json['host']
                response, response_dict = self.url_get(_token, _url)
                if ('code' in response_dict and response_dict['code'] == 0 and 'body' in response_dict):
                    _json = response_dict['body']
                else:
                    response, response_dict = self.url_get(_token, _url)
                    if ('code' in response_dict and response_dict['code'] == 0 and 'body' in response_dict):
                        _json = response_dict['body']
                    else:
                        return False, "PMS GetKeys Fail"
            else:
                return False, "PMS token Fail"
            print("[New Token Json]",_json)
            if (_json.get("assignSn",0)==4):
                logger.debug("[PMS]Skip SN Range Recheck")     # 如pms配置的assignSn=4,则跳过SN的范围校验(SN2.0新规则)
            else:
                if ('startSn' in _json):
                    judge = self.check_sn(sn, _json["startSn"], _json["endSn"])
                    if (not judge): return False, "SN OverRange"
            if ((not wmac == 'null') and 'startWmac' in _json):
                judge = self.check_mac(wmac, _json["startWmac"], _json["endWmac"])
                if (not judge): return False, "WMAC OverRange"
            if ((not emac == 'null') and 'startMac' in _json):
                judge = self.check_mac(emac, _json["startMac"], _json["endMac"])
                if (not judge): return False, "EMAC OverRange"
            config_json = base64.b64encode(response.encode()).decode()
            ret = self.echo_file(config_json, "config_keys.txt")
            if not ret:
                logger.error("[echo_file]%s Fail" % file_name)
                return False, 'echo_file Fail'
            logger.debug(f"[{self.boxid}] 请求..")
            response, response_dict = self.url_post(_token, _json["grabKeyUrl"], {"chipId": self.boxid})
            # print(response_dict)
            if (response_dict['code'] == 0):
                replace_res = base64.b64encode(response.encode()).decode()
                self.echo_file(replace_res, file_name)
                ret, msg = self.sendcmd_recv2_data("initRequestKey", file_name, sn, emac, wmac, "config_keys.txt")
                if (not ret):
                    self.error = 0
                    time.sleep(1)
                    ret, msg = self.sendcmd_recv2_data("initRequestKey", file_name, sn, emac, wmac, "config_keys.txt")
            else:
                logger.error(response_dict)
                return False, 'grabKeyUrl Fail'
            if (not ret):
                return False, "[initRequestKey]%s" % msg
            time.sleep(0.1)
            ret, get_json = self.sendcmd_recv2_data("getPutkeyinfo")  # 获取需校验的信息
            if (not ret):
                logger.debug("[getPutkeyinfo]Again")
                time.sleep(0.2)
                ret, get_json = self.sendcmd_recv2_data("getPutkeyinfo")  # 获取需校验的信息
                if (not ret):
                    return False, "getPutkeyinfo Fail"
            checkjson = eval(get_json)
            logger.debug(f"[{self.boxid}] 校验..")
            ret, msg = self.url_post(_token, _json["uploadKeyUrl"], checkjson)  # pms校验信息
            # print(ret) # {"code":16016,"message":"key conflicted, data was recorded","signature":null,"requestId":null,"timestamp":0,"body":null}
            # print(msg) {'code': 16016, 'message': 'key conflicted, data was recorded', 'signature': None, 'requestId': None, 'timestamp': 0, 'body': None}
            if (not msg['code'] == 0):  # if (response_dict['code'] == 0):
                logger.error(msg)
                return False, msg['message']
            if ("oemKey" in _json):
                _oem = _json["oemKey"]
            else:
                _oem = ""
        else:
            if ('start_sn' in _json):
                judge = self.check_sn(sn, _json["start_sn"], _json["end_sn"])
                if (not judge): return False, "SN OverRange"
            if ((not wmac == 'null') and 'start_wmac' in _json):
                judge = self.check_mac(wmac, _json["start_wmac"], _json["end_wmac"])
                if (not judge): return False, "WMAC OverRange"
            if ((not emac == 'null') and 'start_mac' in _json):
                judge = self.check_mac(emac, _json["start_mac"], _json["end_mac"])
                if (not judge): return False, "EMAC OverRange"
            ret, pname = self.set_pms_keys(_token, _json, file_name)  # 获取明文key并写入盒子
            if (not ret):
                return False, pname
            # print(self.sendshell('sync'))  # 传入文件的方式传递
            # print("initRequestKey", file_name, sn, emac, wmac, "null")
            ret, msg = self.sendcmd_recv2_data("initRequestKey", file_name, sn, emac, wmac, "null")  # 通知盒子处理key文件
            if (not ret):
                self.error = 0
                time.sleep(1)
                ret, msg = self.sendcmd_recv2_data("initRequestKey", file_name, sn, emac, wmac, "null")  # 通知盒子处理key文件
                if (not ret):
                    return False, "[initRequestKey_o]%s" % msg
            time.sleep(0.1)
            ret, get_json = self.sendcmd_recv2_data("getPutkeyinfo")  # 获取需校验的信息
            if (not ret):
                logger.debug("[getPutkeyinfo_o]Again")
                time.sleep(0.2)
                ret, get_json = self.sendcmd_recv2_data("getPutkeyinfo")  # 获取需校验的信息
                if (not ret):
                    return False, "[getPutkeyinfo_o]getPutkeyinfo Fail"
            checkjson = eval(get_json)
            if ("attestationkey" in checkjson):  # attestationkey 的特殊处理
                checkjson["attestationkey"] = pname
            data = json.dumps(checkjson)
            if ("server_url_key_record" in _json):
                _url = _json["server_url_key_record"]
                response, response_dict = self.url_put(_token, _url, data)  # pms校验信息
                if ("err_code" in response_dict):
                    logger.error(response)
                    return False, response
            else:
                return False, "Token Config Error"
            if ("oem_key" in _json):
                _oem = _json["oem_key"]
            else:
                _oem = ""
        tags = self.get_tag_keys(_json, isnew, conf_keys)
        if (not tags):
            return False, "Comparison config 配置错误"
        if ("oem" in conf_keys and conf_keys['oem']):  # 特殊处理OEM与DDR类型
            logger.debug("Check OEM and DDR Type")
            checkddr, ddrtype = self.sendcmd_recv2("getDDRType")
            if (checkddr):  # 读取不到DDR也校验OEM规则
                checkddr = self.check_oem(_oem.strip(), ddrtype,_json)
            # checkddr=self.sendcmd_recv1("checkDDROem")
            if (not checkddr):
                return False, "Check[%s] DDR Type[%s] Fail" % (_oem, ddrtype)
        if ("did" in conf_keys and conf_keys['did']):  # 特殊的fbkey处理
            return False, "Burn did(IOT) unsupport"
        if ("vmx" in conf_keys and conf_keys['vmx']):  # 特殊的fbkey处理
            return False, "Burn vmx unsupport"
        if ("irdeto" in conf_keys and conf_keys['irdeto']):  # 特殊的fbkey处理
            return False, "Burn irdeto unsupport"
        if ("fbkey" in conf_keys and conf_keys['fbkey']):  # 特殊的fbkey处理
            hasfbkey = self.sendcmd_recv1("readFbkey")
            if (hasfbkey):
                logger.debug("Found Fbkey exists")
            else:
                logger.debug("Burn Fbkey ..")
                ret, fbpwd = self.fbkey_push(emac, "pc_fbkey")  # 写入fbkey文件
                # print(ret, fbpwd)
                if (ret):
                    ret = self.sendcmd_recv1('burnFbkey', "pc_fbkey", fbpwd)
                    # ret,msg = self.sendcmd_recv2('burnFbkey', "pc_fbkey", fbpwd)
                    if (ret):
                        logger.debug("[%s]Burn fbkey" % self.boxid)
                    else:
                        return False, "Burn fbkey Fail"
                else:
                    return False, "Get fbkey Fail"
        return self.burn_keys(conf_keys)

    def burn_keys(self, conf_keys):
        logger.debug("[%s]Burnning Keys.." % self.boxid)
        result, msg = self.sendcmd_recv2("burnKeyTwo")  # 约1.8~2秒
        if (result):
            msg = "%s" % (','.join([i for i, j in conf_keys.items() if j]))
            logger.debug("[%s]Finish Burn Keys" % self.boxid)
        else:
            logger.error(f"{self.boxid} burnKeyTwo Error:{msg}")
            self.reconnect()    # 重新连接并重新发送烧key指令
            result, msg = self.sendcmd_recv2("burnKeyTwo")  # 约1.8~2秒
            if (result):
                msg = "%s" % (','.join([i for i, j in conf_keys.items() if j]))
                logger.debug("[%s]Finish Burn Keys" % self.boxid)
            else:
                logger.error(f"{self.boxid} burnKeyTwo Again Error:{msg}")
        return result, msg

    def check_mac(self, mac, min, max):
        print(mac, "[min]",min,"[max]", max)
        _mac = mac.split(":")
        if (len(_mac) < 2):
            _mac = [mac[i * 2:i * 2 + 2] for i in range(6)]
        _min = min.split(":")
        if (len(_min) < 2):
            _min = [min[i * 2:i * 2 + 2] for i in range(6)]
        _max = max.split(":")
        if (len(_max) < 2):
            _max = [max[i * 2:i * 2 + 2] for i in range(6)]
        for i, m in enumerate(_mac):
            _mi = _min[i]
            _ma = _max[i]
            # print(m,_mi,_ma,m==_mi and m==_ma)
            if (not (m == _mi and m == _ma)):
                return int(_mi, 16) <= int(m, 16) <= int(_ma, 16)
        return True

    def check_mac_wmac(self, mac, wmac):
        # print(mac, wmac)
        _mac = mac.split(":")
        if (len(_mac) < 2):
            _mac = [mac[i * 2:i * 2 + 2] for i in range(6)]
        _wmac = wmac.split(":")
        if (len(_wmac) < 2):
            _wmac = [wmac[i * 2:i * 2 + 2] for i in range(6)]
        judge = _mac[:-2] == _wmac[:-2]
        if (judge):
            if (_mac[-2] == _wmac[-2]):
                judge = (int(_mac[-1], 16) + 1) == int(_wmac[-1], 16)
            else:
                judge = (int(_mac[-2], 16) + 1) == int(_wmac[-2], 16) and int(_wmac[-1], 16) == 0 and int(_mac[-1],
                                                                                                          16) == 255
        return judge

    def check_sn(self, sn, min, max):
        # print(sn,min,max)
        for i, m in enumerate(sn):
            _mi = min[i]
            _ma = max[i]
            if (not (m == _mi and m == _ma)):
                if (m.isdigit() and _mi.isdigit() and _ma.isdigit()):
                    return int(_mi, 16) <= int(m, 16) <= int(_ma, 16)
                else:
                    # print(_mi<=m<=_ma,_mi,m,_ma)
                    return _mi <= m <= _ma
        return True

    def check_oem(self, oem, matchddr=None,_json={}):  # 2021/07/21划定OEM规则与DDR
        # print(oem,matchddr)
        extrajson=_json.get('extraJson',"")     # 增加客制化(oemRuleType=1)oem规则支持
        if extrajson:
            custom_oem=eval(extrajson).get("oemRuleType","")=="1"
            if custom_oem:
                match = re.match(r"^(ATV00)[01]{1}(000)[0-9]{2}[A-Za-z0-9_]{1,21}$", oem)
                return match
        match = re.match(r"^(ATV00)[01]{1}(000)[0-9]{2}[0]{18}[A][A-Za-z0-9]{2}$", oem)
        if (match):
            if (not matchddr):
                return True
            return "DDR3" in matchddr.upper()
        match = re.match(r"^(ATV00)[01]{1}(000)[0-9]{2}[0]{18}[B][A-Za-z0-9]{2}$", oem)
        if (match):
            if (not matchddr):
                return True
            return "DDR4" in matchddr.upper()
        match = re.match(r"^(ATV00)[01]{1}(000)[0-9]{2}[0]{18}[C][A-Za-z0-9]{2}$", oem)
        if (match):
            if (not matchddr):
                return True
            return "LPDDR4" in matchddr.upper()
        match = re.match(r"^(ATV00)[01]{1}(000)[0-9]{2}[0]{19}[A-Za-z0-9]{2}$", oem)
        if (match):
            return True
        match = re.match(r"^(ATV00)[01]{1}(000)[0-9]{2}[A-Z1-9]{2}[A-Z0-9]{19}$", oem)
        if (match):
            return True
        match = re.match(r"^(ATV00)[01]{1}(000)[0-9]{2}[0]{18}[D-Z][A-Za-z0-9]{2}$", oem)
        if (match):
            return True
        return False

    def check_fbx_mac(self, value):
        ret1, value1 = self.sendcmd_recv2("readKeyValue", "mac")
        ret2, value2 = self.sendcmd_recv2("getFbMac")
        if (ret1 and ret2):
            return self.check_mac(value1, value2, value2)
        logger.error("Read Freebox Mac Error")
        return False

    def keys_read(self):
        _token, _json, isnew = self.get_token_json()
        conf_keys, conf = self.get_apkconfig()
        # print(conf_keys)
        if (not conf_keys):
            conf_keys, conf = self.get_apkconfig()
        if ("did" in conf_keys and conf_keys['did']):  # 特殊的IOT处理
            return False, "Burn did(IOT) unsupport"
        if ("vmx" in conf_keys and conf_keys['vmx']):  # 特殊的vmx处理
            return False, "Burn vmx unsupport"
        if ("irdeto" in conf_keys and conf_keys['irdeto']):  # 特殊的irdeto处理
            return False, "Burn irdeto unsupport"
        # if ("fbkey" in conf_keys and conf_keys['fbkey']):  # 特殊的fbkey处理--已集成到下面fbxserial的子case处理了
        # hasfbkey = self.sendcmd_recv1("readFbkey")
        if (isnew):
            if ('host' in _json):
                _url = "%s/factory/device/operation/batchConf" % _json['host']
                response, response_dict = self.url_get(_token, _url)
                if ('code' in response_dict and response_dict['code'] == 0 and 'body' in response_dict):
                    _json = response_dict['body']
                else:
                    response, response_dict = self.url_get(_token, _url)
                    if ('code' in response_dict and response_dict['code'] == 0 and 'body' in response_dict):
                        _json = response_dict['body']
                    else:
                        return False, "PMS GetKeys Fail"
            else:
                return False, "PMS token Fail"
        tags = self.get_tag_keys(_json, isnew, conf_keys)  # 比较配置key,获取需校验的节点名称
        # print(tags)

        value_check = ["IOT_CERT", "IOT_PRIV", "skywaykey", "mac", "oem", "usid", "fbxserial",
                       'wmac']  # 需要校验内容的unifykeys (注意与加密KEY无交集)
        encrypt_keys = ["netflix_mgkid", "widevinekeybox", "prpubkeybox", "prprivkeybox", "hdcp", "hdcp22_fw_private",
                        "attestationkeybox"]  # PMS加密KEY
        if (tags):
            logger.debug("Check:%s" % tags)
            for k in tags:
                if (k in value_check):
                    judge, value = self.sendcmd_recv2("readKeyValue", k)
                    if (judge):
                        if (k == "IOT_CERT"):
                            # print(k, value)
                            judge = "BEGIN CERTIFICATE" in value and "END CERTIFICATE" in value
                        elif (k == "IOT_PRIV"):
                            # print(k, value)
                            judge = "BEGIN RSA PRIVATE KEY" in value and "END RSA PRIVATE KEY" in value
                        elif (k == "skywaykey"):
                            # print(k, value)
                            judge = "BEGIN RSA PRIVATE KEY" in value and "END RSA PRIVATE KEY" in value
                        elif (k == "oem"):
                            judge = self.check_oem(value,_json=_json)
                        elif (k == "wmac"):
                            if (isnew):
                                if ('startWmac' in _json):
                                    judge = self.check_mac(value, _json["startWmac"], _json["endWmac"])
                            else:
                                if ('start_wmac' in _json):
                                    judge = self.check_mac(value, _json["start_wmac"], _json["end_wmac"])
                        elif (k == "mac"):
                            if (isnew):
                                if ('startMac' in _json):
                                    judge = self.check_mac(value, _json["startMac"], _json["endMac"])
                            else:
                                if ('start_mac' in _json):
                                    judge = self.check_mac(value, _json["start_mac"], _json["end_mac"])
                            if ("fbxserial" in tags):
                                judge, fb_usid = self.sendcmd_recv2("readKeyValue", "usid")  # mac=usid
                                if (judge):
                                    judge = self.check_mac(value, fb_usid, fb_usid)
                                    if (judge):
                                        judge, fb_wmac = self.sendcmd_recv2("readKeyValue", "wmac")  # mac+1=wamc
                                        if (judge):
                                            judge = self.check_mac_wmac(value, fb_wmac)
                                        else:
                                            logger.error("Read Freebox wmac Error")
                                    else:
                                        logger.error("Freebox mac[%s] usid[%s] FAIL" % (value, fb_usid))
                                else:
                                    logger.error("Read Freebox usid Error")
                        elif (k == "usid"):
                            if ("fbxserial" in tags):
                                judge = self.sendcmd_recv1("readFbkey")
                                if (judge):
                                    judge = self.check_fbx_mac(value)
                                else:
                                    logger.error('Freebox Fbkey Error')
                            else:
                                if (isnew):
                                    if (_json.get("assignSn", 0) == 4):
                                        logger.debug(
                                            "[PMS]Skip SN Range Recheck")  # 如pms配置的assignSn=4,则跳过SN的范围校验(SN2.0新规则)
                                    else:
                                        if ('startSn' in _json):
                                            # print(k,value)
                                            judge = self.check_sn(value, _json["startSn"], _json["endSn"])
                                else:
                                    if ('start_sn' in _json):
                                        judge = self.check_sn(value, _json["start_sn"], _json["end_sn"])
                        elif (k == "fbxserial"):
                            if ('start_sn' in _json):
                                judge = self.check_sn(value, _json["start_sn"], _json["end_sn"])
                        else:
                            judge = False
                else:
                    if (isnew):
                        if (k in encrypt_keys):
                            judge = self.sendcmd_recv1("readEncryptKey", k)
                            value = 99999
                        elif (k == "ssn" and "startSsn" in _json):
                            judge, value = self.sendcmd_recv2("readKeyValue", k)
                            judge = self.check_sn(value, _json["startSsn"], _json["endSsn"])
                        else:
                            judge, value = self.sendcmd_recv2("readKeySize", k)
                            if (judge):
                                if (k == "attestationkeybox"):
                                    judge = int(value) > 8000
                                elif (k == "ssn"):
                                    judge = int(value) == 18
                                elif (k == "skey"):
                                    judge = int(value) == 32
                                else:
                                    judge = int(value) > 0
                    else:
                        judge, value = self.sendcmd_recv2("readKeySize", k)
                        if (judge):
                            if (k == "attestationkeybox"):
                                judge = int(value) > 8000
                            elif (k == "ssn"):
                                judge = int(value) == 18
                            elif (k == "skey"):
                                judge = int(value) == 32
                            else:
                                judge = int(value) > 0
                # print(k,value,judge)
                # print(_json)
                if (not judge):
                    return False, "[%s]=%s" % (k, value)
            return True, ",".join(tags)
        return False, "Get Tag Fail"

    def push_fw(self, fw_file="fw_bcm4359c0_ag_mfg.bin", nvram="nvram_ap6398sa3.txt"):
        if (os.path.exists('./%s' % fw_file)):
            self.dev.push('./%s' % fw_file, "/sdcard/%s" % fw_file)
            out = self.sendshell("rmmod dhd")
            time.sleep(0.5)
            out = self.sendshell(
                "insmod /vendor/lib/modules/dhd.ko firmware_path=/sdcard/%s nvram_path=/vendor/etc/wifi/buildin/%s" % (
                    fw_file, nvram))
            time.sleep(1)
            return True
        else:
            logger.error("Not Found fw_file[./%s]" % fw_file)
            return False

    def wifi_fw_start(self, txchain):
        self.sendshell("ifconfig wlan0 down")
        out = self.sendshell("ifconfig")
        if ("wlan0" in out):
            time.sleep(0.5)
        self.sendshell("ifconfig wlan0 up")
        time.sleep(0.5)
        out = self.sendshell("ifconfig")
        if (not "wlan0" in out):
            time.sleep(0.5)
        time.sleep(0.5)
        out = self.sendshell("wl ver")
        if ("WLTEST" in out):
            self.sendshell("wl pkteng_stop tx")
            self.sendshell("wl down")
            self.sendshell("wl mpc 0")
            self.sendshell("wl country ALL")
            self.sendshell("wl band b")
            self.sendshell("wl mimo_bw_cap 1")
            self.sendshell("wl mimo_txbw -1")
            self.sendshell("wl nrate -m 0")  # 传输速率MCS0
            self.sendshell("wl txchain %s" % txchain)  # 天线
            self.sendshell("wl up")
            self.sendshell("wl 2g_rate -r 11 -b 20")  # 频率
            self.sendshell("wl channel 1")  # 信道
            self.sendshell("wl phy_watchdog 0")
            self.sendshell("wl scansuppress 1")
            self.sendshell("wl phy_forcecal 1")
            self.sendshell("wl phy_txpwrctrl 1")
            self.sendshell("wl txpwr1 -1")
            time.sleep(1)
            self.sendshell("wl pkteng_start 00:90:4c:14:43:19 tx 100 1000 0")
            return True
        else:
            return False

    def telnet_router(self, ip, user, pwd):
        if (self.telnet_state): return True
        ret, lanip = self.getEthIp(3)
        if (ret):
            for i in range(3):
                time.sleep(1 + i)  # telnet前增加延时等待
                ret, retdata = self.sendcmd_recv2_data('telnetLogin', ip)
                if (ret):
                    recv = base64.b64decode(retdata).decode()
                    if ("login" in recv):
                        ret, retdata = self.sendcmd_recv2_data('telnetSend', user)
                        if (ret):
                            logger.debug('[%s]%s:%s Login..' % (ip, user, pwd))
                            recv = base64.b64decode(retdata).decode()
                            if ('Password' in recv):
                                ret, retdata = self.sendcmd_recv2_data('telnetSend', pwd)
                                if (ret):
                                    recv = base64.b64decode(retdata).decode()
                                    if ('#' in recv):
                                        self.telnet_state = True
                                        return True
                            else:
                                logger.debug('[%s]%s' % (ip, recv))
        return False

    def telnet_cmdlist(self, cmdlist: list):
        for c in cmdlist:
            time.sleep(0.2)
            for i in range(3):
                recv = self.telnet_router_cmd(c)
                if ("#" in recv):
                    break
                else:
                    logger.debug("[CoupleCMD]Again(%s)" % c)
                    if (i >= 2):
                        return False
                    time.sleep(1)
        return True

    def telnet_router_cmd(self, cmd):
        ret, retdata = self.sendcmd_recv2_data('telnetSend', "'%s'" % (cmd))
        if (ret):
            return base64.b64decode(retdata).decode()
        else:
            return ''

    def telnet_gpon140_cmd(self, cmd):
        ret, retdata = self.sendcmd_recv2_data('telnetSend', "'%s'" % (cmd))
        if (ret):
            recv64 = base64.b64decode(retdata)
            recv = recv64.decode()
            if ("SerialNum" in recv):  # cmd="prolinecmd serialnum display"  # 长SN
                pattern = re.compile(r'SerialNum:(\w+)')
                list = pattern.findall(recv)
                if (list):
                    return list[0]
            if ("XponSN" in recv):  # cmd = "prolinecmd xponsn display"  # 短SN
                pattern = re.compile(r'XponSN:(\w+)')
                list = pattern.findall(recv)
                if (list):
                    return list[0]
            if ("All led is turned on" in recv):  # 'sys led on' LED灯全亮
                return cmd == 'sys led on'
            if ("All led is turned off" in recv):  # 'sys led on' LED灯全灭
                return cmd == 'sys led off'
            print(recv64)
            return ''
        else:
            return ''

    def leds_change(self, mode=1):
        if (mode == 1):
            # self.setNodeValue("/sys/class/leds/aw9523_led/colors","003020")
            self.setNodeValue("/sys/class/leds/aw9523_led/colors", "001015")  # debug
            # self.setNodeValue("/sys/class/leds/aw9523_led/colors","001830")  # debug
            self.setNodeValue("/sys/class/leds/aw9523_led/led1", 0)
            self.setNodeValue("/sys/class/leds/aw9523_led/led2", 0)
            self.setNodeValue("/sys/class/leds/aw9523_led/led3", 0)
        elif (mode == 2):
            self.setNodeValue("/sys/class/leds/aw9523_led/colors", "003018")
            self.setNodeValue("/sys/class/leds/aw9523_led/led1", 0)
            self.setNodeValue("/sys/class/leds/aw9523_led/led2", 0)
            self.setNodeValue("/sys/class/leds/aw9523_led/led3", 0)
        elif (mode == 3):
            self.setNodeValue("/sys/class/leds/aw9523_led/mode", 0)
            # self.setNodeValue("/sys/class/leds/aw9523_led/led1", "0")
            self.setNodeValue("/sys/class/leds/aw9523_led/led1", "0000f5")
            # self.setNodeValue("/sys/class/leds/aw9523_led/led2", "0")
            self.setNodeValue("/sys/class/leds/aw9523_led/led2", "0000f5")
            # self.setNodeValue("/sys/class/leds/aw9523_led/led3", "0")
            self.setNodeValue("/sys/class/leds/aw9523_led/led3", "0000f5")
        elif (mode == 4):
            self.setNodeValue("/sys/class/leds/aw9523_led/colors", "001830")  # debug
