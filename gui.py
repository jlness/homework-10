from buttons import led_off, led_on
import sys
import time


from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QRadioButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
# pin = 18
# GPIO.setup(pin, GPIO.OUT)

class Main(QMainWindow):
  def init(self):
    #initialize
    super().init()

    self.setFixedHeight(1000)
    self.setFixedWidth(450)
    
    #LED Light setup
    wid = QWidget
    led = QPushButton(wid)
    led.setText("LED")
    led.pressed.connect(led_on)
    led.released.connect(led_off)

    #Button Setup
    but = QRadioButton(wid)
    but.setText("button")

    wid.setGeometry(100,100,300,300)
    wid.show()

    


    def my_callback(channel):
        if but.isChecked():
            but.setChecked(False)
        else: but.setChecked(True)

    GPIO.add_event_detect(17, GPIO.BOTH)
    GPIO.add_event_callback(17, my_callback)

    sys.exit(app.exec_())



if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(17, GPIO.IN)
    st = QApplication(sys.argv)
    win = Main()
    win.show()
    st.exec_()
