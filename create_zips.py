#https://stackoverflow.com/questions/32763950/python-continuously-check-size-of-files-being-added-to-list-stop-at-size-zip

import os,os.path, zipfile
from time import *
import timeit
import datetime

file_directory_name = 'islandora_import'

# Specify the directory to look at
dirname = os.path.dirname(__file__)
searchDirectory = os.path.join(dirname, file_directory_name)

# Get list of all files in dir
files = os.listdir(searchDirectory)

# Number of files
num_files = len(files)
print(num_files)

# Count for zip file name
part_count = 1


#### Function to create zip file ####
# Add the files from the list to the zip archive
def zipFunction(zipList, part_count):

    print("Starting Zip Part " + str(part_count))

    # Specify zip archive output location and file name
    t = datetime.datetime.now()
    timestamp = t.strftime('%b_%d_%Y_%H%M')
    dirname = os.path.dirname(__file__)
    zipName = os.path.join(dirname, file_directory_name+'_part'+str(part_count)+'_'+timestamp+'.zip')

    # Create the zip file object
    zipA = zipfile.ZipFile(zipName, "w", allowZip64=True)  

    # Go through the list and add files to the zip archive
    for w in zipList:

        # Create the arcname parameter for the .write method. Otherwise  the zip file
        # mirrors the directory structure within the zip archive (annoying).
        arcname = w[len(root)+1:]

        # Write the files to a zip
        zipA.write(w, arcname, zipfile.ZIP_DEFLATED)

    # Close the zip process
    zipA.close()
    return       
#################################################
#################################################

sTime = datetime.datetime.now()

# Set the size counter
totalSize = 0

# Create an empty list for adding files to count MB and make zip file
zipList = []

# Create a counter to check number of files
count = 0

# Set the root, directory, and file name
for root,direc,f in os.walk(searchDirectory):

        #Go through the files in directory
        for name in sorted(f):

            # Set the os.path file root and name
            full = os.path.join(root,name)

            # Split the file name from the file extension
            n, ext = os.path.splitext(name)

            # Get size of each file in directory, size is obtained in BYTES
            fileSize = os.path.getsize(full)

            # Add up the total sizes for all the files in the directory
            totalSize += fileSize

            if name[:2] != '._' and name[-4:] != '.zip':
                zipList.append(full)
            else:
                 print(name)

            count +=1

            # Convert from bytes to megabytes
                # 1 kilobyte = 1,024 bytes
                # 1 megabyte = 1,048,576 bytes
                # 1 gigabyte = 1,073,741,824 bytes
            if (((totalSize + fileSize) // 1048576 > 900) and (count %2 == 0)) or (count == num_files):
                zipFunction(zipList,part_count)
                zipList = []
                totalSize = 0
                part_count += 1

eTime = datetime.datetime.now()
elapsedTime = eTime - sTime
print("Run time is %s. Number of files is %s. Number of zip files is %s." % (elapsedTime,count,part_count-1))