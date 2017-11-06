#!/usr/bin/python

import sys, getopt
import RPi.GPIO as GPIO
import argparse

parser = argparse.ArgumentParser(description='')

parser.add_argument('-pin', action="store",dest="gpio_pin", type=int, help="GPIO Led Pin")
parser.add_argument('-a', action="store", default=0, dest="value", help="[1:ON | 2:OFF], by default 0", type=int)
parser.add_argument('-board', action="store_true", default=False, dest="type_gpio", help="Add me to use GPIO.BOARD type; by default using GPIO.BCM")
parser.add_argument('-get', action="store_true", default=False, dest="get_status", help="Add me to jsut get status gpio pin")

results = parser.parse_args()
MESSAGE="""{{ "type":{TYPE}, "value":{VALUE}, "gpio":{GPIO} }}"""
GPIO.setwarnings(False)
def setupGpio(type):
   mode = GPIO.BCM
   if(type):
	mode = GPIO.BOARD
   GPIO.setmode(mode)

def setupLedPin(pin, mode):
   GPIO.setup(pin, mode)

def actionLed(pin, value):
   GPIO.output(pin, int(value))

def getLedStatus(pin):
   return GPIO.input(pin)

def main(argv):
   type = results.type_gpio
   if(type):
      type = 1
   else:
      type = 0
   gpio = results.gpio_pin
   value = results.value
   setupGpio(type)
   setupLedPin(gpio, GPIO.OUT)

   if(results.get_status):
        message = MESSAGE.format(TYPE=type,VALUE=getLedStatus(gpio),GPIO=gpio)
	print message
	
   else:
        message = MESSAGE.format(TYPE=type,VALUE=value,GPIO=gpio)
	print message
   	actionLed(gpio, value)
   

if __name__ == "__main__":
   main(sys.argv[1:])
