

# ********** Lec 1 [ PANDAS ]



'''
Pandas is an external liberary which provides high performance data manipulation and analysis tool
'''

#? What are the total marks of topper from the scores dataset

#************************************************** 
#! Using FileHandlingApproach
#************************************************** 
#************************************************** 

'''
f = open('scores.csv', 'r')
scores = f.readlines()[1:]
max = 0
for record in scores:
    fields = record.split(',')
    if int(fields[8]) > max:
        max = int(fields[8])
print(max)

'''


#************************************************** 
#! Using Panda
#************************************************** 
#************************************************** 


'''
python3 -m venv myenv
source myenv/bin/activate
pip install pandas
python 2_whyPandas.py

deactivate

    pip install -r requirements.txt
'''


import pandas as pd
scores = pd.read_csv('scores.csv')

# print(scores)
# print(scores.shape)  # --> tuple
# print(scores.count)  

# print(scores['Total'].max())
# print(scores['Total'].min())

# print(scores['Total'].mean())  # --> mean (avg)
# print(scores['Total'].sum())   # --> sum 

# print(scores['Total'].sort_values())
# print(scores['Total'].sort_values(ascending = False))





