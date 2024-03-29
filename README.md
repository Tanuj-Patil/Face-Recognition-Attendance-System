# Face Recognition Attendance System

The Face Recognition Attendance System is a Python-based application that offers an efficient solution for managing student attendance using facial recognition technology. This system provides a user-friendly graphical interface for importing, viewing, updating, and exporting attendance records.

## Key Features:

- **Face Detection and Recognition:** Utilizes OpenCV for face detection and LBPH (Local Binary Patterns Histograms) Face Recognizer for face recognition.
- **Graphical User Interface (GUI):** Implemented using Tkinter, providing an intuitive interface for users to interact with the system.
- **Attendance Management:** Allows for importing attendance data from CSV files, viewing student attendance records, updating attendance status, and exporting attendance data to CSV files.
- **Data Training:** Includes functionality for training the face recognition model using student images.

## How It Works:

1. **Face Detection and Recognition:**
   - The system uses OpenCV to detect faces in images and LBPH Face Recognizer to recognize faces based on patterns.
   - Images are converted to grayscale for better processing efficiency.

2. **Graphical User Interface (GUI):**
   - Implemented using Tkinter, the GUI provides an intuitive interface for users to interact with the system.
   - Users can import attendance data, view student records, update attendance status, and export data to CSV files.

3. **Attendance Management:**
   - Users can import attendance data from CSV files, which includes student IDs, rolls, names, departments, timestamps, and attendance status.
   - The system allows for viewing student attendance records, updating attendance status (Present/Absent), and resetting data if needed.
   - Attendance records can be exported to CSV files for further analysis or record-keeping purposes.

4. **Data Training:**
   - The system includes functionality for training the face recognition model using images of students' faces.
   - Images are collected and stored in a directory (`data/`), and the `train.py` script is used to train the model and save it as `classifier.xml`.

## Getting Started:

1. **Clone the Repository:**
   - Clone the repository to your local machine using the following command:
     ```
     git clone https://github.com/Tanuj-Patil/Face-Recognition-Attendance-System.git
     ```

2. **Install Dependencies:**
   - Install the required dependencies listed in `requirements.txt` using pip:
     ```
     pip install -r requirements.txt
     ```

3. **Train the Face Recognition Model:**
   - Run the `train.py` script to train the face recognition model.
   
4. **Launch the Attendance Management Interface:**
   - Run the `attendance.py` script to launch the attendance management interface.

5. **Interact with the GUI:**
   - Use the GUI to manage attendance records, including importing data, viewing records, updating status, and exporting data.

## Requirements:

- Python 3.x
- Tkinter
- OpenCV
- PIL (Python Imaging Library)
- MySQL Connector (optional, for database integration)

## Contributors:

- [Tanuj Patil](https://github.com/Tanuj-Patil)

## License:

This project is licensed under the [MIT License](LICENSE).

---

This README provides an overview of the Face Recognition Attendance System, describing its features, functionality, and how to get started with the project.
