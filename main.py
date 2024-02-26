import sys

import statistics as st

import pyqtgraph as pg

from PyQt6 import QtWidgets

from mainWindowApp import Ui_Form

from api import *

from db import auth, reg, get_users

bar_flag = False
graph_flag = True
def get_statistics(lst):
    return (f"Медиана = {round(st.median(lst), 2)}; "
            f"Среднее значение = {round(st.mean(lst), 2)}; "
            f"Отклонение = {round(st.stdev(lst), 2)}")



class MainApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=None)
        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(0)

        self.btn_login.clicked.connect(self.on_login)

        self.btn_register.clicked.connect(self.on_reg)

        self.btn_get_weather.clicked.connect(self.on_get_weather_press)

        self.btn_load_local_file.clicked.connect(self.load_local_table)

        self.btn_load_source_file.clicked.connect(self.load_source_table)

        self.btn_visual.clicked.connect(self.to_visual)

        self.btn_analyze.clicked.connect(self.build_graph)

        self.radio_btn_graph.toggled.connect(self.graph_clicked)

        self.radio_btn_bar.toggled.connect(self.bar_clicked)

    def on_login(self):
        login = self.edit_login.text()
        password = self.edit_password.text()

        if auth(login, password):
            self.stackedWidget.setCurrentIndex(1)
        elif len(login) + len(password) == 0:
            self.error_label.setText("Введите логин и пароль")
        else:
            self.error_label.setText("Вы что-то неправильно ввели")

    def on_reg(self):
        login = self.edit_login.text()
        password = self.edit_password.text()

        if len(login) < 3 or len(password) < 3:
            self.error_label.setText("Длина логина или пароля слишком мала.")
        elif len(login) + len(password) == 0:
            self.error_label.setText("Введите логин и пароль")
        elif login in get_users():
            self.error_label.setText("Такой логин уже существует / неправильный пароль")
        elif ' ' in login or ' ' in password:
            self.error_label.setText("Логин и пароль не должны иметь пробелы")
        else:
            reg(login, password)

    def load_local_table(self):
        pass

    def load_source_table(self):
        pass

    def to_visual(self):
        pass

    def bar_clicked(self):
        rb = self.sender()
        print(rb.isChecked())
        global bar_flag
        bar_flag = rb.isChecked()
        return

    def graph_clicked(self):
        rb = self.sender()
        print(rb.isChecked())
        global graph_flag
        graph_flag = rb.isChecked()
        return

    def build_graph(self):
        if self.graph_layout.count() > 0:
            self.graph_layout.removeWidget(self.plll)
        town = self.edit_town_visual.text()
        if len(town) == 0:
            self.visual_label.setText("Произошла ошибка. Проверьте введеные данные.")
            return
        self.label_town_graph.setText(town)

        #  getting data from dictionary
        data = get_weather_5day(town)
        temperature = get_temp_5day(data)
        humid = get_humid_5day(data)
        time = get_time_5day(data)

        xtime = [i for i in range(len(temperature))]
        xdict = dict(enumerate(time))
        self.plll = pg.plot(title="Погода")

        if graph_flag:
            self.plll.plot(xtime, temperature)
        elif bar_flag:
            self.plll.addItem(pg.BarGraphItem(x=xtime, height=temperature, width=0.3, brush='w'))

        stringaxis = pg.AxisItem(orientation='bottom')
        stringaxis.setTicks([xdict.items()])
        self.plll.setAxisItems(axisItems={'bottom': stringaxis})
        self.graph_layout.addWidget(self.plll)

        self.edit_town_visual.setText("")
        self.temp_stats.setText(get_statistics(temperature))
        self.humid_stats.setText(get_statistics(humid))

        self.Info_Widget.setCurrentIndex(3)

    def on_get_weather_press(self):
        town = self.lineEdit_town.text()
        if len(town) == 0:
            self.label_weather.setText('Введите город')
        else:
            try:
                stats = get_weather(town)
                day_time = get_time(stats)
                wind = stats['wind']
                clouds = stats['weather'][0]['description']
                prime = stats['main']
                max_temp = prime['temp_max']
                min_temp = prime['temp_min']
                self.label_weather.setText(f"Город {stats['name']} \n"
                                       f"Влажность: {prime['humidity']}% \n"
                                       f"Макс. темп: {round(min_temp - 273)}°C \n"
                                       f"Мин. темп: {round(max_temp - 273)}°C \n"
                                       f"Сегодня у нас {clouds} \n"
                                       f"Облачность: {stats['clouds']['all']}% \n"
                                       f"Скорость ветра: {wind['speed']} м/с \n"
                                       f"Давление: {prime['pressure']} Гектопаскалей \n"
                                       f"Дата: {day_time[0]} \n"
                                       f"Текущее время: {day_time[1]} \n"
                                       f"(изменения только по кнопке)")
                self.lineEdit_town.setText('')
            except:
                self.label_weather.setText("Такого города не существует. \n"
                                           "Попробуйте еще раз")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()

    window.show()
    app.exec()
