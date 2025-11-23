
#! Functional approach of sorting a list

# STEPS:
# 1. Find out the minimum most element in the list l
# 2. Append that to a new list
# 3. Remove the minimum from the original list l

l=[90, 23, 97, 88, 5, 1]



# ************************************
# * ALGORITHM #1 - NON MODULAR APPROACH
# ************************************

# def obvious_sort1(l):

#     x = []
#     while(len(l)>0):
#         mini=l[0]
#         for i in range(len(l)):
#             if l[i]<mini:
#                 mini=l[i]
#         x.append(mini)
#         l.remove(mini)
#     return x


# print(obvious_sort1(l))



# ************************************
# * ALGORITHM #2 - MODULAR APPROACH : Breaking problem into smaller chunks and solving them
# ************************************

# def min_list(l):
#     mini=l[0]
#     for i in range(len(l)):
#         if(l[i]<mini):
#             mini=l[i]
#     return mini


# def obvious_sort2(l):
#     x=[]
#     while(len(l)>0):
#         mini=min_list(l)
#         x.append(mini)
#         l.remove(mini)
#     return x
    
# print(obvious_sort2(l))
