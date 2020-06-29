print("Hello World")

# Now look at the piece of code and try to pick out the errors.
print       ("Hello World") # punctuation, spaces between print and bracket
# PRINT "Hello World"      #punctuation, no parethesis + capital PRINT
print ("Hello World")
# print(Hello World)       #no quotes
# Print("Hello World")     #capital P
# priint("Hello World"     #missing )

# Create a python file that will input your first name,
# last name and outputs "Hello [firstname] [lastname]"
firstName = "David"
lastName = "McCartney"
print("Hello "+firstName+" "+lastName)

# Open a new window and type the following:
# get 2 numbers from user converting both to dataType float
number1 = float(input("Please enter 1st number: "))
number2 = float(input("Please enter 2nd number: "))
# add both numbers together and store them
answer = float(number1+number2)
# print both numbers and the answer
print(number1, "+", number2, "= ", answer)