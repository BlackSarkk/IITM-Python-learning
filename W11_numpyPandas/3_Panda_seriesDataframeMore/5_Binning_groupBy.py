
import pandas as pd
scores = pd.read_csv('scores.csv')


#*************************************************
#! Binning
#*************************************************
#*************************************************

# print(scores.groupby('Gender').groups)  # Gets dict of M and F as Key, and Card No. as their index values

#? print(scores.groupby("Every key is a unique value from this Col").groups)
#? This groupBy feature of panda is very handy when we try to divide our data into BINS



#*************************************************
#! Old code with not repetitons. (using groupby)
#*************************************************
#*************************************************

subject = ['Mathematics', 'Physics', 'Chemistry']

for sub in subject:
    print('Above 85 in', sub)
    avg = scores[sub].mean()
    print(scores[scores[sub] > avg].groupby('Gender').groups)




# Whatever we have seen so for wrt python pandas, is just the tip of the iceburg
# In rest of other courses we'll see lot more...
# So don't break head while reading pandas docx... 