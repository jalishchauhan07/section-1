
 # Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
    # Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
    # Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class Calculator:
    
    def __init__(self,a,b,operation):
        if(operation=="addition" or operation=="add" or operation=="Add"):
            print("Addition of ",a," and ",b," is ",self.addition(a,b))
        elif(operation=="subtraction" or operation=="sub"or operation=="Sub"):
            print("Subtraction of ",a," and ",b," is ",self.Subtraction(a,b))
        elif(operation=="division" or operation=="div"or operation=="Div"):
            print("Division of ",a," and ",b," is ",self.division(a,b))
        elif(operation=="multiplication"or operation=="mul" or operation=="Mul"):
            print("Multiplication of ",a," and ",b," is ",self.multiplication(a,b))
        else:
            print("You have Enter Wrong Operation !!!!");
    
    def addition(self,a,b):
        return a+b;
    
    def subtraction(self,a,b):
        return a-b;
    
    def multiplication(self,a,b):
        return a*b;
        
    def division(self,a,b):
        return a/b;
        
p=Calculator(float(input("Enter No:")),float(input("Enter No:")),str(input("Enter operation name :")))
