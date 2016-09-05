import time 

def WriteToLog(log, msg = ""):
	try:
		numlines = log.index('end - 1 line').split('.')[0]
		

		if numlines == 24:
			log.delete(1.0, 2.0)

		if log.index('end-1c') != '1.0':
			log.insert('end', '\n')

		log.insert('end', time.ctime() + ": " + msg)
	except:
		print 1
		
'''
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='#476042', 
						font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
text2.insert(END,'\nWilliam Shakespeare\n', 'big')
quote = """
To be, or not to be that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
"""
text2.insert(END, quote, 'color')
text2.insert(END, 'follow-up\n', 'follow')
'''