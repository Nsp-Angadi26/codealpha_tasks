def add_grade(student_grades):
    student = input("Enter student name: ")
    subject = input("Enter subject: ")
    grade = float(input("Enter grade: "))
    
    if student not in student_grades:
        student_grades[student] = {}
    
    if subject not in student_grades[student]:
        student_grades[student][subject] = []
    
    student_grades[student][subject].append(grade)
    print(f"Added grade {grade} for {student} in {subject}.")

def calculate_average(student_grades):
    student = input("Enter student name: ")
    
    if student not in student_grades:
        print("Student not found.")
        return
    
    total = 0
    count = 0
    for subject, grades in student_grades[student].items():
        total += sum(grades)
        count += len(grades)
    
    if count == 0:
        print("No grades available for this student.")
    else:
        print(f"Average grade for {student}: {total / count:.2f}")

def main():
    student_grades = {}
    while True:
        print("\nStudent Grade Tracker")
        print("1. Add Grade")
        print("2. Calculate Average")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_grade(student_grades)
        elif choice == "2":
            calculate_average(student_grades)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()


