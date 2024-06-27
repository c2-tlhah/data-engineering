import os
import subprocess

def check_archive_exists(archive_dir):
    if os.path.exists(archive_dir):
        files = os.listdir(archive_dir)
        # Check if any *.zip files are present (adjust condition as needed)
        if any(file.endswith('.zip') for file in files):
            return True
    return False

def main():
    # Check if any *.zip files exist in the archive directory
    archive_dir = r'C:\Users\c2tlha\Desktop\data-engineering\Data Collection Scripts\Dataset\terencicp'
    archive_exists = check_archive_exists(archive_dir)

    if archive_exists:
        try:
            # Execute batch script to unzip archive
            batch_script_path_win = r'C:\Users\c2tlha\Desktop\data-engineering\Bash Script\unzip.bat'
            batch_script_path_linux = r'C:\Users\c2tlha\Desktop\data-engineering\Bash Script\unzip.sh'
            
            if os.name == 'nt':
                subprocess.run([batch_script_path_win], shell=True, check=True)
            else:
                subprocess.run([batch_script_path_linux], shell=True, check=True)
            
            print("Archive unzipped successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error unzipping archive: {e}")
    
    try:
        # Always execute batch script to download dataset
        batch_script_path_win = r'C:\Users\c2tlha\Desktop\data-engineering\Bash Script\download_dataset.bat'
        batch_script_path_linux = r'C:\Users\c2tlha\Desktop\data-engineering\Bash Script\download_dataset.sh'
        
        if os.name == 'nt':
            subprocess.run([batch_script_path_win], shell=True, check=True)
        else:
            subprocess.run([batch_script_path_linux], shell=True, check=True)
        
        print("Dataset downloaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading dataset: {e}")

if __name__ == "__main__":
    main()
