from PyQt5 import QtCore, QtGui, QtWidgets
from string import digits, ascii_letters
from random import sample

desired_length = 0

def generate_password():
    global desired_length
    print("In generated password: " + str(desired_length))
    password = ''.join(sample(ascii_letters + digits, desired_length))
    return password

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 291)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DesiredPasswordSubmitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DesiredPasswordSubmitBtn.setGeometry(QtCore.QRect(110, 180, 181, 41))
        self.DesiredPasswordSubmitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DesiredPasswordSubmitBtn.setObjectName("DesiredPasswordSubmitBtn")

        self.DesiredPasswordSubmitBtn.clicked.connect(self.get_password_length) # Get the value of the DesiredPasswordBox when pressed

        self.DesiredPasswordBox = QtWidgets.QSpinBox(self.centralwidget)
        self.DesiredPasswordBox.setGeometry(QtCore.QRect(180, 140, 42, 22))
        self.DesiredPasswordBox.setObjectName("DesiredPasswordBox")
        self.DesiredPasswordLbl = QtWidgets.QLabel(self.centralwidget)
        self.DesiredPasswordLbl.setGeometry(QtCore.QRect(100, 90, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.DesiredPasswordLbl.setFont(font)
        self.DesiredPasswordLbl.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.DesiredPasswordLbl.setObjectName("DesiredPasswordLbl")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 60, 441, 21))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 12, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 423, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DesiredPasswordSubmitBtn.setText(_translate("MainWindow", "Submit "))
        self.DesiredPasswordLbl.setText(_translate("MainWindow", "Enter Desired Password Length"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "")) # This is where to put the password generated
        self.label.setText(_translate("MainWindow", "Your Password Will Appear Here"))
    def get_password_length(self):
        global desired_length
        desired_length = self.DesiredPasswordBox.value()
        p = generate_password()
        print("The password generated is now: " + str(p))
        self.plainTextEdit.setPlainText(p)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
