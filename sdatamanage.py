student_grades = { }

def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a grade of {grade}")

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Updated {name}'s grade to {grade}")
    else:
        print(f"{name} is not found!")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Deleted {name}")
    else:
        print(f"{name} is not found!")

def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} has a grade of {grade}")
    else:
        print("No students are added")

def main():
    while True:
        print("\nStudent Grade Data Management System\n")
        print("1. Add Student\n2. Update Student\n3. Delete Student\n4. View Students\n5. Exit\n")

        try:
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                name = input("Enter the student's Name: ")
                grade = int(input("Enter student grade: "))
                add_student(name, grade)

            elif choice == 2:
                name = input("Enter the student's Name: ")
                grade = int(input("Enter student grade: "))
                update_student(name, grade)

            elif choice == 3:
                name = input("Enter the student's Name: ")
                delete_student(name)

            elif choice == 4:
                display_all_students()

            elif choice == 5:
                print("Thank you.......Exiting......\n")
                break
            else:
                print("Invalid Choice! Try Again...")
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
