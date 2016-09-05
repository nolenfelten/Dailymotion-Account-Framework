from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import OptionMenu
from tkinter import Listbox
from tkinter import Radiobutton
from tkinter.ttk import Scrollbar
from tkinter.ttk import Style
from tkinter.ttk import Treeview
from tkinter.scrolledtext import ScrolledText
from lib.AnimatedGif import AnimatedGif
from lib.Backend import Backend
from config import *




class Tk_Widgets():

	def __init__(self, containers, variables):

		
		# Header
		header = {
			"author": Label(containers["header"], font = ("Helvetica", 13), bg = "#000000", fg = "#FFFFFF"),
			"clock": Label(containers["header"], font = ("Times", 17), bg = "#000000"),
			"logo": Label(containers["header"], bg = "#000000"),
			"title": Label(containers["header"], font = ("Verdana", 37), bg = "#000000"),
			"status": Label(containers["header"], font = ("Helvetica", 12), bg = "#000000", relief = "sunken", borderwidth = 2),
			"gif": AnimatedGif(containers["header"], "./images/made_in_usa.gif", 0.025)
		}
		
		
		# Tab 1
		tab_a = {
			"tree": Treeview(containers["tree_frame"], columns = ('Email', 'URL', "Verified", "Monetization", "Banking"), show = "headings"),
			"scroll": Scrollbar(containers["tab_1"], orient = "vertical"),
			"user_email": Label(containers["item_email_frame"],),
			"user_date": Label(containers["item_date_frame"], text = "0/0/0"),
			"user_partner": Button(containers["item_partner_frame"], text = "-", state = "disabled"),
			"user_banking": Button(containers["item_banking_frame"], text = "-", state = "disabled"),
			"user_ip": Label(containers["item_IP_frame"], text = "0.0.0.0"),
			"user_secret": Label(containers["item_API_frame"], text = "Secret Key"),
			"user_api": Label(containers["item_API_frame"], text =	"Key")
		}
		
		
		# Tab 2
		tab_b = {
			"bot_controllers": {}
		}

		
		# Tab 3
		tab_c = {
			"log": ScrolledText(containers["tab_3"], undo = True),
			"tor": Label(containers["enable_tor"]),
			"tor_label": Label(containers["enable_tor"], text = "Use Tor:"),
			"tor_true": Radiobutton(containers["enable_tor"], text = "True", variable = variables["use_tor"], value = True),
			"tor_false": Radiobutton(containers["enable_tor"], text = "False", variable = variables["use_tor"], value = False),
			"ctrl_label": Label(containers["ctrl_frame"], text = "Control Port: "),
			"ctrl": Entry(containers["ctrl_frame"], textvariable = variables["ctrl_port"], width = 4),
			"socks_label": Label(containers["socks_frame"], text = "Socks Port: "),
			"socks": Entry(containers["socks_frame"], textvariable = variables["socks_port"], width = 4)
			
		}
		
		
		# Setup the scrollbar for the spreadsheet
		tab_a["scroll"].config(command = tab_a["tree"].yview)
		tab_a["tree"].config(height = len(accounts) - 1)
		tab_a["tree"].config(yscroll = tab_a["scroll"].set)

		# Set Width for each column
		tab_a["tree"].column("Email", width = 110, anchor = 'center')
		tab_a["tree"].column("URL", width = 6, anchor = 'center')
		tab_a["tree"].column("Verified", width = 6, anchor = 'center')
		tab_a["tree"].column("Monetization", width = 6, anchor = 'center')
		tab_a["tree"].column("Banking", width = 6, anchor = 'center')
		
		# Set Height for each column
		tab_a["tree"].heading("Email", text = "Email")
		tab_a["tree"].heading("URL", text = "URL")
		tab_a["tree"].heading("Verified", text = "Verified")
		tab_a["tree"].heading("Monetization", text = "Monetization")
		tab_a["tree"].heading("Banking", text = "Banking")
	
		# Populae the Treeview with each account in accounts.txt
		for row_number in range(len(accounts)):
			# Account Email
			email = accounts[row_number].split(",")[0]
			
			# Account URL
			url = accounts[row_number].split(",")[2]
			
			# Email Verified
			verified = accounts[row_number].split(",")[3]
			
			# Monetization Enabled
			monetization = accounts[row_number].split(",")[4]
			
			# Banking Info Enabled
			banking = accounts[row_number].split(",")[5]
			
			# IP used to signup
			ip = accounts[row_number].split(",")[6]
			
			# Signup date
			date = accounts[row_number].split(",")[7]
			
			# API Key and API Secret Key
			api = accounts[row_number].split(",")[8]
			api1 = accounts[row_number].split(",")[9]
			
			# Insert Cell
			tab_a["tree"].insert("", "end", text = str(row_number + 1), value = (email, url, verified, monetization, banking, ip, date, api, api1))
			
		
		# Add dictonaries to dictonary
		widgets = {
			"header": header,
			"tab_one": tab_a,
			"tab_two": tab_b,
			"tab_three": tab_c,
			"tor": variables["use_tor"]
		}
	
		# Set Widget attributes with variables
		widgets["header"]["title"]["text"] = variables["title"]
		widgets["header"]["author"]["text"] = variables["author"]

		# Start Header GIF Animation
		widgets["header"]["gif"].start()
		
		# Set ttk styles
		Style().configure("Treeview", background = "#000000", foreground = "#FFFFFF")
		
		# Store Dictonary in Instance
		self.widgets = widgets
		
		
		
		# Creates the grid of bot controllers on Tab 2
		for bot in range(len(containers["bot_controllers"])):
			self.widgets["tab_two"]["bot_controllers"][str(bot)] = {
				"img": Label(containers["bot_controllers"][str(bot)]),
				"captcha": Entry(containers["bot_controllers"][str(bot)], state = "disabled"),
				"submit": Button(containers["bot_controllers"][str(bot)], font = ("Helvetica", 9), text = "Start", width = 9),
				"robot": Backend(self.widgets)
			}
			
			
			self.widgets["tab_two"]["bot_controllers"][str(bot)]["submit"]["command"] = lambda i = bot: self.widgets["tab_two"]["bot_controllers"][str(bot)]["robot"].grab_captcha(i)
			
				
	def __getitem__(self, key):
		return self.widgets[key]