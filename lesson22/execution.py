from db_operations import StudentManagementSystem
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# З'єднання з БД
DATABASE_URL = "postgresql://postgres:qwerty1985@localhost:5432/mydb_hw21"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

db = StudentManagementSystem (session)

def main():
    print("Виберіть дію:")
    print("1. Додати студента")
    print("2. Додати курс")
    print("3. Показати студентів, зареєстрованих на курс")
    print("4. Показати курси, на які зареєстрований студент")
    print("5. Оновити дані студента")
    print("6. Видалити студента")
    action = input("Введіть номер дії: ")

    if action == "1":
        student_name = input("Введіть ім'я студента: ")
        course_ids = input("Введіть ID курсів через кому (наприклад: 1,2,3): ")
        course_ids = [int(id.strip()) for id in course_ids.split(",")]
        db.add_student(student_name, course_ids)

    elif action == "2":
        course_name = input("Введіть назву курсу: ")
        db.add_course(course_name)

    elif action == "3":
        course_id = int(input("Введіть ID курсу: "))
        db.get_students_by_course(course_id)

    elif action == "4":
        student_id = int(input("Введіть ID студента: "))
        db.get_courses_by_student(student_id)

    elif action == "5":
        student_id = int(input("Введіть ID студента: "))
        new_name = input("Введіть нове ім'я студента: ")
        db.update_student(student_id, new_name)

    elif action == "6":
        student_id = int(input("Введіть ID студента: "))
        db.delete_student(student_id)

    else:
        print("Невірна дія!")

if __name__ == "__main__":
    main()