# Logical Operators

# or
a = 40
b = 60

x = 2
y = 3

out = (a < b) or (x > y)
print(out)                  # output is True

out = (a > b) or (x < y)
print(out)                   # output is True

out = (a > b) and  (x > y)
print(out)                   # output is False

# and

out = (a > b) and  (x < y)
print(out)                   # output is False

out = (a < b) and  (x < y)
print(out)                   # output is True

out = not(x < y)
print(out)                    # output is False