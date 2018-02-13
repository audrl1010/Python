from sources.models.people import People

class Student(People):
    def __init__(self, name, age, gender, studentID, grade, GPA):
        super().__init__(name, age, gender)
        self.studentID = studentID
        self.grade = grade
        self.GPA = GPA