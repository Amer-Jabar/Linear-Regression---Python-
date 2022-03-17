
from random import random, uniform
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from LinearRegressionHel

def getDescX(data_range, scale):
    range_ = []
    for x in range(data_range):
        range_.append(x * scale)
    return range_


x, y = random_data(100, 0.1, 0.05);
x = pd.DataFrame(x).iloc[:, 0]
y = pd.DataFrame(y).iloc[:, 0]

x_scaler = pd.DataFrame(getDescX(100, 0.1)).iloc[:, 0]

eta = 0.01
w1 = 0.5
w0 = 0

for a in range(100):
    y_pred = np.dot(w1, x_scaler) + w0
    
    loss = (1 / 100) * sum((y_pred - y) ** 2)
    
    gradient_w0 = (1 / 100) * sum(((w1 * x + w0) - y) * 1)
    gradient_w1 = (1 / 100) * sum(((w1 * x + w0) - y) * x)
    
    w1 = w1 - eta * gradient_w1
    w0 = w0 - eta * gradient_w0

plt.scatter(x, y)
plt.plot(x_scaler, y_pred)









