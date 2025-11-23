
# ********** Lec 8 [ Type Casting ]

# ? Conversion of a Data from one Data-Type to another Data-Type ika type-casting


a = int(4.2)        # will convert float to int
b = float(5)        # will convert int to float
c = int("10")       # will convert string to int
d = str(10)         # will convert int to string

e = bool(10)        # will convert int to bool      T
f = bool(0)         # will convert int to bool      F 
g = bool(-10)       # will convert int to bool      T
h = bool('0')       # will convert string to bool   T


print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))

# ? In boolean, "false" if and only if it is { 0, 0.0, -0, -0.0, "", None, False } else true


