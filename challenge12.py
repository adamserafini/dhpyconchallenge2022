class A(set):
   def add(self, item):
       print("A")
       super().add(item)


class B(set):
   def add(self, item):
       print("B")
       super().add(item)


class C(A, B):
   def add(self, item):
       print("C")
       super().add(item)


C().add("item")

"""
Answer

C
A
B

Explanation

The super method searches for the next object in the original caller's "Method Resolution Order", which, in class C's case looks like:
C.__mro__ = ['A', 'B', 'set']
 
 This means that when the super method is called within class A,

"""

