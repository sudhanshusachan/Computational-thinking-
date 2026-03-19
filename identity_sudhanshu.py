# Task~1
# Integer
a = 11
print("Before change (int):", id(a))
a = 07
print("After change (int):", id(a))

print("------")

# String
s = "hello"
print("Before change (string):", id(s))
s = "sudhanshu"
print("After change (string):", id(s))

print("------")

# List
lst = [7 , 18, 45]
print("Before change (list):", id(lst))
lst.append(4)
print("After change (list):", id(lst))
