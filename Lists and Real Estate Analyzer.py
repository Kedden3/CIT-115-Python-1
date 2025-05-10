# Lists and Real Estate Analyzer

# FUNCTION TO GET AND VALIDATE FLOAT INPUT

print()
def getFloatInput(sPrompt):
    while True:
        try:
            fvalue = float(input(sPrompt))
            if fvalue <= 0:
                print("Input a number that is greater than 0.")
            else:
                return fvalue
        except ValueError:
            print("Input a number that is greater than 0.")

# FUNCTION TO CALCULATE MEDIAN

def getMedian(salesList):
    iCount = len(salesList)
    iMid = iCount // 2
    if iCount % 2 == 1:
        return salesList[iMid]
    else:
        return (salesList[iMid - 1] + salesList[iMid]) / 2.0

# MAIN FUNCTION
def main():
    salesList = []

    while True:
        fSalesPrice = getFloatInput("Enter property sales value: ")
        salesList.append(fSalesPrice)

        while True:
            sAnswer = input("Enter another value Y or N: ").strip().lower()
            if sAnswer in [ "y" , "n"]:
                break
        if sAnswer == "n":
            break

    if not salesList:
        print("No sale data entered")
        return

# SORT PROPERTIES
    salesList.sort()

    print()
    for iIndex, fValue in enumerate(salesList, start=1):
        print(f"Property {iIndex:<2}         $ {fValue:>10,.2f}")

# CALCULATIONS

    fMin = salesList[0]
    fMax = salesList[-1]
    fTotal = sum(salesList)
    fAverage = fTotal / len(salesList)
    fMedian = getMedian(salesList)
    fCommission = fTotal * 0.03

# DISPLAY

    print()
    print(f"{'Minimum:':<18} $ {fMin  :>10,.2f}")
    print(f"{'Maximum:':<18} $ {fMax  :>10,.2f}")
    print(f"{'Total  :':<18} $ {fTotal:>10,.2f}")
    print(f"{'Average:':<18} $ {fAverage:>10,.2f}")
    print(f"{'Median :':<18} $ {fMedian:>10,.2f}")
    print(f"{'Commission:':<18} $ {fCommission:>10,.2f}")


# RUN MAIN
if __name__ == "__main__":
    main()





