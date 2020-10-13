# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal_design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(302, 365)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(36, 36))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(10, 120, 71, 51))
        self.btn_7.setStyleSheet("font-size:20px;\n"
"background:#264d73;\n"
"color:white;")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(80, 120, 71, 51))
        self.btn_8.setStyleSheet("font-size:20px;\n"
"background:#264d73;\n"
"color:white;")
        self.btn_8.setObjectName("btn_8")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(10, 170, 71, 51))
        self.btn_4.setStyleSheet("font-size:20px;\n"
"background:#264d73;\n"
"color:white;")
        self.btn_4.setObjectName("btn_4")
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setGeometry(QtCore.QRect(220, 70, 71, 51))
        self.btn_div.setStyleSheet("font-size:18px;\n"
"color:#990000;\n"
"background:#ebebe0;")
        self.btn_div.setObjectName("btn_div")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(150, 120, 71, 51))
        self.btn_9.setStyleSheet("font-size:20px;\n"
"background:#264d73;\n"
"color:white;")
        self.btn_9.setObjectName("btn_9")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(80, 170, 71, 51))
        self.btn_5.setStyleSheet("font-size:20px;\n"
"background:#264d73;\n"
"color:white;")
        self.btn_5.setObjectName("btn_5")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(10, 220, 71, 51))
        self.btn_1.setStyleSheet("font-size:20px;\n"
"background:#264d73;\n"
"color:white;\n"
"")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(80, 220, 71, 51))
        self.btn_2.setStyleSheet("font-size:20px;\n"
"background:#264d73;\n"
"color:white;")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(150, 220, 71, 51))
        self.btn_3.setStyleSheet("font-size:20px;\n"
"background:#264d73;\n"
"color:white;")
        self.btn_3.setObjectName("btn_3")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(220, 170, 71, 51))
        self.btn_minus.setStyleSheet("font-size:18px;\n"
"color:#990000;\n"
"background:#ebebe0;")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(150, 170, 71, 51))
        self.btn_6.setStyleSheet("font-size:20px;\n"
"background:#264d73;\n"
"color:white;")
        self.btn_6.setObjectName("btn_6")
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiply.setGeometry(QtCore.QRect(220, 120, 71, 51))
        self.btn_multiply.setStyleSheet("font-size:18px;\n"
"color:#990000;\n"
"background:#ebebe0;")
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(10, 270, 141, 51))
        self.btn_0.setStyleSheet("font-size:20px;\n"
"background:#264d73;\n"
"color:white;")
        self.btn_0.setObjectName("btn_0")
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(150, 270, 71, 51))
        self.btn_dot.setStyleSheet("font-size:18px;\n"
"color:#990000;\n"
"background:#ebebe0;")
        self.btn_dot.setObjectName("btn_dot")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(10, 70, 141, 51))
        self.btn_clear.setStyleSheet("font-size:18px;\n"
"color:#990000;\n"
"background:#ebebe0;")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(150, 70, 71, 51))
        self.btn_back.setStyleSheet("font-size:18px;\n"
"color:#e68a00;\n"
"background:#ebebe0;")
        self.btn_back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Python Docs/Step4-Python/43-PyQt5/Files/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon1)
        self.btn_back.setIconSize(QtCore.QSize(36, 36))
        self.btn_back.setObjectName("btn_back")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(220, 220, 71, 51))
        self.btn_plus.setStyleSheet("font-size:18px;\n"
"color:#990000;\n"
"background:#ebebe0;")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(220, 270, 71, 51))
        self.btn_equal.setStyleSheet("font-size:18px;\n"
"color:white;\n"
"background:#80002a;")
        self.btn_equal.setObjectName("btn_equal")
        self.le_result = QtWidgets.QLineEdit(self.centralwidget)
        self.le_result.setGeometry(QtCore.QRect(10, 10, 281, 51))
        self.le_result.setStyleSheet("font-size:20px;\n"
"background:white;\n"
"color:#264d73;")
        self.le_result.setReadOnly(True)
        self.le_result.setObjectName("le_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 302, 21))
        self.menubar.setObjectName("menubar")
        self.menuCalculator = QtWidgets.QMenu(self.menubar)
        self.menuCalculator.setObjectName("menuCalculator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCalculator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_multiply.setText(_translate("MainWindow", "X"))
        self.btn_back.setText(_translate("MainWindow", "<"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_clear.setText(_translate("MainWindow", "CLEAR"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.menuCalculator.setTitle(_translate("MainWindow", "Calculator"))
        
        ### my code:
        self.btn_0.clicked.connect(lambda: self.number_press('0'))
        self.btn_1.clicked.connect(lambda: self.number_press('1'))
        self.btn_2.clicked.connect(lambda: self.number_press('2'))
        self.btn_3.clicked.connect(lambda: self.number_press('3'))
        self.btn_4.clicked.connect(lambda: self.number_press('4'))
        self.btn_5.clicked.connect(lambda: self.number_press('5'))
        self.btn_6.clicked.connect(lambda: self.number_press('6'))
        self.btn_7.clicked.connect(lambda: self.number_press('7'))
        self.btn_8.clicked.connect(lambda: self.number_press('8'))
        self.btn_9.clicked.connect(lambda: self.number_press('9'))
        self.btn_dot.clicked.connect(lambda: self.number_press('.'))

        self.btn_minus.clicked.connect(lambda: self.operator_press('-'))
        self.btn_plus.clicked.connect(lambda: self.operator_press('+'))
        self.btn_multiply.clicked.connect(lambda: self.operator_press('*'))
        self.btn_div.clicked.connect(lambda: self.operator_press('/'))

        self.btn_back.clicked.connect(self.back_press)
        self.btn_clear.clicked.connect(self.clear_press)
        self.btn_equal.clicked.connect(self.equal_press)

    ### Action Listener:
    def number_press(self, number):
        expression = self.le_result.text()
        self.le_result.setText(expression+number)

    def operator_press(self, operator):
        expression = self.le_result.text()
        self.le_result.setText(expression + operator)

    def back_press(self):
        expression = self.le_result.text()
        if(len(expression)>0):
            expression = expression[:-1]
            self.le_result.setText(str(expression))

    def clear_press(self):
        self.le_result.setText('')

    def equal_press(self):
        try:
            expression = self.le_result.text()
            result = eval(expression)
            self.le_result.setText(str(result))
        except:
            print("expression not valid...")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
