"""
Kmean :- Kmeans algorithm is an iterative algorithm that tries to partition the dataset into Kpre-defined distinct non-overlapping subgroups
 (clusters) where each data point belongs to only one group.
plot :- for ploting all the points and the centroids of the cluster
calculate_avg :- for calculating mean of all the data
euclidian_distances :- for calculating the euclidean distance b/w to points
calculate_total_sum :- for calculating the sum of euclidian distances of all the datapoints with nearer centroids
"""
import numpy as np 
import math
import pandas as pd
import Label_encoder
import matplotlib.pyplot as plt

def plot(centroids,clusters):
    colors = 10*["r", "g", "c", "b", "k"]
    for centroid in centroids:
        

	    plt.scatter(centroid[0], centroid[1], s = 130, marker = "x")
    
    
    for key,values in clusters.items():
        color = colors[key]
        for features in values:
            plt.scatter(features[0], features[1], color = color,s = 30)
    plt.pause(0.05)        
    plt.show()
    plt.close()
    
def calculate_avg(list):
    ls = len(list[0])
    centroids = []
    for i in range(ls):
        sum = 0 
        for lst in list:
            sum += lst[i] 
        centroids.append(sum/len(list))
    
    return centroids
def euclidian_distances(x1,avg):
    dist = 0
    sum = 0
    for i in range(len(avg)):
        
        sum += pow((avg[i] - x1[i]),2)
    dist = math.sqrt(sum)
    
    return dist
 
def kmean(df,k,max_iteration):
    data = df.values
    centroids = []
    for i in range(k):
        centroids.append(data[i])
    threshold = 9999999999999
    sum = 0
    for i in range(max_iteration):
        
        if threshold != sum:
            threshold = sum
            clusters = {key:[] for key in range(k)}
            for points in data:
                distances = [euclidian_distances(points,centroid) for centroid in centroids]
                closest = distances.index(min(distances))
                clusters[closest].append(points)
            for key,values in clusters.items():
                mean_point = calculate_avg(values)
                centroids[key] = mean_point
            sum = calculate_total_sum(clusters,centroids)
            
            
        else:
            break

    plot(centroids,clusters)
    plt.close("all")
    return centroids
        

def calculate_total_sum(clusters,centroids):
    sum = 0
    for key,value in clusters.items():
        for v in value:
            sum += euclidian_distances(v,centroids[key])
    return sum

if __name__ == "__main__":
    path = r"C:\Users\Lonewolf\Desktop\Machine-Learning-Algorithms-from-Scratch-master\data\ipl.csv"
    df = pd.read_csv(path)
    k = 3
    max_iteration = 500    
    centroids = kmean(df,k,max_iteration)



    
    

    