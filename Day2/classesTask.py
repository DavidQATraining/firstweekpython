class Student:
    group = "Student"

    # constructor method
    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.type = group

    # class function
    def getAvgScore(self, score1, score2, score3):
        return "avgScore is " + str((score1+score2+score3) / 3)


# creating 4 entities
Dave = Student("Dave", 30, "Student")
Tadas = Student("Tadas", 27, "Lecturer")
Paul = Student("Paul", 27, "Student")
Robert = Student("Robert", 27, "Student")

print(getattr(Dave, "name"), getattr(Dave, "group"))
print(getattr(Tadas, "name"), getattr(Tadas, "group"))
print(getattr(Robert, "name"), getattr(Robert, "group"))
print(getattr(Dave, "name") + "'s " + Dave.getAvgScore(98, 94, 90))
