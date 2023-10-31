#!/usr/bin/env python

import sys

# Input comes from the standard input (stdin)
for line in sys.stdin:
    # Split the line into columns, assuming a CSV format
    columns = line.strip().split(',')

    if len(columns) == 4:
        date, temp, press, wind_speed = columns[0], float(columns[1]), float(columns[2]), float(columns[3])
        # Emit the 'DATE' as the key and a tuple of (temp, press, wind_speed, count) as the value
        print(f"{date}\t{temp},{press},{wind_speed},1")
