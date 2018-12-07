
import numpy as np
import pandas as pd
from tqdm import tqdm
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
for _, i in df.iterrows():
    if i["guard_number"] != 0:
        last_guard = i["guard_number"]
    elif i["state"] == "start":
        i["guard_number"] = last_guard
        last_guard_start = last_guard
    elif i["state"] == "stop":
        i["guard_number"] = last_guard_start
    else:
        assert False, "Impossible"

guard_sleep_time = np.zeros(df['guard_number'].max())
guard_sleep_start = np.zeros(df['guard_number'].max())
for _, i in df.iterrows():
    if i["state"] == "start":
        guard_sleep_start[i["guard_number"]] = i["minute"]
    if i["state"] == "stop":
        guard_sleep_time[i["guard_number"]] = i["minute"] - guard_sleep_start[i["guard_number"]]

print(df)
print(guard_sleep_time)

