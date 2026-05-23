# ML Data Exploration

This repository contains exploratory machine learning notebooks focused on
unsupervised clustering. The current work is organized around K-Means and
K-Medoids experiments, with an empty placeholder folder for future DBSCAN work.

## Project Structure

```text
.
├── DBSCAN/
├── K-Medoids/
│   ├── Iris.csv
│   ├── functions.py
│   ├── k_medoids_libraries.ipynb
│   ├── k_medoids_scratch.ipynb
│   └── plots.py
├── k-means/
│   ├── Mother Genome.csv
│   ├── functions.py
│   ├── genome.ipynb
│   └── mall_customer.ipynb
├── .gitignore
└── README.md
```

## Folders and Files

### `K-Medoids/`

Contains the K-Medoids clustering work.

- `Iris.csv`: Iris flower dataset with sepal and petal measurements plus species labels.
- `functions.py`: A from-scratch K-Medoids implementation. It includes helper functions for assigning points to medoids, retrieving cluster points, computing cluster costs, updating medoids, and running the full `k_medoids` workflow.
- `plots.py`: Plotting utilities for K-Medoids results. It includes 2D Plotly and Matplotlib cluster plots, optional animation support, and `plot_medoid_clusters`, which can reduce higher-dimensional data with PCA, t-SNE, or UMAP before plotting.
- `k_medoids_scratch.ipynb`: A notebook explaining K-Medoids theory and implementing the algorithm step by step on synthetic data.
- `k_medoids_libraries.ipynb`: A notebook that loads `Iris.csv`, scales numeric features, runs the local `functions.k_medoids` implementation with `k=3`, and visualizes the resulting medoid clusters.

### `k-means/`

Contains K-Means clustering experiments and shared plotting helpers.

- `Mother Genome.csv`: Genome dataset with rsid, chromosome, position, and genotype columns.
- `functions.py`: Small visualization helpers for histogram and bar plots using Matplotlib and Seaborn.
- `genome.ipynb`: Loads the genome data, one-hot encodes chromosome and genotype values, scales genomic positions, applies K-Means clustering, uses an elbow plot to inspect cluster counts, and visualizes clusters with PCA.
- `mall_customer.ipynb`: Performs K-Means clustering on mall customer data. It expects a local `Mall_Customers.csv` file, label-encodes gender, scales features, evaluates cluster counts with elbow and silhouette methods, and visualizes clusters using PCA, t-SNE, heatmaps, and pair plots. The `Mall_Customers.csv` file is referenced by the notebook but is not currently included in the repository.

### `DBSCAN/`

Currently empty. It appears to be reserved for future DBSCAN clustering work.

### `.gitignore`

Ignores Python bytecode files and the `k-means/__pycache__/` directory.

## Dependencies

The notebooks and helper scripts use common Python data science libraries:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `scipy`
- `plotly`
- `nbformat`
- `kagglehub`
- `umap-learn`
- `lightgbm`

Some imports are only used in specific notebooks. For example, `lightgbm` is imported in `k-means/genome.ipynb`, while `umap-learn` is only needed if using the UMAP option in `K-Medoids/plots.py`.

## Getting Started

1. Create and activate a Python environment.
2. Install the required libraries.
3. Open the notebooks in Jupyter Notebook, JupyterLab, or VS Code.
4. Run notebooks from their own folders so relative CSV paths resolve correctly.

Example setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install numpy pandas matplotlib seaborn scikit-learn scipy plotly nbformat kagglehub umap-learn lightgbm jupyter
```
