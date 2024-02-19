from math import log10, sqrt, log,exp
import tkinter as tk
import re
import winsound
class CalculatorModel:

    def __init__(self):
        self.total_value = ''

    def expo(self,current_value):
        self.total_value = str(eval(f"{current_value} ** 2"))
        return self.total_value

    def calculate(self,current_value,method,match):
        if match:
            num = match.group(1)
            num_value = eval(num)
            result = method(float(num_value))
            current_value = current_value.replace(f"{method}({num_value})", str(result))
            self.total_value = str(eval(current_value))
            return self.total_value


    def evaluate(self,current_value):
        if "mod" in current_value:
            current_value = current_value.replace("mod", "%")
            result = str(eval(current_value))
        elif "^" in current_value:
            current_value = current_value.replace("^", "**")
            result = str(eval(current_value))
        elif "sqrt" in current_value:
            # result = self.calculate(current_value,sqrt)
            match = re.search(rf'sqrt\((.*?)\)', current_value)
            result = self.calculate(current_value,sqrt,match)
        elif "log10" in current_value:
            match = re.search(rf'log10\((.*?)\)', current_value)
            result = self.calculate(current_value,log10,match)
        elif "log" in current_value:
            match = re.search(rf'log\((.*?)\)', current_value)
            result = self.calculate(current_value,log,match)
        elif "exp" in current_value:
            match = re.search(rf'exp\((.*?)\)', current_value)
            result = self.calculate(current_value,exp,match)
        else:
            result = str(eval(current_value))
        return result


    def delete(self,current_value):
        if current_value.endswith("sqrt("):
            t = current_value.strip("sqrt(")
        elif current_value.endswith("log("):
            t = current_value.strip("log(")
        elif  current_value.endswith("exp("):
            t = current_value.strip("exp(")
        elif current_value.endswith("ln("):
            t = current_value.strip("ln(")
        else:
            t = current_value[:-1]
        return t

    def invalid_input(self,var,result_label, *args):
        value = var

        try:
            eval(value)
            result_label.config(foreground='white')
        except SyntaxError:
            winsound.Beep(1000,100)
            result_label.config(foreground='red')

    def clear(self):
        return "0"









