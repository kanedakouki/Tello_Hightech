import threading 
import socket


# Tello����̃��X�|���X��M
def udp_receiver():
    count = 0
    while True: 
        try:
            # �N���C�A���g����̃��b�Z�[�W�̎�M����t�J�n(�R�l�N�V�������X�^)
            data, server = sock.recvfrom(1518)
        except Exception:
            print ('\nExit . . .\n')
            break

# Tello���̃��[�J��IP�A�h���X(�f�t�H���g)�A����|�[�g�ԍ�(�R�}���h���[�h�p)
TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889
TELLO_ADDRESS = (TELLO_IP, TELLO_PORT)

# UDP�ʐM�\�P�b�g�̍쐬
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ���z�X�g�Ŏg�p����IP�A�h���X�ƃ|�[�g�ԍ���ݒ�
sock.bind(('', TELLO_PORT))

# ��M�p�X���b�h�̍쐬
thread  = threading.Thread(target=udp_receiver)
thread.daemon = True
thread .start()

while True: 

    try:
        msg = input("")

        # ���b�Z�[�W���Ȃ���Ή������Ȃ�
        if not msg:
            break  

        # �uq�v�Ń\�P�b�g�ʐM�I��
        if 'q' in msg:
            print ('QUIT...')
            sock.close()  
            break

        # �f�[�^�𑗐M
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, TELLO_ADDRESS)

    except KeyboardInterrupt:
        sock.close()  
        break
