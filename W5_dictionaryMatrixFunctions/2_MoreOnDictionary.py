
d = {'key': 'value'}

#* KEY restrications
# A dictionary key has to be immutable and hashable
# Duplication is not allowed
# Allowed data types:     int, float, boolean, string, tuple(with immutable elements),  coz they are immutable 
# not allowed data types: list, dictionary, tuple(with mutable elements) coz they are mutable


#* VALUE restrications
# Duplication is allowed for 'value'
# All data types are allowed in value


#* Dictionary COPY:
# It has similar properties as list so we need to use .copy() to copy a dictionary otherwise it will point to the same memory location


#* Iteration over a dictionary:
d={2:1, 22:23}
print(d)          # accessing entire dictionary

for key in d:
    print(key)    # accessing just the key

for key in d:
    print(d[key]) # accessing just the value


#* Dictionary METHODS:
d.keys()         # list of all keys of dictionary       
d.values()       # list values of all values of dict 
d.items()        # list with every elements inside is a tuple with key value pair: [(0, 0), (1, 1), (2, 2)]


