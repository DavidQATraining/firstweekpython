class Student:
    class_ = "Student"

    # constructor method
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_

    # class function
    def getAvgScore(self, score1, score2, score3):
        return "avgScore is " + str((score1+score2+score3) / 3)


# creating 3 students
Dave = Student("Dave", 30, "Student")
Tadas = Student("Tadas", 27, "Lecturer")
Paul = Student("Paul", 27, "Student")

print(getattr(Dave, "name"), getattr(Dave, "class_"))
print(getattr(Tadas, "name"), getattr(Tadas, "class_"))
print(getattr(Dave, "name") + "'s " + Dave.getAvgScore(98, 94, 90))
