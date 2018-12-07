
import numpy as np
from tqdm import tqdm

fname = "input.txt"


def mask(piece):
    mask = np.zeros((fabric_x, fabric_y))
    for x in range(piece["x_offset"], piece["x_offset"] + piece["x_length"]):
        for y in range(piece["y_offset"], piece["y_offset"] + piece["y_length"]):
            mask[x, y] = True
    return mask


with open(fname) as f:
    content = f.readlines()
    content = [x.rstrip() for x in content]
    new_content = []

    fabric_x = 0
    fabric_y = 0

    for i in content:
        i = i.replace('#', '')
        i = i.replace(' @ ', ';')
        i = i.replace(',', ';')
        i = i.replace(': ', ';')
        i = i.replace('x', ';')
        number, x_pos, y_pos, x_length, y_length = i.split(';')

        fabric_x = max(int(x_pos) + int(x_length), int(fabric_x))
        fabric_y = max(int(y_pos) + int(y_length), int(fabric_y))

        new_content.append({"number": int(number), "x_offset": int(x_pos), "x_length": int(x_length),
                            "y_offset": int(y_pos), "y_length": int(y_length)})

inches_squared = 0
fabric = np.zeros((fabric_x, fabric_y))
for k in tqdm(new_content):
    mask_k = mask(k)
    fabric = fabric + mask_k

inches_squared += len(fabric[fabric > 1])

print(inches_squared)




