
from ast import While
from encodings import utf_8
import threading
import serial

from serial.tools import list_ports
import time
import signal
import sys


PORT = 'COM3'
BAUD = 115200


def selection_serial_port():

	port_list = list(list_ports.grep(""))
	if len(port_list) == 0:
		raise LookupError("시리얼통신 장비를 찾을 수 없습니다.")

	index_port_list_str = [f"[{index}] Port: {port.device}, Description: {port.description}"
						   for index, port in enumerate(port_list)]
	print(index_port_list_str)
    
	while True:
		ind = input("시리얼통신 포트의 인덱스를 선택: ")
		if not str.isdigit(ind):
			print(f"숫자만 입력 가능.")
		elif not (0 <= int(ind) < len(port_list)):
			print("선택가능한 범위가 아님.")
		else:
			return port_list[int(ind)].device

def readed_serial_string(read_str):

    if len(read_str) > 0:
        # print(f'readedSerialString: {read_str}')
        print(read_str, end='')


def read_serial(ser:serial.Serial):

    read_list = []

    while True:

        # 시리얼통신에서 읽어올수 있는 데이터가 존재할때
        # 1byte씩 읽어와 char형으로 변환해 리스트에 추가
        for c in ser.read():
            read_list.append(chr(c))

        read_str = ''.join(read_list)
        readed_serial_string(read_str)
        # callback(read_str)
        read_list.clear()

        # if ser.readable():
        #     # byte 으로 읽어와 문자로 형변환
        #     for c in ser.read():
        #         read_list.append(chr(c))
        # else:
        #     # 리스트를 문자열로
        #     read_str = ''.join(read_list)
        #     #print(read_str)
        #     # 문자열 반환
        #     callback(read_str)
        #     read_list.clear()
        #     #del read_list[:]


def signalHandler():
    sys.exit(0)


if __name__ == "__main__":

    # 시그널 사용 (특정 시그널이 입력되면 해당 핸들러를 호출, SIGINT == KeyboardInterrupt)
    # import signal
    # import sys
    signal.signal(signal.SIGINT, signalHandler)

    ser = serial.Serial(PORT, BAUD)
    time.sleep(1) # 포트를 연결해 통신이 가능한 상태가 되는데 시간이 필요
    # ser = serial.Serial(selection_serial_port(), BAUD)
    # print(ser)
    print('시리얼통신 준비완료')

    # 쓰레드 준비 및 시작
    thread = threading.Thread(target=read_serial, args=(ser,))
    thread.start()

    # print('테스트 문구 전송')
    # ser.write("hello".encode())
    # time.sleep(10)

    while True:
        inputText = input('문구입력: \n')
        ser.write(inputText.encode())

        
    
    # ser.writelines()
    # time.sleep(5)