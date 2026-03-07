import random
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import nbformat
import pandas as pd
from plots import *
from scipy.spatial.distance import cdist


random_seed =1

def assign_medoids(data,medoids):
    # assign the point 
    distances = np.linalg.norm(data[:,np.newaxis,:]- medoids[np.newaxis, :, :], axis=2)
    # compute distances
    medoid_index_assignment = np.argmin(distances, axis =1 ) #min distances 
    return medoid_index_assignment


def get_points(data,x_medoid_assignment,k):
    data = np.array(data)
    points = data[x_medoid_assignment == k]
    return np.array(points) 

def compute(points, medoid):
     #compute distance of all points 
     distances = np.linalg.norm(points - medoid, axis= 1 ) 
     # sum distances to get cost for m 
     cost = np.sum(distances)
     return cost 



def compute_cost(medoids, data,x_medoid_assignment):
    cost_medoids = np.zeros(data.shape[1])
    for k in range(len(medoids)):
        # get x assigned to medoids 
        points= get_points(data,x_medoid_assignment,k)
        cost = compute(points, medoids[k])
        if len(points)==0:
             continue
        # check C(m) vs C(o)
        
        costs = cdist(points, points, metric='euclidean') 
        all_possible_costs = np.sum(costs , axis=0)

        # find min cost and reassign medoids 
        min_idx = np.argmin(all_possible_costs)
        medoids[k] = points[min_idx]
        # cost= all_possible_costs[min_idx]
        cost_medoids[k] = all_possible_costs[min_idx]
        
        # reassign data points based on new medoids 
        x_medoid_assignment = assign_medoids(data,medoids)
             

    return medoids,x_medoid_assignment, np.array(cost_medoids)

def k_medoids(data, k, stop=None):
    # set seed 
    random_seed= 1
    np.random.seed(random_seed) 

    # pick 3 unique indices from the data set 
    random_indices = np.random.choice(data.shape[0], k , replace = False)

    # get the values from the indices data[i]
    medoids = data[random_indices]
    x_medoid_assignment= assign_medoids(data,medoids)
    
    m_cost_sum = np.inf
    iteration = 0
    history = []  # will store medoid + cluster info per iteration 

    while True:
    # get updated variables 
        medoids,x_medoid_assignment,m_cost = compute_cost(medoids, data,x_medoid_assignment)
        new_cost_sum = np.sum(m_cost)

        # plot_iteration(data, medoids, x_medoid_assignment, iteration)
        # Store for Plotly
    #     iteration_data = {
    #         "iteration": iteration,
    #         "medoids": medoids.copy(),
    #         "assignments": x_medoid_assignment.copy()
    #     }
    #     history.append(iteration_data)
        iteration += 1

        if stop is not None:
            if iteration== stop:
                    return new_cost_sum,medoids,x_medoid_assignment

    #     if new_cost_sum >= m_cost_sum:
    #         break
    #     m_cost_sum = new_cost_sum

    # frames = []
    # for h in history:
    #     iteration = h["iteration"]
    #     medoids = h["medoids"]
    #     assignments = h["assignments"]
        
    #     df_iter = pd.DataFrame(data, columns=["x", "y"])
    #     df_iter["cluster"] = assignments
    #     df_iter["iteration"] = iteration
    #     frames.append(df_iter)

    # df_plotly = pd.concat(frames, ignore_index=True)
    # plot_kmedoids_animation(history,df_plotly)


            
        return new_cost_sum,medoids,x_medoid_assignment

    


