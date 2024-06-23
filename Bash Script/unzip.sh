#!/bin/bash

# Set the directory path where zip files are located
sourceDir="/home/user/Desktop/DATA ENGINEERING PROJECT/Dataset/terencicp"

# Check if source directory exists
if [ ! -d "$sourceDir" ]; then
    echo "Directory \"$sourceDir\" not found."
    exit 1
fi

# Change the current directory to the source directory
cd "$sourceDir" || {
    echo "Cannot change to the directory \"$sourceDir\""
    exit 1
}

# Loop through each zip file in the source directory
for f in *.zip; do
    # Extract each zip file directly into the current directory
    unzip "$f" -d "$(dirname "$f")"
    
    # Check if extraction was successful before deleting the zip file
    if [ $? -ne 0 ]; then
        echo "Error extracting \"$f\""
        exit 1
    else
        # Delete the zip file after extraction
        rm "$f"
    fi
done

# Display message indicating process completion
echo "All zip files extracted and deleted successfully."
