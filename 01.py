import aoc

d = aoc.load(1,raw=True)[:-1]

m = [sum(int(j) for j in i.split('\n')) for i in d.split('\n\n')]

print(max(m))
print(sum(sorted(m)[-3:]))

