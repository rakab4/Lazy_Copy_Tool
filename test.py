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

import sqlite3

def image():
    img = "C:\\Users\\rinke\\Desktop\\Dev\\Lazy_Copy_Tool\\noImg.jpg"
    with open(img, 'rb') as file:
        blobData = file.read()
    return blobData

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS noImgDB (id INTEGER PRIMARY KEY AUTOINCREMENT, str TEXT, notes TEXT, image BLOB)")
        self.conn.commit()
        #self.cur.execute("DELETE FROM dropTable WHERE id=?", (0,))
        #self.cur.execute("DROP TABLE noImgDB")
        #self.conn.commit()
        imageDate = image()
        #self.cur.execute("INSERT INTO noImgDB VALUES ('0', 'str', 'notes', ?)",(imageDate,))
        self.cur.execute("INSERT INTO dropTable ('0', 'image') SELECT ('0', 'image') FROM noImgDB")
        self.conn.commit()

    def __del__(self):
        self.conn.close()




db = Database('imageDB.db')
