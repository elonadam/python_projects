logo = """
 _____________________
| ElonFx-991_ ______  |
| |             0.  | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add (a,b):
  """adds two numbers"""
  return a + b
  
def subtract (a,b):
  """subtracts two numbers"""
  return a - b

def multiply (a,b):
  """multiplies two numbers"""
  return a * b

def divide (a,b):
  """divides two numbers"""
  return a / b

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}
print(logo)
def calculator():
  num1 = float(input("What's the 1st number ?: "))
  for key in operations:
    print(key, end=" ") #print all symbols in the same line
  toContinue = True
  
  while(toContinue):
    operator = input("\nchoose the operation you want to perform\n")
    num2 = float(input("What's the 2nd number ?: "))
    func = operations[operator] #chosed function
    answer = func(num1,num2)
    print(f"{num1} {operator} {num2} = {answer}")
    
    user_choice = input(f"If you wish to continue with {answer} press 'c'\nIf you want new to start a new calculation press 'y'\nElse press any key to exit: ")
    if  user_choice == 'c':
      num1 = answer
    elif user_choice == 'n':
      break
    else:
      toContinue = False
      calculator()


calculator()
