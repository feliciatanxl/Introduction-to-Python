name = "John"
age = 17

if name == "John" or age == 17:
    print("name is John")
    print("John is 17 years old")

tasks = ["task1", "task2"]

# CORRECTED: 'if tasks:' automatically evaluates to True if the list has items
if tasks:
    print("Not an empty list!")
else:
    print("tasks are empty!")

tasks.clear()  # Empty the list

# TODO COMPLETED: 'if not tasks:' evaluates to True if the list is empty
if not tasks:
    print("Now empty!")