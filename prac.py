class grand_parent_class:

    def __init__(self) -> None:

        print("grand parent class init")

        self.constructor_var = "grand parent constructor"

       

    def grand_parent_method1(self):

        print("this is grand parent method1 can be used in parent classes & child classes")

# ---------------------------------------------

class parent_class(grand_parent_class):

    def __init__(self) -> None:

        print("parent class init")

        self.constructor_var_parent = "parent constructor"        

    def parent_method1(self):

        print("this is parent method1 can be used in child classes")

# ----------------------------------------------

class child_class1(parent_class):      

    def __init__(self) -> None:

        super().__init__()

        print("child1 class init")      

        self.constructor_var_child = "child1 constructor"

 

    def child1_method1(self):

        print("this is child1 method can only be used by child1")

 

class child_class2(parent_class):

    def __init__(self) -> None:      

        print("child2 class init")  

        self.constructor_var_child = "child2 constructor"

   

    def childe2_method1(self):

        print("this is child2 method can only be used by child2")

# ------------------------------------------------

 

def main():

    try:

        objChild1 = child_class1()

        objChild2 = child_class2() 

        objChild2.childe1_method1()       

    except Exception as e:

        print(f"exception in main: {str(e)}")

if __name__ == "__main__":

    main()