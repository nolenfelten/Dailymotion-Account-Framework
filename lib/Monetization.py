from threading import Thread
from lib.WriteToLog import WriteToLog
from lib.timer import timer
from datetime import datetime

class Monetization():

	def __init__(self, log, submit, bot, browser, email, url, robot):
		# Montetization
		submit['text'] = "Money"
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Go to settings")
		browser.get("http://www.dailymotion.com/settings")
		browser.set_window_size(850, 800)
		# Wait
		submit['text'] = "Sleep"
		timer(submit, 30)

		# Ignore tour
		submit['text'] = "Ignore"
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Ignore Tour")
		browser.find_element_by_xpath('//*[@id="popupContent"]/div[2]/div/a[2]').click()
		
		# Wait
		submit['text'] = "Sleep"
		timer(submit, 5)

		# Open Agreement
		submit['text'] = "Agree"
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Enable Monetization")
		browser.find_element_by_xpath('//*[@id="jq-1"]').click()

		# Wait
		submit['text'] = "Sleep"
		timer(submit, 2)

		# Agree
		submit['text'] = "Agree"
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Agree to monetization")
		browser.find_element_by_css_selector('#popupContent > div:nth-child(4) > div:nth-child(1) > a:nth-child(2)').click()
		
		# Wait
		submit['text'] = "Sleep"
		timer(submit, 2)

		# Submit
		submit['text'] = "Submit"
		WriteToLog(log, "[Bot " + str(bot + 1) + "]: Submit Agreement")
		browser.find_element_by_xpath('//*[@id="save"]').click()
				
		ip = requests.get("https://api.ipify.org/").content
		
		date = datetime.now().strftime("%Y/%d/%m")
		
		# Open file
		f = open("./accounts.txt", 'a')
		
		# Write file
		f.write(email + "," + password + "," + url + "," + "True,True,False," + ip + "," + date + "N/A,N/A")

		browser.quit()
		
		submit["command"] = lambda i = bot: robot.grab_captcha(i)