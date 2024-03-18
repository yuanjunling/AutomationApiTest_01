from pysnmp.hlapi import *

# SNMP目标设备的IP地址和端口
target_ip = '192.168.222.1'
target_port = 161

# SNMP社区字符串
community_string = 'public'

# 要查询的OID（对象标识符）
oid = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)

# 创建SNMP引擎实例
snmp_engine = SnmpEngine()

# 执行SNMP GET请求
errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(snmp_engine,
           CommunityData(community_string),
           UdpTransportTarget((target_ip, target_port)),
           ContextData(),
           [oid])
)

# 检查并处理响应
if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))