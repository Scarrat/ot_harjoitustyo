from calculator import Calculator

calculator = Calculator()


def main():
    ans = None
    while True:
        if ans is None:
            num1 = input("First number: ")
            oper = input("Operand: ")
            num2 = input("Second number: ")
            ans = calculator.calc(num1, oper, num2)
            print(ans)
        else:
            oper = input("Operand: ")
            num2 = input("Second number: ")
            ans = calculator.calc(ans, oper, num2)
            print(ans)
        cont = input("Another calculation (y/n)? ")
        if cont == "n":
            break
        cont2 = input("Continue with last answer (y/n)? ")
        if cont2 == "n":
            ans = None

if __name__ =='__main__':
    main()
