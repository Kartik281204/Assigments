import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("submit🌞", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size:10px;"
                                     "font-family:Time New Roman;")
        self.button.setStyleSheet("font-size:20px;"
                                  "font-family:Serif;")
        self.button.adjustSize()
        self.button.clicked.connect(self.button_clicked)
        self.line_edit.setPlaceholderText("Enter your name")

    def button_clicked(self):
        text = self.line_edit.text()
        print(f"Hello {text} ")
        print("Response Submitted🌞🌞")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
