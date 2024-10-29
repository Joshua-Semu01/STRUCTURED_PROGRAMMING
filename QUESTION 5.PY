def main():
    print("This program calculates the future value of an investment.")
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate (as a decimal): "))
    years = int(input("Enter the number of years: "))
    
    for i in range(years):
        principal = principal * (1 + apr)
    
    print(f"The value after {years} years is: {principal}")