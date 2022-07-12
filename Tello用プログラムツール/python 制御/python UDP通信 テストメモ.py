# -*- coding:utf-8 -*-
# 参考サイト: https://techacademy.jp/magazine/41018

import socket as sk

# gethostname で自身の「デバイス名」を取得し、
# gethostbyname で入力された「デバイス名」の「IPアドレス」を取得する。
My_IP = sk.gethostbyname(sk.gethostname())

# 送信側アドレス設定（ユーザー側）
#           　   (IP,ポート番号)
UserAddr = (My_IP,11111)

# 受信側アドレス設定（Tello側）
#              　 (IP,ポート番号)
TelloAddr = ('192.168.10.1',8889)

# ソケット作成
udpSock = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
# 送信側アドレスにソケットを設定
udpSock.bind(UserAddr)

# 送信データ作成
data = ''
# エンコード変換
data = data.encode('utf-8')

# 受信側へのUDP通信を開始
udpSock.sk.sendto(data,TelloAddr)