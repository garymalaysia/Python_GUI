from tkinter import *
from tkinter import ttk
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

		#master.topFrame = Frame()
		'''
		for x in range(1,10):
			self.randButton()
			self.closeButton()
			self.clear()
		'''
		self.randButton()
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
		#self.label.grid(row=2, sticky = W)
		self.label.pack(anchor=W)

		self.display = StringVar()
		self.display_entry = ttk.Entry(self.master, width=40, textvariable=self.display)
		#self.display_entry.grid(row=2, column=1)
		self.display_entry.pack(anchor=W)

		self.display_button = Button(self.master, text="Enter", command=self.displayMessage)
		#self.display_button.grid(row=3, column=0, sticky = W)
		self.display_button.pack(anchor=W)

	#function to display message to screen, not command line/terminal
	def displayMessage(self):
		self.displayText = self.display.get()
		self.displayLabel = Label(self.master, text=self.displayText).pack()
		#self.displayLabel.grid(row=4, stick= W)
		self.clear()

	def clear(self):
		self.label.pack_forget()
		self.display_entry.pack_forget()
		self.display_button.pack_forget()

if __name__ == "__main__":
	root = Tk()
	my_gui = GUI(root)
	root.mainloop()


#Leftover pieces of code
	#self.randLabel = Label(self.master, text="Click to activate generator")
	#self.randLabel.grid(row=1, column=0, stick=W)