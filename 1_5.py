def sieve(lst):
    return tuple(sorted(set(lst), reverse=True))

print(sieve([3, 5, 3, 8, 1, 7, 7, 1, 4, 9, 2, 2]))