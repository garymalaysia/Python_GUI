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

		self.randLabel = Label(master, text="Number read: ")
		self.randLabel.grid(row=1, column=0, stick=W)
		#self.randLabel.pack()
		#self.randDisplay = StringVar()

		self.display_button = Button(master, text="Random", command=self.randGen)
		self.display_button.grid(row=2, column=0, sticky=W)
		#self.display_button.pack()

		self.close_button = Button(master, text="Close", command=master.quit)
		#self.close_button.grid(row=10, column=5, sticky = E)
		self.close_button.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
		#self.close_button.pack()


	def displayMessage(self):
		self.displayText = self.display.get()
		self.displayLabel = Label(self.master, text=self.displayText)#.pack()
		self.displayLabel.grid(row=8, stick= W)

	def randGen(self):
		self.a = random.randint(1,10)
		if self.a%2 == 0:
			#self.displayRand = Label(self.master, text=self.a).pack()
			self.EnterMessage()
		#print(self.a)
		
	def EnterMessage(self):
		self.label = Label(self.master, text="Enter a message: ")
		self.label.grid(row=5, sticky = W)
		#self.label.pack()

		self.display = StringVar()
		self.display_entry = ttk.Entry(self.master, width=40, textvariable=self.display)
		self.display_entry.grid(row=5, column=1)
		#self.display_entry.pack()

		self.display_button = Button(self.master, text="Enter", command=self.displayMessage)
		self.display_button.grid(row=7, column=0, sticky = W)
		#self.display_button.pack()

if __name__ == "__main__":
	root = Tk()
	my_gui = GUI(root)
	root.mainloop()