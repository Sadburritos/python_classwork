from PyQt5.QtWidgets import *
from sys import *
from calc import My_calculator


class Calc_main_window(QMainWindow):
    calc_view = None

    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)

    def set_view(self, view):
        self.calc_view = view
        self.setCentalWiget(self.calc_view)




