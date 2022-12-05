import aoc

d = aoc.load(4,func=lambda x:[[int(i) for i in j.split('-')] for j in x.split(',')])

print(sum(any(i[j][0] <= i[1-j][0] and i[j][1] >= i[1-j][1] for j in [0,1]) for i in d))
print(sum(all(i[j][1] >= i[1-j][0] for j in [0,1]) for i in d))

