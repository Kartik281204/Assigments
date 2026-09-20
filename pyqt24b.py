import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt


class Mainwindow():
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon(
            "C:\\Users\\nukeg\\OneDrive\\Desktop\\cppDSA\\iron-man-jarvis-desktop-a7p26lw1xf92bxtg.jpg"))
        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)
        pixmap = QPixmap(
            "C:\\Users\\nukeg\\OneDrive\\Desktop\\cppDSA\\2141172-2646x1314-desktop-dual-screen-jarvis-iron-man-wallpaper-photo.jpg")
        label.setPixmap(pixmap)
        label.setGeometry((self.width()-label.width())//2, (self.height() -
                          label.height())//2, label.width(), label.height())
        label.setScaledContents(True)


def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
