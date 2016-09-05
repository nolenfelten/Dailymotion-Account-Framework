from config import *
from os import makedirs
from os import getcwd
from os import path
from os import system
from psutil import process_iter
from psutil import AccessDenied
from stem import Signal
from stem.process import launch_tor_with_config
from stem.control import Controller
from subprocess import check_output
import requests
import time
from lib.Tk_Objects import Tk_Objects
from lib.Backend import Backend


#	 						Variables Index

#  		Key													Value

# Tor Boolean
# Tor SOCKS port
# Tor Control Port






# 						Widget Dictonary Index
#  		Key													Value
 
#	containers
#		header												Root Frame
#		tabs												Root Notebook
#		tree_frame											Treeview Frame
#		item_frame											Account info frame
#		item_image_frame									Account image frame
#		item_details_frame									Account details frame
#		item_email_frame									Account email frame
#		item_date_frame										Account date registered
#		item_partner_frame									Account partner frame
#		item_banking_frame									Account banking frame
#		item_IP_frame										Account ip frame
#		item_API_frame										Account api frame

#	widgets
#		header
#			logo											Root Logo
#			author											Root Author
#			status											Root Status
#			clock											Root Clock
#			title											Root Title
#			gif												GIF Object
#			thread_grid										Tab 2 Thread container
#			enable_tor										Tab 3 Enable Tor Frame

#		tab_one
#			user_email										
#			user_date										Date Signed up
#			user_partner									Partner
#			user_banking									Banking
#			user_ip											User IP
#			user_secret										API Secret
#			user_api										API Key
#			tree											Treeview
#			scroll											Treeview Scrollbar
#			socks_frame										Tab 3 Tor Socks Port Frame
#			tor_ports										Tab 3 Tor Port Settings Frame
#			ctrl_frame										Tab 3 Tor Control Port Frame

#		tab_three
#			log												Tab 3 Debug Log Text Box
#			tor												Tab 3 Tor Image
#			tor_label										Tab 3 "Use Tor:" Label
#			tor_false										Tab 3 Tor = False Radio Button
#			tor_true										Tab 3 Tor = True Radio Button
#			socks_label										Tab 3 Tor Socks Port Label
#			socks											Tab 3 Tor Socks Port Input Field
#			ctrl_label										Tab 3 Tor Control Port Label
#			ctrl											Tab 3 Tor Control Port Input Field
		





class Main():

	def __init__(self):
		
		# GUI Dictonary
		GUI = Tk_Objects()
		
		# Pack Widgets
		GUI.Tk_Pack()
		
		# Start Update Loop
		GUI["root"].after(20, GUI.update_loop())
		
		# Start Mainloop
		GUI["root"].mainloop()
		
		
Main()
