# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grafic_interface.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Моя прога")
        MainWindow.resize(797, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.insert_info = QtWidgets.QPushButton(self.centralwidget)
        self.insert_info.setGeometry(QtCore.QRect(530, 230, 211, 23))
        self.insert_info.setObjectName("insert_info")
        self.text_datebase = QtWidgets.QTextEdit(self.centralwidget)
        self.text_datebase.setGeometry(QtCore.QRect(10, 10, 491, 271))
        self.text_datebase.setObjectName("text_datebase")
        self.money_input = QtWidgets.QLineEdit(self.centralwidget)
        self.money_input.setGeometry(QtCore.QRect(560, 70, 133, 20))
        self.money_input.setObjectName("money_input")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 10, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Nightclub BTN")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 100, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Nightclub BTN Cn")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(610, 160, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Vivaldi")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.date_input = QtWidgets.QLineEdit(self.centralwidget)
        self.date_input.setGeometry(QtCore.QRect(560, 130, 133, 20))
        self.date_input.setObjectName("date_input")
        self.push_email = QtWidgets.QPushButton(self.centralwidget)
        self.push_email.setGeometry(QtCore.QRect(580, 490, 211, 23))
        self.push_email.setObjectName("push_email")
        self.update_datebase = QtWidgets.QPushButton(self.centralwidget)
        self.update_datebase.setGeometry(QtCore.QRect(10, 290, 111, 23))
        self.update_datebase.setObjectName("update_datebase")
        self.update_end = QtWidgets.QLineEdit(self.centralwidget)
        self.update_end.setGeometry(QtCore.QRect(320, 290, 71, 20))
        self.update_end.setObjectName("update_end")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(560, 190, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.sum = QtWidgets.QPushButton(self.centralwidget)
        self.sum.setGeometry(QtCore.QRect(10, 330, 151, 23))
        self.sum.setObjectName("sum")
        self.date_period_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.date_period_1.setGeometry(QtCore.QRect(190, 330, 31, 20))
        self.date_period_1.setObjectName("date_period_1")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 330, 121, 21))
        self.label_6.setObjectName("label_6")
        self.line_total = QtWidgets.QLineEdit(self.centralwidget)
        self.line_total.setGeometry(QtCore.QRect(400, 330, 113, 20))
        self.line_total.setObjectName("line_total")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 40, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Nightclub BTN Cn")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.delete_datebase = QtWidgets.QPushButton(self.centralwidget)
        self.delete_datebase.setGeometry(QtCore.QRect(410, 290, 111, 23))
        self.delete_datebase.setObjectName("delete_datebase")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_sum = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sum.setGeometry(QtCore.QRect(670, 290, 75, 23))
        self.pushButton_sum.setObjectName("pushButton_sum")
        self.label_ID = QtWidgets.QLabel(self.centralwidget)
        self.label_ID.setGeometry(QtCore.QRect(280, 290, 21, 16))
        self.label_ID.setObjectName("label_ID")
        self.comboBox_email = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_email.setGeometry(QtCore.QRect(370, 370, 191, 22))
        self.comboBox_email.setObjectName("comboBox_email")
        self.email_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.email_lineEdit.setGeometry(QtCore.QRect(10, 370, 351, 20))
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 370, 191, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 290, 121, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 410, 551, 101))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 410, 191, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.insert_info.raise_()
        self.text_datebase.raise_()
        self.money_input.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.date_input.raise_()
        self.push_email.raise_()
        self.update_datebase.raise_()
        self.update_end.raise_()
        self.label_3.raise_()
        self.comboBox.raise_()
        self.sum.raise_()
        self.date_period_1.raise_()
        self.label_6.raise_()
        self.line_total.raise_()
        self.delete_datebase.raise_()
        self.pushButton.raise_()
        self.pushButton_sum.raise_()
        self.label_ID.raise_()
        self.comboBox_email.raise_()
        self.email_lineEdit.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.textEdit.raise_()
        self.pushButton_4.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.date_input, self.push_email)
        MainWindow.setTabOrder(self.push_email, self.insert_info)
        MainWindow.setTabOrder(self.insert_info, self.text_datebase)
        MainWindow.setTabOrder(self.text_datebase, self.money_input)
        MainWindow.setTabOrder(self.money_input, self.update_datebase)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Моя прога"))
        self.insert_info.setText(_translate("MainWindow", "Записать в базу данных"))
        self.text_datebase.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Новые данные для записи"))
        self.label_4.setText(_translate("MainWindow", "Дата (по умолчанию - сегодня)"))
        self.label_5.setText(_translate("MainWindow", "День"))
        self.push_email.setText(_translate("MainWindow", "Отправить письмом"))
        self.update_datebase.setText(_translate("MainWindow", "Изменить данные"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Понедельник"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Вторник"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Среда"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Четверг"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Пятница"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Суббота"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Воскресенье"))
        self.sum.setText(_translate("MainWindow", "Посчитать общую сумму"))
        self.label_6.setText(_translate("MainWindow", "Дней (по умолчанию 6)"))
        self.label_3.setText(_translate("MainWindow", "Деньги"))
        self.delete_datebase.setText(_translate("MainWindow", "Удалить данные"))
        self.pushButton.setText(_translate("MainWindow", "Вычесть"))
        self.pushButton_sum.setText(_translate("MainWindow", "Сложить"))
        self.label_ID.setText(_translate("MainWindow", "ID"))
        self.pushButton_2.setText(_translate("MainWindow", "добавить email  в список"))
        self.pushButton_3.setText(_translate("MainWindow", "Достать данные"))

        self.pushButton_4.setText(_translate("MainWindow", "Сформировать сообщение"))


