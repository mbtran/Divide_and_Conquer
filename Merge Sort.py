unsorted = [1, 2, 5, 12, 23, 6, 21, 15, 73, 24, 45, 86, 4, 58, 78,
            77, 63, 43, 45, 32, 122, 32, 21, 23, 55, 32, 76, 75, 22,
            41, 22, 66, 77, 88]

shortList = [3, 12, 32, 45, 23, 12, 63, 33]

unsorted1 = [60, 20, 32, 45, 23, 13, 63, 33, 40, 99, 2, 25, 109, 44, 200, 1, 65]


def MergeSort(unsortedlist):
    '''Recursive function to sort list.'''
    if int(len(unsortedlist)) < 2:
        return unsortedlist
    else:
        # Using integer division, list 'right' will have longer length by 1 if 'unsortedlist' is odd length.
        middle = int(len(unsortedlist)) // 2
        left = MergeSort(unsortedlist[:middle])
        right = MergeSort(unsortedlist[middle:])
    return Merge(left, right)


def Merge(left, right):
    print(left)
    print(right)
    i = 0
    j = 0

    #nrightlength > nleftlength if original list is odd length
    nleftlength = int(len(left))
    nrightlength = int(len(right))

    sorted = []

    # First while loop will merge most of lists Left and Right
    while i < nleftlength and j < nrightlength:
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        elif left[i] > right[j]:
            sorted.append(right[j])
            j += 1

    # Second while loop is when list Right is completely added to Sorted before list Left
    while i < nleftlength:
        sorted.append(left[i])
        i += 1

    # Third while loop is when list Left is completely added to Sorted before list Right
    while j < nrightlength:
        sorted.append(right[j])
        j += 1

    return sorted


print(MergeSort(unsorted))