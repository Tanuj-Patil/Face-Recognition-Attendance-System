from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # Variables declaration
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        
        # Image 1
        img = Image.open(r"D:\YT-FRAS\college_images\dnpcoe.jpg")
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
        title_lbl = Label(bg_img, text="Students", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        main_frame = Frame(bg_img, bd=2,bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)
        
        # Left frame label
        Left_frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 13, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)       
        img_left = Image.open(r"D:\YT-FRAS\college_images\dnpcoe.jpg")
        img_left = img_left.resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)
        
        # Current course
        current_course_frame = LabelFrame(Left_frame, bd=2,bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 13, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=115)
        
        # Department
        dep_label = Label(current_course_frame, text="Department",font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman", 13, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        # Course
        course_label = Label(current_course_frame, text="Course",font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 13, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "FY", "SY", "TY", "Final Year")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        
        # Year
        year_label = Label(current_course_frame, text="Year",font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        
        # Semester
        semester_label = Label(current_course_frame, text="Semester",font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 13, "bold"), state="readonly")
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        
        # Student Class Information
        Class_Student_frame = LabelFrame(Left_frame, bd=2,bg="white", relief=RIDGE, text="Student Class Information", font=("times new roman", 13, "bold"))
        Class_Student_frame.place(x=5, y=250, width=720, height=300)
        
        #  student ID
        studentId_label = Label(Class_Student_frame, text="StudentID:",font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)       
        studentId_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_std_id, width=20, font=("times new roman", 13, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        #  student name
        studentName_label = Label(Class_Student_frame, text="Student Name:",font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)       
        studentName_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        #  Class Division
        class_div_label = Label(Class_Student_frame, text="Class Division:",font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W) 
        div_combo = ttk.Combobox(Class_Student_frame,textvariable=self.var_div,  width=18, font=("times new roman", 13, "bold"), state="readonly")
        div_combo["values"] = ("T1", "T2", "T3")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        #  Roll no
        roll_no_label = Label(Class_Student_frame, text="Roll No:",font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)       
        roll_no_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
        # Gender
        gender_label = Label(Class_Student_frame, text="Gender:",font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(Class_Student_frame,textvariable=self.var_gender, width=18,font=("times new roman", 13, "bold"), state="readonly")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        
        # DOB
        dob_label = Label(Class_Student_frame, text="DOB:",font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)       
        dob_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        
        # Email
        email_label = Label(Class_Student_frame, text="E-mail:",font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)        
        email_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        # Phone no
        phone_label = Label(Class_Student_frame, text="Phone No:",font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)      
        phone_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        
        # Address
        address_label = Label(Class_Student_frame, text="Address:",font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)        
        address_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_address, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        
        # Teacher Name
        teacher_label = Label(Class_Student_frame, text="Teacher Name:",font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)       
        teacher_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        
        # Radio button1
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)
        
        # Radio button2
        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)
        
        # buttons frame
        btn_frame = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=3, y=200, width=710 , height=35)       
        
        # buttons
        save_btn = Button(btn_frame, text="Save",command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        
        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
        
        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)
        
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)
        
        # Take Photo Button Frame 
        btn_frame1 = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=3, y=235, width=710 , height=35)       
        take_photo_btn = Button(btn_frame1,command=self.call_both, text="Take Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)       
        update_btn = Button(btn_frame1, text="Update Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
            
        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 13, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)      
        img_right = Image.open(r"D:\YT-FRAS\college_images\dnpcoe.jpg")
        img_right = img_right.resize((720, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)
        
        # ========== Search System ===========
        Search_frame = LabelFrame(Right_frame, bd=2,bg="white", relief=RIDGE, text="Search System", font=("times new roman", 13, "bold"))
        Search_frame.place(x=3, y=135, width=710, height=70)
               
        search_label = Label(Search_frame, text="Search by:",font=("times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 13, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        search_entry = ttk.Entry(Search_frame, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        search_btn = Button(Search_frame, text="Search", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)
        
        showAll_btn = Button(Search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)
        
        # ========= Table Frame =========
        table_frame = Frame(Right_frame, bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=3, y=210, width=710, height=350)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)  
             
        self.student_table = ttk.Treeview(table_frame, columns=("Dep", "Course", "Year", "Sem", "Id", "Name", "Div", "Roll", "Gender", "DOB", "Email", "Phone", "Address", "Teacher", "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)       
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Id", text="StudentId")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Div", text="Division")
        self.student_table.heading("Roll", text="RollNo")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="E-mail")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("Photo", text="PhotoSampleSatus")
        self.student_table["show"] = "headings"
        
        self.student_table.column("Dep", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("Id", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Div", width=100)
        self.student_table.column("Roll", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Teacher", width=100)
        self.student_table.column("Photo", width=150)       
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # =========== Function Declaration ===========
    
    # =========== Add data Function ===========
    def add_data(self):  
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "Tanuj05@", database = "face_recognizer", port = 3306)
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added Successfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent = self.root)
                
    # =========== fetch data Function ===========
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "Tanuj05@", database = "face_recognizer", port = 3306)
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete( * self.student_table.get_children())

            for i in data :
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    # ============ get cursor Function ============
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus() 
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
               
    # function for take photo sample in which both functions will be called
    def call_both(self):
        self.add_data()
        self.generate_dataset()
               
    # ============= update function =============
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent = self.root)    
                if Update > 0:
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = "Tanuj05@", database = "face_recognizer",port = 3306)
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep = %s, Course = %s, Year = %s, Semester = %s, Name = %s, Division = %s, Roll = %s, Gender = %s, Dob = %s, Email = %s, Phone = %s, Address = %s, Teacher = %s, PhotoSample = %s where Student_id = %s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                        ))
                else:
                    if not Update:
                        return  
                messagebox.showinfo("Success", "Student details successfully updated!", parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent = self.root)    
                
    
    # ============= Delete function =============
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required", parent=self.root)
        else:
            try: 
                delete = messagebox.askyesno("Student Details Delete Page","Do you want to deelete this student details", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = "Tanuj05@", database = "face_recognizer",port = 3306)
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return 
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details", parent=self.root)         
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent = self.root)    
                
    # ============= reset data function =============            
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
    # ================= Generate data set Take Photo Samples ==================  
    # Generate dataset function
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        else:
            try:   
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "Tanuj05@", database = "face_recognizer",port = 3306)
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                    
                my_cursor.execute("update student set Dep = %s, Course = %s, Year = %s, Semester = %s, Name = %s, Division = %s, Roll = %s, Gender = %s, Dob = %s, Email = %s, Phone = %s, Address = %s, Teacher = %s, PhotoSample = %s where Student_id = %s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1
                ))                   
                conn.commit()    
                self.fetch_data()
                self.reset_data()
                conn.close()
                    
                # ================= Load predifined data on frontal face from opencv ================                   
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                # function for cropped face
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # 1.3 means scalling factor
                    # 5 here means minimum neighbour   
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                        
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id),(50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed successfully!!!")                   
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent = self.root)         
        
                
                
                                    
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()