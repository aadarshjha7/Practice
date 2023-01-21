def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
while True:
    num1 = float(input("Enter the first digit: "))
    for symbol in operations:
        print(symbol)
    more_calc = True
    while more_calc:
        calc_operation = input("Select the operation: ")
        num2 = float(input("Enter the next digit: "))
        calc_func = operations[calc_operation]
        answer = calc_func(num1, num2)
        print(answer)
        next = input(
            "Type 'y' to calculate more and 'n' to start new calculation or 'q' to quit:")
        if next == "y":
            num1 = answer
        elif next == "n":
            more_calc = False
        else:
            print("Invalid input")
            break
    if next == "q":
        break
