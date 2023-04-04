'''
Sorting:
slow: selectionsort
quick: quick sort O(nlogn)
'''

def sel_sort(data): #timecomplexity O(n^2)
    #code from lecture 9
    '''
    lenght of the list
    we take first element and the next element
    compare them to each other and then change places 
    n^2 because we have two for-loops
    '''
    n = len(data)
    for i in range(n-1):
        minst = i
        for j in range(i+1,n):
            if data[j] < data[minst]: 
                minst = j
        data[minst],data[i] = data[i], data[minst]

    
#code from lecture 9
#timecomplexity O(n log N)
def quicksort(data):
    sista = len(data) - 1
    qsort(data, 0, sista)

def qsort(data, low, high):
    pivotindex = (low+high)//2 
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]  
    
    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low-1, high, data[high]) 
    
    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]       
    
    if pivotmid-low > 1:
        qsort(data, low, pivotmid-1)
    if high-pivotmid > 1:
        qsort(data, pivotmid+1, high)

def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h: 
            break
    data[v], data[h] = data[h], data[v]
    return v
