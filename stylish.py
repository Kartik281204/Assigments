import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.button4 = QPushButton("#4")
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        self.button4.setObjectName("button4")
        self.initUI()

    def initUI(self):
        central_widgets = QWidget()
        self.setCentralWidget(central_widgets)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        hbox.addWidget(self.button4)
        central_widgets.setLayout(hbox)

        self.setStyleSheet("""
                           QPushButton {
                               font-family:New Times Roman;
                               font-size:30px;
                               padding:15px,20px; 
                               border : 10px solid;
                               border-radius : 15px; 
                           } 
                           QPushButton#button1:hover{
                               background-color : red;}
                           QPushButton#button2:hover{
                               background-color : blue;}
                           QPushButton#button3:hover{
                               background-color : black;}
                           QPushButton#button4:hover{
                               background-color : green;}   
                           """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
