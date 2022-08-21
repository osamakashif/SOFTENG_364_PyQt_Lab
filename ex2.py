__author__ = 'Osama Kashif'
__version__ = '1.0.0'

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QMessageBox)

class Dynamic(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel('This is the first horizontal box'))
        hbox1.addWidget(QLabel('This is the second entry to the first horizontal box'))
        hbox2 = QHBoxLayout()
        hbox2.addWidget(QLabel('This is the second horizontal box'))
        hbox3 = QHBoxLayout()
        hbox3.addWidget(QLabel('This is the third horizontal box inside the second horizontal box'))
        hbox2.addLayout(hbox3)
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        vbox.addWidget(QLabel('This is a vertical box'))
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(QLabel('Above this label are two horizontal boxes and a label inside this vertical box'))

        quit_button = QPushButton('Quit', self)
        quit_button.resize(quit_button.sizeHint())
        quit_button.clicked.connect(self.close)

        vbox.addWidget(quit_button)

        self.setWindowTitle('Dynamic Layout - Box Layouts')
        self.show()
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:        event.accept()
        else:                               event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dynamic()
    sys.exit(app.exec_())