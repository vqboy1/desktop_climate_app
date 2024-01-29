import sys

from PyQt6 import QtWidgets

from mainWindowApp import Ui_Form

from api import get_weather


class MainApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=None)
        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(0)

        self.btn_login.clicked.connect(self.on_login)

        self.btn_get_weather.clicked.connect(self.get_weather)

    def on_login(self):
        self.stackedWidget.setCurrentIndex(1)

    def get_weather(self):
        stats = get_weather()

        self.label_weather.setText(f"Макс. темп: {round(stats[0] - 273)} \n"
                                   f"Мин. темп: {round(stats[1] - 273)}")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()

    window.show()
    app.exec()
