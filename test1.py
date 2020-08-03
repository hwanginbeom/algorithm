def solution(numbers):
    numbers = list(map(str, numbers))
    a=numbers.sort()
    print(a)
    print(numbers.sort())

    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

numbers=[3, 30, 34, 5, 9]
numbers = list(map(str, numbers))
numbers.sort(key=lambda  x: x , reverse=True)
print(numbers)
numbers.sort(key=lambda  x: x *2, reverse=True)
print(numbers)
numbers.sort(key=lambda  x: x *3, reverse=True)
print(numbers)
for i in numbers:
    print(i[0])


print(solution(numbers))