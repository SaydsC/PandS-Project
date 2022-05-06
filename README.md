PandS-Project
PandS Module Project
# Iris Data Research

## The Iris Dataset

The Iris Dataset contains four features (length and width of sepals and petals) of 50 samples of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). These measures were used to create a linear discriminant model to classify the species. The dataset is often used in data mining, classification and clustering examples and to test algorithms.http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html

I used github to import iris dataset in python and to get instruction on how to use it and save it as a cvs file https://gist.github.com/srishtis/10d8e8cecfa128ff694bd8846f825135

According to UCI Machine Learning Repository, the Iris dataset is widely used in pattern recognition learning. One class is linearly separable from the other two classes, which are not linearly separable from each other. The predicted attribute of the data set is the class of Iris plant to which each observation belongs.

The Iris dataset is a multivariate dataset with a default machine learning task of classification. It consists of 150 instances with five attributes, with four of these being the measurements of the sepal and petals lengths and widths in the data set and the fifth being the class or variety of Iris that each observation belongs to. It includes 50 plants each of three classes of Iris plant, where each class is a different type or species of Iris plant. The three classes in the data set are the Iris Setosa, the Iris Versicolor and the Iris Virginica. The data set was donated in 1988 by Michael Marshall but the data set was created by R.A. Fisher in 1936.https://www.angela1c.com/projects/iris_project/the-iris-dataset/

The Iris data set is a relatively small multi-variate data set containing of only 150 rows and 5 fields or variables in columns. Each observation in the Iris data set consists of a four dimensional array of numerical measurements and a single categorical class of iris species to which it belongs and represents one instance of an iris plant or flower.

The columns that represent the 5 variables are :
1. SepalLength
2. SepalWidth
3. PetalLength
4. PetalWidth
5. Variety

The Iris dataset used in this analysis can be found among files in this repository as iris.csv.

## Developing a pporgram to analyse the Iris dataset

To understand what libraries to import I researched the various references across the web in relation to the Data Iris set and also used librabries from our lectures,
Matplotlib.pyplot library is most commonly used in Python in the field of machine learning according to https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/. Matploblib also has the benefit that it can provide graphs in both 2D and 3D. I have used this previously in our weekly tasks. I also imported numpy and pandas

### Imported libraries:
1.  import pandas as pd
2.  import numpy as np
3.  import matplotlib.pyplot 
4.  import sys
5.  import seaborn as sns

I created Iris dataset from online resources and saved as csv file called iris.csv. There were many references recommending importing the data set through sklearn but I opted to create my own file and specify the column titles. I also work largely with excel and I wanted to be able to practise bringing these in to my programming learning. I used pandas as pd and created a command to read in the CSV file; 

  `data = pd.read_csv("iris.csv")`

Then using the print command I was able to get an output of the data set in the terminal. I was able to specify the number of rows of data required e.g. the full 150 varieties or restrict to 10 rows in the example below using command;
  `print (data.head(10))` where the variable is 10

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
  `data.describe()`
  `data.info()` 

I then amended further so that the Dataset summary is not shown while starting the program, but output to analysis.txt.

Function summary_to_file() is created for making the summary and writing it into the file at the same time.
  `def summary_to_file():`
    `sys.stdout = open("summary.txt","w")`

To output the summary into a file I used the sys module and it's standard output stream stdout (per above code) https://www.askpython.com/python/python-stdin-stdout-stderr. I had origianlly tried to redirect output but to no avail and this approach worked for me without requirement for directory paths.

The output gives various overviews of the dataset e.g. summary, overview, number of each variety.

### Histograms

I then looked at creating the histogram, the origianl one I did as a starting point solely looked at sepal length. This command would need to be amended to draw data on the petal or variety of the Iris producing multiple histograms in separate files. I saved the histogram to the repository under the name iris_sepal_length_hist.png. We had previoulsy studied the plot function and I used hist to produce this histogram. One of the great benefits I have found using VS Code is that if I propose to use a command like hist I know it will work if the text autopopulates. It also calls out errors if I have indented my code incorrectly. As someone new to programming I find this wholly beneficial. Once I became more confident and had furthered my research I was able to amend my code to produce four histograms together on one file to allow for ease of comparison of the histograms looking sepal length, width, petal length, width. I found www.rpubs.com/analysisoftheirisdataset most beneficial here.

![Histogram]("C:\Users\daith\OneDrive\Documents\Sadie Code\PandS-Project\histogram.png")

### Scatterplot

The next step was to create a scatterplot.Up to now I hadn't imported seaborn but I found various references to its benefits in the use of scatter plots in my research. I researched the seaborn library at https://seaborn.pydata.org/generated/seaborn.scatterplot.html. Reading I found Seaborn is built on top of Python’s Matplotlib libray. Its function is to allow programmers to plot a graphical visualization using Python’s plotting language, and the code includes a tool to load it into Matplotlib. The benefit being that you can also use the data to understand how data is used and to gain a deep understanding of the different ways we can generate data. I wanted to try it out an imported as; import seaborn as sns.

I first generated a scatterplot comparing the sepal length to petal length. I later alternated the code to look at the petal length by variety. This was very good to visually compare the different petal lengths and it was clear the setosa variety had the shortest petal length. I then used the "hue" feature in seaborn scatterplot to plot the varieties if Iris by colour. The output is the plotted relationship between the sepal length and sepal width of the three different varieties of the Iris.https://mldoodles.com/seaborn-scatterplot-hue-parameter/

### Further Analysis

#### Swarmplot:
In order to be able to display the data of each variety without them overlapping each other I used a swarmplot. The data is clearly visible and not obscurred by over plotting - the result allows you to see each distinct data point.There is also the further options to produce horizontal swarms.

#### Heatmap:
Heat maps are used to find out the correlation between different features in the dataset. High positive or negative values shows that the features have high correlation. This helps us to select the parameters for machine learning. https://mer.vin/2019/08/seaborn. Correlation is a statistical measure that expresses the strength of the relationship between two variables. A good example I found where this can be used outside iris data was from https://vitalflux.com/correlation-heatmap-with-seaborn-pandas/. "Correlation is often used to determine whether there is a cause-and-effect relationship between two variables. For example, if researchers want to know whether watching television causes obesity, they would examine the correlation between television viewing and obesity rates. If they found that there was a strong positive correlation, it would suggest that there may be a causal relationship. However, correlation does not necessarily imply causation; other factors may be at play. However, it is important to remember that correlation does not imply causation. For example, there may be a strong correlation between ice cream sales and swimming accidents, but that doesn’t mean that eating ice cream causes people to have accidents."

### Conclusion

The aim of this analysis was to describe the dataset using Python, in terms of its characteristics, relationships between the variables and the degree to which the three varietys groups differ from each other.

In terms of distrubtion, we can see that the data is generally normally distributed, with low skewness and kurtosis values indicating the data is symmetrical and light tailed. The low volume of outliers suggests that petal and sepal measurements within the species generally fall within a defined range. The exploratory analysis also gave an insight into the morphological characteristics of the species.

The correlation output for the entire data set was markedly different from that for the individual species groups, suggesting that trends seen within the data as a whole are not necessarily evident within species groups.

The final component of the analysis, which compared mean values between groups, found significant differences between all the species. This indicates that each of the three species groups have their own distinct characteristics in terms of flower shape/size.

### Learnings/Potential Improvements

During this project, I got a high-level introduction to data analysis for Python and what can be achieved using the libraries built for this purpose. I would recommend this dataset to anyone who is a beginner in data science and is eager to build their Machine Learning practise based on the following characteristics of this dataset:
  1.  -150 samples, with 4 attributes (same units, all numeric)
  2.  -Balanced class distribution (50 samples for each class)
  3.  -No missing data





### Further References
https://archive.ics.uci.edu/ml/datasets/iris
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/



