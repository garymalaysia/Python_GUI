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
	def __init__(self,root):
		self.root = root
		root.title("New Student")
		width = 400
		height = 200
		x = (root.winfo_screenwidth() // 2) - (width // 2)
		y = (root.winfo_screenheight() // 2) - (height // 2)
		root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

		#self.returnName()
		#self.prompt_with_timeout()

	def prompt_with_timeout(self):

		#self.name = ""

		#print ("name =", self.name)

		#self.display_name = ttk.Entry(self.root, width=40, textvariable=self.name)
		self.display_name = Entry(self.root)
		self.display_name.pack()

		self.button = Button(self.root, text="Enter", command=self.returnName)
		#print(self.button)
		#self.display_name.pack()
		self.button.pack()

		#print("name =", self.name)
		#print("gotName =", gotName)
		#return self.returnName()

	def returnName(self):
		self.gotName = self.display_name.get()
		print ("gotName =", self.gotName)
		#return self.gotName


	
'''
if __name__ == '__main__':
	root = Tk()
	gui = studentGUI(root)
	root.mainloop()
'''