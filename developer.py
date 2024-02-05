from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # Title
        title_lbl = Label(self.root, text="Developer Module", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # Image 1
        img1 = Image.open(r"D:\YT-FRAS\college_images\developer.jpg")
        img1 = img1.resize((1530, 720))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=55, width=1530, height=720)
       
        # Main frame
        main_frame = Frame(f_lbl, bd=2,bg="lightgreen")
        main_frame.place(x=900, y=0, width=600, height=730)

        # Image 2
        img2 = Image.open(r"D:\YT-FRAS\college_images\logo-tanuj.jpeg")
        img2 = img2.resize((200, 200))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=380, y=0, width=200, height=200)

        # Developer information
        dev1_label = Label(main_frame, text="Hello I'm Tanuj Patil",font=("times new roman", 22, "bold"), bg="black", fg="orange")
        dev1_label.place(x=10 ,y=55)        
        dev2_label = Label(main_frame, text="I am a student at DNP COE",font=("times new roman", 22, "bold"), bg="black", fg="orange")
        dev2_label.place(x=10 ,y=100)

        # Image 3
        img3 = Image.open(r"D:\YT-FRAS\college_images\profile-pic-1.jpg")
        img3 = img3.resize((550, 480))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(main_frame, image=self.photoimg3)
        f_lbl.place(x=20, y=210, width=550, height=480)






if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()