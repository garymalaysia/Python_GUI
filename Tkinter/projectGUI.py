from tkinter import *
from tkinter import ttk

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

		self.label = Label(master, text="GUI for HID Scanner")
		self.label.pack()

		self.display = StringVar()
		self.display_entry = ttk.Entry(master, width=7, textvariable=self.display)
		self.display_entry.pack()

		self.display_button = Button(master, text="Enter", command=self.displayMessage)
		self.display_button.pack()

		self.close_button = Button(master, text="Close", command=master.quit)
		self.close_button.pack()



	def displayMessage(self):
		self.displayText = self.display.get()
		self.displayLabel = Label(self.master, text=self.displayText).pack()
		return 

if __name__ == "__main__":
	root = Tk()
	my_gui = GUI(root)
	root.mainloop()