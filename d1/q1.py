
fname = "input.txt"

with open(fname) as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    total = 0
    for i in content:
        total += int(i)
    q1.py
    print(total)
