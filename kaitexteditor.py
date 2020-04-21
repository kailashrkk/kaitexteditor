from tkinter import *
from tkinter.filedialog import *

filename=None

def saveFile():
	"""
	func to save file as untitled
	"""
	global filename
	if not filename:
		filename = 'Untitled 2'
	t = text.get(0.0, END)
	f = open(filename, 'w')
	try:
		f.write(t.rstrip())
	except:
		showerror("There was an error in saving")
	finally:
		f.close()

def openFile():
	"""
	func to save file as untitled 
	"""
	f = askopenfile(mode='r')
	t =  f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)

def saveAsFile():
	"""
	func to save as file as a different extension or in a new path as needed
	"""
	f = asksaveasfile(mode='w', defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror("There was an error in saving")

def newFile():
	"""
	func to new file
	"""
	global filename
	filename = 'Untitled'
	text.delete(0.0, END)


root = Tk()
root.title("Kai Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As..", command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
