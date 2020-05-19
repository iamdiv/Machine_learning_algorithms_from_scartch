"""
fit_distribution : funtion will fit tha data for gaussian fit_distribution
prior_probability : Used  to calculate the prior probability for all the labes
probability : this will be used to calculate likelihood
fit : used to fit the naive_bayes probabilistic_model
predict : used to calculate probability of input with all the labels
"""
import numpy as np
import pandas as pd 
from sklearn import datasets
from scipy.stats import norm
import pickle

def fit_distribution(data):
    mu  = np.mean(data)
    sigma = np.std(data)
    
    dist = norm(mu,sigma)
    return dist
def prior_probability(x,xy):
    prior_prob = len(xy)/len(x)
    return prior_prob
def probability(x,prior,dict_):
    prob = prior
    print("*********************",len(x))
    i = 0
    for  key,value in dict_.items():
        prob *= value.pdf(x[i])
        i += 1
    return prob
def fit(x,y):
    y_ = set(y)
    y_ = list(y_)
    print(y_)
    dict_ = {}
    prior = []
    for j in y_:
        
        xy = x[y == j]
        pri = prior_probability(x,xy)
        prior.append(pri)
        for i in range(list(xy.shape)[1]):
            dict_[str(i)+str(j)] = fit_distribution(xy)
    return prior,dict_
def predict(x,prior):
    print(len(x))
    f = open(r"D:\Machine_learning\probabilistic_model.pkl","rb")
    dict_ = pickle.load(f)
    f.close()
    prior = dict_["prior"]
    i = 0
    proba = prior[0]
    index = 0
    probs = []
    del dict_["prior"]

    for key,value in dict_.items():
        
        if i < len(x):
            proba *= value.pdf(x[i])
            
            i += 1
        if i == len(x):
            probs.append([proba,key[1]])
            
        
            proba = prior[index]
            index += 1
            i = 0
    
    return probs
def naive_bayes(x,y,flag):
    
    if flag == "fit":
        
        prior_prob,dict_ = fit(x,y)
        dict_["prior"] = prior_prob
        
        f = open(r"D:\Machine_learning\probabilistic_model.pkl","wb")
        
        pickle.dump(dict_,f)
        f.close()
    elif flag == "predict":

        probabilities = predict(x,y)
        
        return probabilities
    else:
        print("sent flag can be either fit or predict kindly check and correct")

if __name__ == '__main__':
    iris = datasets.load_iris()
    x = iris['data']
    y = iris['target']
    x_sample,y_sample = x[0],y[0]
    probabilities = naive_bayes(x_sample,y_sample,"predict")
    print(probabilities)
