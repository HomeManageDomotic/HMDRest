#!/usr/bin/python

import sys, getopt
import RPi.GPIO as GPIO
import argparse

parser = argparse.ArgumentParser(description='')

parser.add_argument('-pin', action="store",dest="gpio_pin", type=int, help="GPIO Led Pin")
parser.add_argument('-a', action="store", default=0, dest="value", help="[1:ON | 2:OFF], by default 0", type=int)
parser.add_argument('-board', action="store_true", default=False, dest="type_gpio", help="Add me to use GPIO.BOARD type; by default using GPIO.BCM")

results = parser.parse_args()
MESSAGE="""GPIO({TYPE}) -> PIN {GPIO} VALUE {VALUE} """
GPIO.setwarnings(False)
def setupGpio(type):
   mode = GPIO.BCM
   if(type):
	mode = GPIO.BOARD
   GPIO.setmode(mode)

def setupLedPin(pin):
   GPIO.setup(pin, GPIO.OUT)

def actionLed(pin, value):
   GPIO.output(pin, int(value))

def main(argv):
   type = results.type_gpio
   gpio = results.gpio_pin
   value = results.value
   message = MESSAGE.format(TYPE=type,VALUE=value,GPIO=gpio)
   print message
   setupGpio(type)
   setupLedPin(gpio)
   actionLed(gpio, value)
  	

if __name__ == "__main__":
   main(sys.argv[1:])
