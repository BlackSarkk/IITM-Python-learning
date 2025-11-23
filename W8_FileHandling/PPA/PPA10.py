
'''
Write a function named number_grid that accepts two positive integers m and n as arguments. Within the function, create a file named numgrid.csv. Write the first mn positive integers to the file in the following way:

Each line should be a sequence of n comma-separated integers.
There should be a total of m lines in the file.
For example, for the case of m=5,n=3, the file should be:

1,2,3
4,5,6
7,8,9
10,11,12
13,14,15
You do not have to accept input from the console. You just have to write the function definition.
'''


def number_grid(m, n):
    """
    Write a number grid to a file

    Arguments:
        m, n: positive integers
    Return:
        None
    """
    
    i = 1
    nList = []
    
    f=open("numgrid.csv", "w")
    
    for x in range(m):
        for y in range(n):
            nList.append(i)
            i+=1
            
        f.write(",".join(str(x) for x in nList))        ## IMP****
        
        if (x!=m and y!=n):
            f.write("\n")
            
        nList = []
        
    f.close()
    