heroes = ["Bolan", "Bowie"]

print("Bieber" in heroes < 1)

print("Bowie" in heroes < 1)

"""
Answer

False, TypeError: '<' not supported between instances of 'list' and 'int'

Explanation
This is an example of comparison chaining and short circuiting
Both expressions are chained comparisons that “expand” as follows:

In both cases, heroes < 1 would throw a TypeError (cannot compare list and int).
But in the "Bieber" case, the left side of the expression is False, so the right side is never evaluated due to short-circuit behaviour of the and operator.


"""

