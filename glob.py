import glob
import os
l=glob.glob('/home/niladri/Pictures/ImageToPoetry/**',recursive=True)
poems=""
for i in l:
    try:
        f = open(i,'r')
        poem = f.read()
        poems=poems+poem
        f.close()
    except:
        print("error in ",i)
len(poems)
f= open("poems.txt","w+")
f.write(poems)
f.close()