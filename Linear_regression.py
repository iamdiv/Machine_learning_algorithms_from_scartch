import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import math

def mean(x):
    count = 0
    for i in x:
        count += i
    mean = count / len(x)
    print(mean)
    return mean
def RMSE(Y,Y_pred):
    rmse = np.sqrt(sum((Y - Y_pred) ** 2) / len(Y))
    return rmse 
def r_squared(Y,Y_pred):
    squared_error = sum((Y-Y_pred)**2)
    y_mean = mean(y)
    squared_mean_error = sum((Y-y_mean)**2)
    r2 = 1 - (squared_error/squared_mean_error)
    return r2
    

def gradient_descent(x,y,theta,alpha,iterations):
    costs = []
    m = len(x)
    #theta_all  = [theta]
    for i in range(iterations):
        hyp_y = np.dot(x,theta)
        error = hyp_y - y
        cost = (1/2*m)*np.dot(error.T,error)
        costs.append(cost)
        theta = theta - alpha* (1/m)*np.dot(x.T,error)
        #theta_all.append(theta)
        
        #print(theta)
    
    return costs,theta

def Linear_regression(x,y):

    mean1 = mean(x)

    #dat = x
    x = ((x-mean1)/x.std())
    x = np.c_[np.ones(x.shape[0]), x] 
    alpha = 0.01
    theta  = np.random.rand(2)
    print(theta)
    iterations = 3000
    costs,thetas = gradient_descent(x,y,theta,alpha,iterations)
    
    prediction = np.dot(x,thetas)
    rmse_value = RMSE(y,prediction)
    print(rmse_value,"rmse value")
    r2 = r_squared(y,prediction)
    print(r2,"r squared error")
   
    return thetas,costs
    

if __name__ == "__main__":
    
    data = pd.read_csv(r"D:\Machine_learning\dataset.csv")

    x = data["Head Size(cm^3)"].values
    y = data["Brain Weight(grams)"].values
    
    thetas,costs =  Linear_regression(x,y)
    mean1 = mean(x)
    plt.title("Cost Funtion J")
    plt.xlabel("number of iteration")
    plt.ylabel("cost funtion")
    plt.plot(costs)
    plt.show()
