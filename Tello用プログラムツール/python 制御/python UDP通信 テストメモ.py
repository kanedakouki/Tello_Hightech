# -*- coding:utf-8 -*-
# �Q�l�T�C�g: https://techacademy.jp/magazine/41018

import socket as sk

# gethostname �Ŏ��g�́u�f�o�C�X���v���擾���A
# gethostbyname �œ��͂��ꂽ�u�f�o�C�X���v�́uIP�A�h���X�v���擾����B
My_IP = sk.gethostbyname(sk.gethostname())

# ���M���A�h���X�ݒ�i���[�U�[���j
#           �@   (IP,�|�[�g�ԍ�)
UserAddr = (My_IP,11111)

# ��M���A�h���X�ݒ�iTello���j
#              �@ (IP,�|�[�g�ԍ�)
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