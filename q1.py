import os

def all_files_path(dirc):
    # list of immediate child in the directory inclusing subdirectory or files.
    file_list = os.listdir(dirc)
    #print (listOfFile)
    files = []
    for f in file_list:
        path = os.path.join(dirc,f)
        # If entry is a directory then recursively call for subdirectory
        if os.path.isdir(path):
            files = files + all_files_path(path)
        else:
            files.append(path)
                
    return files


dirc = '/home/pulkit/Desktop/gramener';


files_list = all_files_path(dirc)    
print (files_list)
