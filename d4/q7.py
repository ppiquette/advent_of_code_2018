import pandas as pd
from operator import itemgetter

import re

fname = "input.txt"

with open(fname) as f:
    content = f.readlines()
    content = [x.rstrip() for x in content]

all_months = []
all_days = []
all_minutes = []
all_states = []
all_guard_numbers = []
df = pd.DataFrame()

for text in content:

    m = re.search('\[(.+?)\]', text)
    date, time = m.group(1).split(" ")
    _, month, day = date.split("-")
    _, minute = time.split(":")
    training_text = text.replace(m.group(0), '')

    state = ""
    guard_number = 0
    if training_text.find('falls asleep') != -1:
        state = "start"
    elif training_text.find('Guard') != -1:
        n = re.search('#(.+?) ', text)
        guard_number = int(n.group(1))
        state = ""
    elif training_text.find('wakes up') != -1:
        state = "stop"
    else:
        assert False, "Impossible"

    all_months.append(int(month))
    all_days.append(int(day))
    all_minutes.append(int(minute))
    all_guard_numbers.append(guard_number)
    all_states.append(state)

    df = pd.DataFrame({"month": all_months, "day": all_days, "minute": all_minutes,
                       "guard_number": all_guard_numbers, "state": all_states})

    df = df.sort_values(by=["month", "day", "minute"])

last_guard = []
last_guard_start = []
for index, i in df.iterrows():
    if i["guard_number"] != 0.0:
        last_guard = i["guard_number"]
    elif i["state"] == "start":
        df.at[index, "guard_number"] = last_guard
        last_guard_start = last_guard
    elif i["state"] == "stop":
        df.at[index, "guard_number"] = last_guard_start
    else:
        assert False, "Impossible"

unique_guards = df['guard_number'].unique()

sleep_time = []
for i in unique_guards:
    temp = df[(df['guard_number'] == i) & (df['state'] != "")]
    start_sleep = 0
    sum_sleep = 0
    for j in temp.iterrows():
        if start_sleep:
            sum_sleep += j[1]['minute'] - start_sleep
            start_sleep = 0
        else:
            start_sleep = j[1]['minute']
    sleep_time.append((i, sum_sleep))

print(max(sleep_time, key=itemgetter(1))[0])
print(df)
print(sleep_time)

