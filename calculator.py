import cal_art
print(cal_art.logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

all_operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

# print(all_operations["*"](n1 = 4, n2 = 8))
def calculate():
    should_accumulate = True
    num1 = float(input("what is the first number?: "))
    while should_accumulate:
        for symbol in all_operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is your second number?: "))
        answer = all_operations[operation_symbol](n1 = num1, n2 = num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"type yes to continue calculating with {answer}, or type no to start a new calculation ")
        if choice == "yes":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 50)
            calculate()


calculate()
