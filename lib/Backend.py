from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
from config import *
from threading import Thread
from lib.WriteToLog import WriteToLog
from lib.Tor import Tor
from lib.Submit import Submit
from lib.Signup import SignUp
import requests



class Backend:

	def __init__(self, widgets):
		
		self.widgets = widgets
		self.log = self.widgets["tab_three"]["log"]
		
		
		
	
	def grab_captcha(self, bot):
		# Write to log
		WriteToLog(self.log, "[Bot " + str(bot + 1) + "]: Starting")
		
		# Change submit button text
		self.widgets["tab_two"]["bot_controllers"][str(bot)]["submit"]["text"] = "Submit"
		
		# Change submit button color
		self.widgets["tab_two"]["bot_controllers"][str(bot)]["submit"]["bg"] = "#FFFF00"
				
		# Change anwser entry state
		self.widgets["tab_two"]["bot_controllers"][str(bot)]['captcha']['state'] = "normal"
		
		# Port numbers
		self.sock = int(self.widgets["tab_three"]["socks"].get()) + bot
		self.ctrl = int(self.widgets["tab_three"]["ctrl"].get()) + bot
		self.tor = bool(self.widgets["tor"].get())
		
				
		# Image Label
		self.captcha = self.widgets["tab_two"]["bot_controllers"][str(bot)]['img']
		
		# Submit
		self.submit = self.widgets["tab_two"]["bot_controllers"][str(bot)]["submit"]
		
		# CAPTCHA Anwser
		self.anwser = self.widgets["tab_two"]["bot_controllers"][str(bot)]["captcha"]
		
		self.robot = self.widgets["tab_two"]["bot_controllers"][str(bot)]["robot"]
		
		self.init = Thread(target = SignUp(log = self.log, bot = bot, tor = self.tor, ctrl = self.ctrl, sock = self.sock, captcha = self.captcha, submit = self.submit, anwser = self.anwser, robot = self.robot))
		
		
	def submit(self, log, browser, submit, anwser, robot, email, captcha, bot, url):
		#b = browser, s = bot_button, l = log, a = anwser, e = email, c = self.captcha, b2 = bot, u = chanurl
		self.init = Thread(target = Submit(log, browser, submit, anwser, robot, email, captcha, bot, url))
		
	