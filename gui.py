from io import BytesIO
from PIL import ImageTk
from PIL import Image
from os import makedirs
from os import getcwd
from os import path
from os import system
from psutil import process_iter
from psutil import AccessDenied
from re import findall
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
from stem import Signal
from stem.process import launch_tor_with_config
from stem.control import Controller
from subprocess import check_output
from tkinter import ttk
from threading import Thread
import requests
import time
import tkinter as tk
import tkinter.scrolledtext


class GUI():

	def __init__(self):
	
		# Create Master Widget
		self.root = tk.Tk()
		self.root.title("Dailymotion Account Framework - NolenFelten.com")
		self.root.state('zoomed')	# Maximize Window
	
		# Screenshot viewer
		self.viewer = tk.StringVar()
		self.viewer.set("Bot 1")
	
		# Browser Choice
		self.browser_setting = tk.StringVar()
		self.browser_setting.set("PhantomJS")
	
		# Tor Boolean
		self.use_tor = tk.BooleanVar()
		self.use_tor.set(False)
	
		# Tor SOCKS port
		self.socks_port = tk.IntVar()
		self.socks_port.set("9050")
	
		# Tor Control Port
		self.ctrl_port = tk.IntVar()
		self.ctrl_port.set("5050")
	
		dailymotion = ImageTk.PhotoImage(Image.open("./images/logo.jpg"))
		author = "Made in USA by Nolen Felten - NolenFelten.com - nolenf@gmail.com"
		title = "Account Management Framework"
	
	
		# 						Widget Dictonary Index
	
		#  		Key													Value
		 
		# header											Header [Frame]
		# logo												Dailymotion Image [Label]
		# title												Title Heading [Label]
		# gif												USA Hack [Label]
		# author											Author Information [Label]
		# status											Tor/Browser Settings Status [Label]
	
		# tabs												Notebook Object [Notebook]
		# tab_1												Tab 1 Frame
		# tab_2												Tab 2 Frame
		# tab_3												Tab 3 Frame
	
		# tab_one -> canvas									Spreadsheet Canvas [Canvas]
		# tab_one -> canvas_frame							Canvas Frame [Frame]
		# tab_one -> vsb									Spreadsheet Scrollbar [Scrollbar]
	
		# tab_two -> bots_amount_label						Number of bots to create [Label]
		# tab_two -> bots_amount							Number of bots to create [Entry]
		# tab_two -> bots_button							Start [Button]
		# tab_two -> bot_header_frame						Header [Frame]
		# tab_two -> bot_header_string						Header String [Label]
		# tab_two -> bot_amount_entry						Bot Amount [Entry]
		# tab_two -> start_button							Start button [Button] 
		# tab_two -> stop_all_button						Stop All Button [Button]
		# tab_two -> thread_grid							Thread container [Frame]

		# tab_three -> enable_tor							Tor [Frame]
		# tab_three -> browser_frame						Select Browser [Frame]
		# tab_three -> tor_ports							Tor Port Settings [Frame]
		# tab_three -> brower_menu							Select Browser Drop Down Menu [Optionsmenu]
		# tab_three -> tor									Tor Image [Label]
		# tab_three -> tor_label							"Use Tor:" [Label]
		# tab_three -> tor_false							Tor = False [RadioButton]
		# tab_three -> tor_true								Tor = True [RadioButton]
		# tab_three -> socks_frame							Tor Socks Port [Frame]
		# tab_three -> socks_label							Tor Socks Port [Label]
		# tab_three -> socks								Tor Socks Port Input Field [Entry]
		# tab_three -> ctrl_frame							Tor Control Port Frame [Frame]
		# tab_three -> ctrl_label							Tor Control Port [Label]
		# tab_three -> ctrl									Tor Control Port Input Field [Entry]
	
	
		# Store widgets in a dictonary for easy access
		self.widgets = {
			"threads": [],
			"browser_setting": self.browser_setting,
			"use_tor": self.use_tor,
			"socks_port": self.socks_port,
			"ctrl_port": self.ctrl_port,
			"header": tk.Frame(self.root, relief = "groove", borderwidth = 6, bg = "#000000"),
			"tabs": ttk.Notebook(self.root),
			"tab_1": tk.Frame(),
			"tab_2": tk.Frame(),
			"tab_3": tk.Frame(),
			"tab_one": {},
			"tab_two": {},
			"tab_three": {}
		}
	
	
		# Tab 3 Log Box
		self.widgets["tab_three"]["log"] = tkinter.scrolledtext.ScrolledText(self.widgets["tab_3"], undo = True)

	
		# Start Log
		self.writeToLog("Creating Header Widgets")

		# Logo
		self.widgets["logo"] = tk.Label(self.widgets["header"], image = dailymotion, bg = "#000000")
	
		# Title Heading
		self.widgets["title"] = tk.Label(self.widgets["header"], font = ("Verdana", 30), bg = "#000000")				
	
		# USA Hack
		self.widgets["gif"] = AnimatedGif(self.widgets["header"], "./images/made_in_usa.gif", 0.05)	
	
		# Author Information
		self.widgets["author"] = tk.Label(self.widgets["header"], font = ("Helvetica", 13), bg = "#000000", fg = "#FFFFFF")
	
		# Tor/Browser Settings Status
		self.widgets["status"] = tk.Label(self.widgets["header"], font = ("Helvetica", 12), bg = "#000000")				
	
		# Clock
		self.widgets["clock"] = tk.Label(self.widgets["header"], font = ("Times", 17), borderwidth = 2, relief = "groove", bg = "#000000") 
	
		# Done Header
		self.writeToLog("Done")
	
	
	
	
		# Log Tab 1
		self.writeToLog("Creating Tab 1 Spreadhsheet")
	
		# Tab 1 Spreadsheet Canvas
		self.widgets["tab_one"]["canvas"] = tk.Canvas(self.widgets["tab_1"], borderwidth = 2, height = 900, width = 625)
	
		# Tab 1 Spreadsheet Canvas Frame
		self.widgets["tab_one"]["canvas_frame"] = tk.Frame(self.widgets["tab_one"]["canvas"])		
		self.widgets["tab_one"]["canvas"].create_window((0,0), window = self.widgets["tab_one"]["canvas_frame"], anchor = "nw", tags = 'self.widgets["tab_one"]["canvas_frame"]')
	
		# Tab 1 Scroll Bar	
		self.widgets["tab_one"]["vsb"] = tk.Scrollbar(self.widgets["tab_1"], orient = "vertical", command = self.widgets["tab_one"]["canvas"].yview)
	
		# Create the spreadsheet
		self.populate_spreadsheet()
	
		# Done Tab 1 Log
		self.writeToLog("Done")
	
	
	
	
		# Log Tab 2
		self.writeToLog("Creating Tab 2 Widgets")
	
		# Tab 2 Bot Controller Header
		self.widgets["tab_two"]["bot_header_frame"] = tk.LabelFrame(self.widgets["tab_2"], borderwidth = 3)
	
		# Tab 2 Label String
		self.widgets["tab_two"]["bot_header_string"] = tk.Label(self.widgets["tab_two"]["bot_header_frame"], text = "Enter amount of bots to spawn: ")
	
		# Tab 2 Bot Entry Widget
		self.widgets["tab_two"]["bot_amount_entry"] = tk.Entry(self.widgets["tab_two"]["bot_header_frame"])
	
		# Tab 2 Start Bots Button
		self.widgets["tab_two"]["start_button"] = tk.Button(self.widgets["tab_two"]["bot_header_frame"], text = "Start", command = lambda: self.start())
	
		# Tab 2 Stop Bots Button
		self.widgets["tab_two"]["stop_all_button"] = tk.Button(self.widgets["tab_two"]["bot_header_frame"], text = "Stop All", state = 'disabled', command = lambda: self.stop_all())
	
		# Tab 2 Thread Container
		self.widgets["tab_two"]["thread_grid"] = tk.Frame(self.widgets["tab_2"], borderwidth = 2)
	
		# Log Tab 2 Done
		self.writeToLog("Done")
	
	
	
	
		# Tab 3 Log
		self.writeToLog("Creating Tab 3 Widgets")
	
		# Tab 3 "Enale Tor" Frame
		self.widgets["tab_three"]["enable_tor"] = tk.LabelFrame(self.widgets["tab_3"], borderwidth = 2)
	
		# Tab 3 Tor image object
		self.widgets["tab_three"]["tor_image"] = ImageTk.PhotoImage(Image.open("./images/tor-logo.png"))

		# Tab 3 Tor image Label
		self.widgets["tab_three"]["tor"] = tk.Label(self.widgets["tab_three"]["enable_tor"], image = self.widgets["tab_three"]["tor_image"])
		self.widgets["tab_three"]["tor"]["image"] = self.widgets["tab_three"]["tor_image"]
	
		# Tab 3 "Use Tor:" Label
		self.widgets["tab_three"]["tor_label"] = tk.Label(self.widgets["tab_three"]["enable_tor"], text = "Use Tor:")

		# Tab 3 Tor True Button
		self.widgets["tab_three"]["tor_true"] = tk.Radiobutton(self.widgets["tab_three"]["enable_tor"], text = "True", variable = self.use_tor, value = True, command = lambda: self.update())
	
		# Tab 3 Tor False Button
		self.widgets["tab_three"]["tor_false"] = tk.Radiobutton(self.widgets["tab_three"]["enable_tor"], text = "False", variable = self.use_tor, value = False, command = lambda: self.update())
	
		# Tab 3 Tor Port Settings LabelFrame
		self.widgets["tab_three"]["tor_ports"] = tk.LabelFrame(self.widgets["tab_3"], labelanchor = 'nw', text = "Tor Settings:")
	
		# Tab 3 Tor SOCKS Settings Frame
		self.widgets["tab_three"]["socks_frame"] = tk.Frame(self.widgets["tab_3"])

		# Tab 3 Tor SOCKS Settings Label
		self.widgets["tab_three"]["socks_label"] = tk.Label(self.widgets["tab_three"]["socks_frame"], text = "Socks Port: ")
	
		# Tab 3 Tor SOCKS Settings Entry
		self.widgets["tab_three"]["socks"] = tk.Entry(self.widgets["tab_three"]["socks_frame"], textvariable = self.socks_port, width = 4)
	
		# Tab 3 Tor CTRL Settings Frame
		self.widgets["tab_three"]["ctrl_frame"] = tk.Frame(self.widgets["tab_3"])
	
		# Tab 3 Tor CTRL Settings Label
		self.widgets["tab_three"]["ctrl_label"] = tk.Label(self.widgets["tab_three"]["ctrl_frame"], text = "Control Port: ")

		# Tab 3 Tor CTRL Settings Entry
		self.widgets["tab_three"]["ctrl"] = tk.Entry(self.widgets["tab_three"]["ctrl_frame"], textvariable = self.ctrl_port, width = 4)

		# Tab 3 Browser Settings Frame
		self.widgets["tab_three"]["browser_frame"] = tk.LabelFrame(self.widgets["tab_3"], text = "Select Browser:", labelanchor = 'n')

		# Tab 3 Browser Settings Menu
		self.widgets["tab_three"]["brower_menu"] = tk.OptionMenu(self.widgets["tab_three"]["browser_frame"], self.browser_setting, *["Firefox", "PhantomJS"], command = lambda x: self.update())
		self.widgets["tab_three"]["brower_menu"].config(width = 14)
	
		# Log Tab 3 Done
		self.writeToLog("Done")
	
	
	
	
		# Header Variables
		self.widgets["logo"]["image"] = dailymotion
		self.widgets["title"]["text"] = title
		self.widgets["author"]["text"] = author
	
		self.red = 1
		self.green = 1
		self.blue = 1
		self.seq = 1
	
	
	
	
		# Pack Header Widgets
		self.writeToLog("Packing Header Widgets")
	
		self.widgets["logo"].pack(side = "left", ipady = 4, padx = 80)							# Root Logo
		self.widgets["title"].pack(pady = 28, ipadx = 71, anchor = "ne")						# Root Title
		self.widgets["author"].pack(side = "right", anchor = "se")								# Root Author
		self.widgets["gif"].pack(side = "right", anchor = "se")									# Root GIF
		self.widgets["status"].place(x = 260, rely = 0.89, anchor = "center")					# Root Status
		self.widgets["header"].pack(side = "top", anchor = "nw", fill = "both")					# Root Header
		self.widgets["clock"].place(x = 42, y = 16, anchor = "center")							# Root Clock
	
		self.writeToLog("Done")
	
	
	
	
		# Add Tabs to Notebook
		self.writeToLog("Packing and Adding Tabs")
	
		self.widgets["tabs"].pack(fill = 'both')												# Root Notebook
		self.widgets["tabs"].add(self.widgets["tab_1"], text = "Accounts")						# Add Tab 1
		self.widgets["tabs"].add(self.widgets["tab_2"], text = "Create Accounts")				# Add Tab 2
		self.widgets["tabs"].add(self.widgets["tab_3"], text = "Settings")						# Add Tab 3
	
		self.writeToLog("Done")
	
	
	
	
		# Pack Tab 1
		self.writeToLog("Packing Tab 1 Widgets")
	
		self.widgets["tab_one"]["vsb"].pack(side = "right", fill = "y")							# Tab 1 Spreadsheet Scrollbar
		self.widgets["tab_one"]["canvas"].pack(side = "left", fill = "both", expand = True)		# Tab 1 Spreadsheet Canvas
	
		self.writeToLog("Done")
	
	
	
	
		# Pack Tab 2
		self.writeToLog("Packing Tab 2 Widgets")
	
		self.widgets["tab_two"]["bot_header_frame"].pack(fill = "x", side = 'top')				# Tab 2 Header
		self.widgets["tab_two"]["bot_header_string"].pack(anchor = "center", side = 'left')		# Tab 2 Header String
		self.widgets["tab_two"]["bot_amount_entry"].pack(anchor = "center", side = "left")		# Tab 2 Bot Amount Entry
		self.widgets["tab_two"]["start_button"].pack(side = "left")								# Tab 2 Start buttpm 
		self.widgets["tab_two"]["stop_all_button"].pack(side = "left")							# Tab 2 Stop All Button
		self.widgets["tab_two"]["thread_grid"].pack(anchor = "nw")								# Tab 2 Thread container

		self.writeToLog("Done")

	
	
	
		# Pack Tab 3
		self.writeToLog("Packing Tab 3 Widgets")
	
		self.widgets["tab_three"]["log"].pack(expand = True, fill = 'both', side = "right")			# Tab 3 Debug Log Text Box
		self.widgets["tab_three"]["enable_tor"].pack(anchor = 'nw')									# Tab 3 Enable Tor Frame
		self.widgets["tab_three"]["browser_frame"].pack(anchor = 'w')								# Tab 3 Select Browser Frame
		self.widgets["tab_three"]["tor_ports"].pack(side = "left", anchor = 'nw')					# Tab 3 Tor Port Settings Frame
		self.widgets["tab_three"]["brower_menu"].pack()												# Tab 3 Select Browser Drop Down Menu
		self.widgets["tab_three"]["tor"].pack(side = "top", anchor = 'n')							# Tab 3 Tor Image
		self.widgets["tab_three"]["tor_label"].pack(anchor = 's')									# Tab 3 "Use Tor:" Label
		self.widgets["tab_three"]["tor_false"].pack(side = "right", anchor = 's')					# Tab 3 Tor = False Radio Button
		self.widgets["tab_three"]["tor_true"].pack(side = "left", anchor = 's')						# Tab 3 Tor = True Radio Button
		self.widgets["tab_three"]["socks_frame"].pack(anchor = 'nw')								# Tab 3 Tor Socks Port Frame
		self.widgets["tab_three"]["socks_label"].pack(side = "left", padx = 15)						# Tab 3 Tor Socks Port Label
		self.widgets["tab_three"]["socks"].pack(side = "right")										# Tab 3 Tor Socks Port Input Field
		self.widgets["tab_three"]["ctrl_frame"].pack(anchor = 'nw')									# Tab 3 Tor Control Port Frame
		self.widgets["tab_three"]["ctrl_label"].pack(side = "left", padx = 10)						# Tab 3 Tor Control Port Label
		self.widgets["tab_three"]["ctrl"].pack(side = "right")										# Tab 3 Tor Control Port Input Field
	
		self.writeToLog("Done")
	
	
	
		self.writeToLog("Starting GIF Animation")
		self.widgets["gif"].start()																# Start Header GIF
	
		# quit if the window is deleted
		self.root.protocol("WM_DELETE_WINDOW", self.root.quit)
		self.update()
	
		# Start GUI
		self.writeToLog("Started Application! :)\n")
	

		self.root.mainloop()
	

	
	def update(self):
		hex_array = ["14","28","3C","5F","60","78","8C","A0","B4","Cf","DF","DF","F0"]
		product = "#" + hex_array[self.red] + hex_array[self.green] + hex_array[self.blue]

		if self.seq == 6:
			self.blue -= 1
			if self.blue == 0:
				self.seq = 1


		if self.seq == 5:
			self.red += 1
			if self.red == 12:
				self.seq = 6


		if self.seq == 4:
			self.green -= 1
			if self.green == 0:
				self.seq = 5


		if self.seq == 3:
			self.blue += 1
			if self.blue == 12:
				self.seq = 4

	
		if self.seq == 2:
			self.red -= 1
			if self.red == 0:
				self.seq = 3

	
		if self.seq == 1:
			self.green += 1
			if self.green == 12:
				self.seq = 2
	
		
		self.widgets["clock"]["fg"] = product
		self.widgets["title"]["fg"] = product
		self.widgets["status"]["fg"] = product

	
		self.widgets["clock"]["text"] = time.strftime('%H:%M:%S')
		self.widgets["status"]['text'] = "Tor: " + str(self.use_tor.get()) + "  |  Browser: " + self.browser_setting.get()
	
		self.root.after(20, self.update)

	
	def open_accounts(self, file = "./accounts.txt"):
		# Return Array of Accounts
		return open(file, 'r').read().split("\n")

	
	def onFrameConfigure(self, event):
		# Reset the scroll region to encompass the inner frame
		self.widgets["tab_one"]["canvas"].configure(scrollregion = self.widgets["tab_one"]["canvas"].bbox("all"))

	
	def populate_spreadsheet(self):
		# Tab 1 Store cell cordinates (A1, B3, D2, etc) inside a dictonary for organizing
		self.spreadsheet_cords = {}
	
		# Tab 1 Spreadsheet Headers
		self.colum_headers = ["", 'Email', 'Password', 'URL', 'Email', 'Monetization', 'Banking']
	
		# Tab 1 Populate spreadsheet with account data
		for row in range(len(open("./accounts.txt", "r").read().split("\n")) + 1):		# Create a row for each account in accounts.txt
			for col in range(len(self.colum_headers)):									# Crate a column for each Header
	
				# Colum 0 is where each row is numbered/labeled
				if col == 0:
		
					# Colum 0 on Row 0 is where the headeres are placed, so we create an empty Label.
					if row == 0:
						cell = tk.Label(self.widgets["tab_one"]["canvas_frame"], width = 3)
						cell.grid(row = row, column = col, padx = 1, pady = 1)
			
					else:
						cell = tk.Label(self.widgets["tab_one"]["canvas_frame"], width = 3, text = str(row))
						cell.grid(row = row, column = col, padx = 1, pady = 1)
	
	
				elif row == 0:
					cell = tk.Label(self.widgets["tab_one"]["canvas_frame"], text = self.colum_headers[col])
					cell.grid(row = row, column = col, padx = 1, pady = 2)		    
	
	
				else:
					if col < 4:
						if col == 1:
							entry1 = tk.Entry(self.widgets["tab_one"]["canvas_frame"], width = 23)
				
						elif col == 2:
							entry1 = tk.Entry(self.widgets["tab_one"]["canvas_frame"], width = 5, show = "*")
				
						else:
							entry1 = tk.Entry(self.widgets["tab_one"]["canvas_frame"], width = 10)
			
						# place the object
						entry1.grid(row = row, column = col, padx = 1)  #, padx = 2, pady = 2)
			
			
						# create a dictionary of cell:object pair
						cell = self.colum_headers[col] + str(row)
			
						self.spreadsheet_cords[cell] = entry1
			
						entry1.insert(0, open("./accounts.txt", "r").read().split("\n")[row - 1].split("	")[col - 1])
		
					else:
						entry1 = tk.Entry(self.widgets["tab_one"]["canvas_frame"], width = 2)
			
						# place the object
						entry1.grid(row = row, column = col)  #, padx = 2, pady = 2)
			
						# create a dictionary of cell:object pair
						cell = self.colum_headers[col] + str(row)
			
						self.spreadsheet_cords[cell] = entry1
			
			
						if open("./accounts.txt", "r").read().split("\n")[row - 1].split("	")[col - 1]:
							entry1.insert(0, open("./accounts.txt", "r").read().split("\n")[row - 1].split("	")[col - 1])
							entry1['bg'] = "green"
							entry1['fg'] = "blue"
			
						else:
							entry1['bg'] = "red"
		global account_index
		account_index = len(open("./accounts.txt", "r").read().split("\n")) + 1
	
		# Bind scrollbar to canvas and frame
		self.widgets["tab_one"]["canvas"].configure(yscrollcommand = self.widgets["tab_one"]["vsb"].set)
		self.widgets["tab_one"]["canvas_frame"].bind("<Configure>", self.onFrameConfigure)


	def writeToLog(self, msg):
		numlines = self.widgets["tab_three"]["log"].index('end - 1 line').split('.')[0]

		if numlines == 24:
			self.widgets["tab_three"]["log"].delete(1.0, 2.0)
		if self.widgets["tab_three"]["log"].index('end-1c') != '1.0':
			self.widgets["tab_three"]["log"].insert('end', '\n')
	
		self.widgets["tab_three"]["log"].insert('end', time.ctime() + ": " + msg)


	def start(self):
		# Store the bots in a dictonary
		# bot_id -> bot_widgets
		self.threads = {}

		img = Image.open("./images/dmcaptcha.png")
	
		start_img = ImageTk.PhotoImage(img)

		# Start Tor
		if self.use_tor.get():
			self.writeToLog("Starting Tor Service")
			kwargs = {"log": self.widgets["tab_three"]["log"], "sock": self.widgets["socks_port"], "ctrl": self.widgets["ctrl_port"]}
			Tor.Tor(**kwargs)
	
		self.amount = self.widgets["tab_two"]["bot_amount_entry"].get()
	
		# Change entry state
		self.widgets["tab_two"]["bot_amount_entry"]["state"] = "disabled"

		# Change Start Button state
		self.widgets["tab_two"]["start_button"]["state"] = "disabled"

		# Change Stop Button state
		self.widgets["tab_two"]["stop_all_button"]["state"] = "active"
	
	
		# Create ___ amount of threads from user entry
		self.writeToLog("Starting " + self.amount + " Bots")
		for bot in range(int(self.widgets["tab_two"]["bot_amount_entry"].get())):

			# Create dictonary of thread widgets to store in
			self.threads["thread_" + str(bot)] = {}

			# Thread Frame
			self.threads["thread_" + str(bot)]["frame"] = tk.LabelFrame(self.widgets["tab_two"]["thread_grid"], borderwidth = 3, relief = "groove", labelanchor = "n", text = "Bot " + str(bot + 1) + ":")

			# Thread Image Label
			self.threads["thread_" + str(bot)]["img"] = tk.Label(self.threads["thread_" + str(bot)]["frame"], image = start_img)
			self.threads["thread_" + str(bot)]["img"].image = start_img

			# CAPTCHA Answer 
			self.threads["thread_" + str(bot)]["captcha"] = tk.Entry(self.threads["thread_" + str(bot)]["frame"], state = "disabled")

			# Submit Button
			self.threads["thread_" + str(bot)]["submit"] = tk.Button(self.threads["thread_" + str(bot)]["frame"], state = "disabled", font = ("Helvetica", 8), width = 6, text = "Submit")

			# Stop Button
			self.threads["thread_" + str(bot)]["stop"] = tk.Button(self.threads["thread_" + str(bot)]["frame"], text = "Stop", font = ("Helvetica", 8), width = 6, bg = "#FF0000")


			# Start bot
			Thread(target = Deploy_Bot(self.threads["thread_" + str(bot)], self.widgets["use_tor"], self.widgets["tab_three"]["log"], bot, self.widgets["tab_one"]["canvas_frame"]))


	def stop_all(self):
		self.writeToLog("Pressed Stop Button, Halting Threads")
	
		# Set the start button to active
		self.widgets["tab_two"]["start_button"]["state"] = "normal"
	
		# Set the entry widget to active
		self.widgets["tab_two"]["bot_amount_entry"]["state"] = "normal"

		# Set the stop button to disabled
		self.widgets["tab_two"]["stop_all_button"]["state"] = "disabled"
	
		# For each bot running, destroy the widgets
		for bot in self.threads:
			for x in self.threads[str(bot)]:
				self.threads[str(bot)][x].destroy()

				if str(self.widgets["browser_setting"].get()) == "PhantomJS":
					try:
						system("taskkill /im phantomjs.exe /f")
		
					except:
						system("killall -9 phantomjs")
		
				else:
					try:
						system("taskkill /im firefox.exe /f")
	
					except:
						system("killall -9 firefox-bin")
		self.widgets["threads"].join()
		self.writeToLog("Done")
	
	
class Tor(Thread):

	def __init__(self, sock, ctrl, log):
		# Initialize Thread
		threading.Thread.__init__(self)
	
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
		self.writeToLogg(time.ctime() + ": " + self.getId() + "  ->  Up & Running!")
	
	
	
	def open_tor(self):
		# Open Tor Process
		opened = False
	
		while opened == False:
				# Launch Tor
				self.__torProcess = launch_tor_with_config(config = self.__torConfig, tor_cmd = path.join(getcwd() + "\\lib\\", "tor.exe"), init_msg_handler = self.writeToLogg)
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
	
		# Reset if identity change timed out.
		if timedOut:
			self.reset()
	
		# Output Tor IP address to log
		self.writeToLogg(time.ctime() + ": Tor IP Address - " + requests.get("https://api.ipify.org/", proxies = self.__proxies, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}).content)
	
		return True

	
	def reset(self):
		# Kill All
		self.kill()

		# Start All
		self.open_tor()

		# Inform
		self.writeToLogg(time.ctime() + ": " + self.getId() + " ->  Up & Running After Reset!")


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

	
	def writeToLogg(self, msg):
		# Write to Log box
		numlines = self.log.index('end - 1 line').split('.')[0]
	
		# Enable Log box
		self.log['state'] = 'normal'
	
		if numlines == 24:
			self.log.delete(1.0, 2.0)
	
		if self.log.index('end-1c') != '1.0':
			self.log.insert('end', '\n')

		self.log.insert('end', msg)
	
		self.log['state'] = 'disabled'


# TorConnectionCollector - Sends Free TorConnection To The Thread Function
class TorConnectionCollector(object):

	def __init__(self, sock, ctrl, log):
		# Create Tor Object
		self.__torCons = TorConnection(int(sock.get()), int(ctrl.get()), log)


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
	
		# Tor Boolean
		self.use_tor = bool(use_tor.get())
	
		# Log widgets
		self.log = log
	
		# Bot ID
		self.bot = bot
	
		# Spreadsheet frame
		self.spreadsheet = spreadsheet
	
		# Store Thread Dictonary
		self.widgets = widgets
	
		# Submit entry field value as anwser
		self.widgets["submit"]["command"] = lambda: self.submit()

		# Halt thread and destroy widgets
		self.widgets["stop"]["command"] = lambda: self.stop()	
	
		# Submit Button Yellow
		self.widgets['submit']['bg'] = "#FFFF00"
	
		# Pack widgets
		self.packit()

		# Start run()
		self.start()

	
	def writeToLog(self, msg):
		numlines = self.log.index('end - 1 line').split('.')[0]

		if numlines == 24:
			self.log.delete(1.0, 2.0)
	
		if self.log.index('end-1c') != '1.0':
			self.log.insert('end', '\n')
	
		self.log.insert('end', time.ctime() + " [Bot #" + str(self.bot) + "]: " + msg)


	def run(self):
		# Use Time for Email
		time.sleep(0.555)
		self.email = str(time.time() + self.bot).split(".")[0] + "@lackmail.ru"
		self.writeToLog(self.email)
	
		self.writeToLog("Starting Browser")
		self.browser = self.phantom()

		SignUp(self.browser, self.log, self.bot, self.spreadsheet, self.email)
	
		self.Fetch_CAPTCHA()


	def Fetch_CAPTCHA(self):
		# Take Screenshot
		self.browser.save_screenshot("./images/screenshots/screen_" + str(self.bot) + ".png")
	
		# Open Screenshot
		im_temp = Image.open("./images/screenshots/screen_" + str(self.bot) + ".png")

		# Crop Screenshot
		im_temp = im_temp.crop((200, 640, 365, 690))

		# Save CAPTCHA
		im_temp.save("./images/cache/captcha_" + str(self.bot) + ".jpg", "jpeg")
        
        # Load cropped CAPTCHA
		self.photo = ImageTk.PhotoImage(file = "./images/cache/captcha_" + str(self.bot) + ".jpg")

		# Load image into Label
		self.widgets['img']['image'] = self.photo
	
		# Enable Submit
		self.widgets['submit']['state'] = "normal"
		self.widgets['captcha']['state'] = "normal"
		self.widgets["stop"]['state'] = "disabled"
	
		# Submit Color Green
		self.widgets['submit']['bg'] = "#00FF00"

	
	def stop(self):
		# Destroy each thread widget
		for widget in self.widgets:
			if widget != "stop":
				self.widgets[widget].destroy()

		# Destroy stop button last so that every widget is destroyed
		self.widgets["stop"].destroy()


	def submit(self):
		# Wait for user input to break timeout loop and finish signup
		answer = str(self.widgets["captcha"].get())
		self.writeToLog(answer)
	
		self.widgets['submit']['bg'] = "#00FF00"
		self.widgets['submit']['state'] = "disabled"
		self.widgets['captcha']['state'] = "disabled"
		self.widgets["stop"]['state'] = "normal"
	
		captcha = Finialize_Signup(browser = self.browser, captcha = answer, widgets = self.widgets, email = self.email, log = self.log, bot = self.bot, spreadsheet = self.spreadsheet)
	
		if captcha == False:
			self.Fetch_CAPTCHA()
	
		else:
			self.browser.quit()
			self.run()

	def phantom(self):
		self.writeToLog("Starting PhantomJS")

		# Try for Windows
		if self.use_tor:
			return webdriver.PhantomJS(executable_path = "./lib/phantomjs.exe", service_args = ["--proxy=127.0.0.1:9150", "--proxy-type=socks5", '--disk-cache=true'])

		else:
			return webdriver.PhantomJS(executable_path = "./lib/phantomjs.exe")

	
	def packit(self):
		# Pack Bot Widgets
		if self.bot <= 3:
			self.widgets['frame'].grid(row = 0, column = self.bot, sticky = 'W')
			self.widgets['img'].pack(side = "left")
			self.widgets['captcha'].pack(side = "top")
			self.widgets['submit'].pack(side = "right")
			self.widgets['stop'].pack(side = "right")
	
		elif self.bot > 3:
			self.widgets['frame'].grid(row = 1, column = self.bot - 4, sticky = 'W')
			self.widgets['img'].pack(side = "left")
			self.widgets['captcha'].pack(side = "top")
			self.widgets['submit'].pack(side = "right")
			self.widgets['stop'].pack(side = "right")
	

class SignUp():

	def __init__(self, browser, log, bot, spreadsheet, email):
	
		# Log
		self.log = log
	
		# Bot ID
		self.bot = bot
	
		# Email
		self.email = email
	
		# Fetch Homepage
		self.writeToLog("Open Dailymotion Signin")
		browser.get("http://www.dailymotion.com/signin")

		# Enter Email
		browser.find_element_by_xpath('//*[@id="authentication_form_username"]').send_keys(self.email)
	
		# Click Register Account
		browser.find_element_by_id("authentication_form_authChoice_register_label").click()
	
		# Submit
		browser.find_element_by_id('authentication_form_save').click()
		self.writeToLog("Creating account")

		# Wait
		time.sleep(5)

		# Password
		browser.find_element_by_xpath('//*[@id="userPassword_cont"]/div/input').send_keys("")
	
		# Confirm Password
		browser.find_element_by_xpath('//*[@id="confirm_password_cont"]/div/input').send_keys("")
	
		self.writeToLog("Enter Date of Birth Information")
	
		# Birth month
		browser.execute_script("document.getElementById('select2-chosen-2').innerHTML = 'May'")
	
		# Birth year
		browser.execute_script("document.getElementById('select2-chosen-6').innerHTML = '1993'")
	
		# Birth day
		browser.execute_script("document.getElementById('select2-chosen-4').innerHTML = '13'")

		# Clean autofills
		for letter in range(len(self.email.split("@")[0]) + 1):
			browser.find_element_by_xpath('//*[@id="publicname"]').send_keys(Keys.BACKSPACE)
			browser.find_element_by_xpath('//*[@id="url"]').send_keys(Keys.BACKSPACE)


		e = 0

		# Channel Username
		browser.find_element_by_xpath('//*[@id="publicname"]').send_keys("s02e" + str(e))
	
		# Channel URL
		browser.find_element_by_xpath('//*[@id="url"]').send_keys("s02e" + str(e))
	
		# Wait
		time.sleep(2.9)
	
		# Channel URL
		while 1 == 1:

			if browser.find_element_by_xpath('//*[@id="url_cont"]/div/div'):
	
				# Clear URL input	
				for	letter in "s02e" + str(e):
					browser.find_element_by_xpath('//*[@id="url"]').send_keys(Keys.BACKSPACE)
	
				# Enter attempt
				browser.find_element_by_xpath('//*[@id="url"]').send_keys("s02e" + str(e))
	
				# Wait to check if url is available
				time.sleep(2.9)


			if browser.find_element_by_xpath('//*[@id="url_cont"]/div/div').text == "Url available.":
	
				# Stop Bruteforcing URL Loop
				break

			else:	
	
				# Increment URL
				e += 1

		self.writeToLog("Email - " + self.email + " - Password -  - URL - " + "dailymotion.com/s02e" + str(e))
	


	
	def writeToLog(self, msg):
		numlines = self.log.index('end - 1 line').split('.')[0]

		if numlines == 24:
			self.log.delete(1.0, 2.0)
	
		if self.log.index('end-1c') != '1.0':
			self.log.insert('end', '\n')
	
		self.log.insert('end', time.ctime() + " [Bot #" + str(self.bot) + "]: " + msg)


class Finialize_Signup():

	def __init__(self, browser, captcha, widgets, email, log, bot, spreadsheet):
	
		# Log
		self.log = log
	
		# Bot ID
		self.bot = bot
	
		# Enter CAPTCHA anwser
		browser.find_element_by_xpath('//*[@id="captchaInput"]').send_keys(captcha)
	
		# Submit
		self.writeToLog("Submit CAPTCHA - " + captcha)
		browser.find_element_by_xpath('//*[@id="save"]').click()
	
		# Wait
		time.sleep(3)


		# Check if CAPTCHA was right by checking for "cant read" element
		if browser.find_element_by_xpath('//*[@id="cantread"]'):
	
			# Enable Submit
			widgets['submit']['bg'] = "#FFFF00"
			widgets['submit']['state'] = "normal"
			widgets['captcha']['state'] = "normal"

			self.writeToLog("CAPTCHA Failed. Try Again")


		else:
			
			# Add info to spreadsheet
			account_index += 1

			# Colum 1 (Index)
			cell = tk.Label(spreadsheet, width = 3, text = str(account_index))
			cell.grid(row = account_index, column = 0, padx = 1, pady = 1)

			# Colum 2 (Email)
			cell = tk.Entry(spreadsheet, width = 23)
			cell.insert(0, email)
			cell.grid(row = account_index, column = 1, padx = 1, pady = 1)

			# Colum 3 (Password)
			cell = tk.Entry(spreadsheet, width = 5, show = "*")
			cell.insert(0, "")
			cell.grid(row = account_index, column = 2, padx = 1, pady = 1)

			# Colum 4 (URL)
			cell = tk.Entry(spreadsheet, width = 10)
			cell.insert(0, "s02e" + str(e))
			cell.grid(row = account_index, column = 3, padx = 1, pady = 1)

			# Verify Email
			browser.get("https://temp-mail.org/en/option/change")

			# Wait
			time.sleep(2)

			# Enter email
			browser.find_element_by_xpath('//*[@id="mail"]').send_keys(email)

			# Submit email
			browser.find_element_by_xpath('//*[@id="postbut"]').click()

			# Refresh
			browser.get("https://temp-mail.org/en/option/refresh")

			# Wait
			time.sleep(10)

			# Open Email
			browser.find_element_by_link_text("Dailymotion Account creat").click()

			# Wait
			time.sleep(2)

			# Verify Email
			browser.find_element_by_link_text("Confirm your email address").click()
			self.writeToLog("Email Verified - Begin Monitization")

			# Colum 5 (Verified)
			cell = tk.Entry(spreadsheet, width = 2)
			cell.insert(0, ":)")
			cell['bg'] = "green"
			cell['fg'] = "blue"
			cell.grid(row = account_index, column = 4, padx = 1, pady = 1)

			# Montetization
			browser.get("http://www.dailymotion.com/settings/monetization")
			time.sleep(8)
	
			# Ignore tour
			browser.find_element_by_xpath('//*[@id="popupContent"]/div[2]/div/a[2]').click()
			time.sleep(5)

			# Open Agreement
			browser.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div/div/span[1]').click()
			time.sleep(2)

			# Agree
			browser.find_element_by_xpath('//*[@id="label_partner_vertify"]/i').click()
			time.sleep(2)

			# Submit
			browser.find_element_by_xpath('//*[@id="save"]').click()
			time.sleep(3)

			# Colum 6 (Monetization)
			cell = tk.Entry(spreadsheet, width = 2)
			cell.insert(0, ":)")
			cell['bg'] = "green"
			cell['fg'] = "blue"
			cell.grid(row = account_index, column = 5, padx = 1, pady = 1)


	def writeToLog(self, msg):
		numlines = self.log.index('end - 1 line').split('.')[0]

		if numlines == 24:
			self.log.delete(1.0, 2.0)
	
		if self.log.index('end-1c') != '1.0':
			self.log.insert('end', '\n')
	
		self.log.insert('end', time.ctime() + " [Bot #" + str(self.bot) + "]: " + msg)


class AnimatedGif(tk.Label):
	"""
	Class to show animated GIF file in a label
	Use start() method to begin animation, and set the stop flag to stop it
	"""
	def __init__(self, root, gif_file, delay=0.04, bg = "#000000"):
		"""
		:param root: tk.parent
		:param gif_file: filename (and path) of animated gif
		:param delay: delay between frames in the gif animation (float)
		"""
		tk.Label.__init__(self, root, bg = bg)
		self.root = root
		self.gif_file = gif_file
		self.delay = delay  # Animation delay - try low floats, like 0.04 (depends on the gif in question)
		self.stop = False  # Thread exit request flag
	
		# Daemonize thread
		self.daemon = True
	

		self._num = 0

	def start(self):
		""" Starts non-threaded version that we need to manually update() """
		self.start_time = time.time()  # Starting timer
		self._animate()

	def stop(self):
		""" This stops the after loop that runs the animation, if we are using the after() approach """
		self.stop = True

	def _animate(self):
		try:
			self.gif = tk.PhotoImage(file=self.gif_file, format='gif -index {}'.format(self._num))  # Looping through the frames
			self.configure(image=self.gif)
			self._num += 1
		except tk.TclError:  # When we try a frame that doesn't exist, we know we have to start over from zero
			self._num = 0
		if not self.stop:    # If the stop flag is set, we don't repeat
			self.root.after(int(self.delay*1000), self._animate)

	def start_thread(self):
		""" This starts the thread that runs the animation, if we are using a threaded approach """
		from threading import Thread  # We only import the module if we need it
		self._animation_thread = Thread()
		self._animation_thread = Thread(target=self._animate_thread).start()  # Forks a thread for the animation

	def stop_thread(self):
		""" This stops the thread that runs the animation, if we are using a threaded approach """
		self.stop = True

	def _animate_thread(self):
		""" Updates animation, if it is running as a separate thread """
		while self.stop is False:  # Normally this would block mainloop(), but not here, as this runs in separate thread
			try:
				time.sleep(self.delay)
				self.gif = tk.PhotoImage(file=self.gif_file, format='gif -index {}'.format(self._num))  # Looping through the frames
				self.configure(image=self.gif)
				self._num += 1

			except tk.TclError:  # When we try a frame that doesn't exist, we know we have to start over from zero
				self._num = 0


GUI()