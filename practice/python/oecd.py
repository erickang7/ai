from __future__ import division, print_function, unicode_literals

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn 
import sklearn.linear_model
import os
import myutils as m

plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

np.random.seed(42)

# set the path to the data folder
datapath = os.path.join("..", "..", "datasets", "lifesat", "")

# read csv data into a dataframe using pandas read_csv function
oecd_bli = pd.read_csv(datapath + "oecd_bli_2015.csv", 
    thousands=',')
# read csv data into a dataframe using pandas read_csv function    
gdp_per_capita = pd.read_csv(datapath + "gdp_per_capita.csv", 
    thousands=',', 
    delimiter='\t',
    encoding='latin1',
    na_values="n/a")

# wrangling data see the definition of prepare_country_stats function
country_stats = m.prepare_country_stats(oecd_bli, gdp_per_capita)

# build numpy CClass object of X and Y
X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]

country_stats.plot(kind='scatter', x="GDP per capita", y="Life satisfaction")
plt.show()

model = sklearn.linear_model.LinearRegression()
# model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)

#fit linear model
model.fit(X, y)
X_new = [[22587]]
print("The life satisfaction level for GDP $22,587 is: " + str(model.predict(X_new)))

