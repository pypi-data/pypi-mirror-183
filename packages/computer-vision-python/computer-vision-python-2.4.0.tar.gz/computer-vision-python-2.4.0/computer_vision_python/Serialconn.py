import serial
import time
import logging
import serial.tools.list_ports


class Serial_object:
    def __init__(self, port=None, baud=9600):
        self.port = port
        self.baud = baud
        connected = False
        if self.port is None:
            ports = list(serial.tools.list_ports.comports())
            for p in ports:
                print(f'{p.description} Connected')
                self.ser = serial.Serial(p.device)
                self.ser.baudrate = baud
                connected = True
            if not connected:
                logging.warning("Please enter COM Port Number.")

        else:
            try:
                self.ser = serial.Serial(self.port, self.baud)
                print("Serial Device Connected")
            except:
                logging.warning("Serial Device Not Connected")

    def send(self, data):
        msg = data + '\r'
        self.ser.write(msg.encode())

    def get(self, splitchar):

        data = self.ser.readline()
        data = data.decode("utf-8")
        data = data.split(splitchar)
        dataList = []
        [dataList.append(d) for d in data]
        return dataList[:-1]


def main():
    arduino = Serial_object()
    while True:
        arduino.sendData([1, 1, 1, 1, 1])
        time.sleep(2)
        arduino.sendData([0, 0, 0, 0, 0])
        time.sleep(2)


if __name__ == "__main__":
    main()
