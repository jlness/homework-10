import sys
from PyQt5.QtWidgets import QApplication, QWidget,QRadioButton, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import RPi.GPIO as GPIO

def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   
   button1 = QPushButton(widget)
   button1.setText("Led Light")
   button1.move(64,32)
   button1.pressed.connect(led_on)
   button1.released.connect(led_off)

   button2 = QRadioButton(widget)
   button2.setText("Button2")
   button2.move(64,64)
   


   widget.setGeometry(50,50,320,200)
   widget.setWindowTitle("PyQt5 Button Click Example")
   widget.show()
   sys.exit(app.exec_())


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
    
    

    window()