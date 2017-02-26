import sys
import urllib.request

class LED_board():
    '''Class defined for the LED board'''
    def __init__(self, L):
        '''Board is initialized with an LxL array, with every value set to 
        -1. This is the value used to indicate a light is off'''
        self.array=[[-1]*L for _ in range(L)]
        self.size=L
     
def read_file(link):
    '''Function which reads in a file from a URL and returns the
    contents of the file in a string'''
    req=urllib.request.urlopen(link)
    buffer=req.read().decode('utf-8')   
    return buffer

def main():
    link=sys.argv[2] #Reading link to file from command line parameter
    file=read_file(link)
    arraySize=int(file.split("\n")[0]) #Obtaining size of array from first line of file
    board=LED_board(arraySize)
