from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvis(object):
    def setupUi(self, jarvis):
        jarvis.setObjectName("jarvis")
        jarvis.resize(1362, 836)
        self.centralwidget = QtWidgets.QWidget(jarvis)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1391, 871))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("iron man.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 291, 91))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 381, 141))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("intiating.gif"))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(970, 720, 93, 28))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1080, 720, 93, 28))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        jarvis.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvis)
        QtCore.QMetaObject.connectSlotsByName(jarvis)

    def retranslateUi(self, jarvis):
        _translate = QtCore.QCoreApplication.translate
        jarvis.setWindowTitle(_translate("jarvis", "MainWindow"))
        self.label_2.setText(_translate("jarvis", "TextLabel"))
        self.pushButton.setText(_translate("jarvis", "RUN"))
        self.pushButton_2.setText(_translate("jarvis", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvis = QtWidgets.QMainWindow()
    ui = Ui_jarvis()
    ui.setupUi(jarvis)
    jarvis.show()
    sys.exit(app.exec_())
