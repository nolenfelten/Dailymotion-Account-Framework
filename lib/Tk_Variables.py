from tkinter import BooleanVar
from tkinter import IntVar
from tkinter import StringVar
from lib.Tk_Containers import Tk_Containers
from lib.Tk_Widgets import Tk_Widgets



class Tk_Variables:

	def __init__(self):
		
		# Variables used for widgets
		variables = {
			"title": "Account Management Framework",
			"author": "Made in USA by Nolen Felten - NolenFelten.com - nolenf@gmail.com",
			"ctrl_port": IntVar(),
			"socks_port": IntVar(),
			"use_tor": BooleanVar()
		}

		variables["use_tor"].set(False)					# Tor Boolean
		variables["socks_port"].set("9050")				# Tor SOCKS port
		variables["ctrl_port"].set("5050")				# Tor Control Port
		
		self.variables = variables
		
	def __getitem__(self, key):
		return self.variables[key]