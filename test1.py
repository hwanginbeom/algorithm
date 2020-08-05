citations	=[3 ,0, 6, 1, 5]


def solution(citations):
    citations.sort(reverse=True)
    for i, n in enumerate(citations):
        print("##")
        print(i)
        print(n)
        if n <= i:
            return i
    return len(citations)

print(solution(citations))
