def do_twice(func):  #3rd call comes here

    def wrapper_do_twice():  #5th call comes here

        func()  #6th call comes here and from here say_hello will be called

        func()  #9th call comes here and from here say_hello will be called

    return wrapper_do_twice  #4th call comes here and def wrapper_do_twice is called

 

@do_twice  #2nd call comes here and execution goes to def do_twice(func), where func is say_hello

def say_hello():  #7th call comes here, 10th call comes here again

    print("Hello There")  #8th call comes here and this is printed, 11th call comes here again and gets printed for second time

 

say_hello()  #1st call comes here, 12th call comes here and program execution is over.


