import platform
def separator(path):
    if platform.system=="Windows":
        pass
    else:
        k=path.split('/')
        return k[len(k)-1], '/'.join(k[0:len(k)-1])
        
fileName,Directory=separator("/Users/pragyabharti/Desktop/pythonPrac/stringPath.py")
print("file name is: ", fileName ,"and", "Directory is: ", Directory)