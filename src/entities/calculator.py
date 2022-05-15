import re
class Calculator:
    """The class that manages the logic part of calculator.
    """
    def calc(self, num1, oper, num2):
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
        if "." in num1 or "." in num2:
            if oper == "+":
                return round(float(num1)+float(num2),2)
            if oper == "-":
                return round(float(num1)-float(num2),2)
            if oper == "*":
                return round(float(num1)*float(num2),2)
            if oper == "/":
                if float(num2) == 0:
                    return "Please don't divide by zero"
                return round(float(float(num1)/float(num2)),2)
        if oper == "+":
            return int(num1)+int(num2)
        if oper == "-":
            return int(num1)-int(num2)
        if oper == "*":
            return int(num1)*int(num2)
        if oper == "/":
            if float(num2) == 0:
                return "Please don't divide by zero"
            return round(float(int(num1)/int(num2)),2)
