import sys, datetime

from PyQt6 import QtWidgets

from mainWindowApp import Ui_Form

from api import get_weather, get_time


class MainApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=None)
        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(0)

        self.btn_login.clicked.connect(self.on_login)

        self.btn_get_weather.clicked.connect(self.on_get_weather_press)

    def on_login(self):
        self.stackedWidget.setCurrentIndex(1)

    def on_get_weather_press(self):
        town = self.lineEdit_town.text()
        try:
            stats = get_weather(town)
            time = get_time(stats)
            wind = stats['wind']
            clouds = stats['weather'][0]['description']
            prime = stats['main']
            pressure = prime['pressure']
            max_temp = prime['temp_max']
            min_temp = prime['temp_min']
            humidity = prime['humidity']
            self.label_weather.setText(f"Город {stats['name']} \n"
                                       f"Влажность: {humidity - 6}% \n"
                                       f"Макс. темп: {round(min_temp - 273)}°C \n"
                                       f"Мин. темп: {round(max_temp - 273)}°C \n"
                                       f"Сегодня у нас капец как {clouds} \n"
                                       f"Скорость ветра: {wind['speed']} мчс \n"
                                       f"Давление {pressure} давит как депресия в 0 лет \n"
                                       f"Текущее время: {time}")
        except:
            self.label_weather.setText("Такого города не существует")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()

    window.show()
    app.exec()
