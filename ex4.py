__author__ = 'Osama Kashif'
__version__ = '1.0.0'

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
import time

class Counter(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        counter_label = QLabel('Second Counter')
        counter_label.setFont(QFont('Times', 14))
        counter_label.setMaximumWidth(600)
        counter_label.setMinimumHeight(25)
        counter_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(counter_label)
        self.count = 0
        self.timer_label = QLabel(str(self.count))
        self.timer_label.setFont(QFont('Times', 14))
        self.timer_label.setMaximumWidth(600)
        self.timer_label.setMinimumHeight(25)
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.timer_label)

        self.counter_thread = CounterThread(self.count, self.timer_label)

        self.timer_button = QPushButton('Start', self)
        self.timer_button.clicked.connect(self.counter)
        layout.addWidget(self.timer_button)
        self.counting = False
        self.started = False

        quit_button = QPushButton('Quit', self)
        quit_button.resize(quit_button.sizeHint())
        quit_button.clicked.connect(self.close)

        layout.addWidget(quit_button)

        self.setWindowTitle('Second Counter - Threading Example')
        self.setGeometry(300, 300, 400, 250) # (starting x coordinate on screen for window, starting y coordinate on screen for window, width, height)
        self.show()
    
    def counter(self):
        if not self.started:
            self.counter_thread.start()
            self.started = True
            self.counting = True
            self.timer_button.setText("Pause")
        else:
            if not self.counting:
                self.counter_thread.restart()
                self.timer_button.setText("Pause")
            else:
                self.counter_thread.stop()
                self.timer_button.setText("Resume")
            self.counting = not self.counting
        # Causes the program to get held
        # while True:
        #     self.count += 1
        #     self.timer_label.setText(str(self.count))
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:        event.accept()
        else:                               event.ignore()

class CounterThread(QThread):
    update = pyqtSignal()

    def __init__(self, count, timer_label):
        super().__init__()
        self.Running = True
        self.count = count
        self.timer_label = timer_label
    
    def run(self):
        while True:
            while self.Running:
                self.count += 1
                self.timer_label.setText(str(self.count))
                self.update.emit()
                time.sleep(1)
    
    def stop(self):
        self.Running = False

    def restart(self):
        self.Running = True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Counter()
    sys.exit(app.exec_())