# 🎓 Student Management System

A simple **command-line Student Management System** built in Python with colorful terminal output using `colorama`. It allows you to add, view, search, update, and delete student records, along with extra features like report cards, topper detection, and average marks calculation. All data is stored persistently in a local `students.json` file.

---

## ✨ Features

- ➕ **Add Student** – Add a new student with ID, name, age, course, and marks
- 📋 **View Students** – List all students with their grades
- 🔍 **Search Student** – Find a student by ID
- ✏️ **Update Student** – Edit existing student details (leave blank to keep old value)
- ❌ **Delete Student** – Remove a student record
- 🔢 **Total Students** – Show total number of students
- 🧾 **Report Card** – Generate a formatted report card for a student
- 🏆 **View Topper** – Show the student with the highest marks
- 📊 **Average Marks** – Calculate the average marks of all students
- 🎨 **Colored Terminal Output** – Clean, color-coded UI using `colorama`
- 💾 **Persistent Storage** – Data is saved automatically to `students.json`

---

## 📦 Requirements

- Python 3.7+
- [`colorama`](https://pypi.org/project/colorama/)

Install the dependency:

```bash
pip install colorama
```

---

## 🚀 Getting Started

1. Clone the repository

   ```bash
   git clone https://github.com/<your-username>/student-management-system.git
   cd student-management-system
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Run the program

   ```bash
   python student_management.py
   ```

---

## 🖥️ Usage

On running the program, you'll see a menu like this:

```
=============================================
     STUDENT MANAGEMENT SYSTEM
=============================================
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Total Students
7. Report Card
8. View Topper
9. Average Marks
10. Exit

Enter Choice :
```

Simply enter the number corresponding to the action you want to perform.

---

## 📁 Project Structure

```
student-management-system/
│
├── student_management.py   # Main application file
├── students.json            # Auto-generated data file (created on first run)
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```

---

## 🧮 Grading Scale

|
 Marks Range 
|
 Grade 
|
|
-------------
|
-------
|
|
 90 - 100    
|
 A+    
|
|
 80 - 89     
|
 A     
|
|
 70 - 79     
|
 B     
|
|
 60 - 69     
|
 C     
|
|
 50 - 59     
|
 D     
|
|
 Below 50    
|
 F     
|

---

## 🛠️ Built With

- **Python** – Core language
- **colorama** – Terminal text coloring
- **json** – Data persistence

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork this repo and submit a pull request.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
