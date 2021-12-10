import sys
import time
import Rpi.GPIO as GPIO

from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt

GPIO.setmode(GPIO.BCM)
pin = 18
GPIO.setup(pin, GPIO.OUT)

class Main(QMainWindow):
  def init(self):
    #initialize
    super().init()
    self.setFixedHeight(450)
    self.setFixedWidth(450)
    
    # Press and indicator text
    press = QLabel("Press button to turn the LED light on")
    self.button = QPushButton("Light")
    self.indicator = QLabel("Not Connected")
    
    A = QWidget()
    H = QHBoxLayout()
    V = QVBoxLayout()
    
    
    H.addWidget(self.button)
    H.addWidget(self.indicator)
    V.addWidget(press)
    V.addWidget(H)
    A.setLayout(V)
    self.setCentralWidget(A)
    self.button.clicked.connect(self.light_LED)
    self.i = True



  def my_callback(self):
    self.indicator.setText("Connected")
  def light_LED(self):
    if self.i == True:
      GPIO.output(pin, GPIO.LOW)
      self.indicator.setText("Not Connected")
      self.i = True
      return




if __name__ == '__main__':
  st = QApplication(sys.argv)
  win = Main()
  win.show()
  st.exec_()
