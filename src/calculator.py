import re
class Calculator:

    def calc_basic(self,expression):
        result = 0
        split = re.split('(\d+)', expression)
        del split[0]
        del split[len(split)-1]
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


