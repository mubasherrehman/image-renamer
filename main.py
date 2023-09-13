import os

# Get the current directory where the Python script is located
folder_path = os.path.dirname(os.path.abspath(__file__))

# Get a list of all files in the current directory
files = os.listdir(folder_path)

# Iterate through each file in the current directory
for filename in files:
    file_path = os.path.join(folder_path, filename)

    # Check if the file is a regular file (not a directory)
    if os.path.isfile(file_path):
        # Check if the file doesn't have an extension
        if '.' not in filename:
            # Rename the file with a .png extension
            new_filename = filename + '.png'
            new_file_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')
