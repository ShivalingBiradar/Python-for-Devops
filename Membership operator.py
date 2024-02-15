# Membership Operator

first_tuple = ("IOT", "DevOps", 47, 89, 1.5)
ans ="DevOps" in first_tuple
print(ans)                  # output is true

ans ="DevOps" not in first_tuple
print(ans)                  # output is False

ans =67 in first_tuple
print(ans)                  # output is False

ans =47 in first_tuple
print(ans)                  # output is True


ans =67 not in first_tuple
print(ans)                  # output is True