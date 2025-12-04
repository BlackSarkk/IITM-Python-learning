

import pandas as pd
scores = pd.read_csv('scores.csv')


#*************************************************
#! Conditions and Looping
#*************************************************
#*************************************************

subject = ['Mathematics', 'Physics', 'Chemistry']

for sub in subject:
    print('Above 85 in', sub)
    print(scores[(scores[sub] > 85) & (scores['Gender'] == "M")].shape[0], 'M')             
    print(scores[(scores[sub] > 85) & (scores['Gender'] == "F")].shape[0], "F")     



#*************************************************
#! Multiple Conditions and Loops
#*************************************************
#*************************************************

subject = ['Mathematics', 'Physics', 'Chemistry']

for sub in subject:
    print('Above 85 in', sub)
    avg = scores[sub].mean()

    print(scores[(scores[sub] > avg) & (scores['Gender'] == "M")].shape[0], 'M')             
    print(scores[(scores[sub] < avg) & (scores['Gender'] == "M")].shape[0], 'M')             

    print(scores[(scores[sub] > avg) & (scores['Gender'] == "F")].shape[0], "F")     
    print(scores[(scores[sub] > avg) & (scores['Gender'] == "F")].shape[0], "F")     

