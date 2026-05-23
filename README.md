# ML Data Exploration

A growing collection of exploratory machine learning notebooks focused on understanding algorithms from the ground up through implementation, experimentation, visualization, and real-world datasets.

This repository currently focuses on unsupervised clustering methods, including K-Means and K-Medoids, with plans to expand into additional machine learning algorithms and techniques over time.

The goal of this project is not only to use machine learning algorithms, but to understand how they work internally by implementing and analyzing them step by step.

---

## Project Goals

* Implement machine learning algorithms from scratch
* Explore the mathematical intuition behind clustering methods
* Visualize how algorithms behave on real-world datasets
* Compare scratch implementations with library-based approaches
* Build a growing educational machine learning reference library
* Strengthen practical machine learning and data analysis skills

---

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

---

## Folders and Files

### `K-Medoids/`

Contains the K-Medoids clustering work.

* `Iris.csv`: Iris flower dataset with sepal and petal measurements plus species labels.
* `functions.py`: A from-scratch K-Medoids implementation. It includes helper functions for assigning points to medoids, retrieving cluster points, computing cluster costs, updating medoids, and running the full `k_medoids` workflow.
* `plots.py`: Plotting utilities for K-Medoids results. It includes 2D Plotly and Matplotlib cluster plots, optional animation support, and `plot_medoid_clusters`, which can reduce higher-dimensional data with PCA, t-SNE, or UMAP before plotting.
* `k_medoids_scratch.ipynb`: A notebook explaining K-Medoids theory and implementing the algorithm step by step on synthetic data.
* `k_medoids_libraries.ipynb`: A notebook that loads `Iris.csv`, scales numeric features, runs the local `functions.k_medoids` implementation with `k=3`, and visualizes the resulting medoid clusters.

Key concepts explored:

* Distance-based clustering
* Medoid optimization
* Cluster cost minimization
* Dimensionality reduction for visualization
* Comparing scratch implementations with library workflows

---

### `k-means/`

Contains K-Means clustering experiments and visualization helpers.

* `Mother Genome.csv`: Genome dataset with rsid, chromosome, position, and genotype columns.
* `functions.py`: Visualization helpers for histogram and bar plots using Matplotlib and Seaborn.
* `genome.ipynb`: Loads genome data, performs preprocessing and feature engineering, applies K-Means clustering, evaluates cluster counts using elbow plots, and visualizes clusters with PCA.
* `mall_customer.ipynb`: Performs K-Means clustering on mall customer data. It label-encodes gender, scales features, evaluates cluster counts using elbow and silhouette methods, and visualizes clustering results using PCA, t-SNE, heatmaps, and pair plots.

Key concepts explored:

* Feature preprocessing
* One-hot encoding
* Scaling and normalization
* Elbow and silhouette evaluation methods
* PCA and t-SNE visualization
* Real-world clustering analysis

> Note: `Mall_Customers.csv` is referenced by the notebook but is not currently included in the repository.

---

### `DBSCAN/`

Currently empty and reserved for future DBSCAN clustering work.

Planned additions include:

* Density-based clustering
* Noise point detection
* Cluster comparison experiments
* Visualization of non-linear clusters

---

## Current Focus of the Repository

This project currently emphasizes:

* Unsupervised learning
* Clustering algorithms
* From-scratch implementations
* Visualization and interpretability
* Educational walkthroughs in Jupyter notebooks
* Real-world dataset experimentation

Each notebook is designed to explain both the theory and practical implementation details of the algorithms being explored.

---

## Technologies Used

The notebooks and helper scripts use common Python data science and machine learning libraries:

* Python
* Jupyter Notebook
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* SciPy
* Plotly
* UMAP
* LightGBM
* KaggleHub

Some imports are only used in specific notebooks. For example:

* `lightgbm` is imported in `k-means/genome.ipynb`
* `umap-learn` is used for optional dimensionality reduction visualizations in `K-Medoids/plots.py`

---

## Dependencies

Example environment setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install numpy pandas matplotlib seaborn scikit-learn scipy plotly nbformat kagglehub umap-learn lightgbm jupyter
```

---

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
```

2. Navigate into the repository:

```bash
cd your-repository-name
```

3. Create and activate a Python environment.

4. Install the required dependencies.

5. Open the notebooks in:

* Jupyter Notebook
* JupyterLab
* VS Code

6. Run notebooks from their own folders so relative CSV paths resolve correctly.

---

## Planned Future Implementations

This repository is intended to continue growing over time.

Planned future additions include:

* DBSCAN
* Hierarchical Clustering
* Linear Regression
* Logistic Regression
* Decision Trees
* Random Forests
* Support Vector Machines (SVM)
* Naive Bayes
* Principal Component Analysis (PCA)
* Neural Networks
* Additional visualization and evaluation utilities

---

## Why This Project?

This project was created as a way to deeply understand machine learning algorithms by building and analyzing them manually instead of treating them as black-box tools.

The repository also serves as:

* A personal machine learning learning archive
* A growing algorithm implementation library
* A portfolio project demonstrating machine learning and data analysis skills
* A foundation for future experimentation and research

---

## Future Improvements

Planned improvements include:

* More clustering algorithms
* More supervised learning methods
* Improved visualizations and animations
* Additional datasets
* Performance benchmarking
* Evaluation metrics and comparisons
* Interactive experimentation notebooks
* Better modularization of helper functions

---

## Author

Created by a Computer Science and Data Science student with interests in machine learning, software engineering, data analysis, and algorithm implementation.

---
