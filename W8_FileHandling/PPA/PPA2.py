'''
Write a function named read_line that accepts a text file named filename and a positive integer 
n as arguments. Within the function, read the file and return the nth line of the file. If the file has fewer than 
n lines, return the string 'None'.

(1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 'public_1.txt'.

(2) You do not have to accept input from the console or print the output. You have to write the function definition.
'''

def read_line(filename, n):
    """
    Read the nth line of the file

    Argument:
        filename: string, name of the file to be read
    Return:
        string: return nth line of the file
    """
    
    f=open(filename, "r")
    
    if ( len(f.readlines()) < n ):
        f.close()
        return 'None'
        
    f.seek(0)
    
    for index, line in enumerate(f.readlines(), start=1):
        if index == n:
            f.close()
            return line
            
            
    f.close()
    
    return 'None'