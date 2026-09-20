import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTime, QTimer


class Stop_Watch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.label = QLabel("00:00:00:00")
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.timer_reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stop Watch")
        self.setGeometry(500, 300, 300, 100)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.timer_reset_button)
        vbox.addLayout(hbox)
        self.setStyleSheet("""
                           QPushButton , QLabel {padding : 40px; font-family: New Times Roman ; font-weight:Bold}
                           QPushButton{font-size :30px ;color: rgb(125, 19, 19)}
                           QLabel{font-size :150px ;color: rgb(234, 16, 60); background-color:rgb(16, 15, 15); border-radius:50px}""")
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.timer_reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec()//10
        return f"{hours:02} : {minutes:02} : {seconds:02} . {milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    watch = Stop_Watch()
    watch.show()
    sys.exit(app.exec_())
