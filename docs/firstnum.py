'''
Created on 26 Feb 2017

@author: Conor
'''
import re

def first(str):
    newstr=""
    i=0
    while i<len(str):
        if str[i] in "0123456789,":
            newstr+=str[i]
        i+=1
    return newstr

print(first("switch 109  ,   920 through 331, 392"))

        
        