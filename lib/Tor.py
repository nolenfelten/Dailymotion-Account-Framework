from psutil import process_iter
from psutil import AccessDenied
from stem import Signal
from stem.process import launch_tor_with_config
from stem.control import Controller
from subprocess import check_output
from threading import Thread
from os import makedirs
from os import getcwd
from os import path
import time
from threading import Thread
from lib.WriteToLog import WriteToLog

class Tor(Thread):

	def __init__(self, sock, ctrl, log):
		# Initialize Thread
		Thread.__init__(self)

		# Store Variables in dictonary
		kwargs = {"sock": sock, "ctrl": ctrl, "log": log}
		self.args = kwargs

		# Daemonize Thread. Thread will stop on when window is closed
		self.daemon = True

		# Launchs run() function
		connection = self.start()


	def run(self):
		# Launch Tor
		return self.proxy(**self.args)


	def proxy(self, sock, ctrl, log):
		# Create Tor Connection Object
		torConnColl = TorConnectionCollector(sock, ctrl, log)

		self.torConn = torConnColl.getFreeConnection()

		return self.torConn


# TorConnection - Contains Controller And Subprocess
class TorConnection(object):

	def __init__(self, sock, ctrl, log):

		# Store arguments in object variable
		self.__isFree = False
		self.__socksPort = sock
		self.__ctrlPort = ctrl
		self.__torConfig = None
		self.__torProcess = None
		self.__torCtrl = None
		self.__proxies = None
		self.__lastTimeIpChanged = 0
		self.log = log

		# Run Thread
		self.start()


	def start(self):
		# Cache Folder
		cache_folder = path.join(getcwd() + "\\cache", str(self.__socksPort))

		# Make a folder for Tor thread's cache, if their is not one already
		if not path.exists(cache_folder):
			makedirs(cache_folder)

		self.password = check_output([path.join(getcwd() + "\\lib\\", "tor.exe"), "--hash-password", 'lol']).strip().split("\n")[-1]
		# Create Configuration Dictionary
		self.__torConfig = {
			"ControlPort": str(self.__ctrlPort),
			"HashedControlPassword": self.password,
			"ExcludeNodes": "{CN},{HK},{MO}",
			"SOCKSPort": str(self.__socksPort),
			"DataDirectory": cache_folder
		}

		# IP:Port
		IP_Port = "127.0.0.1" + ":" + str(self.__socksPort)

		# Create Proxy String
		self.__proxies = {
			"http": "socks5://" + IP_Port,
			"https": "socks5://" + IP_Port
		}

		# Open Tor Process
		self.open_tor()

		# The Tor Connection Is Now Ready To Use
		self.__isFree = True

		# Up And Running Message
		WriteToLog(self.log, self.getId() + "  ->  Up & Running!")



	def open_tor(self):
		def Log(msg):
			WriteToLog(self.log, msg)
		# Open Tor Process
		opened = False

		while opened == False:
				# Launch Tor
				self.__torProcess = launch_tor_with_config(config = self.__torConfig, tor_cmd = path.join(getcwd() + "\\lib\\", "tor.exe"), init_msg_handler = Log)
				self.__torProcess.stdout.close()

				opened = True

		if not opened:
			# Terminate
			self.__torProcess.terminate()

		# Open Tor Control
		self.__torCtrl = Controller.from_port(address = "127.0.0.1", port = self.__ctrlPort)

		# Send Control the Password
		self.__torCtrl.authenticate('lol')


	def id(self):
		# Signal the command to change identity
		self.__torCtrl.signal(Signal.NEWNYM)

		timedOut = False

		# Reset if botentity change timed out.
		if timedOut:
			self.reset()

		# Output Tor IP address to log
		WwriteToLog("Tor IP Address - " + requests.get("https://api.ipify.org/", proxies = self.__proxies, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}).content)

		return True


	def reset(self):
		# Kill All
		self.kill()

		# Start All
		self.open_tor()

		# Inform
		WriteToLog(self.getId() + " ->  Up & Running After Reset!")


	def kill(self):
		# Kill Tor
		self.__torCtrl.close()

		self.__torProcess.terminate()


	def changeState(self):
		# Return False if port is already in use
		self.__isFree = not self.__isFree


	def isFree(self):
		return self.__isFree


	def getId(self):
		return "[Port " + str(self.__socksPort) + "] "



# TorConnectionCollector - Sends Free TorConnection To The Thread Function
class TorConnectionCollector(object):

	def __init__(self, sock, ctrl, log):
		# Create Tor Object
		self.__torCons = TorConnection(sock, ctrl, log)


	def getFreeConnection(self):
		while True:
			if self.__torCons.isFree():
				self.__torCons.changeState()

				return self.__torCons


	def killConnections(self):
		self.__torCons.kill()


class Deploy_Bot(Thread):

	def __init__(self, widgets, use_tor, log, bot, spreadsheet):
		# Initialize thread
		Thread.__init__(self)

		# Daemonize thread
		self.daemon = True


		# Log widgets
		self.log = log

		# Bot ID
		self.bot = bot

		# Spreadsheet frame
		self.spreadsheet = spreadsheet

		# Store Thread Dictonary
		self.widgets = widgets

		# Halt thread and destroy widgets
		self.widgets["stop"]["command"] = lambda: self.stop()

		# Submit Button Yellow
		self.widgets['submit']['bg'] = "#FFFF00"

		# Pack widgets
		self.packit()

		# Start run()
		self.start()


