import sys
import urllib.request

class LED_board():
    '''Class defined for the LED board'''
    def __init__(self, L):
        '''Board is initialized with an LxL array, with every value set to 
        -1. This is the value used to indicate a light is off'''
        self.array=[[-1]*L for _ in range(L)]
        self.size=L

    def turn_on(self, start, end):
        if start[0]<0:
            start[0]=0
        if start[1]<0:
            start[0]=0
        if end[0]>=self.size:
            end[0]=self.size-1
        if end[1]>=self.size:
            end[1]=self.size-1
        for i in range(start[0],end[0]+1):
            for j in range(start[1], end[1]+1):
                self.array[i][j]=1
    
    def turn_off(self, start, end):
        if start[0]<0:
            start[0]=0
        if start[1]<0:
            start[0]=0
        if end[0]>=self.size:
           end[0]=self.size-1
        if end[1]>=self.size:
            end[1]=self.size-1
        for i in range(start[0],end[0]+1):
            for j in range(start[1], end[1]+1):
                self.array[i][j]=-1
 
    def toggle(self, start, end):
        if start[0]<0:
            start[0]=0
        if start[1]<0:
            start[0]=0
        if end[0]>=self.size:
            end[0]=self.size-1
        if end[1]>=self.size:
            end[1]=self.size-1
        for i in range(start[0],end[0]+1):
            for j in range(start[1], end[1]+1):
                self.array[i][j]*=-1   
                
def read_file(link):
    '''Function which reads in a file from a URL and returns the
    contents of the file in a string'''
    req=urllib.request.urlopen(link)
    buffer=req.read().decode('utf-8')   
    return buffer

def return_coordinates(a):
    '''Function which reads in a string with coordinates "x,y" and returns
    the coordinates as integers in a list'''
    x,y=a.split(",")
    return [int(x), int(y)]

def main():
    link=sys.argv[2] #Reading link to file from command line parameter
    file=read_file(link)
    arraySize=int(file.split("\n")[0]) #Obtaining size of array from first line of file
    board=LED_board(arraySize)
    
    for line in file.split("\n"):
        if "turn on" in line:
            line=line.replace(" ,",",")
            line=line.replace(", ",",")
            a,b,c,d,e=line.split() #splits string into 5 variables, with coordinates in c and e
            start_point,end_point=return_coordinates(c),return_coordinates(e)
            board.turn_on(start_point, end_point)
        elif "turn off" in line:
            line=line.replace(" ,",",")
            line=line.replace(", ",",")
            a,b,c,d,e=line.split()
            start_point, end_point=return_coordinates(c), return_coordinates(e)
            board.turn_off(start_point, end_point)
        elif "switch" in line:
            line=line.replace(" ,",",")
            line=line.replace(", ",",")
            a,b,c,d=line.split()
            start_point, end_point=return_coordinates(b), return_coordinates(d)
            board.toggle(start_point, end_point)
        else:
            pass
     
    on_count=0
    for i in range(arraySize):
        for j in range(arraySize):
            if board.array[i][j]==1:
                on_count+=1
    print(on_count)

    