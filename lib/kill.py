from os import system

def kill(root):
	system("taskkill /im phantomjs.exe /f")

	system("taskkill /im firefox.exe /f")
	
	system("taskkill /im tor.exe /f")

	root.quit()
		