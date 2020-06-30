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

def calcperc(hwMark, assMark, examMark):
    totalperc = ((hwMark+assMark+examMark) / 175) * 100

    if totalperc > 89:
        grade = "A"
    elif totalperc > 79:
        grade = "B"
    elif totalperc > 69:
        grade = "C"
    elif totalperc > 59:
        grade = "D"
    else:
        grade = "F"

    result = stuName + " got a grade of '" + grade + "' with " + str(round(totalperc)) + "%"
    return result


print(calcperc(hwMark, assMark, examMark))



