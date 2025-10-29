class Calculotor:
  def __init__(self,a,b):
    X = a
    Y = b

def operate(self, operation):
  if operation == "add":
    return X + Y
  elif operation == "substract":
    return X-Y
  elif operation == "multiply":
    return X*Y
  elif operation == "divide":
    if Y != 0:
      return X/Y
    else:
      return "Error:Divison by Zero"
  else:
    return "Invalid operation"
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
op = input("Enter operation (add/substract/multiply/divide):").lower()

calc = Calculator(a,b)
print("Result:", calc.operate(op))

       
