import numpy as np 
import pandas as pd 
import math
from sklearn import datasets
from sklearn.metrics import confusion_matrix
class Logistic_regression:
    def __init__(self,iterations = 5000,alpha = 0.01,threshold = 0.5):
        self.iteration = iterations
        self.alpha = alpha
        self.threshold = threshold
    def sigmoid(self,a):
         y = (1/(1 + np.exp(-a)))
         return y
    def cost_function(self,y,z):
        m = len(y)
        cost = (1/m)*(np.dot(y,np.log(z)) + np.dot((1-y),np.log(1-z))) 
        return cost 
    def cost_derivatives(self,z,y,x):
        m = len(y)
        dj_dw = (1/m)*(np.dot(x.T,(z - y)))
        return dj_dw
    def fit(self,x,y):
        w = np.random.rand(x.shape[1])
        
        cost = []
        weights = [w]
        for i in range(self.iteration):

            a = np.dot(x,w)
            z = self.sigmoid(a)
            j = self.cost_function(y,z)
            cost.append(j)
            dj_dw = self.cost_derivatives(z,y,x)
            w = w - self.alpha * dj_dw
        return w
    def predict(self,x,w):
        threshold = self.threshold
        a = np.dot(x,w)
        probability = self.sigmoid(a)
        predictors = []
        for i in probability:
            
            if i >= threshold:
                predictors.append(1)
            else:
                predictors.append(0)
        return predictors
if __name__ == "__main__":
    iris = datasets.load_iris()
    
    x = iris.data[:, :2]
    y = (iris.target != 0) * 1

    lr = Logistic_regression()
    wt = lr.fit(x,y)
    
    st = lr.predict(x,wt)
   
    
    print(confusion_matrix(y,st))