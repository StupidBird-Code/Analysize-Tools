import os

#Used to xor one byte to find hidden IPaddress\PE\URL in malware
#Author: SangFor APT Team---- Stupid Bird

size = 0
def main(path):
    global size
    key = 1
    while key<256:
        i=0
        print key
        data = open(path,"rb")
        size = os.path.getsize(path)
        while 1:   
            try:
                s = data.read(1)
                s  = key^ord(s)
                i = i + 1
                if s==77:            #4D
                    t = data.read(1)
                    t  = key^ord(t)
                    i = i + 1
                    if t==90:        #"MZ" flag
                        JudgePE(data,key,i)
                
                if s==46:             
                    t = data.read(3)
                    l  = key^ord(t[0])
                    m  = key^ord(t[1])
                    n  = key^ord(t[2])
                    if l ==99 and m==111 and n==109:    #.com
                        print(key,hex(i-1),"Find .com URL!")
                    if l ==110 and m==101 and n==116:   #.net
                        print(key,hex(i-1),"Find .net URL!")
                    data.seek(-3,1)

                if 48<=s<=57:
                    t = data.read(1)
                    t  = key^ord(t)
                    i = i + 1
                    if 48<=t<=57:        #"MZ" flag
                        JudgeIP(data,key,i,s,t)
                                                
            except Exception as e:
                break
                
        data.close()
        key = key + 1

def JudgePE(data,key,i):
    dosheader = data.read(60)             #0x3C = 60
    s  = key^ord(dosheader[58])
    t = key^ord(dosheader[59])
    offset = t*16+s
    pe = data.read(offset-60)
    s  = key^ord(pe[offset-62])
    t = key^ord(pe[offset-61])
    if s == 80 and t == 69:          #"PE" flag
        print(key,hex(i-2),"Find PE!")
    data.seek(-offset,1)


def JudgeIP(data,key,i,s,t):

    global size
    ipdata = ""
    countlist = []
    if size-i>13:
        rawdata = data.read(13)          #MAX IP length = 15
    for c in rawdata:
        number = key^ord(c)
        ipdata += chr(number)
        countlist.append(number)

    if ipdata.count(".")>=3:
        index=ipdata.find(".")
        if 48<=countlist[index+1]<=57 and 48<=countlist[index-1]<=57:
            index2=ipdata.find(".",index+1)
            if 48<=countlist[index2+1]<=57 and 48<=countlist[index2-1]<=57:
                index3=ipdata.find(".",index2+1)
                if 48<=countlist[index3+1]<=57 and 48<=countlist[index3-1]<=57:
                    ipdata = chr(s) + chr(t) + ipdata
                    print (key,hex(i),"Find IP address:",ipdata) 
        
    data.seek(-13,1)
   
       
if __name__ == '__main__':
    path = "C:\\trickbot.dll"
    main(path)
