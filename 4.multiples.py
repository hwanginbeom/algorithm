"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
#
# def d(n):
#     return n + sum([int(x) for x in str(n)])
# # str 을 91 이라고 들어오면 9 랑 1 이 들어온다.

sum = 0

for i in range(1, 1000):
    if 3 * i < 1000:
        sum = sum + (3 * i)
    if 5 * i < 1000:
        sum = sum + (5 * i)
    if 15 * i < 1000:
        sum = sum - (15 * i)

print(sum)



# res = [n for n in range(5000) if n not in sub]
# sum(res)

