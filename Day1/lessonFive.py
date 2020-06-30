# def addCalc(num1, num2):
#     answer = num1 + num2
#     return answer
#
#
# addedNum = addCalc(5, 5)
#
# print(addedNum + 20)

stuName = input("Enter student name: ")
hwMark = int(input("Enter your homework mark out of 25: "))
assMark = int(input("Enter your assessment mark out of 50: "))
examMark = int(input("Enter your exam mark out of 100: "))

def calcperc(hwMark, assMark, exaMark):
    totalperc = ((hwMark+assMark+exaMark) / 175) * 100
    grade = ""
    if totalperc >= 90:
        grade = "A"
    elif totalperc >= 80:
        grade = "B"
    elif totalperc >= 70:
        grade = "C"
    elif totalperc >= 60:
        grade = "D"
    else:
        grade = "F"

    print(stuName, "got a grade of", grade, "with",
          round(totalperc), "%")
    return grade, totalperc


calcperc(hwMark, assMark, examMark)



