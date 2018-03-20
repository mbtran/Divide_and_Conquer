#unsorted = [1, 5, 4, 8, 10, 2, 6, 9, 12, 11, 3, 7]

# Opens Assignment2.txt and inputs to list 'unsorted'
with open('Assignment2.txt') as file:
    unsorted = file.readlines()

# Removes /n after every inputted value
unsorted = [x.strip() for x in unsorted]

# Converts each value in the list from string to integer
unsorted = [int(i) for i in unsorted]
global leftcount
global rightcount
global splitcount

def sort_and_count(unsortedlist):
    '''Recursive function to count inversions and sort list.'''

    if int(len(unsortedlist)) < 2:
        return 0, unsortedlist
    else:
        # Using integer division,
        # List 'right' will have longer length by 1 if 'unsortedlist' is odd length.
        middle = int(len(unsortedlist)) // 2
        leftcount, left = sort_and_count(unsortedlist[:middle])
        rightcount, right = sort_and_count(unsortedlist[middle:])
        splitcount, sorted = merge_and_count(left, right)

        invcount = leftcount + rightcount + splitcount
    return (invcount, sorted)


def merge_and_count(left, right):
    i = 0
    j = 0
    splitcount = 0

    sorted = []

    # nrightlength > nleftlength if original list is odd length
    nleftlength = int(len(left))
    nrightlength = int(len(right))

    # 1st while loop will merge most of lists Left and Right
    while i < nleftlength and j < nrightlength:
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        elif left[i] > right[j]:
            sorted.append(right[j])
            j += 1

            splitcount += (nleftlength - i)

    # 2nd while loop is when list Right is completely added
    # to Sorted before list Left
    while i < nleftlength:
        sorted.append(left[i])
        i += 1

    # 3rd while loop is when list Left is completely added
    # to Sorted before list Right
    while j < nrightlength:
        sorted.append(right[j])
        j += 1

    return splitcount, sorted

invcount, sorted = sort_and_count(unsorted)

print(invcount)
print(sorted)

'''with open('Assignment2Sorted.txt', 'w') as output:
    output.write(str(sorted))'''

