def main():
    print("Celsius to Fahrenheit consersion table")
for celsius in range(0, 101, 10):
            fahrenheit = 9/5 * celsius + 32
            print(f"{celsius}\t{fahrenheit:2f}")