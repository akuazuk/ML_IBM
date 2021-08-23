#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np


df = pd.read_csv("/Users/advertmaster3/PycharmProjects/pythonProject2/ML_IBM/FuelConsumption.csv")
# take a look at the dataset
df.head()
# summarize the data

df.describe()

cdf = df[['ENGINESIZE', 'FUELCONSUMPTION_CITY','FUELCONSUMPTION_COMB', 'CO2EMISSIONS', 'FUELCONSUMPTION_COMB_MPG']]
cdf.head(1000)

viz = cdf[['ENGINESIZE','FUELCONSUMPTION_CITY','CO2EMISSIONS','FUELCONSUMPTION_COMB','FUELCONSUMPTION_COMB_MPG']]
viz.hist()
#plt.show()


plt.scatter(cdf.FUELCONSUMPTION_CITY, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("FUELCONSUMPTION_CITY")
plt.ylabel("Emission")
#plt.show()


msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]
#print (test)



plt.scatter(train.FUELCONSUMPTION_CITY, train.CO2EMISSIONS,  color='blue')
plt.xlabel("FUELCONSUMPTION_CITY")
plt.ylabel("Emissions")
#plt.show()



from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['FUELCONSUMPTION_CITY']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (train_x, train_y)
# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)


plt.scatter(train.FUELCONSUMPTION_CITY, train.CO2EMISSIONS,  color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")


from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['FUELCONSUMPTION_CITY']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y , test_y_) )
print (regr.predict(test_x))






