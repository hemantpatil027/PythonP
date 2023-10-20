def wrapper_upper_case_func(func):

    def upper_case(var:str):

        inner_var = var.upper()

        func(inner_var)

    return upper_case

 

@wrapper_upper_case_func

def do_something(var:str):

    print(f"changed var: {var}")

 

do_something("i-tek")
print(("hemant patil").upper())
