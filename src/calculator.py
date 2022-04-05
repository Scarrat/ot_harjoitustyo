class Calculator:

    def calc(self, n1, o, n2):
        n1 = int(n1)
        n2 = int(n2)
        if o == "+":
            return n1+n2
        if o == "-":
            return n1-n2
        if o == "*":
            return n1*n2
        if o == "/":
            return n1/n2

