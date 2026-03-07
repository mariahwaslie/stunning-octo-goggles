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


import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap  # optional: install via pip install umap-learn

def plot_medoid_clusters(data, medoids, x_medoid_assignment, method='pca', n_components=2, figsize=(8,6), title="Medoid Clusters"):
    """
    Plots medoid clusters in 2D (or 3D) after dimensionality reduction.
    
    Parameters:
    - data: np.ndarray, shape (n_samples, n_features)
    - medoids: np.ndarray, shape (n_medoids, n_features)
    - x_medoid_assignment: np.ndarray, shape (n_samples,), cluster assignment for each point
    - method: str, 'pca', 'tsne', or 'umap' for dimensionality reduction
    - n_components: int, 2 or 3 dimensions to reduce to
    - figsize: tuple, size of the figure
    - title: str, plot title
    """
    
    # ---- Dimensionality reduction ----
    if method.lower() == 'pca':
        reducer = PCA(n_components=n_components)
    elif method.lower() == 'tsne':
        from sklearn.manifold import TSNE
        reducer = TSNE(n_components=n_components, random_state=42)
    elif method.lower() == 'umap':
        reducer = umap.UMAP(n_components=n_components, random_state=42)
    else:
        raise ValueError("method must be 'pca', 'tsne', or 'umap'")
    
    # Fit reducer on the data
    data_reduced = reducer.fit_transform(data)
    medoids_reduced = reducer.transform(medoids) if hasattr(reducer, 'transform') else reducer.fit_transform(medoids)
    
    # ---- Plot ----
    plt.figure(figsize=figsize)
    
    if n_components == 2:
        plt.scatter(data_reduced[:,0], data_reduced[:,1], c=x_medoid_assignment, cmap='tab10', alpha=0.6, s=50)
        plt.scatter(medoids_reduced[:,0], medoids_reduced[:,1], c='red', marker='X', s=200, label='Medoids')
        plt.xlabel('Component 1')
        plt.ylabel('Component 2')
    elif n_components == 3:
        from mpl_toolkits.mplot3d import Axes3D
        ax = plt.axes(projection='3d')
        ax.scatter(data_reduced[:,0], data_reduced[:,1], data_reduced[:,2], c=x_medoid_assignment, cmap='tab10', alpha=0.6, s=50)
        ax.scatter(medoids_reduced[:,0], medoids_reduced[:,1], medoids_reduced[:,2], c='red', marker='X', s=200, label='Medoids')
        ax.set_xlabel('Component 1')
        ax.set_ylabel('Component 2')
        ax.set_zlabel('Component 3')
    
    plt.title(title)
    plt.legend()
    plt.show()