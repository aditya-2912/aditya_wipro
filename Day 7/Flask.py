from abc import ABC, abstractmethod
from functools import wraps
import json
import csv
import os

# ================= DECORATOR =================
def requires_admin(func):
    @wraps(func)
    def inner(self, *args, **kwargs):
        if self.user_role != "admin":
            print("❌ Admin access required")
            return
        return func(self, *args, **kwargs)
    return inner

# ================= DESCRIPTORS =================
class MarksValidator:
    def __set_name__(self, owner, name):
        self.attr = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.attr)

    def __set__(self, instance, value):
        if any(m < 0 or m > 100 for m in value):
            raise ValueError("Marks must be between 0 and 100")
        setattr(instance, self.attr, value)

class SalaryProtect:
    def __get__(self, instance, owner):
        raise PermissionError("Salary access restricted")

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Invalid salary amount")
        instance._salary = value

# ================= ABSTRACT CLASS =================
class Person(ABC):
    def __init__(self, uid, name, dept):
        self.uid = uid
        self.name = name
        self.dept = dept

    @abstractmethod
    def display(self):
        pass

# ================= STUDENT =================
class Student(Person):
    marks = MarksValidator()

    def __init__(self, sid, name, dept, sem, marks):
        super().__init__(sid, name, dept)
        self.sem = sem
        self.marks = marks

    def evaluate_student(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        return round(avg, 2), grade

    def display(self):
        avg, grade = self.evaluate_student()
        print("=" * 35)
        print(f"Student ID : {self.uid}")
        print(f"Name       : {self.name}")
        print(f"Department : {self.dept}")
        print(f"Semester   : {self.sem}")
        print(f"Average    : {avg}")
        print(f"Grade      : {grade}")

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)

# ================= FACULTY =================
class Faculty(Person):
    salary = SalaryProtect()

    def __init__(self, fid, name, dept, salary):
        super().__init__(fid, name, dept)
        self.salary = salary

    def display(self):
        print("=" * 35)
        print(f"Faculty ID : {self.uid}")
        print(f"Name       : {self.name}")
        print(f"Department : {self.dept}")

# ================= COURSE =================
class Course:
    def __init__(self, code, title, credits, faculty_id):
        self.code = code
        self.title = title
        self.credits = credits
        self.faculty_id = faculty_id
        self.enrolled_students = []

    def register(self, student):
        self.enrolled_students.append(student)

# ================= MAIN SYSTEM =================
class SmartUniversity:
    def __init__(self):
        self.students = {}
        self.faculty = {}
        self.courses = {}
        self.user_role = None
        self.load_data()

    # ---------- FILE LOAD ----------
    def load_data(self):
        self._load_json("students.json", "student")
        self._load_json("faculty.json", "faculty")
        self._load_json("courses.json", "course")

    def _load_json(self, filename, dtype):
        if not os.path.exists(filename):
            return
        with open(filename) as f:
            data = json.load(f)

        for item in data:
            if dtype == "student":
                self.students[item["id"]] = Student(
                    item["id"], item["name"],
                    item["department"], item["semester"], item["marks"]
                )
            elif dtype == "faculty":
                self.faculty[item["id"]] = Faculty(
                    item["id"], item["name"],
                    item["department"], item["salary"]
                )
            else:
                self.courses[item["code"]] = Course(
                    item["code"], item["name"],
                    item["credits"], item["faculty_id"]
                )

    # ---------- LOGIN ----------
    def login(self):
        role = input("Login as (admin/user): ").lower()
        if role not in ("admin", "user"):
            raise ValueError("Invalid login role")
        self.user_role = role
        print(f"✅ Logged in as {role.upper()}")

    # ---------- SAVE ----------
    def save_json(self, filename, data):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    # ---------- ADMIN OPERATIONS ----------
    @requires_admin
    def add_student(self):
        sid = input("Student ID: ")
        if sid in self.students:
            raise ValueError("Student already exists")

        s = Student(
            sid,
            input("Name: "),
            input("Department: "),
            int(input("Semester: ")),
            list(map(int, input("Marks: ").split()))
        )
        self.students[sid] = s
        self.save_json("students.json", [
            vars(st) | {"marks": st.marks} for st in self.students.values()
        ])
        print("✅ Student added successfully")

    @requires_admin
    def add_faculty(self):
        fid = input("Faculty ID: ")
        f = Faculty(
            fid,
            input("Name: "),
            input("Department: "),
            int(input("Salary: "))
        )
        self.faculty[fid] = f
        self.save_json("faculty.json", [
            {"id": x.uid, "name": x.name, "department": x.dept, "salary": x._salary}
            for x in self.faculty.values()
        ])
        print("✅ Faculty added")

    @requires_admin
    def compare_students(self):
        s1 = self.students[input("First Student ID: ")]
        s2 = self.students[input("Second Student ID: ")]
        print(f"{s1.name} > {s2.name} :", s1 > s2)

    # ---------- USER OPERATIONS ----------
    def view_student(self):
        self.students[input("Student ID: ")].display()

    def view_faculty(self):
        self.faculty[input("Faculty ID: ")].display()

    def enroll_student(self):
        sid = input("Student ID: ")
        code = input("Course Code: ")
        self.courses[code].register(self.students[sid])
        print("✅ Enrollment successful")

    # ---------- MENU ----------
    def run(self):
        while True:
            try:
                if self.user_role == "admin":
                    print("""
ADMIN PANEL
1. Add Student
2. Add Faculty
3. Compare Students
4. Exit
""")
                    ch = input("Choice: ")
                    if ch == "1": self.add_student()
                    elif ch == "2": self.add_faculty()
                    elif ch == "3": self.compare_students()
                    elif ch == "4": break
                else:
                    print("""
USER PANEL
1. View Student
2. View Faculty
3. Enroll Course
4. Exit
""")
                    ch = input("Choice: ")
                    if ch == "1": self.view_student()
                    elif ch == "2": self.view_faculty()
                    elif ch == "3": self.enroll_student()
                    elif ch == "4": break
            except Exception as e:
                print("⚠ Error:", e)

# ================= RUN =================
if __name__ == "__main__":
    app = SmartUniversity()
    app.login()
    app.run()
    print("🙏 Thank you for using Smart University System")
