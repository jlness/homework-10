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

def main():
#initialize

    # self.setFixedHeight(1000)
    # self.setFixedWidth(450)
    st = QApplication(sys.argv)
    wid = QWidget()
    
    #LED Light setup
    led = QPushButton(wid)
    led.setText("Press to turn the LED light on, release to turn off")
    led.move(128,32)
    led.pressed.connect(led_on)
    led.released.connect(led_off)

    #Button Setup
    but = QRadioButton(wid)
    but.setText("Filled if circuit is complete")
    but.move(128,128)

    
    wid.setGeometry(100,60,1000,800)
    wid.show()

    def my_callback(channel):
        if but.isChecked() == True:
            but.setChecked(False)
        else: but.setChecked(True)

    GPIO.add_event_detect(17, GPIO.BOTH)
    GPIO.add_event_callback(17, my_callback)

    #Some Trial and Error work I was doing, did not work out


    # text = QLabel("Press to light LED")
    # HB = QHBoxLayout()
    # HB.addWidget(self.button)
    # HB.indicator = QLabel("disconnected")

    # VB = QVBoxLayout()
    # VB.addwidget(text)
    # VB.addLayout(HB)

    sys.exit(st.exec_())

# def led_on():
#    GPIO.output(18, GPIO.HIGH)
# def led_off():  
#    GPIO.output(18, GPIO.LOW)



if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(17, GPIO.IN)
    main()
    # sys.exit(st.exec_())
