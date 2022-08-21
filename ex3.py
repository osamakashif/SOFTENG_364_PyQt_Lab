__author__ = 'Osama Kashif'
__version__ = '1.0.0'

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox)
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest

ICON_IMAGE_URL="https://osamakashif.dev/logo192.png" # Example online image url

class Counter(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.colour_label = QLabel('Dark Mode')
        self.colour_label.setFont(QFont('Times', 30))
        self.colour_label.setMaximumWidth(600)
        self.colour_label.setMinimumHeight(25)
        self.colour_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.colour_label)

        self.switch_button = QPushButton('Switch')
        self.switch_button.clicked.connect(self.switch)
        self.switch_button.setFont(QFont('Times', 12))
        self.switch_button.setMinimumHeight(20)
        self.switch_button.setStyleSheet("background-color: white; color: black; border-radius : 2")

        self.layout.addWidget(self.switch_button)
        self.dark = True
        self.setStyleSheet("background-color: black; color: white")

        self.quit_button = QPushButton('Quit', self)
        self.quit_button.resize(self.quit_button.sizeHint())
        self.quit_button.clicked.connect(self.close)
        self.quit_button.setFont(QFont('Times', 12))
        self.quit_button.setMinimumHeight(20)
        self.quit_button.setStyleSheet("background-color: white; color: black; border-radius : 2")
        self.layout.addWidget(self.quit_button)

        # Network Access Manager used to get icon from online url
        self.nam = QNetworkAccessManager()
        self.nam.finished.connect(self.set_window_icon_from_response)
        self.nam.get(QNetworkRequest(QUrl(ICON_IMAGE_URL)))

        self.setWindowTitle('Light/Dark Mode - Styling Example')
        self.setGeometry(300, 300, 400, 250) # (starting x coordinate on screen for window, starting y coordinate on screen for window, width, height)
        self.show()
        
    def set_window_icon_from_response(self, http_response): # Function from https://stackoverflow.com/questions/48255299/pyqt5-5-9-setwindowicon-qiconweb-link
        pixmap = QPixmap()
        pixmap.loadFromData(http_response.readAll())
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:        event.accept()
        else:                               event.ignore()
    
    def switch(self):
        self.dark = not self.dark
        if (self.dark):
            self.colour_label.setText("Dark Mode")
            self.setStyleSheet("background-color: black; color: white")
            self.switch_button.setStyleSheet("background-color: white; color: black; border-radius : 2")
            self.quit_button.setStyleSheet("background-color: white; color: black; border-radius : 2")
        else:
            self.colour_label.setText("Light Mode")
            self.setStyleSheet("background-color: #FFFFFF; color: #000000")
            self.switch_button.setStyleSheet("background-color: black; color: white; border-radius : 2")
            self.quit_button.setStyleSheet("background-color: black; color: white; border-radius : 2")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Counter()
    sys.exit(app.exec_())