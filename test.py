#This is a program created for testing code using the Iris Dataset 
#Rough work code 'test.py' 
#Author Sadie Concannon

import numpy as np
import pandas as pnd 
import matplotlib.pyplot as plt 
#Importing the needed libraries 

#to output summary to text file
f = open("summarytest.txt", "w")    #https://www.w3schools.com/python/python_file_write.asp
#adding in txt file

file = "iris.csv"

data = pnd.read_csv("iris.csv") 

print("\n")

import seaborn as sns

sns.pairplot(data, hue="variety",height=4)
plt.show()









