"""Shell Sort"""

#Code is from https://www.geeksforgeeks.org/dsa/shell-sort/

#Function of Code: Choose a interval(gap) sequence and sort the elements with the help of the insertion sort (putting the
# elements in the unsorted portion one by one in to the sorted portion by comparison). Reduce the interval(gap) and repeat till
# the interval(gap) becomes 1. 

def shell_sort(arr):
    n = len(arr)

    # gap is reduced
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]
            j = i

            # Move earlier elements that are bigger than the temp value
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Place the temp in correct position
            arr[j] = temp

        # gap is reduced
        gap //= 2

def print_array(arr):
    print(" ".join(map(str, arr)))

arr = [5, 21, 98, 34, 52]

shell_sort(arr)
print_array(arr)