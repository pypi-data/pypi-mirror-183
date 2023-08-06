"""
intro:
	A python misc tools for game and other things!
	
class:
	PyMisc()

method:
	createTyper()
	createLoadingBar()
	customExit()
	createBanner()
	
this is BETA VERSION and don't have completed functions :(
"""

__email__ = "<mail@progamedev12@gmail.com>"

import sys,time,os
from pyfiglet import Figlet

class PyMisc:
	def __init__(self, foobar: str=""):
		self.foobar = foobar
	
	def createTyper(self, text: str="", delay: float=0.1):
		for char in text:
			sys.stdout.write(char)
			sys.stdout.flush()
			time.sleep(delay)
			
	def createLoadingBar(self, types: int=2, max: int=100, delay: float=0.3):
		if types == 1:
			# -
			sys.stdout.write("Loading: ")
			for chars in range(max):
				sys.stdout.write("-")
				sys.stdout.flush()
				time.sleep(delay)
			sys.stdout.write(" [✓]\n")
		elif types == 2:
			# =
			sys.stdout.write("Loading: ")
			for chars in range(max):
				sys.stdout.write("=")
				sys.stdout.flush()
				time.sleep(delay)
			sys.stdout.write(" [✓]\n")
		elif types == 3:
			# *
			sys.stdout.write("Loading: ")
			for chars in range(max):
				sys.stdout.write("*")
				sys.stdout.flush()
				time.sleep(delay)
			sys.stdout.write(" [✓]\n")
		else:
			print("Types not valid! [THIS ERROR MESSAGE FROM PyMisc MODULE!]")
			
	def customExit(self, cls: bool=True, isDelayed: bool=True, delay: float=1.0):
		if cls == True and isDelayed == True:
			time.sleep(delay)
			os.system("cls")
			sys.exit()
		elif cls == False and isDelayed == True:
			time.sleep(delay)
			sys.exit()
		elif isDelayed == False and cls == True:
			os.system("cls")
			sys.exit()
		else:
			sys.exit()
			
	def createBanner(self, text: str="", font: str="Larry3D", isDelayed: bool=True, delay: float=1, cls: bool=True):
		if isDelayed == True or cls == True:
			os.system("cls")
			time.sleep(delay)
			print(Figlet(font=font).renderText(text))
		else:
			print(Figlet(font=font).renderText(text))
			
	"""
	This function just for testing :)
	Please ignore this.
	"""
	def oi(self):
		return print(self.foobar)
		
	"""
	END REGION
	"""