# author Sadie Concannon
#program that outputs a summary of each variable to a single text file,
#saves a histogram of each variable to png files, and
#outputs a scatter plot of each pair of variables.
#performs any other analysis you think is appropriate

#import libraries to work with the dataset iris.csv,
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #for plotting
import sys
import seaborn as sns

data = pd.read_csv("iris.csv")

def summary_to_file():
    sys.stdout = open("summary.txt","w")
    print ("\n")
    print ("==============================================================================")
    print ("Overview of the whole dataset:")
    print ("\n")
    print (data)
    print ("\n")
    print ("==============================================================================")
    print ("Summary of numeric values: ")
    print ("\n")
    # reference for .describe() and .info(): https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77
    print (data.describe())
    print ("\n")
    print ("==============================================================================")
    print ("Number of samples of each varirety of Iris:")
    print ("\n")
    print (data.info())
    print ("\n")
    print ("==============================================================================")
    print("Number of occurances of each variety of Iris:")
    print ("\n")
    print (data["variety"].value_counts())
    print ("\n")
    print("     In percentile:")
    print("\n")
    # reference: https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6
    print (((data["variety"].value_counts(normalize=True))*100))
    print("\n")
    print ("==============================================================================")
    sys.stdout.close()


#histogram amended to have 4 on one page
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
#imported seaborn as sns above
f = plt.figure(figsize=(11,6))
fig = sns.scatterplot(x="variety", y="petal.length", data=data)

sns.set()
plt.show()

#further analysis

#swarm plot grouping swarms by the variety of iris
f=plt.figure(figsize=(11,6))
sns.swarmplot(x="sepal.width", y="sepal.length", hue="variety", data=data)
plt.show()

data["variety"].value_counts()
print(pd.value_counts)


#Heat map
def heatmap():
    fig=plt.gcf()
    fig.set_size_inches(10,7)
    fig=sns.heatmap(data.corr(),annot=True,cmap='cubehelix',linewidths=1,linecolor='k',square=True,mask=False, vmin=-1, vmax=1, cbar_kws={"orientation": "vertical"},cbar=True)
    plt.show()

#Bivariate Analysis
sns.pairplot(data, hue="variety",height=4)
plt.show()

summary_to_file()

heatmap()
