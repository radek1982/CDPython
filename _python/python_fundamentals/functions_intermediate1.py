import math
import random
def randInt(min=0 , max=100   ):

    if max<min return -1
    if (max < 0 ) return -1
     
    num = min + (random.random() * (max)) 
    return round(num)

for n in range(21): 
    print(n, randInt(max=5))