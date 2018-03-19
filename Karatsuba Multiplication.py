x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

def splitnumber(number, n):
    '''Takes a number and splits it in half by digits'''
    n1 = number // (10 ** (n // 2))
    n2 = number % (10 ** (n // 2))
    return n1, n2


def multiply(x, y):
    '''Karatsuba multiplication by recursion'''

    # base case
    if x < 10 or y < 10:
        return x * y

    n = int(len(str(x)))
    # Removes a 'digit' if digits are odd prior to taking half.
    # Why does this make it work?! Shouldn't using // effectively do the same thing?
    # It looks like a, b, c, d are the same values with and without this line of code
    # But with n -= n % 2 the answers come out correct?!
    n -= n % 2
    halfn = int(n // 2)

    a, b = splitnumber(x, n)
    c, d = splitnumber(y, n)

    ac = multiply(a, c)
    bd = multiply(b, d)
    aplusbcplusd = multiply((a + b), (c + d))
    adbc = aplusbcplusd - ac - bd

    answer = (ac * (10 ** n)) + (adbc * (10 ** (halfn))) + bd
    return answer


print(multiply(x, y))
