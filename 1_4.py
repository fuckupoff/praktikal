from collections import Counter

def count_it(sequence):
        return dict(Counter(map(int, sequence)).most_common(3))

print(count_it("2547545085240407022466426"))
