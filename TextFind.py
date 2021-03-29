
#Used to search text wanted in lots of files
#Author: Stupid Bird

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
    
    print("SearchPath:\n",databasepath,"\n\n")
    
    searchfile(databasepath,'c')
    searchfile(databasepath,'h')
    searchfile(databasepath,'yar')
    searchfile(databasepath,'yara')
    searchfile(databasepath,'txt')


    print("SearchResult:\n")
    for retinfopath in pathlist:
        f=open(retinfopath,'r',encoding='utf-8')
        line = 0  
        alllines=f.readlines()
        for eachline in alllines:
                line = line + 1
                title = str(eachline)
                if title.find(string)!=-1:
                    print(retinfopath,"\n",line,"\n",eachline,"\n\n")
                                                       
        f.close()


if __name__=="__main__":
    databasepath = sys.path[0] + "\searchpath"
    string = "2d845bd6662e7449f4db7a922e67c665df70cd045af48e2cb3d689a5d0004b2f"
    main(databasepath,string) 
