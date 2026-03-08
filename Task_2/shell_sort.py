"""Shell Sort"""

#Shell Sort is an algorithm that is used to sort lists but not by comparing adjacent elements. It compares
#elements that are far apart using a gap which is reduced in size. 

def shell_sort(a):
    n = len(a)
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for g in gaps:
        if g >= n: 
            continue
        for i in range(g, n):
            t = a[i]
            j = i
            while j >= g and a[j-g] > t:
                a[j] = a[j-g]
                j -= g
            a[j] = t

arr = [5, 12, 32, 22, 31]
shell_sort(arr)
print(arr)