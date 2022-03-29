# author Sadie Concannon
#program that outputs a summary of each variable to a single text file,
#saves a histogram of each variable to png files, and
#outputs a scatter plot of each pair of variables.
#performs any other analysis you think is appropriate

#import libraries to work with the dataset iris.csv,
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #for plotting

data = pd.read_csv("iris.csv")
print (data.head(150))
data.describe()
data.info()
plt.figure(figsize = (10, 7))
x = data['sepal.length']

plt.hist(x, bins = 20, color = "green")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count")

plt.show()


