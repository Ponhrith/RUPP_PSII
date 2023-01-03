getGender = input("Boy or Girl:")
option1 = "boy"
option2 = "girl"
dad = int(input("Enter the father's height in cm: "))
mom = int(input("Enter the mother's height in cm: "))

def boy():
    boyHeight = (dad + mom)/2 + 6.5
    print(boyHeight, "cm")

def girl():
    girlHeight = (dad + mom)/2 - 6.5
    print(girlHeight, "cm")

if getGender.lower() == option1.lower():
    print("The boy's height is:", end = ' ')
    boy()
elif getGender.lower() == option2.lower():
    print("The girl's height is:", end = ' ')
    girl()
else:
    print("Please read the instruction again!")