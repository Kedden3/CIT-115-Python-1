# PROMPT FOR PERSON'S NAME

sPersonName = input("Name of the person we are calculating the grades for : ")

# PROMPT FOR FOUR TEST SCORES / LOWEST GRADE DROP FROM CALCULATION

iTest1 = int(input("Test 1: "))
iTest2 = int(input("Test 2: "))
iTest3 = int(input("Test 3: "))
iTest4 = int(input("test 4: "))
sDropLowestG = input("Do you wish to Drop the Lowest Grade Y or N ? (Y/N)  ").upper()

# WHOLE NUMBER VALIDATION

if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0.")
    exit()

# DROP LOWEST SCORE VALIDATION

if sDropLowestG != "Y" and sDropLowestG != "N":
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()

# CALCULATION AVERAGE WITH/WITHOUT LOWEST SCORE DROP

if sDropLowestG == "Y" :
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        fAverage = (iTest2 + iTest3 + iTest4) / 3
    elif iTest2 <= iTest1 and iTest2 <= iTest3 and iTest2 <= iTest4:
        fAverage = (iTest1 + iTest3 + iTest4) / 3
    elif iTest3 <= iTest1 and iTest3 <= iTest2 and iTest3 <= iTest4:
        fAverage = (iTest1 + iTest2 + iTest4) / 3
    else :
        fAverage = (iTest1 + iTest2 + iTest3) / 3
else :
    fAverage = (iTest1 + iTest2 + iTest3 + iTest4) / 4

# LETTER GRADE VALUE

if fAverage >= 97.0:
    sGrade = "A+"
elif fAverage >= 94.0:
    sGrade = "A"
elif fAverage >= 90.0:
    sGrade = "A-"
elif fAverage >= 87.0:
    sGrade = "B+"
elif fAverage >= 84.0:
    sGrade = "B"
elif fAverage >= 80.0:
    sGrade = "B-"
elif fAverage >= 77.0:
    sGrade = "C+"
elif fAverage >= 74.0:
    sGrade = "C"
elif fAverage >= 70.0:
    sGrade = "C-"
elif fAverage >= 67.0:
    sGrade = "D+"
elif fAverage >= 64.0:
    sGrade = "D"
elif fAverage >= 60.0:
    sGrade = "D-"
else:
    sGrade = "F"

# OUTPUT

print(f"{sPersonName} test average is : {fAverage:.1f}")
print(f"Letter Grade for the test is : {sGrade}")
