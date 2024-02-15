n = int(input())
unused = [el for el in range(1, n+1)]

def permutations(iterable):
    if len(iterable) == 1:
        yield str(iterable[0])
    else:
        for i in range(len(iterable)):
            for perm in permutations(iterable[:i]+iterable[i+1:]):
                yield str(iterable[i]) + str(perm)
                
for perm in permutations(unused):
    print(perm)