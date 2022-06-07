# ↓文字コード指定で読み込み
# （UTF-8でファイルを保存する必要性が無い）
# -*- coding:utf-8 -*-

import socket
# ホスト名を取得、表示
host = socket.gethostname()
print(host)

# ipアドレスを取得、表示
ip = socket.gethostbyname(host)
print(ip)