from lib.WriteToLog import WriteToLog
from lib.timer import timer

def confirm_email(log, submit, browser, bot, email):

	# Take Screenshot
	browser.save_screenshot("./images/screenshots/screen_" + str(bot) + ".png")
	
	# Verify Email
	submit['text'] = "Get Email"
	WriteToLog(log, "[Bot " + str(bot + 1) + "]: Go to temp-mail.org")
	browser.get("https://temp-mail.org/")
	
	browser.get("https://temp-mail.org/en/option/refresh")

	# Wait
	submit['text'] = "Sleep 15"
	timer(submit, 15)
	
	# Open Email
	submit['text'] = "Open Email"
	WriteToLog(log, "[Bot " + str(bot + 1) + "]: Open Email")
	browser.find_element_by_link_text("Confirm your email addres").click()
	
	# Wait
	submit['text'] = "Sleep"
	timer(submit, 3)

	# Verify Email
	submit['text'] = "Confirm"
	WriteToLog(log, "[Bot " + str(bot + 1) + "]: Confirm link")
	browser.find_element_by_link_text("Confirm your email address").click()