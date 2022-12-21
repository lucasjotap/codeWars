# if number is even then number = number/2
# if number is odd then number = 3*number+1

def hotpo(n):
    """Defining function that lets you know
    how many times a number needs processing to reach value 1."""
    countEven = 0
    countOdd = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            if n != 1:
                countEven = 1 + countEven
                continue
        else:
            n = 3 * n + 1
            if n != 1: 
                countOdd = 1 + countOdd
                continue
    return countEven + countOdd

print(hotpo(1))
print(hotpo(7))


# def hotpo(n):
#     cnt = 0
#     while n != 1:
#         n = 3 * n + 1 if n % 2 else n / 2
#         cnt += 1
#     return cnt