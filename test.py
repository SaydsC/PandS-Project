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

#http://www.hpc-carpentry.org/hpc-python/03-lists/
#write code and create a variable for each row of data 
#taking a closer look at each of the variables 
#lets use python to describe the statistical properties of each variable 
#https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html
#with our newly created variables above we can run stats for the min, max, mean, and st. dev for each 
#I will also plot each variable on a histrgram 
#https://bit.ly/325l7aw


#Having looked back over previous lectures and searching online for a way to tidy up my code 
#I tried creating a dict which would hold the variable title and its assocaited data
#Rough work was carried out in roughwork.py
#https://learnonline.gmit.ie/pluginfile.php/293981/mod_label/intro/Lab%2005%20dataStructures.pdf 
#https://jakevdp.github.io/WhirlwindTourOfPython/06-built-in-data-structures.html

print("As seen above, the dataset contains numeric data which is held within four seperate columns")
print("A statistical summary of each variable will be output to 'summary.txt'")
print()

#sepallength = dataset[:,0]
#sepalWidth = dataset[:,1]
#petallength = dataset[:,2]
#petalWidth = dataset[:,3]


#column = [{                              #Creating a dict containing variable and corresponding data 
 #   "title": "Sepal length",
  #  "data": sepallength,
#},{
 #   "title": "Sepal Width",
  #  "data": sepalWidth,
#}, {
 #   "title": "Petal length",
  #  "data": petallength,
#}, {
 #   "title": "Petal Width",
  #  "data": petalWidth,
#}]
#for x in column:                   #creating a for loop to go through our dict 
 #   variableMin = np.min(x["data"])   #creating varaibles to loop through 
  #  variableMax = np.max(x["data"])
   # variableMean = np.mean(x["data"])
    #variableStd = np.std(x["data"])
    #print("The Minimum value for {} is {}".format(x["title"], variableMin), file = f)    
    #print("The Maximum value for {} is {}".format(x["title"], variableMax), file = f)
    #print("The Mean value for {} is {}".format(x["title"], variableMean), file = f)
    #print("The Standard Deviation for {} is {}".format(x["title"], variableStd), file = f)
    #f.write("\n")



