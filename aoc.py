import requests, os

cookie = ""
year = "2022"
def load(day, delimiters=' ', raw=False, func=lambda x:process(x, delimiters)):
    if not os.path.exists(str(day).zfill(2) + ".txt"):
        r = requests.get("https://adventofcode.com/" + year + "/day/" + str(day) + "/input", headers = {"Cookie": "session=" + cookie})
        if r.status_code != 200:
            print("Input could not be retrieved.")
            return []
        with open(str(day).zfill(2) + ".txt", "w+") as f:
            f.write(inp := r.text)
    else:
        with open(str(day).zfill(2) + ".txt") as f:
            inp = f.read()
    if raw:return inp
    inp = [func(line) for line in inp.split("\n")[:-1]]
    return inp

def pi(arr):
    return arr[0] if len(arr) == 1 else arr[0] * pi(arr[1:])

def process(line, whitespace):
    if len(line) == 0:
        return ''
    for char in whitespace[1:]:
        line = line.replace(char, whitespace[0])
    while 2*(whitespace[0]) in line:
        line = line.replace(2*(whitespace[0]), whitespace[0])
    r = [int(w) if w.isdigit() or (w[0]=='-' and w[1:].isdigit()) else w for w in line.split(whitespace[0])]
    if len(r) == 1:
        return r[0]
    return r

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = "abcdefghijklmnopqrstuvwxyz"
