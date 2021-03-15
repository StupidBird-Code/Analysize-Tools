import os
import sys
import re

pathlist = []

def searchfile(root, target):
    global pathlist
    items = os.listdir(root)
    for item in items:
        path = os.path.join(root, item)
        if os.path.isdir(path):
            searchfile(path, target)
        elif item.split('.')[-1] == target:
            pathlist.append(path)


def main(databasepath,string):
    
    global pathlist
    repeatlist = []
    
    print databasepath
    searchfile(databasepath,'c')
    searchfile(databasepath,'h')
 
    for retinfopath in pathlist:
        f=open(retinfopath,'r')
        line = 0  
        alllines=f.readlines()
        for eachline in alllines:
                line = line + 1
                title = str(eachline)
                if title.find(string)!=-1:
                    print retinfopath
                    print eachline
                    print "find"
                    print line
                    
                                    
        f.close()


if __name__=="__main__":
    databasepath = sys.path[0] + "\\mbedtls-development"
    string = "ERROR_CODES"
    main(databasepath,string) 
