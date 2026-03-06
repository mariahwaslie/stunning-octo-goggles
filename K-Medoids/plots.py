import plotly.express as px
import random
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import nbformat
import pandas as pd

random_seed =1

def plot_data(data,x_medoid_assignment,iteration,medoids):
    df = pd.DataFrame(data, columns=["x", "y"])
    df["cluster"] = x_medoid_assignment
    df["iteration"] = iteration

    # Plot with Plotly Express
    fig = px.scatter(df, x="x", y="y", color="cluster", 
                    symbol=df["cluster"], size_max=10,
                    title=f"K-Medoids Iteration {iteration}")
    # Add medoids manually
    fig.add_scatter(x=medoids[:,0], y=medoids[:,1], mode="markers", 
                    marker=dict(size=20, symbol="star", color="black"),
                    name="Medoids")
    fig.show()

def plot_iteration(data, medoids, x_medoid_assignment, iteration):
    plt.figure(figsize=(6,6))
    
    # Scatter plot of points by cluster
    for k in range(len(medoids)):
        cluster_points = data[np.array(x_medoid_assignment) == k]
        plt.scatter(cluster_points[:,0], cluster_points[:,1], label=f"Cluster {k}")
    
    # Plot medoids
    plt.scatter(medoids[:,0], medoids[:,1], marker='*', s=200, color='black', label='Medoids')
    
    plt.title(f"K-Medoids Iteration {iteration}")
    plt.legend()
    plt.show()
def plot_kmedoids_animation(history,df_plotly):
    fig = px.scatter(df_plotly, 
                    x="x", y="y", 
                    color="cluster",
                    animation_frame="iteration",
                    title="K-Medoids Animation",
                    width=700, height=700)

    # Add medoids as stars per iteration
    for h in history:
        medoids = h["medoids"]
        fig.add_scatter(x=medoids[:,0], y=medoids[:,1],
                        mode="markers",
                        marker=dict(size=15, symbol='star', color='black'),
                        name='Medoids',
                        showlegend=False)  # only show legend once

    fig.show()
