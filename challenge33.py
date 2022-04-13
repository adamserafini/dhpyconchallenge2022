val = True
print("mytext" * val)
val = False
print("mytext" * val)

"""
Answer
a)  line 1 →”mytext”, line 2 → “”

Explanation
 Booleans are subclass of integers in Python.
The integer value of True is 1 and False is 0.
So, “mytext” * 1 = “mytext”
“mytext” * 0 = “”

"""