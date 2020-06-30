# print name + is awesome 5 times
count = 0
name = str(input("What is your name?"))
while count < 5:
    print(name, "is awesome")
    count += 1

# print 5,6,7,8,9,10
for i in range(5,11):
    print(i)

# print 10,12,14,16,18,20
for i in range(10,21,2):
    print(i)

# ask user for 5 names, print they are awesome
x = 0
for i in range(5):
    names = str(input("What name now?"))
    print(names, "is awesome!")
    x += 1

# 0*0... till 3, 1*0... til 3, 2*0... till 3
for i in range(3):
    for j in range(4):
        print(i,"*", j, "=", i*j)

# Your organization doesn't allow you
# to use work content with this application
for i in range(1, 100):
    square = i*i
    if square < 2000:
        print(i, "*", i, "=", square)

# count vowels in word
# word = input("Enter a word: ")
# vCount = 0
#
# for char in word:
#     if (char == "a" or char == "e" or char == "i" or
#             char == "o" or char == "u"):
#         vCount +=1
# print("The amount of vowels in word:", vCount)

word = input("Enter a word: ").lower()
vCount = 0
for char in word:
    if char in "aeiou":
        vCount += 1
print("The amount of vowels in word:", vCount)

for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)




