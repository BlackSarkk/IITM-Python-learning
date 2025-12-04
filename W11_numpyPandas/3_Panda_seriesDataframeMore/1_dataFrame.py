
import pandas as pd


#*************************************************
#! DataFrame, series
#*************************************************
#*************************************************

scores = pd.read_csv('scores.csv')
# scores contain whole complete table of scores.csv file
# Wrt pandas this table is what is known as dataFrame

#? DataFrame is nothing but a 2D dimention structure which is used to store a tabular data
print(type(scores))  # DataFrame 


#? Any specific column in DataFrame ika Series in pandas
#? It is a 1D entity.
print(type(scores['Name']))  # series 







