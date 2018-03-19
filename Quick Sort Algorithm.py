testarray = [10, 33, 8, 21, 1, 4, 15, 5, 11, 9, 17, 21, 22, 2, 6, 7, 54]
parray = []

r = int(len(testarray)) - 2
l = 0

def partition(array, l, r):
    '''array is the input array
    l denotes the left boundary of the array - the start == 0?
    r denotes the right boundary of the array - the end?
    j denotes the boundary between the seen and unseen
    i denotes the boundary between the elements < and > p
    p is the partition index'''

    p = array[l]
    i = l + 1
    j = i

    while j <= r:
        if array[j] > p:
            j += 1

        if array[j] < p:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

            i += 1
            j += 1

        print(array[j])

    array[l] = array[i - 1]
    array[i - 1] = p

    return array


parray = partition(testarray, l, r)
print(parray)





