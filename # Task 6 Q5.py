# Task 6 Q5
def hello_decorator(func):
  
    def inner1():
        print("Hello, this is before function execution")
  
        func()
  
        print("This is after function execution")
          
    return inner1
  
def function_to_be_used():
    print("This is inside the function !!")
  

function_to_be_used = hello_decorator(function_to_be_used)
  
  
# calling the function
function_to_be_used()