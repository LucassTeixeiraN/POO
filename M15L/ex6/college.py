from students import Student

class College:
    def __init__(self):
        self.students: list[Student] = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print("Erro: O objeto não é um estudante válido.")

    def list_students(self):
        for student in self.students:
            print(student)