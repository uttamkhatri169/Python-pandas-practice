import pandas as pd
import numpy as np

#dataframe from 2-D dictionary
dict1={
    'students':['Uttam','Saurav','Ritik','Hardik','Ankush'],
    'Marks':[34,56,43,23,23],
    'section':['a','b','c','d','e']
}

df=pd.DataFrame(dict1)
print(df)

#dataframe from list of dictionaries

d1={'name':'Uttam','age':'20', 'score':'89'}
d2={'name':'Rashmi','age':'19', 'score':'104'}
d3={'name':'Saurav','age':'20', 'score':'56'}
d4={'name':'Hardik','age':'19', 'score':'109'}
lst=[d1,d2,d3,d4]
df1=pd.DataFrame(lst)
print(df1)

# dataframe from an 2D array
a1=np.array([[1,2,3,4],[34,56,67,78],[20,40,50,60]])
df=pd.DataFrame(a1,index=['a','b','c'])
print(df)

# Basic info
df.info()

# First three rows
print(df.head(3))

# Descriptive statistics
print(df.describe())



data = {
    'Name': ['Uttam', 'Japjot', 'Saurav', 'Hardik', 'Vansh'],
    'Age': [24, 27, None, 32, 29],
    'City': ['Rohtak',None, None, 'Rohtak', 'Delhi'],
    'Score': [85.6, 90.4, 78.9, None, 92.1]
}
df2 = pd.DataFrame(data)
print(df2)

# Checking for missing values in each column
print( "missing values:")
print(df2.isnull().sum())

# Extracting the 'Age' column
print(df2['Age'])

# Extracting the 'Name' and 'City' columns
print(df2[['Name', 'City']])

#getting data of particular row
print(df2.iloc[2])

# Frequency of each unique value in the 'City' column
city_counts = df2['City'].value_counts()
print(city_counts)

# List unique values in the 'City' column
unique_cities = df2['City'].unique()
print(unique_cities)

# Correlation matrix for 'Age' and 'Score'
correlation_matrix = df2[['Age', 'Score']].corr()
print(correlation_matrix)
