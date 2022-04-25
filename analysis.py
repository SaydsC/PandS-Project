# author Sadie Concannon
#program that outputs a summary of each variable to a single text file,
#saves a histogram of each variable to png files, and
#outputs a scatter plot of each pair of variables.
#performs any other analysis you think is appropriate

#import libraries to work with the dataset iris.csv,
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #for plotting

data = pd.read_csv("iris.csv")
print (data.head(150))
data.describe()
data.info()

plt.figure(figsize = (10, 7))
x = data['sepal.length']

#histogram
fig, axes = plt.subplots(2, 2, figsize=(10,10))

axes[0,0].set_title("Sepal Length")
axes[0,0].hist(data['sepal.length'], bins=7)

axes[0,1].set_title("Sepal Width")
axes[0,1].hist(data['sepal.width'], bins=5) 

axes[1,0].set_title("Petal Length")
axes[1,0].hist(data['petal.length'], bins=6)

axes[1,1].set_title("Petal Width")
axes[1,1].hist(data['petal.width'], bins=6)


#scatter plot
import seaborn as sns
f = plt.figure(figsize=(11,6))
fig = sns.scatterplot(x="sepal.length", y="petal.length", data=data)

sns.set()
#swarm plot grouping swarms by the variety of iris
sns.swarmplot(x="variety", y="petal.length", data=data)
plt.show()

data["variety"].value_counts()
print (data.head(150))

#Heat map
fig=plt.gcf()
fig.set_size_inches(10,7)
fig=sns.heatmap(data.corr(),annot=True,cmap='cubehelix',linewidths=1,linecolor='k',square=True,mask=False, vmin=-1, vmax=1, cbar_kws={"orientation": "vertical"},cbar=True)
plt.show()

print(data.describe())




