#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argv = argv[1:]

    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[0])
    operator = argv[1]
    b = int(argv[2])

    if operator == '+':
        operation = add(a, b)
    elif operator == '-':
        operation = sub(a, b)
    elif operator == '*':
        operation = mul(a, b)
    elif operator == '/':
        operation = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, operation))
    