rows = 5

# Upper Part
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2*i - 1))

# Lower Part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2*i - 1))