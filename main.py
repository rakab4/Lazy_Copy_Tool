from ast import Global
from cgitb import text
from email.mime import image
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from types import CellType
from PIL import Image, ImageTk
from imageDB import Database
from io import BytesIO
from tkinter import messagebox


# define connection to image database

db = Database('imageDB.db')

def readData():
    clearTreeview()
    for row in db.fetch():
        tree.insert(parent='', index='end', iid=row, text='',values=(row[0],row[1],row[2]))

def readSelectedData():
    print("Read treeview selected data from database")

def selectFromTreeview(event):
    mainText_entry.delete(0, END)
    noteText_entry.delete(0, END)

    global selected_text
    index = tree.focus()
    selected_text = tree.item(index, 'values')
    mainText_entry.insert(END, selected_text[1])
    noteText_entry.insert(END, selected_text[2])
    #print(selected_text[0])
    if selected_text[0] == '':
        retriveNoImg()
    else:
        #retriveNoImg()
        retriveImage(selected_text[0])

def retriveNoImg():
    noImageData = db.fetchNoImg(0)
    binaryToImage(noImageData)


def refText_Text(e):
    mainText_entry.delete(0, END)
    
def refText_Note(e):
    noteText_entry.delete(0, END)

def clearEntry():
    mainText_entry.delete(0, END)
    mainText_entry.insert(0, 'Text')
    noteText_entry.delete(0, END)
    
    noteText_entry.insert(0, 'Notes')

def clearTreeview():
    for record in tree.get_children():
        tree.delete(record)

def addText():
    global imageName
    if mainText_entry.get() == "Text" or noteText_entry.get() == "Notes" or mainText_entry.get() == "" or noteText_entry.get() == "":
        messagebox.showerror('What ??', 'Please enter correct and all details !!')
        return
    try:
        imageData = convertImgToBinary(imageName)
    except:
        imageData = noImageBlobDataFn()
    db.insert(mainText_entry.get(), noteText_entry.get(), imageData)
    clearEntry()
    readData()
    print(imageName)
    imageName = ''


    
def delText():
    db.delete(selected_text[0])
    readData()
    
def updateText():
    global imageName
    try:
        imageData = convertImgToBinary(imageName)
    except:
        imageData = db.fetchOne(selected_text[0])
    db.update(selected_text[0],mainText_entry.get(), noteText_entry.get(), imageData)
    readData()
    imageName = ''

def copyText():
    print("Copied")

def selectImage():
    global imageName
    imageName = filedialog.askopenfilename(initialdir= "/", title= "Select an image to upload", filetypes=(("png files", "*.PNG"),("jpeg files", "*.jpeg"),("All files","*.*")))
    print(imageName)
    label = ttk.Label(mainframe, text="")
    label.configure(text= imageName)
    if imageName == '':
        imageName = 'noImage'
    
def noImageBlobDataFn():
    noImageBlobData = db.fetchNoImg(0)
    return noImageBlobData
    

def convertImgToBinary(imageName):
    with open(imageName, 'rb') as file:
        blobData = file.read()
    print(imageName)
    imageName = "/"
    return blobData

def binaryToImage(data):
    img_date = BytesIO(data)
    img = Image.open(img_date)
    size = 180
    img = img.resize((size, size))
    photo = ImageTk.PhotoImage(img)
    imageLabel = Label(mainframe, image=photo)
    imageLabel.image = photo
    imageLabel.grid(row=2, column=0, columnspan=2, sticky=W, padx=20)

def retriveImage(id_no):
    imageData = db.fetchOne(id_no)
    binaryToImage(imageData)
    
    
    

    
# defining window
root = Tk()
root.title("Lazy Copy Tool V 1.0")
root.geometry('500x350')
root.resizable(False, False)
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# buttons and input boxes

mainText = StringVar()
mainText_entry = ttk.Entry(mainframe, width=18, textvariable=mainText)
mainText_entry.grid(row=0, column=0, padx=20, columnspan=3, pady=10, sticky=(W))
mainText_entry.insert(0, "Text")


noteText = StringVar()
noteText_entry = ttk.Entry(mainframe, width=18, textvariable=noteText)
noteText_entry.grid(row=0, column=0, padx=5, columnspan=3, sticky=(E))
noteText_entry.insert(0, "Notes")

# browse a file button 
ttk.Button(mainframe, text = "Image?",command = selectImage).grid(row=0, column=3, padx=5)

# Add, delete, update and copy buttons
ttk.Button(mainframe, text = "Add",command = addText).grid(row=1, column=0, padx=20, pady=5, sticky=(W))
ttk.Button(mainframe, text = "Delete",command = delText).grid(row=1, column=1, padx=5)
ttk.Button(mainframe, text = "Update",command = updateText).grid(row=1, column=2, padx=5, sticky=(E))
ttk.Button(mainframe, text = "Copy",command = copyText).grid(row=1, column=3, padx=5)

# define list treeview

tree = ttk.Treeview(mainframe)
tree["column"]=('id', 'text','notes')
tree.column("#0", width=0, stretch=NO)
tree.column('id', anchor=CENTER, width=30, minwidth=25)
tree.column('text', anchor=CENTER, width=100, minwidth=25)
tree.column('notes', anchor=CENTER, width=100, minwidth=25)

tree.heading('#0', text='')
tree.heading('id', text='ID', anchor=CENTER)
tree.heading('text', text='Text to copy', anchor=CENTER)
tree.heading('notes', text='Notes', anchor=CENTER)
tree.grid(row=2, column=2, columnspan=2, padx=20, sticky='W')


tree.bind('<ButtonRelease-1>', selectFromTreeview)
readData()
focusID = tree.get_children()
if focusID:
    tree.focus(focusID[0])
    tree.selection_set(focusID[0])
    #retriveImage(focusID[0][0])


#retriveImage(selected_text[0])


mainText_entry.bind("<FocusIn>", refText_Text)
noteText_entry.bind("<FocusIn>", refText_Note)



madeBy = Label(root, text="Developed by Rinkesh Patel with Love !!")
madeBy.grid(row=4, column=0, columnspan=4, pady=5)
root.mainloop()
