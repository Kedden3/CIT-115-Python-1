# PAINT JOB CODE

from math import ceil

# FUNCTION TO GET AND VALIDATE FLOAT INPUT FROM USER

def getFloatInput (sPrompt):
    while True:
        try:
            fValue = float(input(sPrompt))
            if fValue <= 0:
                print("Value must be greater than zero.")
            else :
                return fValue
        except ValueError:
            print("Enter a valid number.")


# GALLON PAINT NEEDED

def getGallonOfPaint(fSquareFeet, fFeetPerGallon):
    return ceil(fSquareFeet / fFeetPerGallon)

# LABOUR HOUR NEEDED

def getLaborHours(fLaborHourPerGallon, iGallons):
    return fLaborHourPerGallon * iGallons

# LABOR CHARGES

def getLaborCharges(fLaborHours, fLaborRate):
    return fLaborHours * fLaborRate

# PAINT CHARGES

def getPaintCharges(iGallons, fPaintPrice):
    return iGallons * fPaintPrice

# SALE TAX BASED ON STATES

def getSalesTax(sState):
    sState = sState.upper()
    if sState == "CT":
        return .06
    elif sState == "MA":
        return .0625
    elif sState == "ME":
        return .085
    elif sState == "NH":
        return .0
    elif sState == "RI":
        return .07
    elif sState == "VT":
        return .06
    else:
        return 0.0

# COST ESTIMATE TO FILE

def showCostEstimate(sLastName, iGallons,fLaborHours, fPaintCharges, fLaborCharges, fTax, fTotal):
    sFileName = sLastName + "_PaintJobOutput.txt"

    sOutput = (
        f"Gallons of paint: {iGallons}\n"
        f"Hours of labor: {fLaborHours:.1f}\n"
        f"Paint charges: ${fPaintCharges:,.2f}\n"
        f"Labor charges: ${fLaborCharges:,.2f}\n"
        f"Tax: ${fTax:,.2f}\n"
        f"Total cost: ${fTotal:,.2f}\n"

    )

    print(sOutput)
    with open(sFileName, "w") as f:
        f.write(sOutput)
        print(f"File: {sFileName} was created.")

print()
# MAIN PROGRAM
def main():

    fSquareFeet = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallon = getFloatInput("Enter feet per Gallon: ")
    fLaborHourPerGallon = getFloatInput("How many labor hours per gallon: ")
    fLaborRate = getFloatInput("Labor charges per hour: ")

    sState = input("State job is in: ")
    sLastName = input("Customer Last Name: ")

    iGallons = getGallonOfPaint(fSquareFeet, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHourPerGallon, iGallons)
    fPaintCharges = getPaintCharges(iGallons, fPaintPrice)
    fLaborCharges = getLaborCharges(fLaborHours, fLaborRate)
    fSubTotal = fPaintCharges + fLaborCharges
    fTaxRate = getSalesTax(sState)
    fTax = round(fSubTotal * fTaxRate, 2)
    fTotal = round(fSubTotal + fTax, 2)

    showCostEstimate(sLastName, iGallons,fLaborHours, fPaintCharges, fLaborCharges, fTax, fTotal)

# RUN MAIN
if __name__ == "__main__":
    main()
