import csv
import os
import sys


class Grades:
    def main_table(self):
        table = f"{'No.':<5}{'NAME':<20}{'SCORE'}\n" + ("-"*32) + "\n"
        
        students = self.get_students()
        for student in students:
            table += f"{students.index(student):<5}{student['name']:<20}{(int(student['exam']) + int(student['assignment1']) + int(student['assignment2']))}\n"
        table += ("-"*32)
        
        table += """
[1] Add student
[2] Remove student
[3] See student
[4] EXIT
"""
        os.system('cls' if os.name == 'nt' else 'clear')
        return table

    def student_table(self, index):
        students = self.get_students()
        student = students[index]

        table = student["name"].center(30) + ("\n") + ("-"*30) + f"""
Exam: {student["exam"]}
Assignment 1: {student["assignment1"]}
Assignment 2: {student["assignment2"]}
TOTAL: {int(student['exam']) + int(student['assignment1']) + int(student['assignment2'])}
"""+ ("-"*30) + f"""
[1] Edit exam
[2] Edit assignment 1
[3] Edit assignment 2
[4] BACK
"""
        os.system('cls' if os.name == 'nt' else 'clear')
        return table

    def get_students(self):
        with open("students.csv") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def add_student(self, **kwargs):
        self.students = self.get_students()
        self.students.append(kwargs)
        self.write_students()

    def remove_student(self, index):
        self.students = self.get_students()
        self.students.pop(index)
        self.write_students()

    def edit_student(self, student_index, exam_index, new_grade):
        self.students = self.get_students()
        self.students[student_index][exam_index] = new_grade
        self.write_students()        

    def write_students(self):
        with open("students.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames=["name","exam","assignment1","assignment2"],lineterminator="\n")
            writer.writeheader()
            writer.writerows(self.students)


def main():
    grades = Grades()

    while True:
        print(grades.main_table())

        menu = get_menu()
        match menu:
            case 1:
                add = get_student()
                grades.add_student(**add)
                continue

            case 2:
                remove = get_index(len(grades.get_students())-1)
                grades.remove_student(remove)
                continue

            case 3:
                student_index = get_index(len(grades.get_students())-1)
                
                while True:
                    print(grades.student_table(student_index))

                    st_menu = get_menu()

                    match st_menu:
                        case 1:
                            new_grade = get_grade("New grade: ", 100)
                            grades.edit_student(student_index, "exam", new_grade)
                            continue
                        case 2:
                            new_grade = get_grade("New grade: ", 50)
                            grades.edit_student(student_index, "assignment1", new_grade)
                            continue
                        case 3:
                            new_grade = get_grade("New grade: ", 50)
                            grades.edit_student(student_index, "assignment2", new_grade)
                            continue
                        case 4:
                            break
            case 4:
                print("Thank you!")
                sys.exit()

def get_student():
    name = input("Student's name: ")

    exam = get_grade("Exam grade (100 max): ", 100)
    assignment1 = get_grade("Assignment 1 grade (50 max): ", 50)
    assignment2 = get_grade("Assignment 2 grade (50 max): ", 50)

    return {"name": name, "exam": exam, "assignment1": assignment1, "assignment2": assignment2}

def get_grade(text, max):
    while True:
        try:
            print("-"*20)
            grade = int(input(text))
            if 0 <= grade <= max:
                return grade
            else:
                print(f"Grade should be a number between 0 and {max}")        
        
        except ValueError:
            print("Grade is not valid")
            continue

def get_menu():
    while True:
        try:
            choice = int(input(">>> "))
            if 1 <= choice <= 4:
                return choice
        
        except ValueError:
            print("You must type a number")
            continue

def get_index(max):
    while True:
        try:
            choice = int(input("Student's number: "))
            if 0 <= choice <= max:
                return choice
        
        except ValueError:
            print("You must type a number")
            continue


if __name__ == "__main__":
    main()
