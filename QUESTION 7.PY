def main():
    print("This program calculates the future value of an investment with compounding periods.")
    principal = float(input("Enter the initial principal: "))
    rate = float(input("Enter the yearly interest rate (as a decimal): "))
    periods = int(input("Enter the number of times the interest is compounded each year: "))
    years = int(input("Enter the number of years: "))

    for i in range(years * periods):
        principal = principal * (1 + rate / periods)
    
    print(f"The value after {years} years is: {principal}")