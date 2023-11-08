import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def average(x, n):
    if (n == 0):
        return 0
    else:
        sum = 0
        for i in range(n):
            sum += x[i]
        return (sum / n)

def covariance(x, x_average: float, y, y_average: float, n):
    sum = 0
    for i in range(n):
        sum += ((x[i] - x_average) * (y[i] - y_average))
    return sum / (n - 1)

def correlation(covariance, sx, sy):
    return (covariance / (sx * sy))

def estimated_regression_line(b_0, b_1, x_i):
    return (b_0 + b_1 * x_i)

def estimated_variance(b_0, b_1, x, y, n):
    sum = 0
    for i in range(n):
        sum += ((y[i] - estimated_regression_line(b_0, b_1, x[i]))**2)
    return (sum / (n - 2))

def t_alpha(alpha, n):
    return ((1 - alpha) / 2, n - 2)

def SE(S, covariance_x):
    return (S / covariance_x**(1/2))

def confidence_b_1(t_alpha, b_1, SE):
    return ((b_1 - (t_alpha * SE)), (b_1 + (t_alpha * SE)))

def R_2(covariance_y: float, variance: float):
    return ((covariance_y - variance) / covariance_y)

def point_variance(x, x_average, n):
    sum = 0
    for i in range(len(x)):
        sum += ((x[i] - x_average)**2)
    return sum / (n - 1)

def getCorrelationRelatedToElement(dataframe, element):
    n = len(dataframe)
    
    if (n == 0):
        return 0
    
    price = np.asarray(dataframe["Price"])
    category = np.asarray(dataframe[element])
    
    average_price = average(price, n)
    average_category = average(category, n)
    
    covariance_xy = covariance(category, average_category, price, average_price, n)
    covariance_x = covariance(category, average_category, category, average_category, n)
    covariance_y = covariance(price, average_price, price, average_price, n)
    
    b_1 = covariance_xy / covariance_x
    b_0 = average_price - b_1 * average_category
    
    Sx = np.sqrt(point_variance(category, average_category, n))
    Sy = np.sqrt(point_variance(price, average_price, n))

    return correlation(covariance_xy, Sx, Sy)