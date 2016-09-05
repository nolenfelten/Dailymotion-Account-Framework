from lib.WriteToLog import WriteToLog
from lib.timer import timer
from lib.Monetization import Monetization
from threading import Thread
from PIL import Image	
from PIL import ImageTk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
class Submit(Thread): 

		
	def __init__(self, log, browser, submit, anwser, robot, email, captcha, bot, url):
		Thread.__init__(self)
		
		self.captcha = captcha
		
		self.browser = browser
		self.submit = submit
		self.log = log
		self.anwser = str(anwser.get())
		self.email = email
		self.robot = robot
		self.bot = bot
		self.url = url
		
		self.start()
		
	def run(self):
		
		def reattempt():
		
			self.submit['text'] = "FAILED"
			WriteToLog(self.log, "[Bot " + str(self.bot + 1) + "]: CAPTCHA Failed")
		
			self.submit['text'] = "Sleep"
			timer(self.submit, 6)

			self.CAPTCHA(self.log, self.bot, self.browser)
			
		
		#Submit
		WriteToLog(self.log, "[Bot " + str(self.bot + 1) + "]: Submittting CAPTCHA " + self.anwser)
		self.browser.find_element_by_xpath('//*[@id="save"]').click()
		
		# Wait
		self.submit['text'] = "Sleep"
		timer(self.submit, 6)

		self.browser.find_element_by_xpath('//*[@id="captchaInput"]').click()
		self.browser.find_element_by_xpath('//*[@id="captchaInput"]').send_keys(self.anwser)
			
		#Submit
		self.browser.find_element_by_xpath('//*[@id="save"]').click()
		timer(self.submit, 3)
			
		try:
			
			self.browser.find_element_by_xpath('//*[@id="cantread"]')
			reattempt()
					
		except:
			self.grab_email()
			
			
	def grab_email(self):

		# Load temp email site
		self.browser.get("https://temp-mail.org/en/option/change")
		
		# New email
		self.browser.find_elements_by_xpath('//*[@id="mail"]')[1].click()
		self.browser.find_elements_by_xpath('//*[@id="mail"]')[1].send_keys(self.email.split("@")[0])
		
		# Submit
		self.browser.find_element_by_xpath('//*[@id="postbut"]').click()
				
		self.verify()
		
		
	def verify(self):
		# Verify Email
		self.browser.get("http://temp-mail.org/en/")
		timer(self.submit, 3)
		
		# Open Emai
		self.browser.find_element_by_partial_link_text("Confirm").click()
		timer(self.submit, 2)

		# Verify Email
		self.browser.find_element_by_partial_link_text("Confirm").click()
		timer(self.submit, 8)
	
		Monetization(log = self.log, submit = self.submit, bot = self.bot, browser = self.browser, email = self.email, url = self.url, robot = self.robot)
	
	def CAPTCHA(self):
			
		# Take Screenshot
		self.browser.save_screenshot("./images/screenshots/screen_" + str(self.bot) + ".png")
		
		# Open Screenshot
		im_temp = Image.open("./images/screenshots/screen_" + str(self.bot) + ".png")

		# Crop Screenshot
		im_temp = im_temp.crop((167, 661, 359, 723))

		# Save CAPTCHA
		im_temp.save("./images/cache/captcha_" + str(self.bot) + ".jpg", "jpeg")
		
		# Load cropped CAPTCHA
		self.photo = ImageTk.PhotoImage(file = "./images/cache/captcha_" + str(self.bot) + ".jpg")

		self.captcha["image"] = self.photo
		
		