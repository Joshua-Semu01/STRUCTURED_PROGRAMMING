def main():
    print("This program calculates the total accumulation of your yearly investments.")
    amount = float(input("Enter the amount to invest each year: "))
    apr = float(input("Enter the annual interest rate (as a decimal): "))
    years = int(input("Enter the number of years: "))
    total = 0

    for i in range(years):
        total = (total + amount) * (1 + apr)
    
    print(f"The total accumulation after {years} years is: {total}")