import pandas as pd
import sklearn
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.model_selection import train_test_split
df = pd.read_csv("Conversion Data Set.csv")
df.head()
df.describe()
import  seaborn as sns
sns.scatterplot(data = df, x = df["Age"], y = df["Conversion"])
