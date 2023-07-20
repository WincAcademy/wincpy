# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line

import os
import shutil
from zipfile import ZipFile

###
# --- Make sure the imports are on the top of the file ---
###

base_path = os.getcwd()
cache_path = os.path.join(base_path, "cache")
data_path = os.path.join(base_path, "data.zip")
"""
Here we create the paths we use in the assignment as global variables, this way you only have to define them once.
Create the paths using "getcwd()" and "join()" so the paths can be used on every computer and OS.
"""

# 1

def clean_cache():
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
    os.mkdir(cache_path)

###
# If "cache" exists, delete the directory. Then make a new directory.
###

# 2

def cache_zip(zip, cache):
    with ZipFile(zip, "r") as zipObj:
        zipObj.extractall(cache)

###
# Use the zipfile module to extract the zip file in a small amount of code.
###

# 3

def cached_files():
    cached_files_list = []
    for path in os.listdir(cache_path):
        full_path = os.path.join(cache_path, path)
        cached_files_list.append(full_path)
    return cached_files_list
"""
Here we do the following:
    - Use listdir to loop over the name of every file. 
    - Make the full path with "join()"
    - Use "append()" to add the path to a predefined list
    - return the list

Note: We can also use a list comprehension as seen below. Read this as:
        'do something for every value in list'
"""
def cached_files_alternative():
    return [os.path.join(cache_path, path) for path in os.listdir(cache_path)]



# 4

def find_password(list_of_files):
    for file in list_of_files:
        with open(file) as f:
            for line in f:
                if "password" in line:
                    split_line = line.split(" ", 1)
                    return split_line[1].strip()
"""
Here we do the following:
    - Loop over every file in a list of files
    - Open the file in the iteration
    - Loop over every line in the file
    - if "password" is found in the line:
        - split the line 
        - return the password and strip off non-ascii characters
"""

# This block is only executed when run from "main", and not when imported.
if __name__ == "__main__":
    clean_cache()
    cache_zip(data_path, cache_path)
    cached_files()
    print(find_password(cached_files()))