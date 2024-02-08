# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(835, 581)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edit_login = QtWidgets.QLineEdit(parent=self.page)
        self.edit_login.setObjectName("edit_login")
        self.horizontalLayout_3.addWidget(self.edit_login)
        self.edit_password = QtWidgets.QLineEdit(parent=self.page)
        self.edit_password.setObjectName("edit_password")
        self.horizontalLayout_3.addWidget(self.edit_password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_register = QtWidgets.QPushButton(parent=self.page)
        self.btn_register.setObjectName("btn_register")
        self.horizontalLayout_2.addWidget(self.btn_register)
        self.btn_login = QtWidgets.QPushButton(parent=self.page)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_2.addWidget(self.btn_login)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.error_label = QtWidgets.QLabel(parent=self.page)
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.verticalLayout_2.addWidget(self.error_label)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Info_Widget = QtWidgets.QTabWidget(parent=self.page_2)
        self.Info_Widget.setMinimumSize(QtCore.QSize(500, 140))
        self.Info_Widget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Info_Widget.setObjectName("Info_Widget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_11 = QtWidgets.QFrame(parent=self.tab_2)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(parent=self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_4.addWidget(self.frame_11)
        self.frame_10 = QtWidgets.QFrame(parent=self.tab_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget = QtWidgets.QWidget(parent=self.frame_10)
        self.widget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.lineEdit_town = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_town.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_town.setObjectName("lineEdit_town")
        self.verticalLayout_16.addWidget(self.lineEdit_town)
        self.btn_get_weather = QtWidgets.QPushButton(parent=self.widget)
        self.btn_get_weather.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_get_weather.setObjectName("btn_get_weather")
        self.verticalLayout_16.addWidget(self.btn_get_weather)
        self.horizontalLayout_5.addWidget(self.widget)
        self.line = QtWidgets.QFrame(parent=self.frame_10)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.label_weather = QtWidgets.QLabel(parent=self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_weather.setFont(font)
        self.label_weather.setText("")
        self.label_weather.setObjectName("label_weather")
        self.horizontalLayout_5.addWidget(self.label_weather)
        self.verticalLayout_4.addWidget(self.frame_10)
        self.Info_Widget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.tab_5)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(parent=self.tab_5)
        self.frame.setMinimumSize(QtCore.QSize(500, 140))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_6 = QtWidgets.QFrame(parent=self.frame)
        self.frame_6.setMinimumSize(QtCore.QSize(260, 60))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.lineEdit_source = QtWidgets.QLineEdit(parent=self.frame_6)
        self.lineEdit_source.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_source.setMaximumSize(QtCore.QSize(480, 16777215))
        self.lineEdit_source.setObjectName("lineEdit_source")
        self.verticalLayout_10.addWidget(self.lineEdit_source)
        self.horizontalLayout_6.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.btn_load_source_file = QtWidgets.QPushButton(parent=self.frame_7)
        self.btn_load_source_file.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_load_source_file.setFont(font)
        self.btn_load_source_file.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_load_source_file.setObjectName("btn_load_source_file")
        self.verticalLayout_11.addWidget(self.btn_load_source_file, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(10, 3, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_11.addItem(spacerItem2)
        self.btn_load_local_file = QtWidgets.QPushButton(parent=self.frame_7)
        self.btn_load_local_file.setMinimumSize(QtCore.QSize(200, 40))
        self.btn_load_local_file.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_load_local_file.setFont(font)
        self.btn_load_local_file.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_load_local_file.setObjectName("btn_load_local_file")
        self.verticalLayout_11.addWidget(self.btn_load_local_file, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_6.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(parent=self.tab_5)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.btn_visual = QtWidgets.QPushButton(parent=self.frame_3)
        self.btn_visual.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_visual.setFont(font)
        self.btn_visual.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_visual.setObjectName("btn_visual")
        self.verticalLayout_8.addWidget(self.btn_visual, 0, QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.error_label_loadfile = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.error_label_loadfile.setFont(font)
        self.error_label_loadfile.setObjectName("error_label_loadfile")
        self.verticalLayout_8.addWidget(self.error_label_loadfile, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout.addWidget(self.frame_3)
        self.Info_Widget.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(parent=self.tab)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(parent=self.tab)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.edit_town_visual = QtWidgets.QLineEdit(parent=self.frame_5)
        self.edit_town_visual.setMinimumSize(QtCore.QSize(200, 30))
        self.edit_town_visual.setMaximumSize(QtCore.QSize(200, 16777215))
        self.edit_town_visual.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.edit_town_visual.setObjectName("edit_town_visual")
        self.horizontalLayout_4.addWidget(self.edit_town_visual)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame_5)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.radio_btn_graph = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radio_btn_graph.setObjectName("radio_btn_graph")
        self.verticalLayout_13.addWidget(self.radio_btn_graph)
        self.radio_btn_bar = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radio_btn_bar.setObjectName("radio_btn_bar")
        self.verticalLayout_13.addWidget(self.radio_btn_bar)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_8 = QtWidgets.QFrame(parent=self.tab)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_3.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(parent=self.tab)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.btn_analyze = QtWidgets.QPushButton(parent=self.frame_9)
        self.btn_analyze.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_analyze.setFont(font)
        self.btn_analyze.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_analyze.setObjectName("btn_analyze")
        self.verticalLayout_12.addWidget(self.btn_analyze)
        self.visual_label = QtWidgets.QLabel(parent=self.frame_9)
        self.visual_label.setMaximumSize(QtCore.QSize(16777215, 10))
        self.visual_label.setObjectName("visual_label")
        self.verticalLayout_12.addWidget(self.visual_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.Info_Widget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_12 = QtWidgets.QFrame(parent=self.tab_4)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_14.addWidget(self.label_6, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_7.addWidget(self.frame_12, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_town_graph = QtWidgets.QLabel(parent=self.tab_4)
        self.label_town_graph.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_town_graph.setObjectName("label_town_graph")
        self.verticalLayout_7.addWidget(self.label_town_graph, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.graph_layout = QtWidgets.QVBoxLayout()
        self.graph_layout.setObjectName("graph_layout")
        self.verticalLayout_7.addLayout(self.graph_layout)
        self.Info_Widget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.Info_Widget.addTab(self.tab_3, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.label_4 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_4.setGeometry(QtCore.QRect(9, 9, 600, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Info_Widget.addTab(self.tab_1, "")
        self.horizontalLayout_7.addWidget(self.Info_Widget)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        self.Info_Widget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.edit_login.setPlaceholderText(_translate("Form", "Логин"))
        self.edit_password.setPlaceholderText(_translate("Form", "Пароль"))
        self.btn_register.setText(_translate("Form", "Зарегистрироваться"))
        self.btn_login.setText(_translate("Form", "Войти"))
        self.label.setText(_translate("Form", "Мониторинг"))
        self.lineEdit_town.setPlaceholderText(_translate("Form", "Город"))
        self.btn_get_weather.setText(_translate("Form", "Получить текущую погоду"))
        self.Info_Widget.setTabText(self.Info_Widget.indexOf(self.tab_2), _translate("Form", "Мониторинг"))
        self.label_2.setText(_translate("Form", "Работа с файлами"))
        self.label_3.setText(_translate("Form", "Ссылка"))
        self.btn_load_source_file.setText(_translate("Form", "Загрузить ссылку"))
        self.btn_load_local_file.setText(_translate("Form", "Загрузить файл (CSV, XLSX)"))
        self.btn_visual.setText(_translate("Form", "Визуализация"))
        self.error_label_loadfile.setText(_translate("Form", "Выберите файлы или вставьте ссылку для загрузки"))
        self.Info_Widget.setTabText(self.Info_Widget.indexOf(self.tab_5), _translate("Form", "Загрузка данных"))
        self.label_5.setText(_translate("Form", "Визуализация"))
        self.edit_town_visual.setPlaceholderText(_translate("Form", "Местоположение"))
        self.groupBox.setTitle(_translate("Form", "Тип данных"))
        self.radio_btn_graph.setText(_translate("Form", "График"))
        self.radio_btn_bar.setText(_translate("Form", "Диаграмма"))
        self.btn_analyze.setText(_translate("Form", "Анализ"))
        self.visual_label.setText(_translate("Form", "Тут можно вывести данные на графики"))
        self.Info_Widget.setTabText(self.Info_Widget.indexOf(self.tab), _translate("Form", "Визуализация"))
        self.label_6.setText(_translate("Form", "Анализ"))
        self.label_town_graph.setText(_translate("Form", "Тут будет название города"))
        self.Info_Widget.setTabText(self.Info_Widget.indexOf(self.tab_4), _translate("Form", "Анализ"))
        self.Info_Widget.setTabText(self.Info_Widget.indexOf(self.tab_3), _translate("Form", "Прогнозирование"))
        self.label_4.setText(_translate("Form", "Добро пожаловать! В этом приложении все разделы расположены в навигации сверху."))
        self.Info_Widget.setTabText(self.Info_Widget.indexOf(self.tab_1), _translate("Form", "Информация"))
