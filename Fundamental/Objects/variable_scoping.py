#Local - Inside the current function
#Enclosing Any and all enclosing function
#Global Top-level of module
#Built-in Provide by the builtins module

#LEGB 

count = 0

def show_count():
    print("count=", count)

def set_count(c):
    global count
    count = c

show_count()
set_count(10)
show_count()
