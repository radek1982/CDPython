
from math import inf

def biggie_size (list):
    for n in range(len(list)):
        if list[n] > 0: 
            list[n] = "big"
    return list

print(biggie_size([-1, 3, 5, -5]))

def count_positives (list):
    count=0
    for n in range(len(list)):
        if list[n] > 0: 
                count+=1
        
    list[len(list) -1 ] = count

    return list

print(count_positives([-1, 1,1,1]))

def sum_total (list):
    total = 0
    for n in list:
        total +=n
    return total

print(sum_total([1,2,3]))

def average (list):
    
    t = sum_total(list)
    return t / len(list)

print(average([1,2]))

def length(list):
    count = 0
    
    for n in range(len(list)): 
        count+=1

    return count

print(length([]))

def minimum (list):
    n  = inf

    for i in list:
        if i < n: 
            n = i
    return n

print(minimum([1000000,3,7]))   

def maximum (list):
    n = -inf

    for i in list:
        if i >n:
            n = i
    return n 

print(maximum([10,7,2])) 

def ultimate_analysis (list):
    return {"sum": sum_total(list), "avg": average(list), "min": minimum(list), "max": maximum(list)}


print(ultimate_analysis([1,2,3]))

def reverse(list):

    mid = len(list) // 2

    for i in range(mid):

        # 1 2 3 
        # 1 > 3
        x = list[i] 
        last = (len(list) -1) - i # list[3]
        y = list[last] # 3

        list[i] = y
        list[last] = x

    return list

print(reverse([1,2,3]))