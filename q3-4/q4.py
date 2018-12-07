fname = "input.txt"

with open(fname) as f:
    content = f.readlines()
    content = [x.rstrip() for x in content]

    number_of_2 = 0
    number_of_3 = 0

    for index, first in enumerate(content):
        for second in content[index:]:
            words = zip(first, second)
            if len([c for c, d in words if c != d]) == 1:
                print(f"{first} - {second}")


