import pandas as pd
import numpy as np
# pandas series

# 1.Pandas Series from the list ['a', 'b', 'c', 'd'] with index [q,w,e,r]
ser_list = pd.Series(['a', 'b', 'c', 'd'],index=['q','w','e','r'])
print(ser_list)

# 2.panda series from an numpy array
array=np.array([2,4,5,6,8,7])
arr_ser=pd.Series(array)
print(arr_ser)

# 3.Pandas Series from a dictionary {'a': 1, 'b': 2, 'c': 3, 'd': 4}.
series_dict = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(series_dict)

# 4. Panda series with a scalar value
scalar_series=pd.Series(12000,index=['a','b','c','d'])
print(scalar_series)

# 5.series [10,20,30,40] with index=[a,b,c,d] and extract the value of B
ser=pd.Series([10,20,30,40],index=['a','b','c','d'])
print("Required Series:")
print(ser)
value_b=ser['b']
print(value_b)

# 6.getting first 3 elements of series [10,20,30,40]
s=pd.Series([10,20,30,40])
print("first 3 elements:")
print(s.head(3))

# 7. sorting the list 
print("sorted list:")
print(s.sort_values())

# 8.computing the mean,meadian and standard deviation
data=pd.Series([23.5,65.8,89.0,32.0,21.8])
print(data)
print("mean: ",data.mean())
print("median:",data.median())
print("std:",data.std())


