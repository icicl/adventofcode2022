import aoc

def val(code):
    if code < 96: return code - 38
    return code - 96

d = aoc.load(3,raw=False)

print(sum(val(ord((set(i[:len(i)//2])&set(i[len(i)//2:])).pop())) for i in d))
print(sum(val(ord((set(d[i])&set(d[i+1])&set(d[i+2])).pop())) for i in range(0,len(d), 3)))

