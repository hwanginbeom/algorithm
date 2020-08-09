def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)
    print(s)

    for i enumerate(answers):
        print(q)
        for i, v in enumerate(p):
            print("##")
            print(i,v)
            if a == v[q % len(v)]:
                s[i] += 1
                print(s)
    return [i + 1 for i, v in enumerate(s) if v == max(s)]

#answers=[1,2,3,4,5]
answers=[1,3,2,4,2]

print(solution(answers))