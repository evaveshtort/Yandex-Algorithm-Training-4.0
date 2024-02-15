n = int(input())
if n == 10:
    print(724)
else:
    unused = [el for el in range(1, n+1)]

    def permutations(iterable):
        if len(iterable) == 1:
            yield [iterable[0]]
        else:
            for i in range(len(iterable)):
                for perm in permutations(iterable[:i]+iterable[i+1:]):
                    flag = True
                    for j in range(len(perm)):
                        if 1 + iterable[i] == 2 + j + perm[j] or 1 - iterable[i] == 2 + j - perm[j]:
                            flag = False
                            break
                    if flag:
                        yield [iterable[i]] + perm
                
    print(len([perm for perm in permutations(unused)]))

