class Student:
    grade: int = 0
    surname: str = ""
    name: str = ""
    def __init__(self, name: str, surname: str, grade: int):
        self.name = name
        self.surname = surname
        self.grade = grade

    def add_grade(self):
        self.grade = self.grade + 1

    def print_info(self):
        print(f"Student: {self.name} {self.surname}")
        print(f"Grade: {self.grade}")

class PythonStudent(Student):
    python_mark: int = 0
    __is_learned: bool = False

    def learn_python(self):
        self.__is_learned = True

    def get_mark_python(self, hw1, hw2, hw3, hw4):
        if not self.__is_learned:
            print("Надо пойти учить питон")
            return 0
        self.python_mark = round(0.3*hw1+ 0.3*hw2 + 0.3*hw3 + 0.1*hw4)
        return self.python_mark

    def print_info(self):
        super().print_info()
        print(f"Python mark: {self.python_mark}")

s1 = Student("Ivan", "Ivanov", 3)
python_student = PythonStudent("Petr", "Ivanov", 3)
print(s1.name, s1.surname, s1.grade)
print(python_student.name, python_student.surname)
print(python_student.python_mark)

python_student.get_mark_python(1,1,1,1)
python_student.get_mark_python(1,1,1,1)
python_student.print_info()
python_student.surname = "sdfsdfsdf"


