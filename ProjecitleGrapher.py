from tkinter import *
from tkinter import messagebox

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

UI_WIDTH = 25

###########
# GRAPHER #
###########

def main():
	# get inputs
	option = Option.get()
	airResistance = AirResistance.get()
	initialForce = InitialForce.get()
	angle = Angle.get()
	gravity = Gravity.get()
	delta = Delta.get()

	# cheak values
	if airResistance == "" and option != "Air Resistance":
		return messagebox.showwarning("Error","Must enter air resistance!")
	if initialForce == "" and option != "Initial Force":
		return messagebox.showwarning("Error","Must enter initial force!")
	if angle == "" and option != "Angle":
		return messagebox.showwarning("Error","Must enter angle!")
	if gravity == "" and option != "Gravity":
		return messagebox.showwarning("Error","Must enter gravity!")
	if delta == "" and option != "Delta":
		return messagebox.showwarning("Error","Must enter delta!")	

	#graph it
	plt.ion()
	fig = plt.figure()
	plt.plot([1,2,3,4])

#############
# SET UP UI #
#############

root = Tk()
root.title("Projecitle Grapher")
 
# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=10, padx=10)

# Enter option 
Option = StringVar(root)
choices = ['Air Resistance','Initial Force','Angle','Gravity','Delta']
popupMenu = OptionMenu(mainframe, Option, *choices)
popupMenu.config(width=UI_WIDTH)
popupMenu.grid(row = 2, column =1)
Label(mainframe, text="Select Y axis").grid(row = 1, column = 1)
Option.set(choices[0])

#enter air resistance
Label(mainframe, text="Air Resistance").grid(row = 3, column = 1)
AirResistance = Entry(mainframe, width=UI_WIDTH)
AirResistance.grid(row = 4, column = 1)

#enter air resistance
Label(mainframe, text="Initial Force").grid(row = 5, column = 1)
InitialForce = Entry(mainframe, width=UI_WIDTH)
InitialForce.grid(row = 6, column = 1)

#enter air resistance
Label(mainframe, text="Angle").grid(row = 7, column = 1)
Angle = Entry(mainframe, width=UI_WIDTH)
Angle.grid(row = 8, column = 1)

#enter air resistance
Label(mainframe, text="Gravity").grid(row = 9, column = 1)
Gravity = Entry(mainframe, width=UI_WIDTH)
Gravity.grid(row = 10, column = 1)

#enter delta
Label(mainframe, text="Delta").grid(row = 11, column = 1)
Gravity = Entry(mainframe, width=UI_WIDTH)
Gravity.grid(row = 12, column = 1)

#graph it
Button(mainframe, text="Graph It!", command=main).grid(row = 13, column = 1)

root.mainloop()