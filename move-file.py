import os
import shutil

DIRECTORY = os.path.dirname(os.path.abspath(__file__))

source = os.path.join(DIRECTORY, 'data/train/dogs')                # files location
destination =  os.path.join(DIRECTORY, 'data/validation/dogs')     # where to move to 
folder = os.listdir(source)               # returns a list with all the files in source

for i in range(1500):                 # 1500 files 
  file = folder[0]                    # select the file's name
  curr_file = source + '/' + file     # creates a string - full path to the file
  shutil.move(curr_file, destination) # move the files
  folder.pop(0)                       # Remove the moved file from the list
