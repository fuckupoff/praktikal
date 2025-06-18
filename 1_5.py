def sieve(list):
    nums = set(list)
    nums = sorted(nums, reverse = True)
    return tuple(nums)
print(sieve([3, 5, 3, 8, 1, 7, 7, 1, 4, 9, 2, 2]))
