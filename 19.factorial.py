def factorial(a):
    sum = 1
    for i in range(1,a+1):
        sum = sum * i
    return sum

print(factorial(5))


def fact(n):

    if n <= 1:

        return 1

    return n * fact(n - 1)

print(fact(10))
