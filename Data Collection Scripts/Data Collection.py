import os
import subprocess
import sys

# Function to check if dataset files exist
def check_dataset_exists(dataset_dir):
    if os.path.exists(dataset_dir):
        files = os.listdir(dataset_dir)
        # Check if dataset files are present (adjust condition as needed)
        if any(file.endswith('.sqlite') for file in files):
            return True
    return False

def check_archive_exists(archive_dir):
    if os.path.exists(archive_dir):
        files = os.listdir(archive_dir)
        # Check if dataset files are present (adjust condition as needed)
        if any(file.endswith('.zip') for file in files):
            return True
    return False
# Main script
def main():
    # Define dataset directory
    dataset_dir = r'C:\Users\c2tlha\Desktop\DATA ENGINEERING PROJECT\Dataset\terencicp'
    dataset_exists = check_dataset_exists(dataset_dir)

    # Check if any *.zip files exist in the archive directory
    archive_dir = r'C:\Users\c2tlha\Desktop\DATA ENGINEERING PROJECT\Dataset\terencicp'
    archive_exists = check_archive_exists(archive_dir)

    # If dataset files do not exist, download the dataset

    
    if archive_exists:
        try:
            # Execute batch script to download dataset
            batch_script_path_win = r'C:\Users\c2tlha\Desktop\DATA ENGINEERING PROJECT\Bash Script\unzip.bat'
            batch_script_path_linux = r'C:\Users\c2tlha\Desktop\DATA ENGINEERING PROJECT\Bash Script\unzip.sh'
            #check operating system if windows or linux
            #if linux run batch_script_path_linux
            #if windows run batch_script_path_win

            if os.name == 'nt':
                subprocess.run([batch_script_path_win], shell=True, check=True)
            else:
                subprocess.run([batch_script_path_linux], shell=True, check=True)
            
            print("Archive unziped successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error unzipping archive: {e}")
    
    if not dataset_exists:
        try:
            # Execute batch script to download dataset
            batch_script_path_win = r'C:\Users\c2tlha\Desktop\DATA ENGINEERING PROJECT\Bash Script\download_dataset.bat'
            batch_script_path_linux = r'C:\Users\c2tlha\Desktop\DATA ENGINEERING PROJECT\Bash Script\download_dataset.sh'
            
            if os.name == 'nt':
                subprocess.run([batch_script_path_win], shell=True, check=True)
            else:
                subprocess.run([batch_script_path_linux], shell=True, check=True)
            
            print("Dataset downloaded successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error downloading dataset: {e}")
    else:
        print("Dataset already exists. Skipping download.")

if __name__ == "__main__":
    main()
