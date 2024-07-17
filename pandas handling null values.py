import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the data for students and their marks in subjects
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

# Create a DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Step 1: Identify null values
print("\nIdentifying null values using isnull:")
print(df.isnull())
print("\nSum of null values per column:")
print(df.isnull().sum())
print("\nDataFrame summary using info:")
df.info()

# Step 2: Handle null values (example filling with mean for simplicity)
df_filled_mean = df.fillna(df.mean())
print("\nDataFrame after filling NaN with mean:")
print(df_filled_mean)

# Step 3: Visualize the effect of filling NaN values (example)
fig, axes = plt.subplots(3, 2, figsize=(15, 18))

# Example plot: Original vs Mean-filled for Maths marks
df.set_index('Student')[['Maths_Q1', 'Maths_Q2', 'Maths_Q3', 'Maths_Q4']].plot(kind='bar', ax=axes[0, 0], title="Original Maths Data")
df_filled_mean.set_index('Student')[['Maths_Q1', 'Maths_Q2', 'Maths_Q3', 'Maths_Q4']].plot(kind='bar', ax=axes[0, 1], title="Filled Maths Data")

# Plot for Physics marks
df.set_index('Student')[['Physics_Q1', 'Physics_Q2', 'Physics_Q3', 'Physics_Q4']].plot(kind='line', marker='o', ax=axes[1, 0], title="Original Physics Data")
df_filled_mean.set_index('Student')[['Physics_Q1', 'Physics_Q2', 'Physics_Q3', 'Physics_Q4']].plot(kind='line', marker='o', ax=axes[1, 1], title="Filled Physics Data")

# Plot for Chemistry marks
df.set_index('Student')[['Chemistry_Q1', 'Chemistry_Q2', 'Chemistry_Q3', 'Chemistry_Q4']].plot(kind='scatter', ax=axes[2, 0], title="Original Chemistry Data")
df_filled_mean.set_index('Student')[['Chemistry_Q1', 'Chemistry_Q2', 'Chemistry_Q3', 'Chemistry_Q4']].plot(kind='scatter', ax=axes[2, 1], title="Filled Chemistry Data")

plt.tight_layout()
plt.show()

# Step 4: Drop NaN values (similar options as shown in the previous example)

# Drop rows with any NaN values
df_dropped_any = df.dropna()
print("\nDataFrame after dropping rows with any NaN values:")
print(df_dropped_any)

# Drop columns with any NaN values
df_dropped_columns_any = df.dropna(axis=1)
print("\nDataFrame after dropping columns with any NaN values:")
print(df_dropped_columns_any)

# Drop rows with NaN values only in specified columns
df_dropped_subset = df.dropna(subset=['Maths_Q3', 'Maths_Q4'])
print("\nDataFrame after dropping rows with NaN values in 'Maths_Q3' and 'Maths_Q4':")
print(df_dropped_subset)

# Drop rows if a specified number of non-NaN values are not present (thresh)
df_dropped_thresh = df.dropna(thresh=8)
print("\nDataFrame after dropping rows with less than 8 non-NaN values:")
print(df_dropped_thresh)

# Drop NaN values based on different axes (row and column)
df_dropped_rows = df.dropna(axis=0)  # Default, drops rows
print("\nDataFrame after dropping rows with any NaN values (axis=0):")
print(df_dropped_rows)

df_dropped_columns = df.dropna(axis=1)
print("\nDataFrame after dropping columns with any NaN values (axis=1):")
print(df_dropped_columns)

# Drop rows or columns based on 'how' parameter ('all' or 'any')
df_dropped_all_rows = df.dropna(how='all')
print("\nDataFrame after dropping rows where all values are NaN:")
print(df_dropped_all_rows)

# Adding a column with all NaNs for demonstration
df['All_NaN'] = np.nan

df_dropped_all_columns = df.dropna(axis=1, how='all')
print("\nDataFrame after dropping columns where all values are NaN:")
print(df_dropped_all_columns)
