# -*- coding: utf-8 -*-
import socket as sk

# Tello���ւ̑��M�A�h���X�ݒ�
T_IP = '192.168.10.1'
T_PORT = 8889
T_ADD = (T_IP,T_PORT)

# ���z�X�g�̎�M�A�h���X�ݒ�
My_IP = sk.gethostbyname(sk.gethostname())
My_PORT = 8889
My_ADD = (My_IP,My_PORT)

# UDP�ʐM�\�P�b�g���쐬����
# ���A�h���X�t�@�~���FAF_INET�iIPv4�j�A�\�P�b�g�^�C�v�FSOCK_DGRAM�iUDP�ʐM�j
sock=sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

# �\�P�b�g�Ɏ��z�X�g��IP�A�h���X�ƃ|�[�g�ԍ���ݒ肷��
sock.bind(My_ADD)