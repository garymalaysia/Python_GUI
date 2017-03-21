from tkinter import *
from tkinter import ttk
from pythoncard import * #getReaders, waitforcard, waitforcardevent
import random

class GUI:
	def __init__(self, master):
		self.master = master
		master.title("JJAY Veterans Association HID Scanner")
		master.update_idletasks()
		width = 400
		height = 400
		x = (master.winfo_screenwidth() // 2) - (width // 2)
		y = (master.winfo_screenheight() // 2) - (height // 2)
		master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

		#self.randButton()
		self.pythonCard()
		self.closeButton()

	#creates a button called 'Random'
	def randButton(self):
		self.display_button = Button(self.master, text="Random", command=self.randGen)
		#self.display_button.grid(row=1, sticky=W)
		self.display_button.pack(anchor=W)

	#creates a button called 'Close'
	def closeButton(self):
		self.close_button = Button(self.master, text="Close", command=self.master.quit)
		#self.close_button.grid(row=10, column=5, sticky = E)
		self.close_button.place(rely=1.0, relx=0.0, x=0, y=0, anchor=SW)
		#self.close_button.pack()

	#function that will call enterMessage function if rand_num is even
	def randGen(self):
		self.a = random.randint(1,10)
		if self.a%2 == 0:
			self.enterMessage()

	#creates a bar to enter string and calls displayMessage function to display to window
	def enterMessage(self):
		self.label = Label(self.master, text="Enter a message: ")
		
		self.display = StringVar()
		self.display_entry = ttk.Entry(self.master, width=40, textvariable=self.display)
		
		self.display_button = Button(self.master, text="Enter", command=self.displayMessage)
		
		#Pack methods
		self.label.pack(side=TOP, anchor=W)
		#self.label.grid(row=2, sticky = W)

		self.display_entry.pack(side=TOP, anchor=W)
		#self.display_entry.grid(row=2, column=1)
		
		self.display_button.pack(side=TOP, anchor=W)
		#self.display_button.grid(row=3, column=0, sticky = W)
		
		#Update for reuse on screen - should reset GUI window
		self.label.update
		self.display_entry.update
		self.display_button.update

	#function to display message to screen, not command line/terminal
	def displayMessage(self):
		self.displayText = self.display.get()
		self.displayWord = Label(self.master, text=self.displayText)
		self.displayWord.pack(side=BOTTOM, anchor=W, pady=100) 
		#self.displayLabel.grid(row=4, stick= W)

	def clear(self):
		self.label.pack_forget()
		self.display_entry.pack_forget()
		self.display_button.pack_forget()

	def pythonCard(self):
		self.wb=load_workbook('testing.xlsx', data_only = True)
		self.wb.active
		self.worksheet= wb.get_sheet_names()
		self.sheet = wb.get_sheet_by_name('Sheet')

		self.cardtype = "3B 8F 80 01 80 4F 0C A0 00 00 03 06 40 00 00 00 00 00 00 28"
		self.length=10
		self.txt = Label(self.master, text="------Tap card to SIGN IN-------")
		self.txt.pack(side=TOP)
		
		'''
		self.cr = CardRequest(timeout=None, newcardonly=True)
		self.cs = self.cr.waitforcard()
		self.cs.connection.connect()
		self.card = toHexString(cs.connection.getATR())
		self.SELECT = [0xFF, 0xCA, 0x00, 0x00, 0x00]

		self.response, self.sw1, self.sw2 = self.cs.connection.transmit( SELECT)
		self.texting = toHexString(self.response).replace(' ','')
		self.word_len=len(self.texting)
		if self.card == self.cardtype and self.length == word_len :
			header()
			search_Student(texting)
			cs.connection.disconnect()
			formular()
		
		'''
	    

	    

if __name__ == "__main__":
	root = Tk()
	my_gui = GUI(root)
	root.mainloop()


#Leftover pieces of code
	#self.randLabel = Label(self.master, text="Click to activate generator")
	#self.randLabel.grid(row=1, column=0, stick=W)