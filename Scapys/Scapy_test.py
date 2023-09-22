from scapy.all import *
from scapy.layers.inet import IP

a=IP(dst='192.168.2.11')
a.dst
ls()