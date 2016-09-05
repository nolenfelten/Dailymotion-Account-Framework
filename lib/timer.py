import time


def timer(widget, seconds):
	passed = 0
	for second in range(int(seconds)):
		widget['text'] = "Sleep " + str(int(seconds) - passed)
		time.sleep(1)
		passed += 1