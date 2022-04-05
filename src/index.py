from calculator import Calculator

calculator = Calculator()

def main():
    while True:
        num1 = input("First number: ")
        oper = input("Operand: ")
        num2 = input("Second number: ")
        print(calculator.calc(num1, oper, num2))
        cont = input("Another calculation (y/n)?")
        if cont == "n":
            break

if __name__ =='__main__':
    main()
