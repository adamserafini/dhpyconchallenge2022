input = {
    "todo": ["TASK-1", "TASK-2"],
    "development": {"TASK-3": "IN PROGRESS"},
    "done": {"TASK-4": "2022-01-01"}
}

match input:
    case {"development": {}}:
        print("OPTION 1")
    case {"todo": [], "development": {}, "done": []}:
        print("OPTION 2")
    case {"todo": todo, "development": dev, "done": done}:
        print("OPTION 3")
    case _:
        print("OPTION 4")

"""
Answer
a) OPTION 1

Explanation
Structural pattern matching does not require an exact match when it comes to dicts: it is a match as long as all 
key/value pairs which are present in the 'case' clause are also present in the input dictionary, but not vice versa.

If option 3 were first in the match statement, it would be the correct answer because the patterns also match. 

"""
