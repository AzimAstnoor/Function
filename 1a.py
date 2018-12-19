a = {1}
b = {6}
print(a)
a.update(a, {2, 3})
b.update(b, {4, 5})
print(a)
c = a | b
print(c)
d = c - a
print(d)
b.discard(4)
b.discard(5)
print(b)
a = {"Saurabh", "Ajay", "Ishank", "Prashant"}
b = {"Saurabh", "Vijay", "Shanks", "Drashant"}
c = a & b
print(c)
print(a^b)
c = (a^b).pop()
print(c)