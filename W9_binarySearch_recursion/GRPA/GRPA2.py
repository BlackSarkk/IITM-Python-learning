
def Linear(p, q, k):
    
    if len(p) != len(q):
        return False
    
    if len(p) == 0:
        return True

    if q[0] == k*p[0]:
        return Linear(p[1:], q[1:], k)
    else:
        return False


p = [1, 2, 3, 4, 5]
q = [2, 6, 6, 8, 10]
k = 2

print(Linear(p, q, k))