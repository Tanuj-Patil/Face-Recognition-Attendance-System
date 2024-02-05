from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_re import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import os
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0") 
        self.root.title("Face Recognition System")
        
        # Image 1
        # r is used to convert \ to /, because in python we use / for images path 
        img = Image.open(r"D:\YT-FRAS\college_images\dnpcoe.jpg")
        
        # to set the size, Antialias converts high resolution img to low resolution
        # Here i have removed ->  img = img.resize((500, 130), Image.ANTIALIAS)
        img = img.resize((510, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=510, height=130)
        
        # Image 2
        img1 = Image.open(r"D:\YT-FRAS\college_images\img2.jpg")
        img1 = img1.resize((510, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=510, y=0, width=510, height=130)

        # Image 3
        img2 = Image.open(r"D:\YT-FRAS\college_images\dnpcoe2.jpg")
        img2 = img2.resize((510, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1020, y=0, width=510, height=130)

        # Background-Image
        img3 = Image.open(r"D:\YT-FRAS\college_images\bg.jpg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)
        
        # Title 
        title_lbl = Label(bg_img, text="Face Recognition Attendance System", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # =============== Time function ================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl = Label(title_lbl, font=('times new roman', 14, 'bold'), background='white', foreground='blue')
        lbl.place(x=0, y=0, width=110, height=50)
        time()
        
        
        # Modules buttons on Main page
        
        # Student details button
        img4 = Image.open(r"D:\YT-FRAS\college_images\student-img1.png")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)       
        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        b1_1 = Button(bg_img, text="STUDENT DETAILS", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)
        
        # Detect Face button
        img5 = Image.open(r"D:\YT-FRAS\college_images\face_recog.jpg")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_img, image=self.photoimg5,command=self.face_data, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)
        b2_1 = Button(bg_img, text="FACE RECOGNITION",command=self.face_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b2_1.place(x=500, y=300, width=220, height=40)
        
        # Attendance button
        img6 = Image.open(r"D:\YT-FRAS\college_images\attendance_system.jpg")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(bg_img, image=self.photoimg6, command=self.attendance_data, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)
        b3_1 = Button(bg_img, text="ATTENDANCE", command=self.attendance_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b3_1.place(x=800, y=300, width=220, height=40)
        
        # Help Desk button
        img7 = Image.open(r"D:\YT-FRAS\college_images\help_desk.jpg")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 = Button(bg_img, image=self.photoimg7,command=self.help_desk, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)
        b4_1 = Button(bg_img, text="HELP DESK",command=self.help_desk, cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b4_1.place(x=1100, y=300, width=220, height=40)
        
        # Train face button
        img8 = Image.open(r"D:\YT-FRAS\college_images\train_img.jpg")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)       
        b5 = Button(bg_img, image=self.photoimg8,command=self.train_data, cursor="hand2")
        b5.place(x=200, y=380, width=220, height=220)    
        b5_1 = Button(bg_img, text="TRAIN DATA",command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b5_1.place(x=200, y=580, width=220, height=40)
        
        # Photos button
        img9 = Image.open(r"D:\YT-FRAS\college_images\photos.png")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)       
        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b6.place(x=500, y=380, width=220, height=220)      
        b6_1 = Button(bg_img, text="PHOTOS", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b6_1.place(x=500, y=580, width=220, height=40)
        
        # Developer button
        img10 = Image.open(r"D:\YT-FRAS\college_images\logo-tanuj.jpeg")
        img10 = img10.resize((220, 220))
        self.photoimg10 = ImageTk.PhotoImage(img10)       
        b7 = Button(bg_img, image=self.photoimg10,command=self.developer_data, cursor="hand2")
        b7.place(x=800, y=380, width=220, height=220)       
        b7_1 = Button(bg_img, text="DEVELOPER",command=self.developer_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b7_1.place(x=800, y=580, width=220, height=40)
        
        # Exit button
        img11 = Image.open(r"D:\YT-FRAS\college_images\exit.jpg")
        img11 = img11.resize((220, 220))
        self.photoimg11 = ImageTk.PhotoImage(img11)        
        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b8.place(x=1100, y=380, width=220, height=220)     
        b8_1 = Button(bg_img, text="EXIT", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b8_1.place(x=1100, y=580, width=220, height=40)
        
    def open_img(self):
        os.startfile("data")
    
    # Exit button function
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Do you want to exit this project?", parent = self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return 
    
    # ======== Function buttons =========
    
    # Student details function
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
    # Train data function 
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    # Face Detection function
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
    
    # attendance Function
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
    
    # developer function
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
    
    # Help Desk function
    def help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)
    

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()