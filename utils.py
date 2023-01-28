from main import *

# list maker to avoid confusing number of repeated zeroes

def listmaker(element, times):
    if(times==0):
        return
    else:
        return listmaker(element, times - 1)
    
listmaker(0,16)