import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
from sklearn.impute import IterativeImputer

# Updated DataFrame
data = {
    'Student': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Maths_Q1': [85, 78, np.nan, 92, 88],
    'Maths_Q2': [np.nan, 80, 75, 88, 82],
    'Maths_Q3': [90, 82, 79, 85, np.nan],
    'Maths_Q4': [88, 85, np.nan, 90, 86],
    'Physics_Q1': [78, 82, 85, 88, 90],
    'Physics_Q2': [np.nan, 85, 80, 90, 88],
    'Physics_Q3': [82, 88, 86, np.nan, 90],
    'Physics_Q4': [85, 90, 88, 92, 86],
    'Chemistry_Q1': [83, 80, 85, np.nan, 88],
    'Chemistry_Q2': [85, 88, 82, 90, 86],
    'Chemistry_Q3': [80, 86, 88, 92, 90],
    'Chemistry_Q4': [82, 90, 85, 88, 86]
}

df = pd.DataFrame(data)

# Identify null values
null_info = df.isnull().sum()
print("Null values in the DataFrame:")
print(null_info)

# Interpolation Techniques

# Linear Interpolation
df_interpolated_linear = df.interpolate(method='linear')
print("\nDataFrame after Linear Interpolation:")
print(df_interpolated_linear)

# Padding (Forward Fill)
df_interpolated_pad = df.interpolate(method='pad')
print("\nDataFrame after Padding Interpolation:")
print(df_interpolated_pad)

# Backward Fill
df_interpolated_bfill = df.interpolate(method='bfill')
print("\nDataFrame after Backward Fill Interpolation:")
print(df_interpolated_bfill)

# Replace method

# Replace NaN with specific values
df_replace = df.replace({np.nan: -1, None: 'Unknown'})
print("\nDataFrame after Replacing NaN values:")
print(df_replace)

# End of Distribution Method

# Fill NaN with values at the end of the distribution (e.g., 95th percentile)
df_end_of_dist = df.fillna(df.quantile(0.95, numeric_only=True))
print("\nDataFrame after End of Distribution Imputation:")
print(df_end_of_dist)

# Visualizing Before and After Interpolation

# Boxplots to visualize distributions
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Original Data
df[['Maths_Q1', 'Maths_Q2', 'Maths_Q3', 'Maths_Q4']].plot(kind='box', ax=axes[0, 0], title='Maths Original Data')
df[['Maths_Q1', 'Maths_Q2', 'Maths_Q3', 'Maths_Q4']].plot(kind='hist', bins=10, alpha=0.7, ax=axes[1, 0], title='Maths Original Data')

# After Linear Interpolation
df_interpolated_linear[['Maths_Q1', 'Maths_Q2', 'Maths_Q3', 'Maths_Q4']].plot(kind='box', ax=axes[0, 2], title='Maths Linear Interpolation')
df_interpolated_linear[['Maths_Q1', 'Maths_Q2', 'Maths_Q3', 'Maths_Q4']].plot(kind='hist', bins=10, alpha=0.7, ax=axes[1, 2], title='Maths Linear Interpolation')

plt.tight_layout()
plt.show()

# Assessing Skewness and Symmetry with Quartiles

# Calculate quartiles
quartiles = df[['Maths_Q1', 'Maths_Q2', 'Maths_Q3', 'Maths_Q4']].describe()
print("\nQuartiles of the Maths data:")
print(quartiles)

# Calculate Interquartile Range (IQR)
iqr = quartiles.loc['75%'] - quartiles.loc['25%']
print("\nInterquartile Range (IQR) for Maths:")
print(iqr)

# Advanced Imputation Techniques

# K-Nearest Neighbors (KNN) Imputation
knn_imputer = KNNImputer(n_neighbors=2)
df_knn_imputed = pd.DataFrame(knn_imputer.fit_transform(df[['Maths_Q1', 'Maths_Q2', 'Maths_Q3', 'Maths_Q4']]), columns=['Maths_Q1', 'Maths_Q2', 'Maths_Q3', 'Maths_Q4'])
print("\nDataFrame after KNN Imputation for Maths:")
print(df_knn_imputed)

# Multiple Imputation by Chained Equations (MICE)
mice_imputer = IterativeImputer(max_iter=10, random_state=0)
df_mice_imputed = pd.DataFrame(mice_imputer.fit_transform(df[['Maths_Q1', 'Maths_Q2', 'Maths_Q3', 'Maths_Q4']]), columns=['Maths_Q1', 'Maths_Q2', 'Maths_Q3', 'Maths_Q4'])
print("\nDataFrame after MICE Imputation for Maths:")
print(df_mice_imputed)
