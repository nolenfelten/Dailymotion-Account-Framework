from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
from config import *
from datetime import datetime
from lib.timer import timer
from lib.Firefox import firefox
import time
from lib.confirm_email import confirm_email
from lib.Monetization import Monetization
from lib.Register_Dailymotion import Register_Dailymotion
from lib.WriteToLog import WriteToLog

'''
	This enters the information to register and returns CAPTCHA 
'''

class SignUp(Thread):

	def __init__(self, log, bot, tor, ctrl, sock, captcha, submit, anwser, robot):
		# Initialize Thread
		Thread.__init__(self)
		
		self.log = log
		self.bot = bot
		self.tor = tor
		self.ctrl = ctrl
		self.sock = sock
		self.captcha = captcha
		self.submit = submit
		self.anwser = anwser
		self.robot = robot
		
		# Start Thread
		self.start()
		
		
	def run(self):
		
		# Started Thread
		WriteToLog(self.log, "[Bot " + str(self.bot + 1) + "]: Started Thread")
		self.submit['bg'] = "#CCCCCC"
								
		# Email
		self.email = str(time.time() + self.bot).split(".")[0] + "@lackmail.ru"
		WriteToLog(self.log, "[Bot " + str(self.bot + 1) + "]: " + self.email)
		
		# Browser
		self.submit['text'] = "Starting"
		self.browser = firefox(self.tor, self.sock + self.bot)
		
		self.browser.set_window_size(550, 1080)
		WriteToLog(self.log, "[Bot " + str(self.bot + 1) + "]: Started Firefox")

		'''# Loops until a CAPTCHA is returned then stops and waits for user to submit.
		try:
		'''
		# Register account at Dailymotion
		self.r = Register_Dailymotion(log = self.log, bot = self.bot, browser = self.browser, email = self.email, password = password, chanurl = "s0", bot_button = self.submit, anwser = self.anwser, captcha = self.captcha, robot = self.robot)

		
		'''except:
			
			# Kill Browser
			self.browser.quit()
			
			# Run again
			self.run()
	'''