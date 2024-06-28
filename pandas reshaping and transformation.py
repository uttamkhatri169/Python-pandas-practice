import pandas as pd
import numpy as np

data = {
    'Name': ['Uttam', 'Saurav', 'Hardik', 'Japjot', 'Tarun', 'Vansh', 'Ishaan', 'Kartik'],
    'Age': [24, 27, 22, 32, 29, 25, np.nan, 30],
    'City': ['Delhi', 'Faridabad', 'Hyderabad', 'Mumbai', 'Jaipur', 'Mumbai', 'Rohtak','Jaipur'],
    'Score': [85.6, 90.4, 78.9, 88.2, 92.1, 75.0, 89.5, 91.2],
    'Date': pd.date_range(start='2023-01-01', periods=8, freq='M')
}

df = pd.DataFrame(data)
print(df)


#reshaping

#pivoting data
df_pivot = df.pivot(index='City', columns='Name', values='Score')
print(df_pivot)

#melting data
df_melt = df.melt(id_vars=['Name', 'City'], value_vars=['Age', 'Score', 'Date'])
print(df_melt)

#stacking data
df_stacked = df.set_index(['Name', 'City']).stack()
print(df_stacked)

#Unstacking data
df_unstacked = df_stacked.unstack()
print(df_unstacked)

#using pivot table
df_pivot_table = df.pivot_table(values='Score', index='City', columns='Name', aggfunc='mean')
print(df_pivot_table)


# data transformation

#groupby and aggregation
df_grouped = df.groupby('City')['Score'].mean()
print(df_grouped)

#Aggregation with Multiple Functions
df_agg = df.groupby('City')['Age'].agg(['mean', 'max'])
print(df_agg)

# Resampling Time Series Data
df_resampled = df.set_index('Date').resample('M')['Score'].mean()
print(df_resampled)

# Applying Functions
df['Adjusted_Score'] = df['Score'].apply(lambda x: x * 1.10)
print(df)

# Dropping Columns
df_dropped = df.drop(columns=['Age', 'City'])
print(df_dropped)

# Renaming Columns
df_renamed = df.rename(columns={'Score': 'Exam_Score'})
print(df_renamed)







