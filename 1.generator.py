"""
-----------------------------------------------------------------------------------------------------------------------
1. generator 알고리즘 (넥슨 알고리즘 테스트)

어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.

예를 들어

d(91) = 9 + 1 + 91 = 101

이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.

어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.

1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.

-----------------------------------------------------------------------------------------------------------------------
1.
1에서 5000까지의 값을 배열로 저장한 후 5000이 넘지 않는 제너레이터를 구한 후 하나씩 빼는 형태로 한 후
배열에 셀프 넘버만 남겨 놓는다. 그 후 배열을 하나씩 더한다.

2.1부터 차례대로 제너레이터를 구한 후 제너레이터 값이 아닐 경우에만 하나의 변수에 계속 더하는 식으로 한다.
    1.제너레이터를 구한다.
    2. 1000 / 100 / 10 / 1 단위로 나눠 몫으로 값을 하나씩 구한다.

start : 3시 50분
end : 5시 20 분
-----------------------------------------------------------------------------------------------------------------------
"""


def generator(range_val):
    generator_val = []
    sum = 0
    self_sum = 0

    for i in range(1,len(range_val)):
        if i >= 1000:
            thousand = int(i / 1000)
            hundred = int(i % 1000 / 100)
            ten = int(i % 1000 % 100 / 10)
            one = int(i % 10)
            if 5000 > thousand + hundred + ten + one + i:
                generator_val.append(thousand + hundred + ten + one + i)

        elif i >= 100:
            hundred = int(i / 100)
            ten = int(i % 100 / 10)
            one = int(i % 10)
            generator_val.append(hundred + ten + one + i)

        elif i >= 10:
            ten = int(i / 10)
            one = int(i % 10)
            generator_val.append(ten + one + i)

        else:
            generator_val.append(i + i)

        generator_val = list(set(generator_val))
    print(generator_val)

    for i in generator_val:
        range_val.remove(i)
    print(range_val)

    for i in range_val:
        self_sum = self_sum + i
    return self_sum

range_val = list(range(1 , 5000))

print(generator(range_val))

