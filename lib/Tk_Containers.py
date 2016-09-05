from tkinter import Frame
from tkinter import LabelFrame
from tkinter.ttk import Notebook
from config import *

class Tk_Containers:
	
	def __init__(self, root):
		# The container Frames and Canvas widgets
		containers = {										
			"bot_controllers": {},
			"header": Frame(root, relief = "groove", borderwidth = 6, bg = "#000000"),		# Header Widget
			"tabs": Notebook(root)
		}
		
		# Tab Frames
		containers["tab_1"] = Frame(containers["tabs"])
		containers["tab_2"] = Frame(containers["tabs"])
		containers["tab_3"] = Frame(containers["tabs"])
		
		# Treeview Frame
		containers["tree_frame"] = Frame(containers["tab_1"])
		
		# Treeview Item detail Frames
		containers["item_frame"] = Frame(containers["tab_1"])
		containers["item_image_frame"] = LabelFrame(containers["item_frame"], text = "Profile Image:", labelanchor = 'nw', width = 150, height = 150, borderwidth = 6)
		containers["item_details_frame"] = LabelFrame(containers["item_frame"], text = "Information:", labelanchor = 'nw', font = ("Helvetica", 14), borderwidth = 4)
		containers["item_email_frame"] = LabelFrame(containers["item_details_frame"], text = "Email:", labelanchor = 'w', borderwidth = 2)
		containers["item_date_frame"] = LabelFrame(containers["item_details_frame"], text = "Date Created:", labelanchor = 'w', borderwidth = 2)
		containers["item_partner_frame"] = LabelFrame(containers["item_details_frame"], text = "Monetization:", labelanchor = 'w', borderwidth = 2)
		containers["item_banking_frame"] = LabelFrame(containers["item_details_frame"], text = "Banking:", labelanchor = 'w', borderwidth = 2)
		containers["item_IP_frame"] = LabelFrame(containers["item_details_frame"], text = "IP Registered With:", labelanchor = 'w', borderwidth = 2)
		containers["item_API_frame"] = LabelFrame(containers["item_details_frame"], text = "API:", labelanchor = 'w', borderwidth = 2)
		
		# Tab 3 Settings Frames
		containers["browser_frame"] = LabelFrame(containers["tab_3"], text = "Select Browser:", labelanchor = 'n')		# Tab 3 Browser Settings Frame
		containers["ctrl_frame"] = Frame(containers["tab_3"])															# Tab 3 Tor CTRL Settings Frame
		containers["enable_tor"] = LabelFrame(containers["tab_3"], borderwidth = 2, relief = "raised")					# Tab 3 "Enale Tor" Frame
		containers["socks_frame"] = Frame(containers["tab_3"])															# Tab 3 Tor SOCKS Settings Frame
		containers["thread_grid"] = Frame(containers["tab_2"], borderwidth = 2)											# Thread Container
		containers["tor_ports"] = LabelFrame(containers["tab_3"], labelanchor = 'nw', text = "Tor Settings:")			# Tab 3 Tor Port Settings LabelFrame

		for bot in range(number_of_bots):
			containers["bot_controllers"][str(bot)] = LabelFrame(containers["thread_grid"], borderwidth = 3, relief = "groove", labelanchor = "n", text = "Bot " + str(bot + 1) + ":")
		
		# Store in instance
		self.containers = containers
		
		# Add Tabs
		self.containers["tabs"].add(self.containers["tab_1"], text = "Accounts")						# Add Tab 1
		self.containers["tabs"].add(self.containers["tab_2"], text = "Create Accounts")				# Add Tab 2
		self.containers["tabs"].add(self.containers["tab_3"], text = "Settings")						# Add Tab 3
		
	
	def __getitem__(self, key):
		return self.containers[key]
		