# ==============================================
# Student Management System
# Fixed & Complete Version (with colorama)
# ==============================================

import json
import os
from colorama import Fore, Style, init

init(autoreset=True)


class Student:

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def calculate_grade(self):

        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def grade_color(self, grade):
        colors = {
            "A+": Fore.GREEN,
            "A": Fore.GREEN,
            "B": Fore.CYAN,
            "C": Fore.YELLOW,
            "D": Fore.YELLOW,
            "F": Fore.RED,
        }
        return colors.get(grade, Fore.WHITE)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
            "grade": self.calculate_grade()
        }

    def report_card(self):

        grade = self.calculate_grade()
        gcolor = self.grade_color(grade)

        print(Fore.CYAN + "=" * 40)
        print(Fore.CYAN + Style.BRIGHT + "            REPORT CARD")
        print(Fore.CYAN + "=" * 40)
        print(Fore.WHITE + f"Student ID : {self.student_id}")
        print(Fore.WHITE + f"Name       : {self.name}")
        print(Fore.WHITE + f"Age        : {self.age}")
        print(Fore.WHITE + f"Course     : {self.course}")
        print(Fore.WHITE + f"Marks      : {self.marks}")
        print(gcolor + Style.BRIGHT + f"Grade      : {grade}")
        print(Fore.CYAN + "=" * 40)


class StudentManager:

    def __init__(self):
        self.filename = "students.json"
        self.students = []
        self.load_students()

    def load_students(self):

        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)

                    for item in data:
                        student = Student(
                            item["student_id"],
                            item["name"],
                            item["age"],
                            item["course"],
                            item["marks"]
                        )
                        self.students.append(student)

            except Exception:
                self.students = []

    def save_students(self):

        data = [student.to_dict() for student in self.students]

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # ---------------- Add ----------------
    def add_student(self):

        print(Fore.CYAN + Style.BRIGHT + "\n===== Add Student =====")

        student_id = input("Enter Student ID : ").strip()

        for s in self.students:
            if s.student_id == student_id:
                print(Fore.RED + "Student ID already exists.")
                return

        name = input("Enter Name : ").strip()
        age = int(input("Enter Age : "))
        course = input("Enter Course : ").strip()
        marks = float(input("Enter Marks : "))

        student = Student(student_id, name, age, course, marks)

        self.students.append(student)
        self.save_students()

        print(Fore.GREEN + "\nStudent Added Successfully.")

    # ---------------- View ----------------
    def view_students(self):

        print(Fore.CYAN + Style.BRIGHT + "\n========= Student List =========")

        if len(self.students) == 0:
            print(Fore.YELLOW + "No Students Found")
            return

        for student in self.students:
            grade = student.calculate_grade()
            gcolor = student.grade_color(grade)

            print(Fore.CYAN + "-" * 40)
            print(Fore.WHITE + "ID     :", student.student_id)
            print(Fore.WHITE + "Name   :", student.name)
            print(Fore.WHITE + "Age    :", student.age)
            print(Fore.WHITE + "Course :", student.course)
            print(Fore.WHITE + "Marks  :", student.marks)
            print(gcolor + "Grade  :", grade)

        print(Fore.CYAN + "-" * 40)

    # ---------------- Search ----------------
    def search_student(self):

        print(Fore.CYAN + Style.BRIGHT + "\n===== Search Student =====")

        sid = input("Enter Student ID : ").strip()

        for student in self.students:
            if student.student_id == sid:
                grade = student.calculate_grade()
                gcolor = student.grade_color(grade)

                print(Fore.GREEN + "\nStudent Found")
                print(Fore.CYAN + "----------------------")
                print(Fore.WHITE + "ID :", student.student_id)
                print(Fore.WHITE + "Name :", student.name)
                print(Fore.WHITE + "Age :", student.age)
                print(Fore.WHITE + "Course :", student.course)
                print(Fore.WHITE + "Marks :", student.marks)
                print(gcolor + "Grade :", grade)
                return

        print(Fore.RED + "Student Not Found")

    # ---------------- Update ----------------
    def update_student(self):

        print(Fore.CYAN + Style.BRIGHT + "\n===== Update Student =====")

        sid = input("Enter Student ID : ").strip()

        for student in self.students:
            if student.student_id == sid:

                print(Fore.YELLOW + "\nLeave blank to keep old value.\n")

                name = input(f"Name ({student.name}) : ")
                if name != "":
                    student.name = name

                age = input(f"Age ({student.age}) : ")
                if age != "":
                    student.age = int(age)

                course = input(f"Course ({student.course}) : ")
                if course != "":
                    student.course = course

                marks = input(f"Marks ({student.marks}) : ")
                if marks != "":
                    student.marks = float(marks)

                self.save_students()

                print(Fore.GREEN + "\nStudent Updated Successfully.")
                return

        print(Fore.RED + "Student Not Found.")

    # ---------------- Delete ----------------
    def delete_student(self):

        print(Fore.CYAN + Style.BRIGHT + "\n===== Delete Student =====")

        sid = input("Enter Student ID : ").strip()

        for student in self.students:
            if student.student_id == sid:
                self.students.remove(student)
                self.save_students()
                print(Fore.GREEN + "\nStudent Deleted Successfully.")
                return

        print(Fore.RED + "Student Not Found.")

    # ---------------- Total ----------------
    def total_students(self):
        print(Fore.CYAN + Style.BRIGHT + "\nTotal Students :", len(self.students))

    # ---------------- Report Card ----------------
    def report_card(self):

        print(Fore.CYAN + Style.BRIGHT + "\n===== Report Card =====")

        sid = input("Enter Student ID : ").strip()

        for student in self.students:
            if student.student_id == sid:
                student.report_card()
                return

        print(Fore.RED + "Student Not Found")

    # ---------------- Topper ----------------
    def topper(self):

        if len(self.students) == 0:
            print(Fore.YELLOW + "No Students Available")
            return

        top = max(self.students, key=lambda s: s.marks)
        grade = top.calculate_grade()
        gcolor = top.grade_color(grade)

        print(Fore.MAGENTA + Style.BRIGHT + "\n" + "=" * 40)
        print(Fore.MAGENTA + Style.BRIGHT + "🏆  TOPPER")
        print(Fore.MAGENTA + Style.BRIGHT + "=" * 40)
        print(Fore.WHITE + "Name  :", top.name)
        print(Fore.WHITE + "Marks :", top.marks)
        print(gcolor + "Grade :", grade)

    # ---------------- Average ----------------
    def average_marks(self):

        if len(self.students) == 0:
            print(Fore.YELLOW + "No Students")
            return

        total = sum(student.marks for student in self.students)
        average = total / len(self.students)

        print(Fore.CYAN + Style.BRIGHT + "\n" + "=" * 40)
        print(Fore.WHITE + "Average Marks :", round(average, 2))
        print(Fore.CYAN + Style.BRIGHT + "=" * 40)


def menu():

    manager = StudentManager()

    while True:

        print("\n")
        print(Fore.BLUE + Style.BRIGHT + "=" * 45)
        print(Fore.BLUE + Style.BRIGHT + "     STUDENT MANAGEMENT SYSTEM")
        print(Fore.BLUE + Style.BRIGHT + "=" * 45)

        print(Fore.WHITE + "1. Add Student")
        print(Fore.WHITE + "2. View Students")
        print(Fore.WHITE + "3. Search Student")
        print(Fore.WHITE + "4. Update Student")
        print(Fore.WHITE + "5. Delete Student")
        print(Fore.WHITE + "6. Total Students")
        print(Fore.WHITE + "7. Report Card")
        print(Fore.WHITE + "8. View Topper")
        print(Fore.WHITE + "9. Average Marks")
        print(Fore.WHITE + "10. Exit")

        choice = input(Fore.YELLOW + "\nEnter Choice : ").strip()

        if choice == "1":
            try:
                manager.add_student()
            except ValueError:
                print(Fore.RED + "Invalid Input.")

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            manager.search_student()

        elif choice == "4":
            try:
                manager.update_student()
            except ValueError:
                print(Fore.RED + "Invalid Input.")

        elif choice == "5":
            manager.delete_student()

        elif choice == "6":
            manager.total_students()

        elif choice == "7":
            manager.report_card()

        elif choice == "8":
            manager.topper()

        elif choice == "9":
            manager.average_marks()

        elif choice == "10":
            print(Fore.GREEN + Style.BRIGHT + "\nThank You For Using Student Management System.")
            break

        else:
            print(Fore.RED + "Invalid Choice. Please Try Again.")


if __name__ == "__main__":
    menu()