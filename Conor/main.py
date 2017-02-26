import sys
import urllib.request

def read_file(link):
    '''Function which reads in a file from a URL and returns the
    contents of the file in a string'''
    req=urllib.request.urlopen(link)
    buffer=req.read().decode('utf-8')   
    return buffer

'''
link=sys.argv[2] #Reads in the link from the command line parameter
file=read_file(link)

for line in file.split("\n"): #printing out file in the command line
    print(line)
'''