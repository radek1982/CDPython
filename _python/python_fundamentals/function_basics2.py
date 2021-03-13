def countdown(num):
  return [* range(num, -1, -1)]
print(countdown(5))

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))

def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))


def values_greater_than_second(list):

    
    if len(list) < 2: return False

    x = list[1]
    results = []

    for n in range(len(list)): 
        if list[n] > x: 
                results.append(list[n])
    return results

print(values_greater_than_second([5]))

def length_and_value(l, v):
    results = []

    for n in range(0,l):
        results.append(v);

    return results

print(length_and_value(4, 7))