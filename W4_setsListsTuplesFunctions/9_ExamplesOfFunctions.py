
# ********** Lec 9 [ FUNCTIONS EXAMPLES ]


#* Writing function on lists

def first_element(l):
    return l[0]

def second_element(l):
    return l[1]

x = [1, 2, 3, 4]
first_element(x)
second_element(x)



###########################
###########################
#***************** Example 1

l = [1, 5, 2, 6, 7, -1, 23, 0]
z = [10, 20, 30]

def list_min(l):
    mini = l[0]
    for i in range(len(l)):
        if (l[i]< mini):
            mini=l[i]
    return mini

print(list_min(l))

###########################
###########################
#****************** Example 2

l = [1, 5, 2, 6, 7, -1, 23, 0]
z = [10, 20, 30]

def list_maxi(l):
    maxi=l[0]
    for i in range(len(l)):
        if(l[i] > maxi):
            maxi=l[i]
    return maxi

print(list_maxi(l))

###########################
###########################
#****************** Example 4

l = [1, 5, 2, 6, 7, -1, 23, 0]
z = [10, 20, 30]

def list_appendBefore(l,z):
    newl = []
    for i in range(len(z)):
        newl.append(z[i])
    for i in range(len(l)):
        newl.append(l[i])
    return newl


print(list_appendBefore(l, z))

###########################
###########################
#***************** Example 5

l = [1, 5, 2, 6, 7, -1, 23, 0]
z = [10, 20, 30]

def list_appendEnd(l,z):
    newl = []
    for i in range(len(l)):
        newl.append(l[i])
    for i in range(len(z)):
        newl.append(z[i])
    return newl


print(list_appendBefore(l, z))


###########################
###########################
#***************** Example 6

l = [1, 5, 2, 6, 7, -1, 23, 0]
z = [10, 20, 30]

def list_avg(l): 
    sum = 0
    for i in range(len(l)):
        sum=sum+l[i]
    ans=sum/len(l)
    return ans

print(list_avg(l))








