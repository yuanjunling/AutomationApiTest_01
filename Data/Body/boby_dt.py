setSatelliteList_payload = "para1=1&str=%7B1%2C1%2Csat1%2C76.5%2C1878.5%2C18500%2C20000%2C15000%2C10600%2C0%2C0%2C0%2C1%2C0%2C2%7D"
switchSatellite_payload = "para1=1&para2=1&para3=sat1&para4=76.5&para5=1878.5&para6=18500&para7=20000&para8=15000&para9=10600&para10=0&para11=0&para12=0&para13=1&para14=0&para15=2"
sasySatellite_payload = "para=download"
login_payload = "luci_username=admin&luci_password=admin&luci_lang=zh_cn"
sasySatellite_payload2 = "para=upload"
getIns_payload = "step=1"
setSub_payload = "para1=0&para2=0&para3=0&para4=0"
setAdjustSet_payload = "para1=15&para2=90&para3=12&para4=120&para5=2&para6=1"
manualItems_payload = "para1=-1&para2=2&para3=2"
getLog_payload = "pgn=0&pgs=30"


# 1代表1号天线，2代表2号天线
# ----------------------------------
get_ant_state_info_json = {"ant_type": 1}
get_ins_info_json = {"ant_type": 1}
get_modem_info_json = {"ant_type": 1}
get_aim_sat_info_json = {"ant_type": 1}
get_ant_device_info_json = {"ant_type": 1}
get_sub_info_json = {"ant_type": 1}
get_warn_info_json = {"ant_type": 1}
get_test_info_json = {"ant_type": 1}
set_aim_sat_json = {
    "ant_type": 1,
    "longitude": 1901.500000,
    "trackfreq": 1982,
    "po_mode": 1,
    "symbol_rate": 51000,
    "bandwidth": 20000,
    "_22k": 0,
    "disq": 0,
    "lnb_voltage": 1,
    "track_mode": 0,
    "losttime": 15000,
    "multiaxis": 2,
    "relo": 10600,
    "agc_threshold": 125821,
}

get_test_step_json = {"ant_type": 1}
set_power_save_json = {"ant_type": 1, "function": 1}
set_ant_reset_json = {"ant_type": 1, "function": 1}
set_ant_manual_mode_json = {"ant_type": 1, "function": 0}
set_ant_test_mode_json = {"ant_type": 1, "function": 1}
set_ant_test_cmd_json = {"ant_type": 1, "function": 1}
set_sub_json = {
    "ant_type": 1,
    "sub_state": 1,
    "agc_gain": 1,
    "phase_offset": 2,
    "phase_num": 1,
}

set_manual_cmd_json = {"ant_type": 1, "spiale": 0, "ang_rate": 1, "move_ang": 2}
set_ant_cal_json = {
    "ant_type": 1,
    "pol_zero_cal": 1,
    "pit_up_lim_ang_cal": 2,
    "rol_zero_cal": 2.22,
    "azim_cal": 2.01,
    "cal_type": 1,
}
get_all_info_json = {"ant_type": 1}
set_acu_upload_json = {"file_name": "/root/mac_upload.tar"}
set_mcu_upload_json = {"upload_type": 1, "step": 0, "file_name": "/root/233.bin"}
get_file_to_ant_step_json = {"upload_type": 1}
get_modem_upload_step_json = {"upload_type": 3}
setgisconfig_json = {
    "en": 0,
    "data_ip": "192.168.151.95",
    "data_port": 19001,
    "rule_ip": "192.168.151.95",
    "rule_port": 19002,
    "intervals": 30,
    "start": 1,
}

setacuconfig_json = {
    "chang_type": 63,
    "ant1_ip": "192.168.111.211",
    "ant1_port": 15101,
    "ant2_ip": "192.168.111.211",
    "ant2_port": 15102,
    "verbose_en": 1,
    "log_dir1": "/mnt/sda1/log/ditel_ant_info/retransfer1.log",
    "log_dir2": "/mnt/sda1/log/ditel_ant_info/retransfer2.log",
    "log_fold": "/mnt/sda1/log/ditel_ant_info",
    "adapter": "/dev/ttyS4",
    "outins": "/dev/ttyS9",
    "trans_ip": "0.0.0.0",
    "trans_port": 4001,
}

set_modem_upload_json = {"upload_type": 3, "step": 1, "file_name": "/etc/Eug/111.bin"}
