import pandas  as pd
import numpy as np
import math
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn import preprocessing
data = pd.read_csv("rainfall.csv")
print("Data heads:")
print(data.head())
print("Null values with mean of that particular column")
print(data.isnull().sum())
print("Filling null values with mean of that particular coloumn")
data = data.fillna(np.mean(data))
print("Mean of data:")
print(np.mean(data))
print("Null value in the dataset after preprocessing:")
print(data.isnull().sum())
print("\n\nShape: ",data.shape)
print("Info:")
print(data.info())
print("Group by:")
data.groupby('SUBDIVISION').size()
print("Co-Variance =",data.cov())
print("Co-Relation =",data.corr())
corr_cols = data.corr()['ANNUAL'].sort_values()[::-1]
print("Index of correlation columns:",corr_cols.index)
print("Scatter plot of annual and january attributes")
plt.scatter(data.ANNUAL, data.JAN)