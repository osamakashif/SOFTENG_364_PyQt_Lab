__author__ = 'Osama Kashif'
__version__ = '1.0.0'

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox)

class Structured(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(QLabel('Label at (0, 0)'), 0, 0)
        grid.addWidget(QLabel('Label at (1, 0)'), 1, 0)
        grid.addWidget(QLabel('Label at (0, 1)'), 0, 1)
        grid.addWidget(QLabel('Label at (1, 1)'), 1, 1)
        grid.addWidget(QLabel('Line Edit:'), 2, 0)
        self.line_edit = QLineEdit()
        grid.addWidget(self.line_edit, 2, 1)

        quit_button = QPushButton('Quit', self)
        quit_button.resize(quit_button.sizeHint())
        quit_button.clicked.connect(self.close)

        grid.addWidget(QLabel('Label at (2, 3)'), 2, 3)
        grid.addWidget(quit_button, 3, 3)

        self.setWindowTitle('Structured Layout - GridLayout')
        self.setGeometry(300, 300, 400, 250) # (starting x coordinate on screen for window, starting y coordinate on screen for window, width, height)
        self.show()
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:        event.accept()
        else:                               event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Structured()
    sys.exit(app.exec_())