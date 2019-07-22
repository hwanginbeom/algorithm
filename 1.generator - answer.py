def d(n):
    return n + sum([int(x) for x in str(n)])

sub = [d(i) for i in range(5000)]
res = [n for n in range(5000) if n not in sub]
print(sum(res))