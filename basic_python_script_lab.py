# Python Lab: Task Overview

# 0. Create a python environment using python3 -m venv <environment_name> and install
# required libraries (requests). source lab1/bin/activate

# 1. Create a Custom Directory: Use the os module to create a directory named after your first and last name (e.g., john_doe).

# 2. Download a File: Utilize the requests module to download a file named
# change_me.txt from a specified GitHub repository.

# 3. File Management: Save the downloaded file in your custom directory, renaming it
# to <firstname_lastname>.txt.

# 4. Modify File Content: Replace the content of the downloaded file with user input,
# using the following text:
#    a. "Describe what you have learned so far in a sentence."
#    b. Automatically append current date and time to the end of the file.

# 5. Verify the change in the file content.


from datetime import datetime
import requests
import os

dir_name = "humaidu_ali_mohammed"
file_name = "humaidu_ali_mohammed.txt"

# Create the directory if it doesn't exist
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory {dir_name} Created Successfully")
else:
    print(f"Directory {dir_name} Already Exists !!!")

# GitHub raw file URL for testing
github_url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"

# Set full path to save the file
file_path = os.path.join(dir_name, file_name)

try:
    # Download and save the file
    response = requests.get(github_url)
    response.raise_for_status()

    with open(file_path, 'wb') as f:
        f.write(response.content)

    print(f"File '{file_path}' Saved successfully.")
    
    # Prompt the user for input to replace file content
    user_input = input("Describe what you have learned so far in a sentence: ")

    # Append current date and time to the content
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_to_write = f"{user_input}\n\nTimestamp: {current_time}"
    
    # Write the modified content back to the file
    with open(file_path, "w") as f:
        f.write(content_to_write)

    print(f"File '{file_path}' has been updated with your input and timestamp.")

except requests.exceptions.RequestException as e:
    print(f"Error downloading file: {e}")



