import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout)


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        label6 = QLabel("#6", self)
        label7 = QLabel("#7", self)
        label8 = QLabel("#8", self)

        label1.setStyleSheet("background-color:Blue;")
        label2.setStyleSheet("background-color:Red;")
        label3.setStyleSheet("background-color:Green;")
        label4.setStyleSheet("background-color:Brown;")
        label5.setStyleSheet("background-color:Black;")
        label6.setStyleSheet("background-color:Pink;")
        label7.setStyleSheet("background-color:Yellow;")
        label8.setStyleSheet("background-color:Teal;")

        vbox = QGridLayout()
        vbox.addWidget(label1, 0, 0)
        vbox.addWidget(label2, 0, 1)
        vbox.addWidget(label3, 1, 0)
        vbox.addWidget(label4, 1, 1)
        vbox.addWidget(label5, 2, 0)
        vbox.addWidget(label6, 2, 1)
        vbox.addWidget(label7, 3, 1)
        vbox.addWidget(label8, 3, 2)
        central_widget.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
