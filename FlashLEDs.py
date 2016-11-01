import time
import RPi.GPIO as GPIO
# Slot 2 pins
LRpin = 13
LYpin = 19
LGpin = 14
RRpin = 17
RYpin = 26
RGpin = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(LRpin, GPIO.OUT)
GPIO.setup(LYpin, GPIO.OUT)
GPIO.setup(LGpin, GPIO.OUT)
GPIO.setup(RRpin, GPIO.OUT)
GPIO.setup(RYpin, GPIO.OUT)
GPIO.setup(RGpin, GPIO.OUT)
try:
    while True:
          GPIO.output(LRpin,GPIO.HIGH)
          GPIO.output(LYpin,GPIO.HIGH)
          GPIO.output(LGpin,GPIO.HIGH)
          GPIO.output(RRpin,GPIO.LOW)
          GPIO.output(RYpin,GPIO.LOW)
          GPIO.output(RGpin,GPIO.LOW)
          time.sleep(1)
          GPIO.output(LRpin,GPIO.LOW)
          GPIO.output(LYpin,GPIO.LOW)
          GPIO.output(LGpin,GPIO.LOW)
          GPIO.output(RRpin,GPIO.HIGH)
          GPIO.output(RYpin,GPIO.HIGH)
          GPIO.output(RGpin,GPIO.HIGH)
          time.sleep(1)
    # end while
except KeyboardInterrupt :
    GPIO.cleanup()
