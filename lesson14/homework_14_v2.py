from lesson14.created_classes import Students

students = {}

students["Іван Петренко"] = Students("Іван", "Петренко", 20, 4.5)
students["Олена Коваленко"] = Students("Олена", "Коваленко", 19, 4.7)
students["Петро Іванов"] = Students("Петро", "Іванов", 21, 4.2)

# Функція для виведення інформації про всіх студентів
def display_all_students(students):
    for key, student in students.items():
        print(f"Інформація про студента {key}:")
        student.display_info()
        print()

display_all_students(students)

students["Олена Коваленко"].update_average_grade(4.9)

print("Після зміни середнього балу у Олени Коваленко:\n")
display_all_students(students)