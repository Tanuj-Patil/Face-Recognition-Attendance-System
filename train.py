from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # Title   
        title_lbl = Label(self.root, text="Data Train Module", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)   

        # Image 1 
        img_top = Image.open(r"D:\YT-FRAS\college_images\dnpcoe.jpg")
        img_top = img_top.resize((765, 150))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=70, width=765, height=150)
     
        # Image 2   
        img_right = Image.open(r"D:\YT-FRAS\college_images\dnpcoe.jpg")
        img_right = img_right.resize((750, 150))
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(self.root, image=self.photoimg_right)
        f_lbl.place(x=770, y=70, width=765, height=150)
        
        # Train Data button
        b1_1 = Button(self.root, text="Train Data",command=self.train_classifier, cursor="hand2", font=("times new roman", 25, "bold"), bg="green", fg="white")
        b1_1.place(x=0, y=240, width=1530, height=50)
        
        # Image 3
        img_bottom = Image.open(r"D:\YT-FRAS\college_images\bg.jpg")
        img_bottom = img_bottom.resize((1530, 490))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=310, width=1530, height=490)
    
    # Train data function 
    def train_classifier(self):
        data_dir = ("data")    
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        
        for image in path:
            img = Image.open(image).convert('L')  # Gray scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13       
        ids = np.array(ids)

        # ==================== Train Classifier ======================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed!!!")
            

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()