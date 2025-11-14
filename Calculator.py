
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def get_number(prompt):
    while True:
        try:
            s = input(prompt).strip()
            if s == "":
                print("Input cannot be empty. Please enter a number.")
                continue
            return float(s)
        except ValueError:
            print("Invalid number. Please enter a valid numeric value (e.g., 3.14 or 5).")

def main():
    menu = """
Simple CLI Calculator
Choose an option:
1) Add (+)
2) Subtract (-)
3) Multiply (*)
4) Divide (/)
5) Exit
"""
    while True:
        print(menu)
        choice = input("Enter choice (1/2/3/4/5 or + - * /): ").strip()


        if choice in ("5", "exit", "Exit", "q", "Q"):
            print("Exiting calculator. Goodbye!")
            break

        
        symbol_map = {"+": "1", "-": "2", "*": "3", "/": "4"}
        if choice in symbol_map:
            choice = symbol_map[choice]

        if choice not in ("1", "2", "3", "4"):
            print("Invalid option. Please enter 1,2,3,4 or 5 (or + - * /).")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        try:
            if choice == "1":
                res = add(a, b)
                op = "+"
            elif choice == "2":
                res = subtract(a, b)
                op = "-"
            elif choice == "3":
                res = multiply(a, b)
                op = "*"
            elif choice == "4":
                res = divide(a, b)
                op = "/"

            formatted_res = ("{:.10f}".format(res)).rstrip('0').rstrip('.')
            print(f"{a} {op} {b} = {formatted_res}")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed. Please enter a non-zero second number.")
        except Exception as e:
           
            print("An unexpected error occurred:", str(e))

if __name__ == "__main__":
    main()
