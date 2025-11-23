
# ********** Lec 8 [ FUNCTIONS ]
    
def add(a, b):
    ans= a+b
    print(ans)
    return ans      # <---- need to return if you need to use the value later.

add(1, 6)   # 7
add(10, 72)   # 82


def discount(cost, d):
    ans = cost-(cost*(d/100))
    print(ans)
    return ans        # <---- need to return if you need to use the value later.

discount(100, 8)    # 92

num = add(1,2) + discount(100, 8)