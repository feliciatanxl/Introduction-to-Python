name = "John"
age = 17

# Prints True (name is John)
print(name == "John" or not age > 17)

# Prints False (name is John, but age IS 17, making 'not' false)
print(name == "John" and not age == 17)

# CORRECTED: Groups the names, and explicitly checks the age twice
print((name == "John" or name == "Jane") and (age >= 16 and age <= 25))