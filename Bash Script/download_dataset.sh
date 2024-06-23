#!/bin/bash

# Set Kaggle API credentials (replace with your own)
export KAGGLE_USERNAME="muhammadtalharamzan"
export KAGGLE_KEY="30fd169daa2d17c508d2cd4d75488d49"

# Specify dataset to download
dataset="terencicp/e-commerce-dataset-by-olist-as-an-sqlite-database"
# Destination directory for dataset
destination="C:/Users/c2tlha/Desktop/DATA ENGINEERING PROJECT/Dataset/terencicp"

# Ensure destination directory exists
mkdir -p "$destination"

# Download dataset using Kaggle CLI
kaggle datasets download -d "$dataset" -p "$destination" --unzip
