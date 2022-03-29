# author Sadie Concannon
#program that outputs a summary of each variable to a single text file,
#saves a histogram of each variable to png files, and
#outputs a scatter plot of each pair of variables.
#performs any other analysis you think is appropriate

#import libraries to work with the dataset iris.csv, used in previous classes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #for plotting
import seaborn as sns
from sklearn import metrics
sns.set()
#load the iris data
iris_data = pd.read_csv('iris.csv')
iris_data
