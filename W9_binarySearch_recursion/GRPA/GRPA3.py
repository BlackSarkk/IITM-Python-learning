
def collatz(n:int):

    if n == 1:
        return 0

    if n%2 == 0:
        num = n//2
    else:
        num = ((3*n)+1)

    return 1 + collatz(num)


print(collatz(10))