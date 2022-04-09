# PandS-Project
Module Project
Iris Data Research

The Iris Dataset contains four features (length and width of sepals and petals) of 50 samples of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). These measures were used to create a linear discriminant model to classify the species. The dataset is often used in data mining, classification and clustering examples and to test algorithms.http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html

Used this site to get information on how to import iris dataset in python https://gist.github.com/srishtis/10d8e8cecfa128ff694bd8846f825135

According to UCI Machine Learning Repository, the Iris dataset is widely used in pattern recognition learning. One class is linearly separable from the other two classes, which are not linearly separable from each other. The predicted attribute of the data set is the class of Iris plant to which each observation belongs.

The Iris dataset is a multivariate dataset with a default machine learning task of classification. It consists of 150 instances with five attributes, with four of these being the measurements of the sepal and petals of each observation in the data set and the fifth being the class or species of Iris that each observation belongs to. It includes 50 plants each of three classes of Iris plant, where each class is a different type or species of Iris plant. The three classes in the data set are the Iris Setosa, the Iris Versicolor and the Iris Virginica. The data set was donated in 1988 by Michael Marshall but the data set was created by R.A. Fisher in 1936.https://www.angela1c.com/projects/iris_project/the-iris-dataset/

The Iris data set is a relatively small multi-variate data set containing of only 150 rows and 5 fields or variables in columns. Each observation in the Iris data set consists of a four dimensional array of numerical measurements and a single categorical class of iris species to which it belongs and represents one instance of an iris plant or flower.


To understand what libraries to import I researched the various references across the web in relation to the Data Iris set and also used librabries from our lectures,
Matplotlib.pyplot library is most commonly used in Python in the field of machine learning according to https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/. Matploblib also has the benefit that it can provide graphs in both 2D and 3D. I have used this previously in our weekly tasks. I also imported numpy and pandas

I created Iris dataset from online resources and saved as csv file called iris.csv. There were many references recommending importing the data set through sklearn but I opted to create my own file and specify the column titles. I also work largely with excel and I wanted to be able to practise bringing these in to my programming learning. I used pandas as pd as created a command to read in the CSV file; 
data = pd.read_csv("iris.csv"). 
Then using the print command I was able to get an output of the data set in text file. I was able to specify the number of rows of data required e.g. the full 150 varieties or restrict to 10 rows in the example below using command;
 print (data.head(10)) where the variable is 10

   sepal.length  sepal.width  petal.length  petal.width variety
0           5.1          3.5           1.4          0.2  Setosa
1           4.9          3.0           1.4          0.2  Setosa
2           4.7          3.2           1.3          0.2  Setosa
3           4.6          3.1           1.5          0.2  Setosa
4           5.0          3.6           1.4          0.2  Setosa
5           5.4          3.9           1.7          0.4  Setosa
6           4.6          3.4           1.4          0.3  Setosa
7           5.0          3.4           1.5          0.2  Setosa
8           4.4          2.9           1.4          0.2  Setosa
9           4.9          3.1           1.5          0.1  Setosa

Once imported I was able to to use various commmands to draw whole data from the data set or specific data as specified in the column title in the csv file e.g. using commands such as;
data.describe()
data.info() 

I then looked at creating the histogram, the one saved looks at sepal length. this command can be amended to draw data on the petal or variety of the Iris. I saved the histogram to the repository under the name iris_sepal_length_hist.png. We had previoulsy studied the plot function and I used hist to produce a histogram. One of the great benefits I have found using VS Code is that if I propose to use a command like hist I know it will work if the text autopopulates. It also calls out errors if I have indented my code incorrectly. As someone new to programming I fing this wholly beneficial.

The next step was to create a scatterplot.Up to now I hadn't imported seaborn but I found various references to its benefits in the use of scatter plots in my research. I researched the seaborn library at https://seaborn.pydata.org/generated/seaborn.scatterplot.html. Reading I found Seaborn is built on top of Python’s Matplotlib libray. Its function is to allow programmers to plot a graphical visualization using Python’s plotting language, and the code includes a tool to load it into Matplotlib. The benefit being that you can also use the data to understand how data is used and to gain a deep understanding of the different ways we can generate data. I wanted to try it out an imported as; import seaborn as sns
