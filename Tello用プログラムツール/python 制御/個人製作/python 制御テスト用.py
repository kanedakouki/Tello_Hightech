# -*- coding:utf-8 -*-
# 参考先Web: https://algorithm.joho.info/programming/python/tello-python-command/
# コマンドの一覧はこの参照先をご覧ください

import threading 
import socket
import cv2
import time
import numpy as np

# Telloからのレスポンス受信
def udp_receiver():
    count = 0
    while True: 
        try:
            # クライアントからのメッセージの受信を受付開始(コネクションレス型)
            data, server = sock.recvfrom(1518)
        except Exception:
            print ('\nExit . . .\n')
            break

My_ip = socket.gethostbyname(socket.gethostname())
# Tello側のローカルIPアドレス(デフォルト)、宛先ポート番号(コマンドモード用)
TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889
TELLO_ADDRESS = (TELLO_IP, TELLO_PORT)

# Telloからの映像受信用のローカルIPアドレス、宛先ポート番号
TELLO_CAMERA_ADDRESS = 'udp://@0.0.0.0:11111'

# キャプチャ用のオブジェクト
cap = None

# データ受信用のオブジェクト備
response = None

# UDP通信ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 自ホストで使用するIPアドレスとポート番号を設定
sock.bind((My_ip, 8888))
#192.168.10.2 TELLO_PORT

# 受信用スレッドの作成
thread  = threading.Thread(target=udp_receiver)
thread.daemon = True
thread .start()

while True: 

    try:
        msg = input("")

        # メッセージがなければ何もしない
        if not msg:
            break  

        # 「q」でソケット通信終了
        if 'q' in msg:
            print ('QUIT...')
            sock.close()  
            break

        # データを送信
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, TELLO_ADDRESS)

    except KeyboardInterrupt:
        sock.close()  
        break