# coding=utf-8
import os
import dpkt
import socket
import datetime
import uuid
import json
import sys

sys.path.append("E:\AutomationApiTest_01")
from scapy.sendrecv import sniff
from scapy.utils import wrpcap
from Driver.base_request import request as Response


class Captures(object):
    def get_local_ip(self):
        hostname = socket.gethostname()

        # 获取本机内网ip
        local_ips = socket.gethostbyname_ex(hostname)[-1]
        return local_ips

    def body_transfer(self, body):
        try:
            json_str = json.loads(body)
            # student=json.dumps(json_str)
            print("json=: %s" % json.dumps(json_str, indent=2, ensure_ascii=False))
            for key, value in json_str.items():
                print("   {0}: {1}".format(key, value))
        except Exception:
            str_body = body.decode()
            body_ls = str_body.split("&")
            for item in body_ls:
                key_, value_ = item.split("=")
                print("   {0}: {1}".format(key_, value_))

    def get_dpkt(self):
        dpkt_ = sniff(
            count=100
        )  # 这里是针对单网卡的机子，多网卡的可以在参数中指定网卡,例：iface=Qualcomm QCA9377 802.11ac Wireless Adapter
        _uuid = uuid.uuid1()
        filename = f"{_uuid}.pcap"
        wrpcap(filename, dpkt_)
        return filename

    def print_pcap(self, pcap):
        try:
            local_ips = self.get_local_ip()

            for timestamp, buf in pcap:
                eth = dpkt.ethernet.Ethernet(buf)  # 获得以太包，即数据链路层包
                # print("ip layer:"+eth.data.__class__.__name__) #以太包的数据既是网络层包
                # print("tcp layer:"+eth.data.data.__class__.__name__) #网络层包的数据既是传输层包
                # print("http layer:" + eth.data.data.data.__class__.__name__) #传输层包的数据既是应用层包
                #
                # print('Timestamp: ',str(datetime.datetime.utcfromtimestamp(timestamp))) #打印出包的抓取时间

                if not isinstance(eth.data, dpkt.ip.IP):
                    # print('Non IP Packet type not supported %s' % eth.data.__class__.__name__)
                    continue
                ip = eth.data
                src_ip = socket.inet_ntoa(ip.src)
                dst_ip = socket.inet_ntoa(ip.dst)
                do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
                more_fragments = bool(ip.off & dpkt.ip.IP_MF)
                fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

                if isinstance(ip.data, dpkt.tcp.TCP):
                    # Set the TCP data
                    tcp = ip.data
                    # Now see if we can parse the contents as a HTTP request
                    # 看看是否可以将内容解析为HTTP请求
                    try:
                        request = dpkt.http.Request(tcp.data)
                        print(
                            "IP: %s -> %s (len=%d ttl=%d DF=%d MF=%d offset=%d)"
                            % (
                                src_ip + "(本机)" if src_ip in local_ips else src_ip,
                                dst_ip,
                                ip.len,
                                ip.ttl,
                                do_not_fragment,
                                more_fragments,
                                fragment_offset,
                            )
                        )
                        print("URL: %s" % request.headers.get("host") + request.uri)
                        print("METHOD: %s" % request.method.upper())

                        print("Headers: ")

                        for key, value in request.headers.items():
                            print("   %s: %s" % (key, value))

                        print("Body:")
                        print(request.body)
                        self.body_transfer(request.body)

                        print("Response: ")
                        url = "http://{}".format(
                            request.headers.get("host") + request.uri
                        )
                        METHOD = request.method.upper()
                        print("api_url:{}".format(url))
                        print(METHOD)

                        metadata = json.loads(json.dumps(request.headers))
                        del metadata["host"]
                        del metadata["connection"]
                        del metadata["content-length"]
                        del metadata["accept"]
                        del metadata["user-agent"]
                        del metadata["origin"]
                        del metadata["referer"]
                        del metadata["accept-encoding"]
                        del metadata["accept-language"]

                        json_str = json.loads(request.body)

                        if METHOD == "OPTIONS" or "POST":
                            res = Response.run_main(
                                "POST", url=url, headers=metadata, json=json_str
                            )
                            print(
                                "Response%s"
                                % json.dumps(res, indent=2, ensure_ascii=False)
                            )
                        else:
                            res = Response.run_main("GET", url=url, headers=metadata)
                            print(
                                "Response%s"
                                % json.dumps(res, indent=2, ensure_ascii=False)
                            )
                        print("Data:")
                        self.body_transfer_data(request.data)
                        print("HTTP request: %s\n" % repr(request))
                    except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                        continue

                    # Pull out fragment information (flags and offset all packed into off field, so use bitmasks)

        except Exception as error:
            pass

    def run(self):
        while True:
            filename = self.get_dpkt()
            with open(filename, "rb") as f:
                pcap = dpkt.pcap.Reader(f)
                self.print_pcap(pcap)

            os.remove(filename)


if __name__ == "__main__":
    Cap = Captures()
    Cap.run()
