from tkinter import *
from tkinter import ttk


def addText():
    print("Adding")
    
def delText():
    print("Deleting")
    
def updateText():
    print("Updating")
    
def copyText():
    print("Copied")

def selectImage():
    print("Image selection")
    
def refText_Text(e):
    mainText_entry.delete(0, END)
    
def refText_Note(e):
    noteText_entry.delete(0, END)
    
#defining window
root = Tk()
root.title("Lazy Copy Tool V 1.0")
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#buttons and input boxes

mainText = StringVar()
mainText_entry = ttk.Entry(mainframe, width=18, textvariable=mainText)
mainText_entry.grid(row=0, column=0, padx=5, pady=10, columnspan=3, sticky=(W))
mainText_entry.insert(0, "Text")


noteText = StringVar()
noteText_entry = ttk.Entry(mainframe, width=18, textvariable=noteText)
noteText_entry.grid(row=0, column=0, padx=5, columnspan=3, sticky=(E))
noteText_entry.insert(0, "Notes")

# browse a file button 
ttk.Button(mainframe, text = "Image?",command = selectImage).grid(row=0, column=3, padx=5)

# Add, delete, update and copy buttons
ttk.Button(mainframe, text = "Add",command = addText).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(mainframe, text = "Delete",command = delText).grid(row=1, column=1, padx=5)
ttk.Button(mainframe, text = "Update",command = updateText).grid(row=1, column=2, padx=5)
ttk.Button(mainframe, text = "Copy",command = copyText).grid(row=1, column=3, padx=5)



'''
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
mainText_entry.focus()
root.bind("<Return>", addText)
'''

mainText_entry.bind("<FocusIn>", refText_Text)
noteText_entry.bind("<FocusIn>", refText_Note)

root.mainloop()
