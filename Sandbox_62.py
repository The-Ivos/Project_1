# Python code to illustrate 
# Decorators with parameters in Python 
def decorator(like):
    print("Inside decorator")
    
    def inner(func):
        # code functionality here
        print("Inside inner function")
        print("I like", like) 
        
        def wrapper():
            func()
        
        return wrapper
    
    # returning inner function 
    return inner

@decorator(like="geeksforgeeks")
def my_func():
    print("Inside actual function")

# Call the decorated function
my_func()