class RegularPythonClass:

   @staticmethod
   def print_args(*args):
       print(f"{len(args)} args: {args}")

   @staticmethod
   def print_args(a):
       print(f"1 arg: {a}")

RegularPythonClass().print_args("a", "b")

"""
Answer
b) TypeError when calling print_args

Explanation
The exact exception is: 
TypeError: RegularPythonClass.print_args() takes 1 positional argument but 2 were given

This is because Python classes by default do not support function “overloading”, 
I.e. multiple functions with identical names and different function signatures. 
The namespace for the class ends up only containing the most-recently defined method– in this case, the second one. 

"""