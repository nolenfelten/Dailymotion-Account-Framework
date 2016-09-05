from tkinter import Label
from tkinter import PhotoImage
from tkinter import TclError
import time


class AnimatedGif(Label):
	
	
	def __init__(self, root, gif_file, delay = 0.04, bg = "#000000"):
		
		# Create Label Object
		Label.__init__(self, root, bg = bg)
		
		# Label Parent
		self.root = root
		
		# GIF File
		self.gif_file = gif_file
		
		# Animation delay - try low floats, like 0.04 (depends on the gif in question)
		self.delay = delay
		
		# Thread exit request flag
		self.stop = False

		# Daemonize thread
		self.daemon = True

		# Frame index
		self._num = 0

		
	def start(self):
		# Starting timer
		self.start_time = time.time()
		
		# Starts non-threaded version that we need to manually update()
		self._animate()

		
	def stop(self):
		# This stops the after loop that runs the animation, if we are using the after() approach
		self.stop = True

		
	def _animate(self):
		try:
			# Looping through the frames
			self.gif = PhotoImage(file = self.gif_file, format = 'gif -index {}'.format(self._num))
			
			# Load frame into Label
			self.configure(image = self.gif)
			
			# Move to next frame
			self._num += 1
			
		# When we try a frame that doesn't exist, we know we have to start over from zero
		except TclError:
			self._num = 0

		# If the stop flag is set, we don't repeat
		if not self.stop:    
			self.root.after(int(self.delay * 1000), self._animate)

			
	def start_thread(self):
		# We only import the module if we need it
		from threading import Thread  
		
		# This starts the thread that runs the animation, if we are using a threaded approach
		self._animation_thread = Thread()
		
		# Forks a thread for the animation
		self._animation_thread = Thread(target = self._animate_thread).start()

		
	def stop_thread(self):
		# This stops the thread that runs the animation, if we are using a threaded approach
		self.stop = True

		
	def _animate_thread(self):
		# Normally this would block mainloop(), but not here, as this runs in separate thread
		while self.stop is False:  
			
			# Updates animation, if it is running as a separate thread
			try:
				time.sleep(self.delay)
				
				# Looping through the frames
				self.gif = PhotoImage(file = self.gif_file, format = 'gif -index {}'.format(self._num))
				
				# Load Frame into Label
				self.configure(image = self.gif)
				
				# Move to next Frame
				self._num += 1

			# When we try a frame that doesn't exist, we know we have to start over from zero
			except TclError:  
				self._num = 0

