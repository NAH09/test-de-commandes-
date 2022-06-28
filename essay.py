import imp
import pandas as pd
import seaborn as se
import os
import matplotlib.pyplot as plt
df = pd.read_csv('C:/Users/dell/train_and_test2.csv')
df.head(10)
type(df)
df.columns
se.countplot(x="Embarked",data=df)
plt.show()
se.countplot(x="Embarked",hue="Sex",data=df)
plt.show()