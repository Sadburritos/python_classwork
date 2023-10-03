from logger import log
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal


class MainWindow(QMainWindow):
    sendMessage = pyqtSignal(str,str)


    def __init__(self, username):
        super().__init__()
        uic.loadUi("gui/main.ui", self)
        self.username = username
        
    def show(self):
        super().show()
        button = self.findChild(QPushButton, "Send")
        button.clicked.connect(self.send_message)

    def send_message(self):
        log.d("Кнопка нажата")
        textedit = self.findChild(QTextEdit, "MessageToSend")
        message = textedit.toPlainText()
        print(message)
        self.sendMessage.emit(message,"public")
        textedit.clear() 
    
    def show_message(self,message, message_type):
        display = self.findChild( QTextBrowser,"MessageDisplay")
        display.append(f"{msg.time}| {msg.semderName})

