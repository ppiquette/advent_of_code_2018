from collections import Counter

fname = "input.txt"

with open(fname) as f:
    content = f.readlines()
    content = [x.rstrip() for x in content]

    number_of_2 = 0
    number_of_3 = 0

    for i in content:
        counter = Counter(i)
        found2 = False
        found3 = False
        for key, value in dict(counter).items():
            if value == 2 and found2 is False:
                number_of_2 += 1
                found2 = True
            if value == 3 and found3 is False:
                number_of_3 += 1
                found3 = True

print(number_of_2)
print(number_of_3)
print(number_of_2*number_of_3)


