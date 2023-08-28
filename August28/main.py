from PyQt5.QtWidgets import *
from sys import *
from calc_main_window import Calc_main_window
from calc import My_calculator


if __name__ == "__main__":
    app = QApplication(argv)

    window = Calc_main_window("Caalcularius 0.0.0")
    view = My_calculator()

    calculator = My_calculator()
    calculator.show()
    app.exec()