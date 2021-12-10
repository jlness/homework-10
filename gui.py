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

def init(self):
#initialize

    self.setFixedHeight(1000)
    self.setFixedWidth(450)
    wid = QWidget
    wid.setGeometry(100,100,300,300)
    wid.show()
    
    #LED Light setup
    led = QPushButton(wid)
    led.setText("LED")
    led.move(64,32)
    led.pressed.connect(led_on)
    led.released.connect(led_off)

    #Button Setup
    but = QRadioButton(wid)
    but.setText("button")
    but.move(64,64)

    


    def my_callback(channel):
        if but.isChecked():
            but.setChecked(False)
        else: but.setChecked(True)

    GPIO.add_event_detect(17, GPIO.BOTH)
    GPIO.add_event_callback(17, my_callback)

def led_on():
   print("Led On")
   GPIO.output(18, GPIO.HIGH)
def led_off():
   print("Led Off")   
   GPIO.output(18, GPIO.LOW)



if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(17, GPIO.IN)
    st = QApplication(sys.argv)
    init()
    st.exec_()
