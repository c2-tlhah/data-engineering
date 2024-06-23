@echo off

rem Set your Kaggle API credentials
set KAGGLE_USERNAME=muhammadtalharamzan
set KAGGLE_KEY=30fd169daa2d17c508d2cd4d75488d49

rem Specify the dataset to download
set dataset=terencicp/e-commerce-dataset-by-olist-as-an-sqlite-database

rem Destination directory
set destination=C:\Users\c2tlha\Desktop\DATA ENGINEERING PROJECT\Dataset\terencicp

rem Ensure destination directory exists
mkdir "%destination%"

rem Download dataset using Kaggle API
kaggle datasets download -d %dataset% -p "%destination%" --unzip
