from PyQt6.QtCore import QThread, pyqtSignal
from datetime import datetime
from logger import log
import socket
import threading

class MessageReceiver(QThread):
    message = pyqtSignal(str,str)


    def __init__(self, port):
        super().__init__()
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.running = False
        


    def run(self):
        print("Приемник сообщений запущен")
        self.socket.bind(('localhost', self.port))
        current_time = datetime.now()
        self.running = True
        while self.running:
            data, addr = self.socket.recvfrom(1024)
            message = data.decode(encoding="UTF-8")
            log.d(f'Получено сообщение от {addr}{current_time}: {message} ')
            self.message.emit(message, "public")
            # self.socket.sendto("ОК".encode(), addr)

    def stop(self):
        self.running = False
        
