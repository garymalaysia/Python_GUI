from time import sleep
import openpyxl
from openpyxl import load_workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl.utils import coordinate_from_string
from tkinter import *
from tkinter import ttk
'''
def prompt_with_timeout():
	print ("\t######### MISSING Name or Email ##########\n")

	print('Please press Ctrl-C to enter Name and Email')
	try:
		for i in range(0, 10): # 30 minutes is 30*60 seconds
			sleep(1)
		print("No Name or Email was logged")
		n = ""
		e = ""
		
	except KeyboardInterrupt:
		n = input("Student's Name -> ")
		e = input("Student's Email -> ")
		if n == "" or  e == "" or n == "None" or  e == "None":
			print("No Name or Email was logged")
		else:
			print (n + " and " + e +" added to database")
	return n, e
'''
class studentGUI:
	def __init__(self, master):
		self.master = master
		master.title("New Student")
		#master.update_idletasks()
		width = 400
		height = 150
		x = (master.winfo_screenwidth() // 2) - (width // 2)
		y = (master.winfo_screenheight() // 2) - (height // 2)
		master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

		self.prompt_with_timeout()

	def prompt_with_timeout(self):
		#print ("\t######### MISSING Name or Email ##########\n")
		self.missing = Label(self.master, text="######### MISSING Name or Email ##########")
		self.missing.pack()

		#print('Please press Ctrl-C to enter Name and Email')
		self.ctrl = Label(self.master, text="Please press Ctrl-C to enter Name and Email")
		self.ctrl.pack()

		'''
		#try:
			#for i in range(0, 10): # 30 minutes is 30*60 seconds
				#sleep(1)
			#print("No Name or Email was logged")
			self.noData = Label(self.master, text="No Name or Email was logged")
			self.noData.pack()
			self.name = ""
			self.email = ""
		
		except KeyboardInterrupt:
			#n = input("Student's Name -> ")
			#e = input("Student's Email -> ")
		'''		
		self.name = StringVar()
		self.email = StringVar()
		self.display_name = ttk.Entry(self.master, width=40, textvariable=self.name)
		self.display_name.pack()
		self.display_email = ttk.Entry(self.master, width=40, textvariable=self.email)
		self.display_email.pack()

		self.x, self.y = self.studentLogin()
		#self.display_button = Button(self.master, text="Enter", command=self.studentLogin)
		#self.display_button.pack()


	def studentLogin(self):
		self.gotName = self.name.get()
		self.gotEmail = self.email.get()

		if self.gotName == "" or  self.gotEmail == "" or self.gotName == "None" or  self.gotEmail == "None":
			#print("No Name or Email was logged")
			self.msg = Label(self.master, text="No Name or Email was logged")
			self.msg.pack()
		else:
			#print (n + " and " + e +" added to database")
			self.msg2 = Label(self.master, text=self.gotName + " and " + self.gotEmail +" added to database")
			self.msg2.pack()
			return self.gotName, self.gotEmail
			

if __name__ == "__main__":
	root = Tk()
	studGui = studentGUI(root)
	root.mainloop()