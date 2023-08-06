# Check on what operating system the script is running 

```python
# Tested on windows 
$pip install list-files-with-timestats
from list_files_with_timestats import get_folder_file_complete_path,get_folder_file_complete_path_limit_subdirs
folders = [r"C:\Program Files\NVIDIA Corporation"]
allfi = get_folder_file_complete_path_limit_subdirs(
    folders, maxsubdirs=1, withdate=True
) # calling this function, you can limit the depth of the subdirs, and get the creation and modification times
for a in allfi:
    print(a)


# Listing the files with all subdirs 
fi = get_folder_file_complete_path(folders=[r'C:\Users\Gamer\anaconda3\bin',r"C:\yolovtest"])
for file in fi[:10]:
    print(file.folder, file.file, file.path, file.ext)
    
```




