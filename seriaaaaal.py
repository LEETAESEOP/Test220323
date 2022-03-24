import serial


if __name__ == '__main__':
    ser = serial.Serial(port='COM3', baudrate=115200)

    while True:
      if ser.readable():
      ##  line = ser.readline()
      ##  print(f'line: {line}')
        read555 = ser.readline()
        print(f'readvalue: {read555}')
      ser.write(read555)
