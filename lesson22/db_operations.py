from models import Session, Student, Course

class StudentManagementSystem:

    def __init__(self, session: Session):
        self.session = session

    def add_student(self, student_name: str, course_ids: list[int]):
        new_student = Student(name=student_name)
        new_student.courses = self.session.query(Course).filter(Course.id.in_(course_ids)).all()
        self.session.add(new_student)
        self.session.commit()
        print(f"Student {student_name} added successfully.")

    def add_course(self, course_name: str):
        new_course = Course(name=course_name)
        self.session.add(new_course)
        self.session.commit()
        print(f"Course {course_name} added successfully.")

    def update_student(self, student_id: int, new_name: str):
        student = self.session.query(Student).get(student_id)
        if student:
            student.name = new_name
            self.session.commit()
            print(f"Student ID {student_id} updated successfully.")
        else:
            print(f"Student with ID {student_id} not found.")

    def update_course(self, course_id: int, new_name: str):
        course = self.session.query(Course).get(course_id)
        if course:
            course.name = new_name
            self.session.commit()
            print(f"Course ID {course_id} updated successfully.")
        else:
            print(f"Course with ID {course_id} not found.")

    def delete_student(self, student_id: int):
        student = self.session.query(Student).get(student_id)
        if student:
            self.session.delete(student)
            self.session.commit()
            print(f"Student ID {student_id} deleted successfully.")
        else:
            print(f"Student with ID {student_id} not found.")

    def delete_course(self, course_id: int):
        course = self.session.query(Course).get(course_id)
        if course:
            self.session.delete(course)
            self.session.commit()
            print(f"Course ID {course_id} deleted successfully.")
        else:
            print(f"Course with ID {course_id} not found.")

    def get_students_by_course(self, course_id: int):
        course = self.session.get(Course, course_id)
        if course:
            student_names = [student.name for student in course.students]
            print(f"Students on course {course_id}: {student_names}")
        else:
            print(f"Course with ID {course_id} not found.")

    def get_courses_by_student(self, student_id: int):
        student = self.session.get(Student, student_id)
        if student:
            course_names = [course.name for course in student.courses]
            print(f"Courses of student {student_id}: {course_names}")
        else:
            print(f"Student with ID {student_id} not found.")


if __name__ == "__main__":
    session = Session()

    student_management = StudentManagementSystem(session)

    # Створення 5 курсів
    courses = ["Mathematics", "Physics", "Chemistry", "History", "Literature"]
    for course in courses:
        student_management.add_course(course)

    # Додавання 20 студентів, зареєстрованих на випадкові курси
    from random import sample, randint

    for i in range(20):
        student_name = f"Student_{i+1}"
        random_courses = sample(range(1, 6), randint(1, 3))  # Випадкові курси від 1 до 5
        student_management.add_student(student_name, random_courses)

    # Запит для отримання студентів на певному курсі
    course_id = 1  # Наприклад, отримати всіх студентів на курсі Mathematics
    students_on_course = student_management.get_students_by_course(course_id)
    print(f"Students on course {course_id}: {students_on_course}")

    # Запит для отримання курсів, на які зареєстрований студент
    student_id = 1  # Наприклад, отримати всі курси студента з ID 1
    courses_of_student = student_management.get_courses_by_student(student_id)
    print(f"Courses of student {student_id}: {courses_of_student}")