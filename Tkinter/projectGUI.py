from tkinter import *
from tkinter import ttk
from pythoncard import *

class GUI:
	def __init__(self, master):
		self.master = master
		master.title("JJAY Veterans Association HID Scanner")

		self.label = Label(master, text="GUI for HID Scanner")
		self.label.pack()

		self.greet_button = Button(master, text="Greet", command=self.greet)
		self.greet_button.pack()

		self.close_button = Button(master, text="Close", command=master.quit)
		self.close_button.pack()


	def greet(self, *args):
		print("Greetings!")
		message = 'Greetings'
		gui.set(message)


root = Tk()
my_gui = GUI(root)
root.mainloop()