new_set = {5, 5.0}
print(new_set)

"""
Answer

a) {5}


Explanation

Uniqueness of values in a Python set (or keys in dictionary) is by equivalence, not identity. So even though 5 and 5.0 are distinct objects of different types, since they're equal, they can't both be in the same set.  
"""