# ==============================================
# Student Management System
# Part - 1
# ==============================================

import json
import os


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

    def to_dict(self):

        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
            "grade": self.calculate_grade()
        }


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

            except:

                self.students = []

    def save_students(self):

        data = []

        for student in self.students:
            data.append(student.to_dict())

        with open(self.filename, "w") as file:

            json.dump(data, file, indent=4)

    def add_student(self):

        print("\n===== Add Student =====")

        student_id = input("Enter Student ID : ")

        for s in self.students:

            if s.student_id == student_id:

                print("Student ID already exists.")
                return

        name = input("Enter Name : ")

        age = int(input("Enter Age : "))

        course = input("Enter Course : ")

        marks = float(input("Enter Marks : "))

        student = Student(
            student_id,
            name,
            age,
            course,
            marks
        )

        self.students.append(student)

        self.save_students()

        print("\nStudent Added Successfully.")

    def view_students(self):

        print("\n========= Student List =========")

        if len(self.students) == 0:

            print("No Students Found")

            return

        for student in self.students:

            print("-" * 40)

            print("ID     :", student.student_id)

            print("Name   :", student.name)

            print("Age    :", student.age)

            print("Course :", student.course)

            print("Marks  :", student.marks)

            print("Grade  :", student.calculate_grade())

        print("-" * 40)

    def search_student(self):

        print("\n===== Search Student =====")

        sid = input("Enter Student ID : ")

        for student in self.students:

            if student.student_id == sid:

                print("\nStudent Found")

                print("----------------------")

                print("ID :", student.student_id)

                print("Name :", student.name)

                print("Age :", student.age)

                print("Course :", student.course)

                print("Marks :", student.marks)

                print("Grade :", student.calculate_grade())

                return

        print("Student Not Found")
        
    def update_student(self):

        print("\n===== Update Student =====")

        sid = input("Enter Student ID : ")

        for student in self.students:

            if student.student_id == sid:

                print("\nLeave blank to keep old value.\n")

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

                print("\nStudent Updated Successfully.")

                return

        print("Student Not Found.")

    def delete_student(self):

        print("\n===== Delete Student =====")

        sid = input("Enter Student ID : ")

        for student in self.students:

            if student.student_id == sid:

                self.students.remove(student)

                self.save_students()

                print("\nStudent Deleted Successfully.")

                return

        print("Student Not Found.")

    def total_students(self):

        print("\nTotal Students :", len(self.students))


def menu():

    manager = StudentManager()

    while True:

        print("\n")
        print("=" * 45)
        print("     STUDENT MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Total Students")
        print("7. Report Card")
        print("8. View Topper")
        print("9. Average Marks")
        print("10. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            try:
                manager.add_student()
            except ValueError:
                print("Invalid Input.")

        elif choice == "2":

            manager.view_students()

        elif choice == "3":

            manager.search_student()

        elif choice == "4":

            try:
                manager.update_student()
            except ValueError:
                print("Invalid Input.")

        elif choice == "5":

            manager.delete_student()

        elif choice == "6":

            manager.total_students()

        elif choice == "7":

            print("\nThank You For Using Student Management System.")
            break

        else:

            print("Invalid Choice. Please Try Again.")


if __name__ == "__main__":

    menu()
from colorama import Fore, Style, init

init(autoreset=True)

def report_card(self):

    print("=" * 40)

    print("         REPORT CARD")

    print("=" * 40)

    print(f"Student ID : {self.student_id}")

    print(f"Name       : {self.name}")

    print(f"Age        : {self.age}")

    print(f"Course     : {self.course}")

    print(f"Marks      : {self.marks}")

    print(f"Grade      : {self.calculate_grade()}")

    print("=" * 40)
def report_card(self):

    sid = input("Enter Student ID : ")

    for student in self.students:

        if student.student_id == sid:

            student.report_card()

            return

    print("Student Not Found")
def topper(self):

    if len(self.students) == 0:

        print("No Students Available")

        return

    topper = max(self.students, key=lambda s: s.marks)

    print("=" * 40)

    print("🏆 TOPPER")

    print("=" * 40)

    print("Name :", topper.name)

    print("Marks :", topper.marks)

    print("Grade :", topper.calculate_grade())
def average_marks(self):

    if len(self.students) == 0:

        print("No Students")

        return

    total = 0

    for student in self.students:

        total += student.marks

    average = total / len(self.students)

    print("=" * 40)

    print("Average Marks :", round(average, 2))