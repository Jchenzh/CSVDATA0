# -*- coding:utf-8 -*-
# Author: WUJiang
# 运行环境为Windows7&Python3.7

import serial
import time


ser = serial.Serial("com3", 9600)   # 选择串口，并设置波特率
if ser.is_open:
    print("port open success")
    # hex(16进制)转换为bytes(2进制)，应注意Python3.7与Python2.7此处转换的不同
    send_data = bytes.fromhex('ff 01 00 55 00 00 56')    # 发送数据转换为b'\xff\x01\x00U\x00\x00V'
    ser.write(send_data)   # 发送命令
    time.sleep(0.1)        # 延时，否则len_return_data将返回0，此处易忽视！！！
    len_return_data = ser.inWaiting()  # 获取缓冲数据（接收数据）长度
    if len_return_data:
        return_data = ser.read(len_return_data)  # 读取缓冲数据
        # bytes(2进制)转换为hex(16进制)，应注意Python3.7与Python2.7此处转换的不同，并转为字符串后截取所需数据字段，再转为10进制
        str_return_data = str(return_data.hex())
        feedback_data = int(str_return_data[-6:-2], 16)
        print(feedback_data)
else:
    print("port open failed")

