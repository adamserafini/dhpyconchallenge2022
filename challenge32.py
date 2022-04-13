my_list = [1, 2, 3, 4, 5]

try:
    print(my_list[10])
except Exception as e:
    print(e)
print(my_list[10:])


"""
Answer
a)  line 1 → IndexError, line 2 →  [ ] (empty list)

Explanation
1. Attempting to access a member of a list using an index that exceeds the number of members results in an IndexError.

2. However, attempting to access a slice of a list  that exceeds the number of members in the list will not result in an IndexError and will simply return an empty list.

"""
