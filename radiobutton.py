import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QButtonGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("StateBank", self)
        self.radio4 = QRadioButton("Credit Card", self)
        self.radio5 = QRadioButton("Debit Card", self)
        self.buttongroup1 = QButtonGroup()
        self.buttongroup2 = QButtonGroup()
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)
        self.setStyleSheet(
            "QRadioButton { font-size: 30px; font-family : Arial; padding :10px;}")

        self.buttongroup1.addButton(self.radio1)
        self.buttongroup1.addButton(self.radio2)
        self.buttongroup1.addButton(self.radio3)
        self.buttongroup2.addButton(self.radio4)
        self.buttongroup2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_buttonchanged)
        self.radio2.toggled.connect(self.radio_buttonchanged)
        self.radio3.toggled.connect(self.radio_buttonchanged)
        self.radio4.toggled.connect(self.radio_buttonchanged2)
        self.radio5.toggled.connect(self.radio_buttonchanged2)

    def radio_buttonchanged(self):
        radio_button = self.sender()
        if radio_button.isChecked:
            print(f"{radio_button.text()} is selected")

    def radio_buttonchanged2(self):
        radio_button = self.sender()
        if radio_button.isChecked:
            print(f"{radio_button.text()} is selected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
