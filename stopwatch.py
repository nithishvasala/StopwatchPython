#stopwatch - tkinter -20-09-2020
#2nd project - Nithish vasala

# import required modules
from tkinter import *
from datetime import datetime

# setting initial delay
counter = 66600
running = False #setting running false - as not running

def counter_label(label):
	def count(): 
		if running: 
			global counter 
	
			# To manage the intial delay. 
			if counter==66600:			 
				display="00:00:00"
			else: 
				tt = datetime.fromtimestamp(counter) 
				string = tt.strftime("%H:%M:%S") 
				display=string 
	
			label['text']=display 
			label.after(1000, count) 
			counter += 1
	
	count()	 

# start function
def Start(label): 
	global running 
	running=True
	counter_label(label) 
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'

# stop function
def Stop(): 
	global running 
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	running = False
	
#Reset function
def Reset(label): 
	global counter #setting as global so we can access from anywhere
	global running 
	counter=66600
	
	if running==False:	 
		reset['state']='disabled'
		label['text']='00:00:00'
	else:
		start['state']='normal'
		stop['state']='disabled'
		reset['state']='normal'
		running = False
		reset['state']='disabled'
		label['text']='00:00:00'
	
# tkinter GUI
root = Tk() 
root.title("Stopwatch") 
	
# Fixing the window size. 
root.minsize(width=250, height=70)

root.configure(background="lightslategray")

label = Label(root, text="00:00:00", fg="black", font="Verdana 30 bold", background="lightslategray")
label.pack(padx=10, pady=30)

root.geometry("400x250")

p1 = PhotoImage(file = 'Screenshots/index.png')
root.iconphoto(False, p1)

f = Frame(root, background="lightslategray") 
start = Button(f, text='Start',height=2, width=10, command=lambda:Start(label)) 
stop = Button(f, text='Stop',height=2, width=10,state='disabled', command=Stop) 
reset =Button(f, text='Reset',height=2,width=10, state='disabled', command=lambda:Reset(label))  
f.pack(anchor = 'center',pady=5) 

start.pack(side = LEFT, padx=10, pady=10)
stop.pack(side = LEFT, padx=10, pady=10)
reset.pack(side = LEFT, padx=10, pady=10)

root.resizable(0,0)

root.mainloop()

