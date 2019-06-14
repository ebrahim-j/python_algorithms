import os

# os.walk('path') generates a tuple (dirpath, dirnames, filenames), 
# dirpath is a string, the path to the directory.
# dirnames is a list of the names of the subdirectories in dirpath (excluding '.' and '..')
# fielnames is a list of the names of the non-directory files in dirpath
for (dirpath, dirnames, filenames) in os.walk('/Path/to/top/directory'): 
    for filename in filenames:
        if filename.startswith('whatever'): # this could well be any sort of pattern you are looking to match

            # os.rename('a', 'b') requires the proper paths to each a and b, 
            # failing to give the proper path for b might move the file to the current directory
            os.rename(os.sep.join([dirpath, filename]), os.sep.join([dirpath, filename.replace('opengazettes', 'gazeti')]))

# more details at https://docs.python.org/3/library/os.html
