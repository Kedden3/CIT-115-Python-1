# TEMPERATURE CONVERTER

print("Welcome Yao E. KUVODU to temperature converter: \n\n")

# INPUT - PROMPT USER for Temp and Temp Type

fTemp = float(input("Enter a temperature: "))

sTemp=(input("Is the temp F for Fahrenheit or C for Celsius? "))

# PROCESS + OUTPUT - CALCULATIONS / LOGIC

fFahrenheit = ((9.0 / 5.0) * fTemp) + 32 

fCelcius = ((5.0 / 9) * (fTemp - 32))


if  sTemp == "F" or sTemp == "f":
  if fTemp > 212:
    print("Temp can not be > 212")
  elif fTemp < 212:
    print("The Celsius equivalent is: " , round(fCelcius, 1))
elif sTemp == "C" or sTemp == "c":
  if fTemp > 100:
    print("Tempe can not be > 100")
  elif fTemp < 100:
    print ("The Fahrenheit equivalent is: " , round(fFahrenheit, 1))
else: 
  print("You must enter a F or C")
