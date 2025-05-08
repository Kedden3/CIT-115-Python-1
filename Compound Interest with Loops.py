# COMPOUND INTEREST WITH LOOPS

# PROMPT USER FOR INPUT VALUES / DATA VALIDATION

# DEPOSIT

print()
while True:
    try:
        fDeposit = float(input("What is the Original Deposit (positive value): "))
        if fDeposit > 0:
            break
        else:
            print("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")

# INTEREST RATE

while True:
    try:
        fInterestRate = float(input("What is the Interest Rate (positive value): "))
        if fInterestRate > 0:
            break
        else:
            print("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")

# MONTHS

while True:
    try:
        iMonths = int(input("What is the Number of Months (positive value): "))
        if iMonths > 0:
            break
        else:
            print("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")

# GOAL

while True:
    try:
        fGoal = float(input("What is the Goal Amount (can enter 0 but not negative): "))
        if fGoal >= 0:
            break
        else:
            print("Input must be 0 or greater")
    except ValueError:
        print("Input must be a positive numeric value")

# MONTHLY INTEREST RATE CALCULATION

fMonthlyRate = fInterestRate / 100 / 12

# EACH MONTH BALANCE

fBalance = fDeposit
iNumber = 1
while iNumber <= iMonths:
     fBalance += fBalance * fMonthlyRate
     print(f"Month: {iNumber:<4} Account Balance is: ${fBalance:,.2f}")
     iNumber += 1

# GOAL AMOUNT

if fGoal > 0 and fDeposit < fGoal:
    iMonthsToGoal = 0
    while fDeposit < fGoal:
          fDeposit += fDeposit * fMonthlyRate
          iMonthsToGoal += 1
    print(f"\nIt will take: {iMonthsToGoal} months to reach the goal of ${fGoal:,.2f}")