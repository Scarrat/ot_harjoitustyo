class Calculator:

    def calc(self, n_1, oper, n_2):
        n_1 = int(n_1)
        n_2 = int(n_2)
        if oper == "+":
            return n_1+n_2
        if oper == "-":
            return n_1-n_2
        if oper == "*":
            return n_1*n_2
        if oper == "/":
            return n_1/n_2
