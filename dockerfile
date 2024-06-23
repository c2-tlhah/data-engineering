# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python scripts and data collection scripts into the container
COPY main.py ./
COPY "Bash Script"/download_dataset.bat "Bash Script"/
COPY "Data Collection Scripts"/Data\ Collection.py "Data Collection Scripts"/

# Install any needed packages specified in requirements.txt
RUN pip install kaggle pandas numpy matplotlib seaborn requests

# Set Kaggle API credentials as build arguments
ARG KAGGLE_USERNAME=muhammadtalharamzan
ARG KAGGLE_KEY=30fd169daa2d17c508d2cd4d75488d49

# Set environment variables for Kaggle API
ENV KAGGLE_USERNAME=$KAGGLE_USERNAME
ENV KAGGLE_KEY=$KAGGLE_KEY

# Run the Python application when the container launches
CMD ["python", "./main.py"]
