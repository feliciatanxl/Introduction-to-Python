string = '0123456789'

# Loops through the string to get characters, and loops 10 times to make 10 rows
matrix = [[char for char in string] for _ in range(10)]

for row in matrix:
    print(row)