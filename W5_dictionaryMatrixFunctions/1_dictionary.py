

#***************************
# DICTIONARY v/s SET creation
#***************************

# p={1}
# d={} 

# print(type(p))  #set
# print(type(d))  #dictionary


# d['sudarshan'] = 2390842390
# d['ramya']= 423424323
# d['ravi']= 324241423

# print(d['sudarshan'])   # 2390842390




#**********************************************************
#**********************************************************


malgudi = ['it', 'was', 'Monday', 'morning', 'Swaminathan', 'was', 'reluctant', 'to', 'open', 'his', 'eyes', 'he', 'considerd', 'Monday', 'specially', 'unpleasant', 'in', 'the', 'calendar', 'After', 'the', 'delecious', 'freedom', 'of', 'saturday', 'and', 'sunday', 'it', 'was', 'difficult', 'to', 'get', 'into', 'the', 'Monday', 'mood', 'of', 'work', 'and', 'discipline', 'He', 'shuddered', 'at', 'the', 'very', 'thought', 'of', 'school', 'that', 'dismal', 'yellow', 'building', 'the', 'fire', 'eyed', 'Vednayagam', 'his', 'class', 'teacher', 'and', 'the', 'headmaster', 'with', 'his', 'thin', 'long', 'cane']
s = set(malgudi)   # no repetition


# ***************************
# Creating a Dictionary with word count
# ***************************


# d={}
# for x in s:
#     d[x] = 0

# print(d)

# for x in malgudi:
#     d[x]=d[x]+1

# print(d)



# ***************************
# Finding max frequency of words
# ***************************


# d={}
# max = 0 
# for x in s:
#     d[x] = 0

# for x in malgudi:
#     d[x]=d[x]+1
#     if(d[x])>max:   # max frequency
#         max=d[x]

# print(max)




# ***************************
# Finding most frequent word
# ***************************


d={}
max = 0 
answer_word=''
for x in s:
    d[x] = 0

for x in malgudi:
    d[x]=d[x]+1
    if(d[x])>max:   
        max=d[x]
        answer_word = x

print(answer_word)




# ***************************
# ***************************


d = {}
d['sudarshan']=[92,34,21]
d['ajit']=[32,23,45]
d['supriya']=[42,33,23]

d['sudarshan'][0]



# ***************************
# ***************************


d = {}
d['sudarshan']=[92,34,21,'sudharshan@gmail.com']
d['ajit']=[32,23,45,'ajit.rao123@gmail.com']
d['supriya']=[42,33,23,'supriya321@gmai.com']

d['supriya'][1]
d['supriya'][3]