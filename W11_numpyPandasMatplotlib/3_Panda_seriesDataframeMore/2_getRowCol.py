

import pandas as pd
scores = pd.read_csv('scores.csv')


#*************************************************
#! Printing specific rows/cols
#*************************************************
#*************************************************

#? Whenever we try to print entire dataFrame, it displays all the rows from the given dataFrame
#? Here the dataSet is smaller so its easy to print it and read it, things gets complicated when we have much larger dataset
#? Sometimes we may prefer to look over some sample rows from the given dataset
print(scores.head())  # gets only top 5 rows from the given dataSet
print(scores.tail())  # gets only last 5 rows from the given dataSet


print(scores[scores['Name'] == "Nisha"])   # Get all the dataset named scores, but make sure to get the row which has name as Nisha  
print(scores[scores['Gender'] == "M"]['Total'].max())  # Get the M topper
print(scores[scores['Gender'] == "F"]['Total'].max())  # Get the F topper


