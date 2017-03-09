from tkinter import *

root = Tk()

theLabel = Label(root, text="I'll show you the dark side!")
theLabel.pack()	#puts the contents of theLabel to display on gui screen

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)  #parameter places frame on bottom of gui screen

#parameters include which frame, text, and color
button1 = Button(topFrame, text="Button1", fg="red")
button2 = Button(topFrame, text="Button2", fg="blue")
button3 = Button(topFrame, text="Button3", fg="green")
button4 = Button(bottomFrame, text="Button4", fg="purple")

#each widget created must be packed to display on screen
button1.pack(side=LEFT) #parameter places widget to far left of screen
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()



#Learning about parameters 'fill' and 'expand' for pack() method
#to make widget grow or shink in window size
one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)
four = Label(root, text="Four", bg="yellow", fg="black")
four.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()	#continually running a loop to display the gui screen