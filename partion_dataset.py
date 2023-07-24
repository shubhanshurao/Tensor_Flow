import os
import random
import shutil

def extract_and_save_40_percent(source_folder, destination_folder):
    # List all files in the source folder
    all_files = os.listdir(source_folder)

    # Calculate the number of files to extract (40% of total files)
    num_files_to_extract = int(len(all_files) * 0.4)

    # Select random files to extract
    files_to_extract = random.sample(all_files, num_files_to_extract)

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Copy or move the selected files to the destination folder
    for file in files_to_extract:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        # Use shutil.copy() to copy files or shutil.move() to move files
        shutil.copy(source_path, destination_path)
        # If you want to move the files instead of copying, use:
        # shutil.move(source_path, destination_path)

# Example usage:
source_folder = r"D:\Bronchi\left"
destination_folder = r"D:\Bronchi\left40"
extract_and_save_40_percent(source_folder, destination_folder)
