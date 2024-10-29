def main():
    print("Welcome to the temperature converter!")
    for _ in range(5):
        celsius = eval(input("enter the temperature in celsius: "))
        fahrenheit= 9/5 * celsius + 32
        print(f"the temperature in fahrenheit is: {fahrenheit:.2f}")
        print("Celsius to Fahrenheit consersion table")
        print("Celsius\tFahrenheit")
        for celsius in range(0, 101, 10):
            fahrenheit = 9/5 * celsius + 32
            print(f"{celsius}\t{fahrenheit:2f}")