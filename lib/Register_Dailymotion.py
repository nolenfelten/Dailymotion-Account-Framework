from lib.timer import timer
from lib.WriteToLog import WriteToLog
from lib.Submit import Submit
from selenium.webdriver.common.keys import Keys
from PIL import Image	
from PIL import ImageTk


	
class Register_Dailymotion:

	def __init__(self, browser, log, bot, email, password, chanurl, bot_button, anwser, captcha, robot):
		
		# Open dailymotion.com
		browser.get("http://www.dailymotion.com/us")
	
		# Sign up button (top eright)
		browser.find_element_by_css_selector('.sd_header__login').click()
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Open Signup")
	
		# Wait
		timer(bot_button, 6)
	
		# Email
		browser.find_element_by_name("username").send_keys(email)
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Entered Email")
		
		# Sign up button
		browser.find_element_by_xpath("//*[@id='authentication_form_authChoice_register_label']").click()
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Check Signup")
		
		# Submit
		browser.find_element_by_xpath('//*[@id="authentication_form_save"]').click()
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Submit - Window 1 Completed")

		# Wait
		timer(bot_button, 2)
			
		# Password
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Window 2 Start")
		while 1 == 1:
			try:
				browser.find_element_by_xpath('//*[@id="userPassword"]').send_keys(password)
				break
			
			except:	
				continue
				
				
		WriteToLog(log, "[Bot " + str(bot + 1) + "]:  Password Entered")
		# Confirm Password
		browser.find_element_by_xpath("//*[@id='confirm_password']").send_keys(password)
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Password Confirmed Entered - ")
		
		# Birth month
		browser.find_element_by_xpath('//*[@id="select2-chosen-2"]').click()
		browser.find_element_by_css_selector('#select2-drop').send_keys("may" + Keys.RETURN)
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Month Entered")
		timer(bot_button, 1)
		
		# Birth day
		browser.find_element_by_css_selector('#s2id_autogen3 > a:nth-child(1)').click()
		browser.find_element_by_css_selector('#select2-drop').send_keys("13" + Keys.RETURN)
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Day Entered")
		timer(bot_button, 1)
		
		# Birth year
		browser.find_element_by_css_selector('.select2-default').click()
		browser.find_element_by_css_selector('#select2-drop').send_keys("1993" + Keys.RETURN)
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Year Entered")
		timer(bot_button, 1)

		# Clean autofill
		for letter in email.split("@")[0]:
			browser.find_element_by_xpath('//*[@id="publicname"]').send_keys(Keys.BACKSPACE)
			browser.find_element_by_xpath('//*[@id="url"]').send_keys(Keys.BACKSPACE)

		# Channel Username
		e = 0
		public = "s0e" + str(e + 1)
		while 1 == 1:
			
			if browser.find_element_by_xpath('//*[@id="publicname_cont"]/div/div').text == "Public name looks good.":
				break
			else:
				for	letter in range(e):
					browser.find_element_by_xpath('//*[@id="publicname"]').send_keys(Keys.BACKSPACE)
				browser.find_element_by_xpath('//*[@id="publicname"]').send_keys(public)
			
				timer(bot_button, 6)
				
				e += 1
		
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Channel Username Entered - " + public)
		
		# Channel URL
		while 1 == 1:
			
			if browser.find_element_by_xpath('//*[@id="url_cont"]/div/div'):
				# if URL is taken, up the episode number				
				for	letter in "s0e" + chanurl:
					browser.find_element_by_xpath('//*[@id="url"]').send_keys(Keys.BACKSPACE)
				chanurl = chanurl + str(int(chanurl.split("s")[1]) + 1)
				chanurl = str(chanurl)
				browser.find_element_by_xpath('//*[@id="url"]').send_keys("s0e" + str(chanurl))
				timer(bot_button, 2.9)
			
			try:
				if browser.find_element_by_xpath('//*[@id="url_cont"]/div/div').text == "Url available.":
					break
			except:
				continue
				
				
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Channel URL Entered - " + chanurl)
		
		# Set button Text
		bot_button['text'] = "Submit"
		
		# Set button color
		bot_button['bg'] = "#FFFF00"

		self.captcha = captcha
		
		self.CAPTCHA(bot, browser)
		
		self.captcha["image"] = self.photo
		
		# Set the command
		bot_button["command"] = lambda b = browser, s = bot_button, l = log, a = anwser, r = robot, e = email, c = self.captcha, b2 = bot, u = chanurl: robot.submit(log = l, browser = b, submit = s, anwser = a, robot = r, email = e, captcha = c, bot = b2, url = u)
		
		
		
	
	def CAPTCHA(self, bot, browser):
			
		# Take Screenshot
		browser.save_screenshot("./images/screenshots/screen_" + str(bot) + ".png")
		
		# Open Screenshot
		im_temp = Image.open("./images/screenshots/screen_" + str(bot) + ".png")

		# Crop Screenshot
		im_temp = im_temp.crop((167, 661, 359, 723))

		# Save CAPTCHA
		im_temp.save("./images/cache/captcha_" + str(bot) + ".jpg", "jpeg")
		
		# Load cropped CAPTCHA
		self.photo = ImageTk.PhotoImage(file = "./images/cache/captcha_" + str(bot) + ".jpg")

		self.captcha["image"] = self.photo
		
		