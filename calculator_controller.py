from calculator_view import  *
from calculator_model import  *

class CalculatorController:
    def __init__(self):
        self.model =  CalculatorModel()
        self.view = CalculatorUI(self)


    def clear(self):
        current_value = self.model.clear()
        self.view.get_current_value = current_value
        self.view.selected_option.set("")


    def delete(self,current_value):
        del_value = self.model.delete(current_value)
        self.view.get_current_value = del_value


    def evaluate(self,current_value):
        result = self.model.evaluate(current_value)
        if result:
            self.view.history_result.append(f"{current_value} = {result}")
        self.view.get_current_value = result

    def invalid_input(self):
        self.model.invalid_input(self.view.get_current_value,self.view.result_label)

    def run(self):
        self.view.mainloop()






