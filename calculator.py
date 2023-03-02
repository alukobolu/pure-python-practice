import math

x=input()

class calculate:

    program_name="calculator.py"

    def __init__(self):
        print("welcome to my calulator")
        self.printing ="the answer is :"

    def set_printout(self, printout):
        self.printing = printout

    def get_printout(self):
        return self.printing

    @classmethod
    def info(cls):
        return cls.program_name

    @staticmethod
    def typing():
        print("syntax error")

    def seperate(self,sti):
        for i in sti.split(): 
            if i.isdigit():
                res=i
            elif i=="!":
                j=res-1
                while j!=0:
                    res=res*j
                j=j-1

        print(self.printing ,res) 

    class basic(calculate):
        
        def __init__(self):
            print("you will now be calculating with basic math operators")

calc=calculate()
calc.seperate(x)