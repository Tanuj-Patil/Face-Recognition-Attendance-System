from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # Title
        title_lbl = Label(self.root, text="Help Desk Module", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # Image 1
        img1 = Image.open(r"D:\YT-FRAS\college_images\help_desk_bg.jpg")
        img1 = img1.resize((1530, 720))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # Developer Label
        dev1_label = Label(f_lbl, text="Email: tanujpatil9561@gmail.com",font=("times new roman", 35, "bold"), bg="black", fg="red")
        dev1_label.place(x=450 ,y=250)
        dev2_label = Label(f_lbl, text="Instagram: i_patil_tanuj",font=("times new roman", 28, "bold"), bg="black", fg="red")
        dev2_label.place(x=450 ,y=310)
        dev3_label = Label(f_lbl, text="LinkedIn: Tanuj Patil",font=("times new roman", 28, "bold"), bg="black", fg="red")
        dev3_label.place(x=450 ,y=360)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()