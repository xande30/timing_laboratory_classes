#demonstrating classes using a lab test

import sys
from termcolor import colored, cprint
from colorama import Fore


class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'


reset = '\033[0m'
bold = '\033[01m'
disable = '\033[02m'
underline = '\033[04m'
reverse = '\033[07m'
strikethrough = '\033[09m'
invisible = '\033[08m'

def two_digits(val):
	s = str(val)
	if len(s) == 1:
		s = '0' + s
	return s

class Timing:
	def __init__(self, hours=0, minutes=0, seconds=0):
		self.__hours = hours
		self.__minutes = minutes
		self.__seconds = seconds

	def __str__(self):
		return two_digits(self.__hours) +  ":" + two_digits(self.__minutes) + ":" + two_digits(self.__seconds)

	def next_second(self):
		self.__seconds += 1
		if self.__seconds > 59:
			self.__seconds = 0
			self.__minutes += 1
			if self.__minutes > 59:
				self.__minutes = 0
				if self.__hours > 23:	
					self.__hours = 0
	def prev_second(self):
		self.__seconds -= 1
		if self.__seconds < 0:
			self.__seconds = 59
			self.__hours -= 1
			if self.__hours < 0:
				self.__hours = 23


#text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
#print(text)

text = Timing(23,59,59)
print(colored("The Time Is: ","red", attrs=["reverse","blink"]),text)
text.next_second()
print(colored("The Time Is: ","yellow", attrs=["reverse","blink"]),text)
text.prev_second()
print(colored("The Time Is: ","blue", attrs=["reverse","blink"]),text)

print("***" "+" "THE END" "+" "***")
