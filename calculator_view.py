import tkinter as tk
from tkinter import  ttk
from option_Enum import *
class CalculatorUI(tk.Tk):
    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.title("Calculator")
        self.current_value = tk.StringVar(value='0')
        self.selected_option = tk.StringVar()
        self.keys = list('789456123 0.')
        self.op_keys = ["*", "/", "+", "-", "^", "(",")","mod","="]
        self.operations = ["s","l","e"]
        self.get_current_value = self.current_value.get()
        self.history_result = []
        self.get_selected_option = self.selected_option.get()

        self.display_frame = self.create_display_frame()
        self.init_components()


    def init_components(self):
        ##create label and combobox
        self.result_label = tk.Label(self.display_frame, text = self.get_current_value,anchor = tk.E, bg = "BLACK")
        self.selected_advance_op = ttk.Combobox(self, textvariable= self.selected_option)


        #create button
        self.keypad = self.create_keypad(self.keys,3,"WHITE")
        self.op = self.create_keypad(self.op_keys,1,"#FFA500")

        self.clear_button = self.create_method_button("CLR",11,self.clear)
        self.del_button = self.create_method_button("DEL",10,self.delete)
        self.his_button = self.create_method_button("History",12,self.handle_history)

        #bind section
        self.selected_advance_op.bind("<<ComboboxSelected>>",self.handle_selected_op)



        #set_combobox
        self.selected_advance_op["values"] = list(Operations)

        #pack sections
        self.selected_advance_op.pack(side = tk.TOP, expand = True , fill = tk.BOTH)
        self.keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.op.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        self.result_label.pack(expand = True , fill = tk.BOTH)


    def create_display_frame(self):
        display_frame = tk.Frame(self,height = 200, bg = "BLACK")
        display_frame.pack(expand = True , fill = tk.BOTH)
        return display_frame


    def handle_history(self):
        self.root = tk.Tk()
        self.root.title("History")
        history_frame = tk.Frame(self.root, height=200, bg="RED")
        history_frame.pack(side=tk.LEFT)
        self.history_text = tk.Text(history_frame, height=10, width=20)
        for i, value in enumerate(self.history_result):
            equal_index = value.find("=")
            self.history_text.insert(tk.END, value + "\n")
            self.history_text.tag_add(f"expression_tag{i}", f"{str(i+1)}.0", f"{str(i+1)}.{equal_index}")
            self.history_text.tag_add(f"result_tag{i}", f"{str(i+1)}.{equal_index+1}", f"{str(i+1)}.end")
            self.history_text.tag_bind(f"expression_tag{i}", "<Button-1>", lambda event, start=f"{str(i+1)}.0",
                                       end=f"{str(i+1)}.{equal_index}": self.recall_history(start, end))
            self.history_text.tag_bind(f"result_tag{i}", "<Button-1>", lambda event, start=f"{str(i + 1)}.{equal_index+1}",
                                                                              end=f"{str(i + 1)}.end": self.recall_history(start, end))

        self.history_text.pack()

    def recall_history(self, start, end):
        selected_text = self.history_text.get(start, end)
        self.get_current_value = selected_text
        self.update_result_label()




    def create_keypad(self,key,column,color):
        key_frame = tk.Frame()
        mem_list = len(key) // column
        for j in range(column):
            key_frame.grid_columnconfigure(j,weight=1)
        for k in range(mem_list):
            key_frame.grid_rowconfigure(k,weight=1)
        for i, key_num in enumerate(key):
            col = i % column
            row = i // column
            button = tk.Button(key_frame, text = key_num, bg = color,fg = "BLACK")
            button.grid(row=row, column=col, padx=2, pady=1, sticky=tk.NSEW)
            button.grid_columnconfigure(i,weight= 0)
            button.grid_rowconfigure(i,weight = 0)
            if key_num == "=":
                button.bind("<Button-1>", lambda event: self.evaluate(), add="+")
            else:
                button.bind("<Button-1>", self.display_value, add="+")
                button.bind("<Button-1>", self.invalid_input, add="+")

            button["fg"] = "blue"
        return key_frame


    def create_method_button(self,text,row,func):
        button = tk.Button(self.op, text=text, command=func)
        button.grid(row=row, column=0, padx=2, pady=1, sticky=tk.NSEW)
        button.grid_columnconfigure(1, weight=0)
        button.grid_rowconfigure(row, weight=0)
        return button


    def update_result_label(self):
        self.result_label.config(text = self.get_current_value)


    def handle_selected_op(self,event):
        if self.get_current_value == "0":
            self.get_current_value = self.selected_option.get() + "("
        elif self.selected_option.get() == "sqrt":
            if self.get_current_value[-1] in self.op_keys:
                self.get_current_value += "sqrt("
            else:
                for i in self.get_current_value:
                    if i not in self.op_keys:
                        self.get_current_value = f"sqrt({self.get_current_value})"
                        break
        elif self.selected_option.get() == "exp":
            if self.get_current_value[-1] in self.op_keys:
                self.get_current_value += "exp("
            else:
                for i in self.get_current_value:
                    if i not in self.op_keys:
                        self.get_current_value = f"exp({self.get_current_value})"
                        break
        elif self.selected_option.get() == "log10":
            if self.get_current_value[-1] in self.op_keys:
                self.get_current_value += "log10("
            else:
                for i in self.get_current_value:
                    if i not in self.op_keys:
                        self.get_current_value = f"log10({self.get_current_value})"
                        break

        elif self.selected_option.get() == "log":
            if self.get_current_value[-1] in self.op_keys:
                self.get_current_value += "log("
            else:
                for i in self.get_current_value:
                    if i not in self.op_keys:
                        self.get_current_value = f"log({self.get_current_value})"
                        break
        else:
            self.get_current_value += self.selected_option.get()
        self.update_result_label()


    def display_value(self, event):
        current_value = event.widget.cget("text")

        if self.get_current_value == '0':
            self.get_current_value = current_value
        else:
            self.get_current_value += current_value
        self.update_result_label()



    def evaluate(self):
        self.controller.evaluate(self.get_current_value)
        self.update_result_label()

    def clear(self):
        self.controller.clear()
        self.update_result_label()

    def invalid_input(self, *args):
        self.controller.invalid_input()

    def delete(self):
        self.controller.delete(self.get_current_value)
        self.update_result_label()


    def run(self):
        self.mainloop()





