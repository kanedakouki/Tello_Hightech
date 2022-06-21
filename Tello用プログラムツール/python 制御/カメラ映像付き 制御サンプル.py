# -*- coding:utf-8 -*-

import socket
import threading
import cv2
import time
import numpy as np

# �f�[�^�󂯎��p�̊֐�
def udp_receiver():
    while True:
        try:
            response, _ = sock.recvfrom(1024)
        except Exception as e:
            print(e)
            break

# Tello���̃��[�J��IP�A�h���X(�f�t�H���g)�A����|�[�g�ԍ�(�R�}���h���[�h�p)
TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889
TELLO_ADDRESS = (TELLO_IP, TELLO_PORT)

# Tello����̉f����M�p�̃��[�J��IP�A�h���X�A����|�[�g�ԍ�
TELLO_CAMERA_ADDRESS = 'udp://@0.0.0.0:11111'

# �L���v�`���p�̃I�u�W�F�N�g
cap = None

# �f�[�^��M�p�̃I�u�W�F�N�g��
response = None

# �ʐM�p�̃\�P�b�g���쐬
# ���A�h���X�t�@�~���FAF_INET�iIPv4�j�A�\�P�b�g�^�C�v�FSOCK_DGRAM�iUDP�j
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ���z�X�g�Ŏg�p����IP�A�h���X�ƃ|�[�g�ԍ���ݒ�
sock.bind(('', TELLO_PORT))

# ��M�p�X���b�h�̍쐬
thread = threading.Thread(target=udp_receiver, args=())
thread.daemon = True
thread.start()

# �R�}���h���[�h
sock.sendto('command'.encode('utf-8'), TELLO_ADDRESS)

time.sleep(1)

# �J�����f���̃X�g���[�~���O�J�n
sock.sendto('streamon'.encode('utf-8'), TELLO_ADDRESS)

time.sleep(5)

if cap is None:
    cap = cv2.VideoCapture(TELLO_CAMERA_ADDRESS)

if not cap.isOpened():
    cap.open(TELLO_CAMERA_ADDRESS)

time.sleep(1)

while True:
    ret, frame = cap.read()

    # ����t���[������Ȃ�X�L�b�v
    if frame is None or frame.size == 0:
        continue

    # �J�����f���̃T�C�Y�𔼕��ɂ��ăE�B���h�E�ɕ\��
    frame_height, frame_width = frame.shape[:2]
    frame = cv2.resize(frame, (int(frame_width/2), int(frame_height/2)))
    
    cv2.imshow('Tello Camera View', frame)

    # q�L�[�ŏI��
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        break
cap.release()
cv2.destroyAllWindows()

# �r�f�I�X�g���[�~���O��~
sock.sendto('streamoff'.encode('utf-8'), TELLO_ADDRESS)