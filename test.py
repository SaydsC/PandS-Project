#This is a program created for testing code using the Iris Dataset 
#Rough work code 'test.py' 
#Author Sadie Concannon

import numpy as np
import pandas as pnd 
import matplotlib.pyplot as plt 
#Importing the needed libraries 

#to output summary to text file
f = open("summary.txt", "w")    #https://www.w3schools.com/python/python_file_write.asp
#adding in txt file

file = "iris.csv"
index = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width', 'variety']
data = pnd.read_csv("iris.csv", names = index) 

print("\n")
print("The total number of rows and columns respectively in the Iris Dataset are:",data.shape)  
print("This is confirmed in the below output:")
print(data.info())
print(data.head(150))
#print(dataset.to_string()) #this will print out the entire dataset if wanted. 
print("\n")
print("The data places variables evenly into three species of Iris Flower:")
print(data.groupby('species').size())
print("\n")

#Now I will read the file for NumPy 
dataset = np.genfromtxt(file, delimiter=',')
#print(data)








