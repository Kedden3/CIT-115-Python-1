# COMPOUND INTEREST CALCULATOR


# 1.Input : Get information from user

f_principal = float(input("Enter the starting principal: "))

f_Interest_Rate = float(input("Enter the annual interest rate: "))

f_Compounding_Times = float(input("How many times per year is the interest compounded? "))

i_Term_Number = int(input("For how many years the account will earn interest? "))                      

# 2.Process : Calculate formula using input

f_Future_value  =  f_principal  *  ( 1 +  (f_Interest_Rate / 100) / f_Compounding_Times)  **  (f_Compounding_Times * i_Term_Number)


# 3.Output : Display result to screen, formatted properly


print(f"At the end of {i_Term_Number} years you will have $ {f_Future_value:1,.2f}")
                         
