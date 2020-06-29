string1, string2, string3 = "Good", "Day", "David"
print(string1+string2+string3)

#get 2 numbers from user, one whole and one decimal
number1 = input("Enter a whole number: ")
number2 = input("Enter a decimal number: ")
#declare int and float numbers then round the float number
integer_num = int(number1)
float_num = float(number2)
round_number = int(round(float_num))
#print all 3 numbers
print(number1)
print(number2)
print(round_number)

#output the animal that comes first alphabetically
animal1 = input("Enter an animal: ")
animal2 = input("Enter another animal: ")
animalName = [animal1, animal2]
animalName.sort()
print(animalName[0])







