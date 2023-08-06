#!/usr/bin/python3
import collections
import os
import queue
import socket
import threading
import time
import traceback
from socket import *
import struct
import base64
import select

# see https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol
# see https://zh.wikipedia.org/wiki/%E5%8A%A8%E6%80%81%E4%B8%BB%E6%9C%BA%E8%AE%BE%E7%BD%AE%E5%8D%8F%E8%AE%AE
# section DHCP options
import netifaces
from autotk.AutoCoreLite import logger

def inet_ntoaX(data):
    return ['.'.join(map(str, data[i:i + 4])) for i in range(0, len(data), 4)]


def inet_atonX(ips):
    return b''.join(map(inet_aton, ips))


dhcp_message_types = {
    1: 'DHCPDISCOVER',
    2: 'DHCPOFFER',
    3: 'DHCPREQUEST',
    4: 'DHCPDECLINE',
    5: 'DHCPACK',
    6: 'DHCPNAK',
    7: 'DHCPRELEASE',
    8: 'DHCPINFORM',
}
reversed_dhcp_message_types = dict()
for i, v in dhcp_message_types.items():
    reversed_dhcp_message_types[v] = i

shortunpack = lambda data: (data[0] << 8) + data[1]
shortpack = lambda i: bytes([i >> 8, i & 255])


def macunpack(data):
    s = base64.b16encode(data)
    return ':'.join([s[i:i + 2].decode('ascii') for i in range(0, 12, 2)])


def macpack(mac):
    return base64.b16decode(mac.replace(':', '').replace('-', '').encode('ascii'))


def unpackbool(data):
    return data[0]


def packbool(bool):
    return bytes([bool])


options = [
    # RFC1497 vendor extensions
    ('pad', None, None),
    ('subnet_mask', inet_ntoa, inet_aton),
    ('time_offset', None, None),
    ('router', inet_ntoaX, inet_atonX),
    ('time_server', inet_ntoaX, inet_atonX),
    ('name_server', inet_ntoaX, inet_atonX),
    ('domain_name_server', inet_ntoaX, inet_atonX),
    ('log_server', inet_ntoaX, inet_atonX),
    ('cookie_server', inet_ntoaX, inet_atonX),
    ('lpr_server', inet_ntoaX, inet_atonX),
    ('impress_server', inet_ntoaX, inet_atonX),
    ('resource_location_server', inet_ntoaX, inet_atonX),
    ('host_name', lambda d: d.decode('ASCII'), lambda d: d.encode('ASCII')),
    ('boot_file_size', None, None),
    ('merit_dump_file', None, None),
    ('domain_name', None, None),
    ('swap_server', inet_ntoa, inet_aton),
    ('root_path', None, None),
    ('extensions_path', None, None),
    # IP Layer Parameters per Host
    ('ip_forwarding_enabled', unpackbool, packbool),
    ('non_local_source_routing_enabled', unpackbool, packbool),
    ('policy_filer', None, None),
    ('maximum_datagram_reassembly_size', shortunpack, shortpack),
    ('default_ip_time_to_live', lambda data: data[0], lambda i: bytes([i])),
    ('path_mtu_aging_timeout', None, None),
    ('path_mtu_plateau_table', None, None),
    # IP Layer Parameters per Interface
    ('interface_mtu', None, None),
    ('all_subnets_are_local', unpackbool, packbool),
    ('broadcast_address', inet_ntoa, inet_aton),
    ('perform_mask_discovery', unpackbool, packbool),
    ('mask_supplier', None, None),
    ('perform_router_discovery', None, None),
    ('router_solicitation_address', inet_ntoa, inet_aton),
    ('static_route', None, None),
    # Link Layer Parameters per Interface
    ('trailer_encapsulation_option', None, None),
    ('arp_cache_timeout', None, None),
    ('ethernet_encapsulation', None, None),
    # TCP Parameters
    ('tcp_default_ttl', None, None),
    ('tcp_keep_alive_interval', None, None),
    ('tcp_keep_alive_garbage', None, None),
    # Application and Service Parameters Part 1
    ('network_information_service_domain', None, None),
    ('network_informtaion_servers', inet_ntoaX, inet_atonX),
    ('network_time_protocol_servers', inet_ntoaX, inet_atonX),
    ('vendor_specific_information', None, None),
    ('netbios_over_tcp_ip_name_server', inet_ntoaX, inet_atonX),
    ('netbios_over_tcp_ip_datagram_distribution_server', inet_ntoaX, inet_atonX),
    ('netbios_over_tcp_ip_node_type', None, None),
    ('netbios_over_tcp_ip_scope', None, None),
    ('x_window_system_font_server', inet_ntoaX, inet_atonX),
    ('x_window_system_display_manager', inet_ntoaX, inet_atonX),
    # DHCP Extensions
    ('requested_ip_address', inet_ntoa, inet_aton),
    ('ip_address_lease_time', lambda d: struct.unpack('>I', d)[0], lambda i: struct.pack('>I', i)),
    ('option_overload', None, None),
    ('dhcp_message_type', lambda data: dhcp_message_types.get(data[0], data[0]),
     (lambda name: bytes([reversed_dhcp_message_types.get(name, name)]))),
    ('server_identifier', inet_ntoa, inet_aton),
    ('parameter_request_list', list, bytes),
    ('message', None, None),
    ('maximum_dhcp_message_size', shortunpack, shortpack),
    ('renewal_time_value', None, None),
    ('rebinding_time_value', None, None),
    ('vendor_class_identifier', None, None),
    ('client_identifier', macunpack, macpack),
    ('tftp_server_name', None, None),
    ('boot_file_name', None, None),
    # Application and Service Parameters Part 2
    ('network_information_service_domain', None, None),
    ('network_information_servers', inet_ntoaX, inet_atonX),
    ('', None, None),
    ('', None, None),
    ('mobile_ip_home_agent', inet_ntoaX, inet_atonX),
    ('smtp_server', inet_ntoaX, inet_atonX),
    ('pop_servers', inet_ntoaX, inet_atonX),
    ('nntp_server', inet_ntoaX, inet_atonX),
    ('default_www_server', inet_ntoaX, inet_atonX),
    ('default_finger_server', inet_ntoaX, inet_atonX),
    ('default_irc_server', inet_ntoaX, inet_atonX),
    ('streettalk_server', inet_ntoaX, inet_atonX),
    ('stda_server', inet_ntoaX, inet_atonX),
]


class ReadBootProtocolPacket(object):
    for i, o in enumerate(options):
        locals()[o[0]] = None
        locals()['option_{0}'.format(i)] = None

    del i, o

    def __init__(self, data, address=('0.0.0.0', 0)):
        self.data = data
        self.address = address
        self.host = address[0]
        self.port = address[1]

        # wireshark = wikipedia = data[...]

        self.message_type = self.OP = data[0]
        self.hardware_type = self.HTYPE = data[1]
        self.hardware_address_length = self.HLEN = data[2]
        self.hops = self.HOPS = data[3]

        self.XID = self.transaction_id = struct.unpack('>I', data[4:8])[0]

        self.seconds_elapsed = self.SECS = shortunpack(data[8:10])
        self.bootp_flags = self.FLAGS = shortunpack(data[8:10])

        self.client_ip_address = self.CIADDR = inet_ntoa(data[12:16])
        self.your_ip_address = self.YIADDR = inet_ntoa(data[16:20])
        self.next_server_ip_address = self.SIADDR = inet_ntoa(data[20:24])
        self.relay_agent_ip_address = self.GIADDR = inet_ntoa(data[24:28])

        self.client_mac_address = self.CHADDR = macunpack(data[28: 28 + self.hardware_address_length])
        index = 236
        self.magic_cookie = self.magic_cookie = inet_ntoa(data[index:index + 4]);
        index += 4
        self.options = dict()
        self.named_options = dict()
        while index < len(data):
            option = data[index];
            index += 1
            if option == 0:
                # padding
                # Can be used to pad other options so that they are aligned to the word boundary; is not followed by length byte
                continue
            if option == 255:
                # end
                break
            option_length = data[index];
            index += 1
            option_data = data[index: index + option_length];
            index += option_length
            self.options[option] = option_data
            if option < len(options):
                option_name, function, _ = options[option]
                if function:
                    option_data = function(option_data)
                if option_name:
                    setattr(self, option_name, option_data)
                    self.named_options[option_name] = option_data
            setattr(self, 'option_{}'.format(option), option_data)

    def __getitem__(self, key):
        print(key, dir(self))
        return getattr(self, key, None)

    def __contains__(self, key):
        return key in self.__dict__

    @property
    def formatted_named_options(self):
        return "\n".join(
            "{}:\t{}".format(name.replace('_', ' '), value) for name, value in sorted(self.named_options.items()))

    def __str__(self):
        return """
NameOptions:{self.named_options}
Message Type: {self.message_type}
client MAC address: {self.client_mac_address}
client IP address: {self.client_ip_address}
your IP address: {self.your_ip_address}
next server IP address: {self.next_server_ip_address}
{self.formatted_named_options}
""".format(self=self)

    def __gt__(self, other):
        return id(self) < id(other)


class WriteBootProtocolPacket(object):
    message_type = 2  # 1 for client -> server 2 for server -> client
    hardware_type = 1
    hardware_address_length = 6
    hops = 0

    transaction_id = None

    seconds_elapsed = 0
    bootp_flags = 0  # unicast

    client_ip_address = '0.0.0.0'
    your_ip_address = '0.0.0.0'
    next_server_ip_address = '0.0.0.0'
    relay_agent_ip_address = '0.0.0.0'

    client_mac_address = None
    magic_cookie = '99.130.83.99'

    parameter_order = []

    def __init__(self, configuration):
        for i in range(256):
            names = ['option_{}'.format(i)]
            if i < len(options) and hasattr(configuration, options[i][0]):
                names.append(options[i][0])
            for name in names:
                if hasattr(configuration, name):
                    setattr(self, name, getattr(configuration, name))

    def to_bytes(self):
        result = bytearray(236)

        result[0] = self.message_type
        result[1] = self.hardware_type
        result[2] = self.hardware_address_length
        result[3] = self.hops

        result[4:8] = struct.pack('>I', self.transaction_id)

        result[8:10] = shortpack(self.seconds_elapsed)
        result[10:12] = shortpack(self.bootp_flags)

        result[12:16] = inet_aton(self.client_ip_address)
        result[16:20] = inet_aton(self.your_ip_address)
        result[20:24] = inet_aton(self.next_server_ip_address)
        result[24:28] = inet_aton(self.relay_agent_ip_address)

        result[28:28 + self.hardware_address_length] = macpack(self.client_mac_address)

        result += inet_aton(self.magic_cookie)

        for option in self.options:
            value = self.get_option(option)
            # print(option, value)
            if value is None:
                continue
            result += bytes([option, len(value)]) + value
        result += bytes([255])
        return bytes(result)

    def get_option(self, option):
        if option < len(options) and hasattr(self, options[option][0]):
            value = getattr(self, options[option][0])
        elif hasattr(self, 'option_{}'.format(option)):
            value = getattr(self, 'option_{}'.format(option))
        else:
            return None
        function = options[option][2]
        if function and value is not None:
            value = function(value)
        return value

    @property
    def options(self):
        done = list()
        # fulfill wishes
        for option in self.parameter_order:
            if option < len(options) and hasattr(self, options[option][0]) or hasattr(self, 'option_{}'.format(option)):
                # this may break with the specification because we must try to fulfill the wishes
                if option not in done:
                    done.append(option)
        # add my stuff
        for option, o in enumerate(options):
            if o[0] and hasattr(self, o[0]):
                if option not in done:
                    done.append(option)
        for option in range(256):
            if hasattr(self, 'option_{}'.format(option)):
                if option not in done:
                    done.append(option)
        return done

    def __str__(self):
        return str(ReadBootProtocolPacket(self.to_bytes()))


class DelayWorker(object):
    def __init__(self):
        self.closed = False
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self._delay_response_thread)
        self.thread.start()

    def _delay_response_thread(self):
        while not self.closed:
            if self.closed:
                break
            try:
                p = self.queue.get(timeout=1)
                t, func, args, kw = p
                now = time.time()
                if now < t:
                    time.sleep(0.01)
                    self.queue.put(p)
                else:
                    func(*args, **kw)
            except queue.Empty:
                continue

    def do_after(self, seconds, func, args=(), kw={}):
        self.queue.put((time.time() + seconds, func, args, kw))

    def close(self):
        self.closed = True


class Transaction(object):
    def __init__(self, server, timeout=10):
        self.offer_delay_time = 0.3
        self.acknowledge_delay_time = 0.2
        self.server = server
        self.configuration = server.configuration
        self.packets = []
        self.done_time = time.time() + timeout
        self.done = False
        self.do_after = self.server.delay_worker.do_after

    def is_done(self):
        return self.done or self.done_time < time.time()

    def close(self):
        self.done = True

    def receive(self, packet):
        # packet from client <-> packet.message_type == 1
        print(f"[{packet.dhcp_message_type}]")
        if packet.message_type == 1 and packet.dhcp_message_type == 'DHCPDISCOVER':
            self.do_after(self.offer_delay_time, self.received_dhcp_discover, (packet,), )
        elif packet.message_type == 1 and packet.dhcp_message_type == 'DHCPREQUEST':
            self.do_after(self.acknowledge_delay_time, self.received_dhcp_request, (packet,), )
        elif packet.message_type == 1 and packet.dhcp_message_type == 'DHCPINFORM':
            self.received_dhcp_inform(packet)
        else:
            return False
        return True

    def received_dhcp_discover(self, discovery):
        if self.is_done(): return
        # print(discovery)  # 接收广播,不具备任何网关信息
        self.send_offer(discovery)

    def send_offer(self, discovery):
        # https://tools.ietf.org/html/rfc2131
        offer = WriteBootProtocolPacket(self.configuration)
        offer.parameter_order = discovery.parameter_request_list
        mac = discovery.client_mac_address

        # offer.client_ip_address =
        offer.transaction_id = discovery.transaction_id
        # offer.next_server_ip_address =
        offer.relay_agent_ip_address = discovery.relay_agent_ip_address
        offer.client_mac_address = mac
        offer.client_ip_address = discovery.client_ip_address or '0.0.0.0'
        offer.bootp_flags = discovery.bootp_flags
        offer.dhcp_message_type = 'DHCPOFFER'
        offer.client_identifier = mac
        try:
            self.server.broadcast_offer(offer)
        except Exception as e:
            print(f"[send_offer]Error:{e}")

    def received_dhcp_request(self, request):
        if self.is_done(): return
        self.server.client_has_chosen(request)
        self.acknowledge(request)
        self.close()

    def acknowledge(self, request):
        requested_ip_address = request.requested_ip_address
        _tmp_gate = request.server_identifier
        if _tmp_gate and self.ip_gate_pass(requested_ip_address, _tmp_gate):
            ack = WriteBootProtocolPacket(self.configuration)
            ack.parameter_order = request.parameter_request_list
            ack.transaction_id = request.transaction_id
            # ack.next_server_ip_address =
            ack.bootp_flags = request.bootp_flags
            ack.relay_agent_ip_address = request.relay_agent_ip_address
            mac = request.client_mac_address
            ack.client_mac_address = mac
            ack.client_ip_address = request.client_ip_address or '0.0.0.0'
            ack.your_ip_address = requested_ip_address
            ack.router = [_tmp_gate]
            ack.domain_name_server = [_tmp_gate]
            ack.broadcast_address = ".".join(ack.your_ip_address.split(".")[:-1] + ["255"])
            ack.dhcp_message_type = 'DHCPACK'
            self.server.broadcast_ack(ack, _tmp_gate)

    def received_dhcp_inform(self, inform):
        self.close()
        self.server.client_has_chosen(inform)

    def ip_gate_pass(self, address, network, subnet_mask="255.255.255.0"):
        a = address.split('.')
        s = subnet_mask.split('.')
        n = network.split('.')
        return all(s[i] == '0' or a[i] == n[i] for i in range(4))


class DHCPServerConfiguration(object):
    # 统一的初始option配置
    bind_address = ''
    network = '192.168.33.0'
    broadcast_address = '255.255.255.255'
    subnet_mask = '255.255.255.0'
    router = None  # list of ips
    # 1 day is 86400
    ip_address_lease_time = 86400  # seconds
    domain_name_server = None  # list of ips

    def __init__(self) -> None:
        super().__init__()


class DHCPServer(object):
    def __init__(self, gate_dict,info_dict):
        self.gate_info = info_dict
        self.gate_dict = gate_dict
        self.gatelist =list(gate_dict.keys())
        self.configuration = DHCPServerConfiguration()
        self.init_data()
        self.socket = socket(type=SOCK_DGRAM)
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket.bind(("0.0.0.0", 67))
        self.delay_worker = DelayWorker()
        self.closed = False
        self.transactions = collections.defaultdict(lambda: Transaction(self))  # id: transaction
        self.time_started = time.time()

    def init_data(self):
        self.ippool_idx = {}  # 寄存分配的ip序号 用于get_ip_next
        for g in self.gatelist:
            self.ippool_idx[g] = 2
        self.bindclient = {}  # 寄存成功ack的client
        self.check_gate_ready=False
        self.auto_disable_count= {}  # 看门狗,异常网关重启下

    def close(self):
        self.socket.close()
        self.closed = True
        self.delay_worker.close()
        for transaction in list(self.transactions.values()):
            transaction.close()

    def update(self, timeout=0):
        try:
            reads = select.select([self.socket], [], [], timeout)[0]
        except ValueError:
            # ValueError: file descriptor cannot be a negative integer (-1)
            return
        for socket in reads:
            try:
                packet = ReadBootProtocolPacket(*socket.recvfrom(4096))
            except OSError:
                # OSError: [WinError 10038] An operation was attempted on something that is not a socket
                pass
            else:
                self.received(packet)
        for transaction_id, transaction in list(self.transactions.items()):
            if transaction.is_done():
                transaction.close()
                self.transactions.pop(transaction_id)

    def received(self, packet):
        if not self.transactions[packet.transaction_id].receive(packet):
            print('received:\n {}'.format(str(packet).replace('\n', '\n\t')))

    def client_has_chosen(self, packet):
        _ip = packet.requested_ip_address or packet.client_ip_address
        if not _ip and _ip != '0.0.0.0':
            return
        print(f"[client_has_chosen] {packet.client_mac_address} {_ip}")

    @property
    def server_identifiers(self):
        return self.gatelist
        # return router

    def ip_gate_pass(self, address, network, subnet_mask="255.255.255.0"):
        a = address.split('.')
        s = subnet_mask.split('.')
        n = network.split('.')
        return all(s[i] == '0' or a[i] == n[i] for i in range(4))

    def get_ip_next(self, gate):
        import socket
        gate_value = struct.unpack('>I', socket.inet_aton(gate))[0]
        ipvalue = gate_value + self.ippool_idx[gate]
        end = (gate_value | (~4294967040 & 0xffffffff))  # subnet_mask="255.255.255.0"
        if ipvalue + 5 >= end:
            self.ippool_idx[gate] = 2
        else:
            self.ippool_idx[gate] += 1
        ip = str(socket.inet_ntoa(struct.pack('>I', ipvalue)))
        return ip

    def broadcast_offer(self, packet):
        for addr in self.server_identifiers:
            broadcast_socket = socket(type=SOCK_DGRAM)
            broadcast_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            broadcast_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
            packet.server_identifier = addr
            packet.router = [addr]
            packet.domain_name_server = [addr]
            packet.broadcast_address = ".".join(addr.split(".")[:-1] + ["255"])
            # print(f'{"-轮询网关-"}{}')
            try:
                if self.check_gate_online(addr):
                    broadcast_socket.bind((addr, 68))
                    packet.your_ip_address = self.get_ip_next(addr)
                    data = packet.to_bytes()
                    broadcast_socket.sendto(data, ('255.255.255.255', 68))
                    broadcast_socket.sendto(data, (addr, 68))
                    print(f"[broadcast_offer] Gate:{addr} {packet.your_ip_address}")
            except Exception as e:
                print(f'[broadcast_offer]Error:{e}')
                time.sleep(1)
            finally:
                broadcast_socket.close()
    def check_gate_online(self,addr):
        for e in netifaces.interfaces():
            _addr = netifaces.ifaddresses(e)
            if _addr.get(2, []):
                _ip = _addr[2][0].get("addr", "")
                if _ip==addr:
                    return True
        return False
    def broadcast_ack(self, packet, addr):
        broadcast_socket = socket(type=SOCK_DGRAM)
        broadcast_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        broadcast_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        packet.server_identifier = addr
        packet.router = [addr]
        packet.domain_name_server = [addr]
        packet.broadcast_address = ".".join(addr.split(".")[:-1] + ["255"])
        try:
            broadcast_socket.bind((addr, 68))
            if not self.ip_gate_pass(packet.your_ip_address, addr):
                packet.your_ip_address = self.get_ip_next(addr)
            data = packet.to_bytes()
            broadcast_socket.sendto(data, ('255.255.255.255', 68))
            broadcast_socket.sendto(data, (addr, 68))
            if not packet.your_ip_address in self.bindclient.values():
                logger.debug(f'DHCP[{addr}] Set {packet.client_mac_address} {packet.your_ip_address}')
            self.bindclient[packet.client_mac_address] = packet.your_ip_address
            print(f"[broadcast_ack] {addr} Done.", self.bindclient)
            self.auto_disable(addr,packet.client_mac_address)
        except Exception as e:
            print(f'[broadcast_ack]Error:{e}')
        finally:
            broadcast_socket.close()

    def run(self):
        while not self.closed:
            try:
                if self.check_gate_ready:
                    self.update(1)
                else:
                    time.sleep(1)
                    self.check_gate_ready = self.check_gateway()
            except KeyboardInterrupt:
                break
            except:
                traceback.print_exc()

    def auto_disable(self,addr,client):
        if not client in self.auto_disable_count:
            self.auto_disable_count[client] = time.time()
        elptime=time.time()-self.auto_disable_count[client]
        if elptime>=3:
            self.auto_disable_count.pop(client)
            _info=self.gate_info.get(addr,{})
            n = _info.get("Name", "")
            print(_info)
            print(f"[auto_disable] {addr} {n}")
            if n:
                os.popen(f'netsh int set int name="{n}" admin=disable && netsh int set int name="{n}" admin=enable')
    def check_gateway(self):
        check_num=0
        for e in netifaces.interfaces():
            _addr = netifaces.ifaddresses(e)
            if _addr.get(2, []):
                _ip = _addr[2][0].get("addr", "")
                if _ip in self.gatelist:
                    check_num+=1
            else:
                _mac=_addr.get(-1000, [])
                if _mac:
                    _mac=_mac[0].get("addr", "")
                    if _mac and ":" in _mac:
                        _mac = _mac.replace(":", "-").upper()
                        if _mac in self.gate_dict.values():
                            check_num += 1
        result= check_num==len(self.gatelist)
        if result:
            if not self.check_gate_ready:
                print(f'Start DHCP Server {self.gatelist}')
                logger.debug(f'Start DHCP Server {self.gatelist}')
            time.sleep(1)
        return result

    def run_in_thread(self):
        thread = threading.Thread(target=self.run, daemon=True)
        thread.start()
        return thread


if __name__ == '__main__':

    from Auto_Deploy import scan_net_deploy,_wmic
    gate_dict,net_now = scan_net_deploy()
    if gate_dict:
        print(net_now)
        print(gate_dict)
        DHCPServer(gate_dict,net_now).run_in_thread()
