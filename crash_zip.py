__author__ = 'rocky'
import zipfile

filename="sample.zip"

dictFile="pwdict.txt"

password=open(dictFile,'r')

zf=zipfile.ZipFile(filename)

for p in password:
    
    p=p.strip('\n')

    try:
        zf.extractall("./sample",pwd=p)

        print "crash. Password is %s" %p

        exit(0)
    except:
        pass



