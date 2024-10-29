def main():
    print("Welcome to the interactive Python calculator!")
    for i in range(100):
        expr = input("Enter a mathematical expression: ")
        try:
            result = eval(expr)
            print(f"The result is: {result}")
        except Exception as e:
            print("Invalid expression. Please try again.")
            continue