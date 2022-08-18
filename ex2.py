__author__ = 'Osama Kashif'
__version__ = '1.0.0'

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)

class Dynamic(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox1 = QHBoxLayout()
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        quit_button = QPushButton('Quit', self)
        quit_button.resize(quit_button.sizeHint())
        quit_button.clicked.connect(self.close)
        
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