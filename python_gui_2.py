from Tkinter import *

root = Tk()

#Grid Layout
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root) #creates a blank field for user input
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E) #by default, column is always labeled as 0
label_2.grid(row=1, sticky=E) #parameter sticky used for alignment. (N,S,W,E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")	#Checkbutton creates the check box
c.grid(columnspan=2)	#columnspan allows you to specify how many columns you wish to occupy

root.mainloop()