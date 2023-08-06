import os.path

import serial
import serial.tools.list_ports
import time
import re
from autotk.AutoCoreLite import logger
import struct
from datetime import datetime
import crcmod.predefined

def load_keycode(file="./irkeycode"):
    if os.path.exists(file):
        with open(file, "r") as f:
            irkeycode = f.read()
        return eval(irkeycode)
    else:
        return {}
_load_ir=load_keycode()

def get_com_device(filter_id=[]):
    '''
    :param <IR模块>"VID_1A86&PID_7523"<电压模块>"VID_067B&PID_2303"<SCAN扫描枪>"VID_E851&PID_1002"
    :return:
    '''
    com_ports = serial.tools.list_ports.comports()
    com_dict = {}
    port_dict = {}
    name_list = []
    for port in com_ports:
        if (port.vid):
            vid = "%04X" % port.vid
            pid = "%04X" % port.pid
            vid_pid = "VID_%s&PID_%s" % (vid, pid)
            name = port.name
            if (filter_id):
                if (vid_pid in filter_id):
                    name_list.append(name)
                    com_dict[vid_pid] = name
                    port_dict[vid_pid] = port
            else:
                com_dict[vid_pid] = name
                port_dict[vid_pid] = port
    return com_dict, port_dict, name_list


class scan_com():
    def __init__(self, Port, BaudRate: str = "9600", TimeOut=10):
        self.defaultport = Port
        self.ports = []
        self.baudrate = BaudRate
        self.timeout = TimeOut
        self.scan_dute = 0.2
        self.scan_count = int(self.timeout / self.scan_dute)
        self.ser = None
        self.err = False
        self.history = ''

    def open(self, Port=None):
        try:
            if Port == None:
                Port = self.defaultport
            self.ser = serial.Serial()
            self.ser.port = Port
            self.ser.baudrate = self.baudrate
            self.ser.timeout = self.scan_dute
            # self.ser.terminator ='\r'
            self.ser.open()
            # logger.info('打开端口%s' % Port)
        except Exception as e:
            logger.critical(e)
            self.err = True
            self.ser = None
        return self.ser

    def cls(self):
        try:
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
        except:
            pass

    def scan_port(self):
        port_names = []
        port_list = list(serial.tools.list_ports.comports())
        for i in port_list:
            port_list_list = list(i)
            port_names.append(port_list_list[0])
        self.ports = sorted(port_names)
        return self.ports

    def scan_loop(self, timeout=None):
        if (timeout):
            self.scan_count = int(timeout / self.scan_dute)
        for i in range(self.scan_count):
            ret_ls = self.ser.readlines()
            # print(ret_ls)
            if (ret_ls):
                self.history = ret_ls[-1]
                return True, self.history
        return False, ""

    def scan(self, timeout=None):
        if (timeout == -1):
            ret = False
            while not ret:
                ret, value = self.scan(10)
                if (ret):
                    logger.info(value)
                    break
            return value
        else:
            if (self.ser):
                try:
                    return self.scan_loop(timeout)
                except Exception as e:
                    try:
                        self.open()
                        return False, ""
                    except:
                        self.err = True
            else:
                try:
                    self.open()
                    return False, ""
                except:
                    self.err = True

    def send(self, msg):
        self.ser.write(msg)

    def trig_recv(self):
        trig = b"\x57\x00\x18\x00\x55\x00"
        trig_end = b"\x57\x00\x19\x00\x55\x00"
        self.ser.write(trig)
        time.sleep(0.2)
        ret = self.ser.readlines()
        result = b""
        if (ret):
            allret = b"".join(ret)
            respond = b"\x31\x00\x00\x00\x55\x00"
            if (respond in allret):
                result = allret[len(respond):]
        self.ser.write(trig_end)
        self.ser.readlines()
        return result.decode().strip()

    def close(self):
        try:
            self.ser.close()
        except:
            pass


class control_com():
    def __init__(self, Port, BaudRate: str = "9600", TimeOut=5):
        self.defaultport = Port
        self.ports = []
        self.baudrate = BaudRate
        self.timeout = TimeOut
        self.scan_dute = 0.2
        self.scan_count = int(self.timeout / self.scan_dute)
        self.ser = None
        self.err = False
        self.history = ''

    def open(self, Port=None):
        try:
            if Port == None:
                Port = self.defaultport
            self.ser = serial.Serial()
            self.ser.port = Port
            self.ser.baudrate = self.baudrate
            self.ser.timeout = self.scan_dute
            # self.ser.terminator ='\r'
            self.ser.open()
            # logger.info('打开端口%s' % Port)
        except Exception as e:
            logger.critical(e)
            self.err = True
            self.ser = None
        return self.ser

    def sendrecv(self, msg):
        self.ser.write(msg)
        time.sleep(0.05)
        return self.ser.readline()

    def open_door(self):
        self.ser.write(b"OPEN\r\n")
        time.sleep(0.05)
        # result=b'open' in out1
        # logger.debug("[Button]OPEN Door %s %s"%(out1,result))
        return True

    def close_door(self):
        self.ser.write(b"CLOSE\r\n")
        time.sleep(0.05)
        # result=b'OK' in out1
        # logger.debug("[Button]CLOSE Door %s %s"%(out1,result))
        return True
    
    def click_power(self, dute=0.4):
        out1 = self.sendrecv(b"Power_ON\r\n")
        # logger.debug("[Button]ON %s"%out1)
        time.sleep(dute)
        out2 = self.sendrecv(b"Power_OFF\r\n")
        # logger.debug("[Button]OFF %s" % out2)
        result = b'OK' in out1 and b'OK' in out2
        # print("[Button]ON %s OFF %s Click %s"%(out1,out2,result))
        logger.debug("[ButtonPower]ON %s OFF %s Click %s" % (out1, out2, result))
        return result
    def click(self, dute=1):
        out1 = self.sendrecv(b"BUTTON_ON\r\n")
        # logger.debug("[Button]ON %s"%out1)
        time.sleep(dute)
        out2 = self.sendrecv(b"BUTTON_OFF\r\n")
        # logger.debug("[Button]OFF %s" % out2)
        result = b'OK' in out1 and b'OK' in out2
        # print("[Button]ON %s OFF %s Click %s"%(out1,out2,result))
        logger.debug("[ButtonReset]ON %s OFF %s Click %s" % (out1, out2, result))
        return result

    def cls(self):
        try:
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
        except:
            pass

    def close(self):
        try:
            self.ser.close()
        except:
            pass

class ir_com():
    def __init__(self, Port, BaudRate: str = "9600", TimeOut=5):
        self.defaultport = Port
        self.ports = []
        self.baudrate = BaudRate
        self.timeout = TimeOut
        self.scan_dute = 0.2
        self.scan_count = int(self.timeout / self.scan_dute)
        self.ser = None
        self.err = False
        self.history = ''
        self.initdata()
        self.nec_mode=None
    def initdata(self):
        self.keyspecial={}
        self.keycode = {"7": b"\x01\xFE\x1E\xE1", "8": b"\x01\xFE\x13\xEC", "9": b"\x01\xFE\x12\xED",
                        "10": b"\x01\xFE\x10\xEF",
                        "11": b"\x01\xFE\x17\xE8", "12": b"\x01\xFE\x16\xE9", "13": b"\x01\xFE\x14\xEB",
                        "14": b"\x01\xFE\x1B\xE4",
                        "15": b"\x01\xFE\x1A\xE5", "16": b"\x01\xFE\x18\xE7"}
        self.keyname = {"0": b"\x01\xFE\x1E\xE1", "1": b"\x01\xFE\x13\xEC", "2": b"\x01\xFE\x12\xED",
                        "3": b"\x01\xFE\x10\xEF",
                        "4": b"\x01\xFE\x17\xE8", "5": b"\x01\xFE\x16\xE9", "6": b"\x01\xFE\x14\xEB",
                        "7": b"\x01\xFE\x1B\xE4",
                        "8": b"\x01\xFE\x1A\xE5", "9": b"\x01\xFE\x18\xE7", "ok": b"\x01\xFE\x55\xAA",
                        "left": b"\x01\xFE\x54\xAB",
                        "rigth": b"\x01\xFE\x15\xEA", "return": b"\x01\xFE\x19\xE6", "up": b"\x01\xFE\x59\xA6",
                        "down": b"\x01\xFE\x51\xAE"}
        # 支持加载的码值替换模块自带码值
        if _load_ir:
            for g,d in _load_ir.items():
                if g in ["694A","01FE"]:        # 固定的NEC红外用户码
                    for n,c in d.items():
                        h=int(c,16)
                        self.keycode[n]=bytes.fromhex(f"{g}{h:02X}{0xff-h:02X}")
                else:      
                    for n,c in d.items():
                        self.keyspecial[n]=bytes.fromhex(c)  # 原始fromhex 转输出byte , 特殊的走特殊的接口
    def check_ir(self):
        try:
            if not self.ser:
                self.open()
            self.send(b"\x01\x03\xf0\x00\x00\x01\xb7\x0a")  # 是否存在该值(xF000=61440 默认1,0xFF广播地址,指定模块)
            time.sleep(0.2)
            ret=self.recv()
            print("check_ir",ret.hex(),ret==b"\x01\x03\x02\x00\x01\x79\x84")
            return ret==b"\x01\x03\x02\x00\x01\x79\x84"
        except:
            return False
        return True
    def get_mode_nec(self):
        self.send(b"\x01\x03\xf0\x04\x00\x01\xf6\xcb")  # 0=占空比时间数据模式 1=NEC红外模式
        time.sleep(0.2)
        ret = self.recv()
        self.nec_mode = ret == b"\x01\x03\x02\x00\x01\x79\x84"
        return self.nec_mode
    def set_mode(self,nec=True):
        try:
            if not self.ser:
                self.open()
            if self.nec_mode==None:
                self.check_ir()
            _isnec=self.get_mode_nec()
            if nec:
                if not _isnec:
                    _cmd06 =b"\x01\x06\xf0\x04\x00\x01\x3a\xcb"
                    self.send(_cmd06)  # 0=占空比时间数据模式 1=NEC红外模式
                    time.sleep(0.2)
                    ret = self.recv()
                    self.nec_mode = ret == _cmd06
                    print(f"[SetMode]{ret.hex()} NEC={self.nec_mode}")
                    logger.debug(f"[SetMode]{ret.hex()} NEC={self.nec_mode}")
                return self.nec_mode
            else:
                if _isnec:
                    _cmd06 = b"\x01\x06\xf0\x04\x00\x00\xfb\x0b"
                    self.send(_cmd06)  # 0=占空比时间数据模式 1=NEC红外模式
                    time.sleep(0.2)
                    ret = self.recv()
                    self.nec_mode = not ret == _cmd06
                    print(f"[SetMode]{ret.hex()} NEC={self.nec_mode}")
                    logger.debug(f"[SetMode]{ret.hex()} NEC={self.nec_mode}")
                return not self.nec_mode
        except Exception as e:
            print(e)
        return False
    def check(self, cmd=b'\xFF\x10\xF0\x00\x00\x06\x0C\x00\x01\x00\x03\x00\x00\x00\x01\x00\x01\x00\x00\x2B\x14'):
        # FF 10 F0 00 00 06 0C 00 01 00 03 00 00 00 01 00 01 00 00 2B 14
        self.ser.write(cmd)
        time.sleep(0.5)
        ret = self.ser.readline()
        judge = ret in [b'\x01\x10\xF0\x00\x00\x06\x73\x0B']
        return judge

    def open(self, Port=None):
        try:
            if Port == None:
                Port = self.defaultport
            self.ser = serial.Serial()
            self.ser.port = Port
            self.ser.baudrate = self.baudrate
            self.ser.timeout = self.scan_dute
            # self.ser.terminator ='\r'
            self.ser.open()
            # logger.info('打开端口%s' % Port)
        except Exception as e:
            logger.critical(e)
            self.err = True
            self.ser = None
        return self.ser

    def recv(self):
        return self.ser.readline()

    def send(self, cmdbyte):
        self.ser.write(cmdbyte)

    def sendspecial(self, code: str = None):
        if self.set_mode(False):
            cmd = self.keyspecial.get(code,b"")
            if cmd:
                self.ser.write(cmd)
                print(f"[IR]{self.ser.port} Send(Special {code}):{cmd.hex()}")
                return True
        else:
            logger.error("[IrMode]Set Mode Fail")
        return False
    def sendkey(self, code: str = None, name: str = None):
        if self.set_mode():
            if (code == None):
                cmd = self.keyname.get(name,b"")
            else:
                cmd = self.keycode.get(code,b"")
            if cmd:
                self.ser.write(cmd)
                print(f"[IR]{self.ser.port} Send({name} {code}):{cmd.hex()}")
                return True
        else:
            logger.error("[IrMode]Set Mode Fail")
        return False

    def cls(self):
        try:
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
        except:
            pass

    def close(self):
        try:
            self.ser.close()
        except:
            pass


class volt_com():
    def __init__(self, Port, BaudRate: str = "57600", TimeOut=5):
        self.defaultport = Port
        self.ports = []
        self.baudrate = BaudRate
        self.timeout = TimeOut
        self.scan_dute = 0.2
        self.scan_count = int(self.timeout / self.scan_dute)
        self.ser = None
        self.err = False
        self.history = ''

    def open(self, Port=None):
        try:
            if Port == None:
                Port = self.defaultport
            self.ser = serial.Serial()
            self.ser.port = Port
            self.ser.baudrate = self.baudrate
            self.ser.timeout = self.scan_dute
            # self.ser.terminator ='\r'
            self.ser.open()
            # logger.info('打开端口%s' % Port)
        except Exception as e:
            logger.critical(f"[VoltCOM]({self.defaultport}) {e}")
            logger.critical(f"[VoltCOM]{self.scan_port()}")
            self.err = True
            self.ser = None
        return self.ser

    def cls(self):
        try:
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
        except:
            pass

    def scan_port(self):
        port_names = []
        port_list = list(serial.tools.list_ports.comports())
        for i in port_list:
            port_list_list = list(i)
            port_names.append(port_list_list[0])
        self.ports = sorted(port_names)
        return self.ports

    def sendrecv(self, msg):
        self.ser.write(msg)
        time.sleep(0.05)
        return self.ser.readline()

    def getVolt_H(self):
        return self.getVolt("H")

    def getVolt_D(self):
        return self.getVolt("D")

    def getVolt(self, cmd="H"):
        try:
            for i in range(3):
                ret = self.sendrecv(cmd.encode())
                out = ret.decode()
                pattern = re.compile(r"\S*V_(\S*)")  # 长度10以上
                list = pattern.findall(out)
                # print(out,list)
                if (list):
                    return float(list[0])
            return None
        except Exception as e:
            logger.critical("[VoltCOM]%s" % e)
            return None

    def getK(self, cmd="K"):
        try:
            for i in range(3):
                ret = self.sendrecv(cmd.encode())
                out = ret.decode()
                # print(out)
                if (cmd in out):
                    return "_P" in out
            return None
        except Exception as e:
            logger.critical("[VoltCOM]%s" % e)
            return None

    def getC(self, cmd="C"):
        try:
            for i in range(3):
                ret = self.sendrecv(cmd.encode())
                out = ret.decode()
                print(out)
                if (cmd in out):
                    return "_P" in out
            return None
        except Exception as e:
            logger.critical("[VoltCOM]%s" % e)
            return None

    def getNo(self, cmd="G"):
        try:
            for i in range(3):
                ret = self.sendrecv(cmd.encode())
                out = ret.decode()
                pattern = re.compile(r"\S*S_(\S*)")  # 长度10以上
                list = pattern.findall(out)
                if (list):
                    return list[0]
            return None
        except Exception as e:
            logger.critical("[VoltCOM]%s" % e)
            return None

    def setNo(self, sn):
        cmd = "S%s" % sn
        try:
            for i in range(3):
                ret = self.sendrecv(cmd.encode())
                out = ret.decode()
                # print(out)
                return "S_P" in out
            return None
        except Exception as e:
            logger.critical("[VoltCOM]%s" % e)
            return None

    def close(self):
        try:
            self.ser.close()
        except:
            pass


class power_com():
    def __init__(self, Port, BaudRate: str = "9600", TimeOut=5):
        self.defaultport = Port
        self.ports = []
        self.baudrate = BaudRate
        self.timeout = TimeOut
        self.scan_dute = 0.2
        self.scan_count = int(self.timeout / self.scan_dute)
        self.ser = None
        self.err = False
        self.recvlist = []
        self.history = ''
        self.crc_func = crcmod.predefined.mkCrcFun('modbus')

    def open(self, Port=None):
        try:

            if Port == None:
                Port = self.defaultport
            self.ser = serial.Serial()
            self.ser.port = Port
            self.ser.baudrate = self.baudrate
            self.ser.timeout = self.scan_dute
            self.ser.stopbits = 2
            self.ser.open()
            # logger.info('打开端口%s' % Port)
        except Exception as e:
            logger.critical("[PowerCOM]%s" % e)
            self.err = True
            self.ser = None
        return self.ser

    def sendrecv(self, msg):
        self.ser.write(msg)
        time.sleep(0.02)
        return self.ser.readline()

    def close(self):
        try:
            self.ser.close()
        except:
            pass

    def read_data(self,slave=0xf8):
        # 0xF8  # 通用地址F8 单从机下用于工厂校准
        _cmd=(slave).to_bytes(1,"little")+b"\x04\x00\x00\x00\x04"
        cmd=_cmd+(self.crc_func(_cmd)).to_bytes(2,"little")
        self.ser.write(cmd)
        # self.ser.write(b"\x01\x04\x00\x00\x00\x04\xF1\xC9")
        # print(self.crc_func(b"\x01\x04\x00\x00\x00\x04"),int.from_bytes(b"\xf1\xc9", 'little'))
        time.sleep(0.02)
        ret = self.ser.read(13)
        d = {}
        if ret:
            crc_ret = int.from_bytes(ret[-2:], 'little')
            crc_value = self.crc_func(ret[:-2])
            if crc_value == crc_ret:
                d["Voltage"] = int.from_bytes(ret[3:5], 'big') / 100
                d["Current"] = int.from_bytes(ret[5:7], 'big') / 100
                d["Power"] = int.from_bytes(ret[9:11] + ret[7:9], 'big') / 10
                # d["Power"]=int.from_bytes(ret[9:11],'big') # 16高位
        return d


class powerz_com():
    def __init__(self, Port, BaudRate: str = "11520000", TimeOut=5):
        self.defaultport = Port
        self.ports = []
        self.baudrate = BaudRate
        self.timeout = TimeOut
        self.scan_dute = 0.2
        self.scan_count = int(self.timeout / self.scan_dute)
        self.ser = None
        self.err = False
        self.recvlist = []
        self.history = ''

    def open(self, Port=None):
        try:
            if Port == None:
                Port = self.defaultport
            self.ser = serial.Serial()
            self.ser.port = Port
            self.ser.baudrate = self.baudrate
            self.ser.timeout = self.scan_dute

            # self.ser.terminator ='\x5A'
            self.ser.open()
            self.ser.set_buffer_size(1024000, 65536)
            # print(self.ser.get_settings())
            # logger.info('打开端口%s' % Port)
        except Exception as e:
            logger.critical("[PowerZCOM]%s" % e)
            self.err = True
            self.ser = None
        return self.ser

    def sendrecv(self, msg):
        self.ser.write(msg)
        time.sleep(0.02)
        return self.ser.readline()

    def close(self):
        try:
            self.ser.close()
        except:
            pass

    def connect(self):
        print(self.sendrecv(b"\xA5\x04\x00\x00\x00\x01\x07\x00\x00\x06\x5A"), "connect")

    def split_pack(self, packs):
        # print("=",packs)
        bdata = b''
        _all = b''.join(packs)
        return self.pack2data(_all)

    def pack2data(self, _all):
        a_idx = _all.find(b"\xA5")
        b_len = _all[a_idx + 1] + 7
        result = _all[b_len - 1] == 90
        if result:
            bdata = _all[a_idx + 6:b_len - 1]
            b = 0
            for i in bdata:
                b ^= i
            result = _all[a_idx + 5] == b
        else:
            print("结束位错误")
        if result:
            return True, bdata, _all[b_len:]
        else:
            print("校验位错误")
            return False, bdata, _all

    def start(self):

        ret = self.sendrecv(b"\xA5\x08\x00\x00\x00\x01\x09\x01\x00\xE8\x03\x00\x00\xE2\x5A")
        # r,d,o=self.pack2data(ret[ret.rfind(b"\xA5"):])
        # print(r,len(d),self.unpack_data(d[3:]))
        # print(self.pack2data(ret))

        print(self.get_MeterData(3))
        time.sleep(2)
        print(self.get_MeterData(3))

        # print()
        print(self.sendrecv(b"\xA5\x04\x00\x00\x00\x01\x07\x10\x00\x16\x5A"), "close")
        self.close()

    def scan_loop(self, timeout=None):
        if (timeout):
            self.scan_count = int(timeout / self.scan_dute)
        for i in range(self.scan_count):
            ret_ls = self.ser.readlines()
            if (ret_ls):
                ret, bdata, other = self.split_pack(self.recvlist + ret_ls)
                self.recvlist = [other]
                self.history = bdata
                return ret, bdata
        return False, ""

    def unpack_data(self, bdata, switch=5):
        d = {}
        d["Voltage"] = struct.unpack("f", bdata[0:4])[0]
        d["Current"] = struct.unpack("f", bdata[4:8])[0]
        d["Power"] = struct.unpack("f", bdata[8:12])[0]
        d["VolatgeDP"] = struct.unpack("f", bdata[12:16])[0]
        d["VolatgeDM"] = struct.unpack("f", bdata[16:20])[0]
        d["Current_UnAbsed"] = struct.unpack("f", bdata[20:24])[0]
        if switch:
            for k, v in d.items():
                d[k] = round(v, switch)
        d["PakcetTime"] = struct.unpack("Q", bdata[24:32])[0]
        # print(datetime.fromtimestamp(d["PakcetTime"]))
        # print(d["Voltage"],len(bdata[24:32]),len(bdata[24:]),bdata[-1])
        return d

    def get_MeterData(self, timeout=None):
        ret, pdata = self.scan_loop(timeout)
        if ret and len(pdata) == 36:
            bdata = pdata[3:]
            d = self.unpack_data(bdata)
            return True, d
        else:
            return False, {}

    def scan(self, timeout=None):
        if (timeout == -1):
            ret = False
            while not ret:
                ret, value = self.scan_loop(10)
                if (ret):
                    logger.info(value)
                    break
            return value
        else:
            if (self.ser):
                try:
                    return self.scan_loop(timeout)
                except Exception as e:
                    try:
                        self.open()
                        return False, ""
                    except:
                        self.err = True
            else:
                try:
                    self.open()
                    return False, ""
                except:
                    self.err = True


if __name__ == '__main__':
    # pp=powerz_com("COM70")
    # pp.open()
    # pp.connect()
    # pp.start()

    # pp = power_com("COM1")
    # pp.open()
    # print(pp.read_data())
    Ir=ir_com("COM71")
    Ir.open()
    print(Ir.set_mode())
