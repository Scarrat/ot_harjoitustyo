import re
class Calculator:
    """The class that manages the logic part of calculator.
    """

    def calc_basic(self,expression):
        """Calculates the answer of the expression written on the calculator screen.

        Args:
            expression: the string given by calculator.

        Returns:
            An integer with the answer to the calculation.
        """
        result = 0
        split = re.split('(\d+)', expression)
        if split[0] != "+" or split[0] != "-" or split[0] != "*" or split[0] != "/":
            del split[0]
        del split[len(split)-1]
        if len(split) < 3:
            return 0
        while split:
            if split[0] == "+" or split[0] == "-" or split[0] == "*" or split[0] == "/":
                sym = split[0]
                if sym == "+":
                    result = self.addition(result,split[1])
                if sym == "-":
                    result = self.subtraction(result,split[1])
                if sym == "*":
                    result = self.multiplication(result,split[1])
                if sym == "/":
                    result = self.division(result,split[1])
                del split[0]
                del split[0]
            else :
                sym = split[1]
                if sym == "+":
                    result = self.addition(split[0],split[2]) + result
                if sym == "-":
                    result = self.subtraction(split[0],split[2]) + result
                if sym == "*":
                    result = self.multiplication(split[0],split[2]) + result
                if sym == "/":
                    result = self.division(split[0],split[2]) + result
                del split[0]
                del split[0]
                del split[0]
        return result

    def addition(self,num1,num2):
        return int(num1)+int(num2)

    def subtraction(self,num1,num2):
        return int(num1)-int(num2)

    def multiplication(self, num1,num2):
        return int(num1)*int(num2)

    def division(self, num1,num2):
        if int(num2) == 0:
            return 0
        return int(int(num1)/int(num2))

    def calc_test(self, num1, oper, num2):
        """Calculates the answer of the expression written on the calculator screen.

        Args:
            num1: first number of the expression.
            oper: operand of the expression.
            num2 : second number of the expression

        Returns:
            An integer with the answer to the calculation.
        """
        if "*" in str(num1+num2) or "/" in str(num1+num2):
            return "Please use correct expression format"   
        if oper == "+":
            return int(num1)+int(num2)
        if oper == "-":
            return int(num1)-int(num2)
        if oper == "*":
            return int(num1)*int(num2)
        if oper == "/":
            if int(num2) == 0:
                return 0
        return int(int(num1)/int(num2))
    