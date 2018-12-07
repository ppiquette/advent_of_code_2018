
fname = "input.txt"

with open(fname) as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    frequency = 0
    all_frequencies = set([0])
    found_sync = False
    while found_sync is False:
        print("loop")
        for i in content:
            frequency += int(i)
            if frequency in all_frequencies:
                print(frequency)
                found_sync = True
                break
            else:
                all_frequencies.add(frequency)




