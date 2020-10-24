import pandas as pd
from pandas import Series
import matplotlib
import matplotlib.pyplot as plt

data = pd.read_csv('fresadora.txt', sep=",", header=None)
plotdata = pd.Series
print(data)
print(data.head(3))
print(data.tail(2))
print(data[0])
datax = data[0]
datay = data[1]
dataz = data[2]
#print(datax)
#print(datay)
#plt.scatter(datax, datay)
plt.scatter(datax,datay)
plt.show()

#Bibliografia
#https://ourcodingclub.github.io/tutorials/pandas-python-intro/




