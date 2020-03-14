import os

def createDir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def getFileSize(size:float):
    unit = ['b','Kb','Mb','Gb','Tb']
    count=0
    while size>1024:
        size = size/1024
        count +=1
    return '%.2f %s' % (size,unit[count])
