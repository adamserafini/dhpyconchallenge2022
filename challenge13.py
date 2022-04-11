from typing import List, AnyStr, Dict


def count_strings(strings: List[AnyStr], counts: Dict[AnyStr, int] = {}):
   counts.update({item: strings.count(item) for item in set(strings)})
   return counts

letter_counts = count_strings(["a", "a"])
number_counts = count_strings(["1", "2"])
print(number_counts)

"""
Answer

{'a': 2, '2': 1, '1': 1}

Explanation

The counts default parameter is a dictionary, which is mutable.
That means that a single default dictionary is instantiated when the function is first declared, and is updated both times the function is called without an explicit counts parameter value.

"""

