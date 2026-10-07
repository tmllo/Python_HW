def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    return a / b


def read_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        operation = input("Choose an operation (1-5): ").strip()
        while operation not in ["1", "2", "3", "4", "5"]:
            print("Invalid operation. Please choose from 1-5.")
            operation = input("Choose an operation (1-5): ").strip()

        if operation == "5":
            print("Bye.")
            break

        first_number = read_number("Enter the first number: ")
        second_number = read_number("Enter the second number: ")

        if operation == "1":
            result = add(first_number, second_number)
        elif operation == "2":
            result = subtract(first_number, second_number)
        elif operation == "3":
            result = multiply(first_number, second_number)
        else:  # operation == "4"
            while second_number == 0:
                print("Cannot divide by 0.")
                second_number = read_number("Enter the second number: ")
            result = divide(first_number, second_number)

        print(f"Result: {result:.10g}")


if __name__ == "__main__":
    main()
