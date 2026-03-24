# Big Data Analytics: Assignment 1

# Employee Analytics Pipeline

## Team Members & IDs
- Rawan Al-Ghobashy  - 231000897
- Farida Abdelmonem - 231000032
- Habiba Salama - 231000040
- Farah Darwish - 231000063

## Project Overview

This project implements a complete **employee analytics pipeline** using Python inside a Docker container.

The pipeline performs:
- Data ingestion
- Data preprocessing
- Analytics (insights generation)
- Data visualization
- Clustering using K-Means

## Technologies Used

- Python 3.11 (Docker)
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Docker

# DOCKER COMMANDS 
docker build -t employee-analytics .
docker run -it --name employee_analytics_container employee-analytics


# Run the Pipeline
python ingest.py employee_dataset.csv


# Pipeline Execution Flow
1. ingest.py
Reads dataset from command line argument
Saves it as data_raw.csv
Passes it to the next stage

2. preprocess.py
Removes duplicates
Handles missing values (median for numeric, mode for categorical)
Encodes categorical variables
Scales numerical features
Applies PCA for dimensionality reduction
Performs discretization (binning)
Saves data_preprocessed.csv

3. analytics.py
Generates textual insights from the dataset
Saves:
insight1.txt
insight2.txt
insight3.txt

4. visualize.py
Creates three plots:
Histogram
Boxplot
Correlation heatmap
Saves summary_plot.png

5. cluster.py
Applies K-Means clustering
Uses selected numerical features
Saves cluster distribution in clusters.txt
summary.sh Explanation

The summary.sh script is used to:
-  Copy all generated output files from the Docker container to the host machine
- Save them inside the results/ folder
- Stop and remove the container
- To run : .\summary.sh

# Output Files:
results/
data_raw.csv
data_preprocessed.csv
insight1.txt
insight2.txt
insight3.txt
summary_plot.png
clusters.txt

# Github Repo Link: https://github.com/FaridaHaitham04/BigData
# DockerHub Link: https://hub.docker.com/r/rawanalghobshy5/employee-analytics