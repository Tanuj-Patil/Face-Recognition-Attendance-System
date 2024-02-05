# Note in use

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="Face Recognition Module", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # 1 img
        img_top = Image.open(r"D:\YT-FRAS\college_images\face_frame_left.jpg")
        img_top = img_top.resize((650, 700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)
        
        # 2 img
        img_bottom = Image.open(r"D:\YT-FRAS\college_images\face_frame.jpg")
        img_bottom = img_bottom.resize((950, 700))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition",command=self.face_recog, cursor="hand2", font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=365, y=620, width=200, height=40)

        # Face Recognition function
    try:
        def face_recog(self):
            def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
                
                coord=[]
                for (x,y,w,h) in features:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
                    
                    # Here predict method is not supported!!!
                    id,predict = clf.predict(gray_image[y:y+h, x:x+w])
                    confidence = int((100*(1-predict/300)))
                    
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = "Tanuj05@", database = "face_recognizer")
                    my_cursor = conn.cursor()
                    
                    # my_cursor.execute("select Student_id from student where Student_id="+str(id))
                    # i = my_cursor.fetchone()
                    # i ="+".join(i)
                    
                    
                    # For Student Id
                    my_cursor.execute("SELECT Student_id FROM student WHERE Student_id = " + str(id))
                    i = my_cursor.fetchone()

                    if i is not None:
                        # Convert the tuple to a string and then join the elements
                        i = "+".join(str(x) for x in i)
                    else:
                        # Handle the case where no row is fetched (i.e., i is None)
                        i = "No data found"

                    # Now, i contains the joined string or an appropriate message if no data is found
                    # print(i)
                    # i = "+".join(str(x) for x in i)


                    # For Name 
                    # my_cursor.execute("select Name from student where Student_id="+str(id))
                    # n = my_cursor.fetchone()
                    # n ="+".join(n)
                    # n = "+".join(str(x) for x in n)
                    my_cursor.execute("SELECT Name FROM student WHERE Student_id = " + str(id))
                    n = my_cursor.fetchone()

                    if n is not None:
                        # Convert the tuple to a string and then join the elements
                        n = "+".join(str(x) for x in n)
                    else:
                        # Handle the case where no row is fetched (i.e., n is None)
                        n = "No data found"
                    
                    
                    # For Roll number
                    # my_cursor.execute("select Roll from student where Student_id="+str(id))
                    # r = my_cursor.fetchone()
                    # r ="+".join(r)
                    # r = "+".join(str(x) for x in r)
                    my_cursor.execute("SELECT Roll FROM student WHERE Student_id = " + str(id))
                    r = my_cursor.fetchone()

                    if r is not None:
                        # Convert the tuple to a string and then join the elements
                        r = "+".join(str(x) for x in r)
                    else:
                        # Handle the case where no row is fetched (i.e., i is None)
                        r = "No data found"
                    
                    # For Department
                    # my_cursor.execute("select Dep from student where Student_id="+str(id))
                    # d = my_cursor.fetchone()
                    # d ="+".join(d)
                    # d = "+".join(str(x) for x in d)
                    my_cursor.execute("SELECT Dep FROM student WHERE Student_id = " + str(id))
                    d = my_cursor.fetchone()

                    if d is not None:
                        # Convert the tuple to a string and then join the elements
                        d = "+".join(str(x) for x in d)
                    else:
                        # Handle the case where no row is fetched (i.e., i is None)
                        d = "No data found"

                    
                    if confidence > 77:
                        cv2.putText(img, f"ID:{i}", (x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                        cv2.putText(img, f"Roll:{r}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                        cv2.putText(img, f"Name:{n}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                        cv2.putText(img, f"Dep:{d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    else:
                        cv2.rectangle(img,(x,y), (x+w, y+h), (0,0,255), 3)
                        cv2.putText(img, "Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    
                    coord=[x,y,w,h]   
                    # coord=[x,y,w,y]
                    
                return coord
            
            def recognize(img, clf, faceCascade):
                coord = draw_boundray(img, faceCascade, 1.1, 10,(255,255,255),"Face", clf)   
                return img

            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap = cv2.VideoCapture(0)
            
            while True:
                ret, img = video_cap.read()
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome To Face Recognition", img)

                if cv2.waitKey(1)==13:
                    break
                
            video_cap.release()
            cv2.destroyAllWindows()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)
    except cv2.error as e:
        print("OpenCV Error:", e)
    except Exception as e:
        print("Error:", e)
  

        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()