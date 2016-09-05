from tkinter import Tk
from PIL import Image	
from PIL import ImageTk
from tkinter import BooleanVar
from lib.Tk_Variables import Tk_Variables
from lib.Tk_Containers import Tk_Containers
from lib.Tk_Widgets import Tk_Widgets
import time
from config import *
from lib.Backend import Backend
from lib.kill import kill
		
class Tk_Objects():

	def __init__(self):
		# Create Master Widget
		root = Tk()
		
		# Set Window Title
		root.title("Dailymotion Account Framework - NolenFelten.com")
		
		# Maximize Window
		root.state('zoomed')
		
		# Quit if the window is deleted
		root.protocol("WM_DELETE_WINDOW", lambda: kill(root))

		# Tk Variables and other data used for widgets
		variables = Tk_Variables()

		# Tk Frames and LabelFrames
		containers = Tk_Containers(root)

		# Tk Widgets
		widgets = Tk_Widgets(containers, variables)
			
		# GUI Dictonary
		self.GUI = {
			"root": root,
			"variables": variables,
			"containers": containers,
			"widgets": widgets,
		}
		
		self.GUI["backend"] = Backend(self.GUI["widgets"])
		
		self.red = 1
		self.green = 1
		self.blue = 1
		self.seq = 1
	
		# Bind double clicking to function
		self.GUI["widgets"]["tab_one"]["tree"].bind("<Double-1>", self.OnDoubleClick)
		

	def OnDoubleClick(self, event):
		# The Item Clicked
		item = self.GUI["widgets"]["tab_one"]["tree"].selection()[0]

		# Setup Email Widget color to green if email has been verified, red otherwise
		self.GUI["widgets"]["tab_one"]["user_email"]["text"] = self.GUI["widgets"]["tab_one"]["tree"].item(item, "values")[0]
		if self.GUI["widgets"]["tab_one"]["tree"].item(item, "values")[2] == "True":
			self.GUI["widgets"]["tab_one"]["user_email"]["fg"] = "#00AA00"
			
		else:
			self.GUI["widgets"]["tab_one"]["user_email"]["fg"] = "#FF0000"
			
			
		# Setup Button properties for partner
		self.GUI["widgets"]["tab_one"]["user_partner"]["text"] = self.GUI["widgets"]["tab_one"]["tree"].item(item, "values")[3]
		if self.GUI["widgets"]["tab_one"]["user_partner"]["text"] == "False":
			self.GUI["widgets"]["tab_one"]["user_partner"]["command"] = lambda: self.writeToLog(self.GUI["widgets"]["tab_one"]["user_partner"]["text"])
			self.GUI["widgets"]["tab_one"]["user_partner"]["bg"] = "#FF0000"
			self.GUI["widgets"]["tab_one"]["user_partner"]["fg"] = "#CCCCCC"
			self.GUI["widgets"]["tab_one"]["user_partner"]["state"] = "normal"
			
		else:
			self.GUI["widgets"]["tab_one"]["user_partner"]["command"] = None
			self.GUI["widgets"]["tab_one"]["user_partner"]["bg"] = "#00FF00"
			self.GUI["widgets"]["tab_one"]["user_partner"]["fg"] = "#FFFFFF"
			self.GUI["widgets"]["tab_one"]["user_partner"]["state"] = "disabled"

			
		# Setup Button properties for banking
		self.GUI["widgets"]["tab_one"]["user_banking"]["text"] = self.GUI["widgets"]["tab_one"]["tree"].item(item, "values")[4]
		if self.GUI["widgets"]["tab_one"]["user_banking"]["text"] == "False":
			self.GUI["widgets"]["tab_one"]["user_banking"]["command"] = lambda: self.writeToLog(self.GUI["widgets"]["tab_one"]["user_banking"]["text"])
			self.GUI["widgets"]["tab_one"]["user_banking"]["bg"] = "#FF0000"
			self.GUI["widgets"]["tab_one"]["user_banking"]["fg"] = "#CCCCCC"
			self.GUI["widgets"]["tab_one"]["user_banking"]["state"] = "normal"

		else:
			self.GUI["widgets"]["tab_one"]["user_banking"]["command"] = None
			self.GUI["widgets"]["tab_one"]["user_banking"]["bg"] = "#00FF00"
			self.GUI["widgets"]["tab_one"]["user_banking"]["fg"] = "#FFFFFF"
			self.GUI["widgets"]["tab_one"]["user_banking"]["state"] = "disabled"

			
		# Account IP address
		self.GUI["widgets"]["tab_one"]["user_ip"]["text"] = self.GUI["widgets"]["tab_one"]["tree"].item(item, "values")[5]

		# Account sign up date
		self.GUI["widgets"]["tab_one"]["user_date"]["text"] = self.GUI["widgets"]["tab_one"]["tree"].item(item, "values")[6]

		# API Keys
		self.GUI["widgets"]["tab_one"]["user_secret"]["text"] = "API Secret: " + self.GUI["widgets"]["tab_one"]["tree"].item(item, "values")[7]
		self.GUI["widgets"]["tab_one"]["user_api"]["text"] = "API Key: " + self.GUI["widgets"]["tab_one"]["tree"].item(item, "values")[8]
	
	
	def update_loop(self):
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
	
		
		self.GUI["widgets"]["header"]["clock"]["fg"] = product
		self.GUI["widgets"]["header"]["title"]["fg"] = product
		self.GUI["widgets"]["header"]["status"]["fg"] = product

	
		self.GUI["widgets"]["header"]["clock"]["text"] = time.strftime('%H:%M:%S')
		self.GUI["widgets"]["header"]["status"]['text'] = "Tor: " + str(self.GUI["variables"]["use_tor"].get())
		
		self.GUI["root"].after(20, self.update_loop)
		
	def Tk_Pack(self):

		# Pack Widgets
		self.GUI["containers"]["header"].pack(side = "top", anchor = "nw", fill = "both")			# Root Header
		self.GUI["widgets"]["header"]["logo"].pack(side = "left", ipady = 8, padx = 50, ipadx = 15)	# Root Logo
		self.GUI["widgets"]["header"]["author"].pack(side = "right", anchor = "se")					# Root Author
		self.GUI["widgets"]["header"]["status"].place(x = 229, rely = 0.899, anchor = "center")		# Root Status
		self.GUI["widgets"]["header"]["clock"].place(x = 42, y = 16, anchor = "center")				# Root Clock
		self.GUI["widgets"]["header"]["gif"].pack(side = "right", anchor = "se")					# GIF Object
		self.GUI["widgets"]["header"]["title"].place(y = 29, relx = 0.362)							# Root Title
		self.GUI["containers"]["tabs"].pack(fill = 'both', expand = True)							# Root Notebook
		self.GUI["containers"]["tree_frame"].pack(fill = 'y', side = 'left', ipadx = 155)			# Treeview Frame
		self.GUI["containers"]["item_frame"].pack(fill = 'both', side = 'right', expand = True)
		self.GUI["containers"]["item_image_frame"].pack(side = "top", pady = 20, padx = 155)				
		self.GUI["containers"]["item_details_frame"].pack(fill = 'both', expand = True)
		self.GUI["containers"]["item_email_frame"].pack(fill = "x", side = 'top')
		self.GUI["containers"]["item_date_frame"].pack(fill = "x", side = 'top')
		self.GUI["containers"]["item_partner_frame"].pack(fill = "x", side = 'top')
		self.GUI["containers"]["item_banking_frame"].pack(fill = "x", side = 'top')
		self.GUI["containers"]["item_IP_frame"].pack(fill = "x", side = 'top')
		self.GUI["containers"]["item_API_frame"].pack(fill = "x", side = 'top')
		self.GUI["widgets"]["tab_one"]["user_email"].pack(fill = "x", side = "right")
		self.GUI["widgets"]["tab_one"]["user_date"].pack(fill = "x", side = "right")
		self.GUI["widgets"]["tab_one"]["user_partner"].pack(fill = "x", side = "right")
		self.GUI["widgets"]["tab_one"]["user_banking"].pack(fill = "x", side = "right")
		self.GUI["widgets"]["tab_one"]["user_ip"].pack(fill = "x", side = "right")
		self.GUI["widgets"]["tab_one"]["user_secret"].pack(fill = "x", side = "right")
		self.GUI["widgets"]["tab_one"]["user_api"].pack(fill = "x", side = "right")
		self.GUI["widgets"]["tab_one"]["tree"].pack(fill = "both", side = "left", expand = True)		# Treeview
		self.GUI["widgets"]["tab_one"]["scroll"].pack(fill = "both", side = "right")					# Treeview Scrollbar
		self.GUI["containers"]["thread_grid"].pack(anchor = "nw")										# Tab 2 Thread container
		self.GUI["widgets"]["tab_three"]["log"].pack(expand = True, fill = 'both', side = "right")		# Tab 3 Debug Log Text Box
		self.GUI["containers"]["enable_tor"].pack(anchor = 'nw')										# Tab 3 Enable Tor Frame
		self.GUI["widgets"]["tab_three"]["tor"].pack(side = "top", anchor = 'n')						# Tab 3 Tor Image
		self.GUI["widgets"]["tab_three"]["tor_label"].pack(anchor = 's')								# Tab 3 "Use Tor:" Label
		self.GUI["widgets"]["tab_three"]["tor_false"].pack(side = "right", anchor = 's')				# Tab 3 Tor = False Radio Button
		self.GUI["widgets"]["tab_three"]["tor_true"].pack(side = "left", anchor = 's')					# Tab 3 Tor = True Radio Button
		self.GUI["containers"]["tor_ports"].pack(side = "left", anchor = 'nw')							# Tab 3 Tor Port Settings Frame
		self.GUI["containers"]["socks_frame"].pack(anchor = 'nw')										# Tab 3 Tor Socks Port Frame
		self.GUI["widgets"]["tab_three"]["socks_label"].pack(side = "left", padx = 15)					# Tab 3 Tor Socks Port Label
		self.GUI["widgets"]["tab_three"]["socks"].pack(side = "right")									# Tab 3 Tor Socks Port Input Field
		self.GUI["containers"]["ctrl_frame"].pack(anchor = 'nw')										# Tab 3 Tor Control Port Frame
		self.GUI["widgets"]["tab_three"]["ctrl_label"].pack(side = "left", padx = 10)					# Tab 3 Tor Control Port Label
		self.GUI["widgets"]["tab_three"]["ctrl"].pack(side = "right")									# Tab 3 Tor Control Port Input Field
		
		self.bot_img = ImageTk.PhotoImage(Image.open("./images/dmcaptcha.png"))
		
		
		self.logo = ImageTk.PhotoImage(Image.open("./images/logo.jpg"))
		self.tor = ImageTk.PhotoImage(Image.open("./images/tor-logo.png"))
		
		
		# Reset the Label images to workaround garbage collection
		self.GUI["widgets"]["header"]["logo"].configure(image = self.logo)
		self.GUI["widgets"]["tab_three"]["tor"].configure(image = self.tor)
		
		# Bot Controllers
		for bot in range(number_of_bots):
			if bot < 3:
				# Row 1
				self.GUI["containers"]["bot_controllers"][str(bot)].grid(row = 0, column = bot, padx = 5, sticky = 'W')

			if bot < 6 and bot >= 3:
				# Row 2
				self.GUI["containers"]["bot_controllers"][str(bot)].grid(row = 1, column = bot - 3, padx = 5, sticky = 'W')
			
			if bot < 9 and bot >= 6:
				# Row 3
				self.GUI["containers"]["bot_controllers"][str(bot)].grid(row = 2, column = bot - 6, padx = 5, sticky = 'W')
	
			if bot < 12 and bot >= 9:
				# Row 4
				self.GUI["containers"]["bot_controllers"][str(bot)].grid(row = 3, column = bot - 9, padx = 5, sticky = 'W')
				
			bot = str(bot)
				
			# Thread CAPTCHA Label
			self.GUI["widgets"]["tab_two"]["bot_controllers"][str(bot)]["img"].pack(side = "left", padx = 10)
	
			# CAPTCHA Answer 
			self.GUI["widgets"]["tab_two"]["bot_controllers"][str(bot)]["captcha"].pack(side = "top", padx = 10)
	
			# Submit Button
			self.GUI["widgets"]["tab_two"]["bot_controllers"][str(bot)]["submit"].pack(side = "right", padx = 10)
	
			# Work around garbage collection
			self.GUI["widgets"]["tab_two"]["bot_controllers"][str(bot)]["img"].configure(image = self.bot_img)
	
	
	def __getitem__(self, key):
		return self.GUI[key]