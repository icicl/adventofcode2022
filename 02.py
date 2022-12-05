import aoc

d = aoc.load(2,func=lambda x:x[::2])

pts_a = {'AX': 4, 'AY': 8, 'AZ': 3,
         'BX': 1, 'BY': 5, 'BZ': 9,
         'CX': 7, 'CY': 2, 'CZ': 6}

pts_b = {'AX': 3, 'AY': 4, 'AZ': 8,
         'BX': 1, 'BY': 5, 'BZ': 9,
         'CX': 2, 'CY': 6, 'CZ': 7}

print(sum(pts_a[i] for i in d))
print(sum(pts_b[i] for i in d))


