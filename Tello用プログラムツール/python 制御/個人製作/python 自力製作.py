# -*- coding: utf-8 -*-
import socket as sk

# Tello側への送信アドレス設定
T_IP = '192.168.10.1'
T_PORT = 8889
T_ADD = (T_IP,T_PORT)

# 自ホストの受信アドレス設定
My_IP = sk.gethostbyname(sk.gethostname())
My_PORT = 8889
My_ADD = (My_IP,My_PORT)

# UDP通信ソケットを作成する
# ※アドレスファミリ：AF_INET（IPv4）、ソケットタイプ：SOCK_DGRAM（UDP通信）
sock=sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

# ソケットに自ホストのIPアドレスとポート番号を設定する
sock.bind(My_ADD)