x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627


def splitnumber(number, n):
    '''Takes a number and splits it in half by digits'''
    n1 = number // (10 ** (n // 2))
    n2 = number % (10 ** (n // 2))
    return n1, n2


def multiply(x, y):
    '''Karatsuba multiplication by recursion'''

    # Base case
    if x < 10 or y < 10:
        return x * y

    # Removes a 'digit' if digits are odd prior to taking half.
    n = int(len(str(x)))
    n -= n % 2
    halfn = int(n // 2)

    # Assigns variables to the first half or second half of the original number
    a, b = splitnumber(x, n)
    c, d = splitnumber(y, n)

    # Recursively multiplies
    ac = multiply(a, c)
    bd = multiply(b, d)
    aplusbcplusd = multiply((a + b), (c + d))
    adbc = aplusbcplusd - ac - bd

    # Karatsuba formula to multiply
    answer = (ac * (10 ** n)) + (adbc * (10 ** (halfn))) + bd
    return answer


print(multiply(x, y))
