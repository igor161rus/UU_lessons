import random
import sqlite3


class University:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect("students.db")
        self.cur = self.conn.cursor()

    def add_student(self, name, age):
        self.cur.execute("INSERT INTO students VALUES (NULL, ?, ?)", (name, age))
        id_student = self.cur.lastrowid
        self.conn.commit()
        return id_student

    def add_grade(self, student_id, subject, grade):
        self.cur.execute("INSERT INTO grades VALUES (NULL, ?, ?, ?)", (student_id, subject, grade))
        self.conn.commit()

    def get_students(self, subject=None):
        if (subject is not None
                and subject in self.cur.execute(f"SELECT subject "
                                                f"FROM grades "
                                                f"WHERE subject = '{subject}'").fetchone()):
            print(self.cur.execute(f"SELECT s.name, s.age, g.subject, g.grade "
                                   f"FROM students s, grades g "
                                   f"WHERE s.id = g.student_id AND g.subject = '{subject}'").fetchall())


uu = University('Urban')

i = int(input('Хотите добавить студентов? - 1, для просмотра - 2: '))
if i == 1:
    list_student = ('Ivan', 'Ilya', 'Anton', 'Egor')
    for i in list_student:
        id_student = uu.add_student(i, random.randint(20, 30))
        # Так выше оценки round(random.uniform(random.randint(1, 4), 5), 1)),
        # чем просто round(random.uniform(3, 5), 1))  )))
        uu.add_grade(id_student, 'Python', round(random.uniform(random.randint(1, 4), 5), 1))
        uu.add_grade(id_student, 'PHP', round(random.uniform(random.randint(1, 4), 5), 1))
# uu.get_students('Python')
elif i == 2:
    credit = input('Какой предмет вы хотите посмотреть? (Pyton, PHP): ')
    uu.get_students(credit)

