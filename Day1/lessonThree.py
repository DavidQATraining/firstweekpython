devsMoney = 100
devCanPlaySmash = False

if devsMoney > 10 and devCanPlaySmash:
    print("Dev enters a smash tournament!")
elif devsMoney < 1 and devCanPlaySmash:
    print("Dev is too poor to enter")
else:
    print("Dev just can't play smash")

# exercise
mark = int(input("What was your mark?: "))


val = int(mark)
if mark > 85:
    print("You go a distinction")
elif mark >= 65:
    print("You passed")
else:
    print("You have failed!")





