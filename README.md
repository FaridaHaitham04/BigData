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

## DOCKER COMMANDS SPACE ##
---------------------------


# Pipeline Execution Flow
- ingest.py
Reads dataset from command line
Saves it as data_raw.csv

- preprocess.py
Cleans data (missing values, duplicates)
Encodes categorical variables
Scales numerical features
Applies PCA for dimensionality reduction
Performs discretization (binning)
Saves data_preprocessed.csv

- analytics.py