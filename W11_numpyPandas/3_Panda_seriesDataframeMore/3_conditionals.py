

import pandas as pd
scores = pd.read_csv('scores.csv')


#*************************************************
#! Divide student based on their marks into 4 different categories
#! Conditions based on same series i.e physics marks
#*************************************************
#*************************************************

print(scores[scores['Physics'] > 85].shape[0])             # Grade A

print(scores[scores['Physics'].between(70, 85)].shape[0])             # Grade B  
print(scores[scores['Physics'].between(70, 85)]['Physics'].count())   # Grade B  (both works)

print(scores[scores['Physics'].between(60, 70)].shape[0])  # Grade C
print(scores[scores['Physics'] < 60].shape[0])             # Grade D

#NOTE: in .between(), endPoints are included

#*************************************************
#! Divide student based on their marks into 4 different categories
#! Conditions based on two different series i.e physics and Gender 
#*************************************************
#*************************************************


# (scores['Physics'] > 85)   #? condition 1
# (scores['Gender'] == "M")  #? condition 2   
# print(scores[ ].shape[0])  #? Shove both the conditions inside [ ] with an '&' sign

print(scores[(scores['Physics'] > 85) & (scores['Gender'] == "M")].shape[0])             
print(scores[(scores['Physics'] > 85) & (scores['Gender'] == "F")].shape[0])             

