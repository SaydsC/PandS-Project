Programming and Scripting

PandS Module Project 2022

Author: Sadie Concannon

# Iris Data Research

## The Iris Dataset

The Iris Dataset contains four features (length and width of sepals and petals) of 50 samples of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). These measures were used to create a linear discriminant model to classify the species. The dataset is often used in data mining, classification and clustering examples and to test algorithms.[1](http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html)

![Iris](https://www.bing.com/images/search?view=detailV2&ccid=c8qywOU0&id=F0DD7681CA0285751925E43CF001D68B197E2843&thid=OIP.c8qywOU03Uz3DIOC54znmwHaFd&mediaurl=https%3a%2f%2fcdn-images-1.medium.com%2fmax%2f1200%2f1*plcDnA6sjme0RWvxbvaWgg.png&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.73cab2c0e534dd4cf70c8382e78ce79b%3frik%3dQyh%252bGYvWAfA85A%26pid%3dImgRaw%26r%3d0&exph=886&expw=1200&q=iris+data+set+&simid=607992980875403567&FORM=IRPRST&ck=5D66083CEA1A236512C1449AAF77C3C3&selectedIndex=6&ajaxhist=0&ajaxserp=0)

A population includes all of the elements from a data set whereas a sample consists of one or more observation from the population. Samples are used to make statistical inferences about the population. Here we use the Iris as the population.

My main objective in this project is to learn more about Python programming by applying it to the Iris data set. I used Visual Studio code to write my program and I used github to import the iris dataset and to get instruction on how to use it and save it as a csv file. [2](https://gist.github.com/srishtis/10d8e8cecfa128ff694bd8846f825135)

According to UCI Machine Learning Repository, the Iris dataset is widely used in pattern recognition learning. This is because one variety of the Iris is linearly separable from the other two varieties, which are not linearly separable from each other. The predicted attribute of the data set is the class of Iris plant to which each observation belongs. Machine learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy.[3](https://www.ibm.com/cloud/learn/machine-learning?msclkid=3efe2586ceb411ec87756ddd7a7b13ed)


The Iris flower dataset is a multivariate dataset with a default machine learning task of classification. It consists of 150 instances with five attributes, with four of these being the measurements of the sepal and petals lengths and widths in the data set and the fifth being the class or variety of Iris that each observation belongs to. It includes 50 plants each of three classes of Iris plant, where each class is a different type or species of Iris plant. The three classes in the data set are the Iris Setosa, the Iris Versicolor and the Iris Virginica. The data set was donated in 1988 by Michael Marshall but the data set was created by British statistician and biologist Ronald .A. Fisher in 1936. [4](https://www.angela1c.com/projects/iris_project/the-iris-dataset/)

Each observation in the Iris data set consists of a four dimensional array of numerical measurements and a single categorical class of iris varieties to which it belongs and represents one instance of an iris plant or flower.

The columns that represent the 5 variables are :
1. SepalLength
2. SepalWidth
3. PetalLength
4. PetalWidth
5. Variety

The Iris dataset used in this analysis can be found among files in this repository as iris.csv.

## Program to analyse the Iris dataset

To understand what libraries to import I researched the various references across the web in relation to the benefits of studying the Iris data set and also referred to librabries used in our lectures and from our weekly tasks.

Matplotlib.pyplot library is most commonly used in Python in the field of machine learning according to [5](https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/). Matplotlib also has the benefit that it can provide graphs in both 2D and 3D as I found having used it previously in our weekly tasks. Pandas provides high-performance, easy-to-use data structures and data analysis tools for the Python programming language. It is designed for working with data that is in a tabular format containing an ordered collection of columns where each column can have a different value type. This makes it ideal for exploring a structured tabular dataset such as the Iris dataset which contains several numerical columns and one categorical column.

NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices. NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely. NumPy stands for Numerical Python.[6](https://www.w3schools.com/python/numpy/numpy_intro.asp)

### Imported libraries:
1.  import pandas as pd
2.  import numpy as np
3.  import matplotlib.pyplot 
4.  import sys
5.  import seaborn as sns

I extrapulated the Iris dataset from online resources and saved as an comma separated values file called iris.csv. There were many references recommending importing the data set through sklearn but I opted to create my own file and specify the column titles. I work largely with excel and I wanted to be able to practise using csv files and bringing other datasets into my programming learning. Using pandas I wrote a command to read in the CSV file; 

  `data = pd.read_csv("iris.csv")`

Then using the print command I was able to get an output of the data set in the terminal. I was able to specify the number of rows of data required e.g. the full 150 varieties or restrict to 10 rows in the example below using command;
  `print (data.head(10))` where the variable for the number of rows is specified as 10.

   |   |sepal.length|sepal.width|petal.length|petal.width|variety|
   |---|------------|-----------|------------|-----------|-------|
   | 0 | 5.1 | 3.5 | 1.4 | 0.2 | Setosa|
   | 1 | 4.9 | 3.0 | 1.4 | 0.2 | Setosa|
   | 2 | 4.7 | 3.2 | 1.3 | 0.2 | Setosa|
   | 3 | 4.6 | 3.1 | 1.5 | 0.2 | Setosa|
   | 4 | 5.0 | 3.6 | 1.4 | 0.2 | Setosa|
   | 5 | 5.4 | 3.9 | 1.7 | 0.4 | Setosa|
   | 6 | 4.6 | 3.4 | 1.4 | 0.3 | Setosa|
   | 7 | 5.0 | 3.4 | 1.5 | 0.2 | Setosa|
   | 8 | 4.4 | 2.9 | 1.4 | 0.2 | Setosa|
   | 9 | 4.9 | 3.1 | 1.5 | 0.1 | Setosa|

Once imported I was able to to use various commmands to draw whole data from the data set or specific data as specified in the column title in the csv file e.g. using commands such as;
  `data.describe()` to get statistical insight like the count, mean values, standard deviation
  `data.info()` to prints information about the dataset including the index dtype and columns, non-null values and memory usage.

I then amended further so that the dataset summary is not shown while starting the program, but output to analysis.txt.

Function summary_to_file() is created for making the summary and writing it into the file at the same time.
  ```def summary_to_file():```
    ```sys.stdout = open("summary.txt","w")```

To output the summary into a file I used the sys module and it's standard output stream stdout (per above code)[7](https://www.askpython.com/python/python-stdin-stdout-stderr). I had originally tried to redirect output but to no avail and this approach worked for me without requirement for directory paths.

The output gives various overviews of the dataset e.g. summary, overview, number of each variety.

### Histograms

I then looked at creating the histogram, the original one I did as a starting point solely looked at sepal length. This command would need to be amended to draw data on the petal or variety of the Iris producing multiple histograms in separate files. I saved the histogram to the repository under the name iris_sepal_length_hist.png. We had previously studied the plot function and I used "hist" to produce this histogram. One of the great benefits I have found using VS Code is that if I propose to use a command like hist I know it will work if the text autopopulates. It also calls out errors if I have indented my code incorrectly. As someone new to programming I find this wholly beneficial. 

It is beneficial to use a histogram when[8](https://asq.org/quality-resources/histogram):

1. The data is numerical
2. You want to see the shape of the data’s distribution, especially when determining whether the output of a process is distributed approximately normally
3. Determining whether the outputs of two or more processes are different
4. You wish to communicate the distribution of data quickly and easily to others

Once I became more confident and had furthered my research I was able to amend my code to produce four histograms together on one file to allow for ease of comparison of the histograms looking sepal length, width, petal length, width. I found this resource [9](www.rpubs.com/analysisoftheirisdataset) most beneficial here.

![Histogram](https://github.com/SaydsC/PandS-Project/blob/master/histogram.png)

### Scatterplot

The next step was to create a scatterplot. Up to now I hadn't imported seaborn but I found various references to its benefits in the use of scatter plots in my research. I researched the seaborn library at [10](https://seaborn.pydata.org/generated/seaborn.scatterplot.html). Reading I found Seaborn is built on top of Python’s Matplotlib libray. Its function is to allow programmers to plot a graphical visualisation using Python’s plotting language, and the code includes a tool to load it into Matplotlib. The benefit being that you can also use the data to understand how data is used and to gain a deep understanding of the different ways we can generate data. I wanted to try it out and imported as; `import seaborn as sns`.

I first generated a scatterplot comparing the sepal length to petal length. I later alternated the code to look at the petal length by variety. This was very good to visually compare the different petal lengths and it was clear the setosa variety had the shortest petal length. 

![Scatterplot](https://github.com/SaydsC/PandS-Project/blob/master/scatterplot%20petal%20length%20by%20variety.png)


### Further Analysis

#### Swarmplot:
In order to be able to display the data of each variety without them overlapping each other I used a swarmplot. The data is clearly visible and not obscurred by over plotting - the result allows you to see each distinct data point. There are also options to produce horizontal swarms.

I then used the "hue" feature in seaborn scatterplot to plot the three varieties of the Iris by colour. The output is the plotted relationship between the sepal length and sepal width of the three different varieties of the Iris.[11](https://mldoodles.com/seaborn-scatterplot-hue-parameter/)

![Scatterplothue](https://github.com/SaydsC/PandS-Project/blob/master/scatterplot%20variety%20hue.png)

We can easily see that the Setosa variety has the smallest sepal length but the largest width. The Versicolor sits in the middle for both sepal length as well as sepal width and the Virginica depicted in green has the largest sepal lengths with smaller sepal widths.

#### Heatmap:
Heat maps are used to find out the correlation between different features in a dataset. High positive or negative values shows that the features have high correlation. This helps us to select the parameters for machine learning. [12](https://mer.vin/2019/08/seaborn). Correlation is a statistical measure that expresses the strength of the relationship between two variables. A good example I found where this can be used outside iris data was from [13](https://vitalflux.com/correlation-heatmap-with-seaborn-pandas/). 

>"Correlation is often used to determine whether there is a cause-and-effect relationship between two variables. For example, if researchers want to know whether watching television causes obesity, they would examine the correlation between television viewing and obesity rates. If they found that there was a strong positive correlation, it would suggest that there may be a casual relationship. However, correlation does not necessarily imply causation; other factors may be at play. However, it is important to remember that correlation does not imply causation. For example, there may be a strong correlation between ice cream sales and swimming accidents, but that doesn’t mean that eating ice cream causes people to have accidents."

![Heatmap](https://github.com/SaydsC/PandS-Project/blob/master/Heatmap.png)

#### Bivariate Analysis:
Bivariate analysis is the analysis of the bivariate data. This is a single statistical analysis that is used to find out the relationship that exists between two value sets. The variables that are involved are X and Y. Pair Plots are one simple way to visually analyse the relationships between these variables. It produces a matrix of relationships between each variable in your the data. [14](https://www.kaggle.com/code/akashrajsrinivasan/data-analysis-on-iris-dataset/notebook)

![Pairplot](https://github.com/SaydsC/PandS-Project/blob/master/Bivariate%20analysis.png)



### Conclusion

The aim of this analysis was to describe the dataset using Python, in terms of its characteristics, relationships between the variables and the degree to which the three varietys groups differ from each other.

In terms of distrubtion, we can see that the data is generally normally distributed, with low skewness and kurtosis (tailedness) values indicating the data is symetrical and light tailed. The low volume of outliers suggests that petal and sepal measurements within the species generally fall within a defined range. The exploratory analysis also gave an insight into the morphological characteristics of the species.

The correlation output for the entire data set was markedly different from that for the individual species groups, suggesting that trends seen within the data as a whole are not necessarily evident within species groups.

The final component of the analysis, which compared mean values between groups, found significant differences between all the species. This indicates that each of the three species groups have their own distinct characteristics in terms of flower shape/size. The setosa variety is easily separable linearly from the other two as they have some overlap of characteristics.

### Learnings/Potential Improvements

During this project, I got a high-level introduction to data analysis for Python and what can be achieved using the libraries built for this purpose. I would recommend this dataset to anyone who is a beginner in data science and is eager to build their Machine Learning practise based on the following characteristics of this dataset:
  1. 150 samples, with 4 attributes (same units, all numeric)
  2. Balanced class distribution (50 samples for each class)
  3. No missing data
  4. four columns of numerical data with one column for the variety

Statistical and data analytical skills are now in high demand. As I have an interest in and work in an area collecting and analysing data this project has bettered my understanding of the basic statistical concepts and how I can apply them them to other data sets. Machine learning is an important component of the growing field of data science. Through the use of statistical methods, algorithms are trained to make classifications or predictions, uncovering key insights within data mining projects. These insights will subsequently drive decision making in industry, in their aim to meet key growth metrics. As big data continues to expand and grow, the market demand for data scientists will increase, requiring them to assist in the identification of the most relevant business questions and subsequently the data to answer them. 

Fishers Iris dataset is the ideal data set to develop the skills needed to properly assess big data.


### Further References
1. https://archive.ics.uci.edu/ml/datasets/iris
2. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
3. https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
4. https://www.ibm.com/cloud/learn/machine-learning?msclkid=3efe2586ceb411ec87756ddd7a7b13ed
5. https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet?msclkid=29ec18edcec111ecb98cc8dd61a84ff0




