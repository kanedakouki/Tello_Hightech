# �Q�l�T�C�g: https://techacademy.jp/magazine/41018

import socket as sk

# ���M���A�h���X�ݒ�
#              (IP,�|�[�g�ԍ�)
UserAddr = ('127.0.0.1',11111)

# ��M���A�h���X�ݒ�
#                 (IP,�|�[�g�ԍ�)
TelloAddr = ('192.168.10.1',8889)

# �\�P�b�g�쐬
udpSock = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
# ���M���A�h���X�Ƀ\�P�b�g��ݒ�
udpSock.bind(UserAddr)

# ���M�f�[�^�쐬
data = ''
# �G���R�[�h�ϊ�
data = data.encode('utf-8')

# ��M���ւ�UDP�ʐM���J�n
udpSock.sk.sendto(data,TelloAddr)