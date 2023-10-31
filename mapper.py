#!/usr/bin/env python

import sys

# Input comes from the standard input (stdin)
for line in sys.stdin:
    # Split the line into key and value
    columns = line.strip().split(',')
    try:
    # Split the values into temp, press, wind_speed, and count
        date, temp, press, wind_speed = columns[0], float(columns[1]), float(columns[2]), float(columns[3])
    except ValueError:
            # Handle lines with invalid data (e.g., non-numeric temperature)
            continue
    # Emit the key-value pair with the 'DATE' as the key and the rest as the value
    print(date + "," + str(temp) + "," + str(press) + "," + str(wind_speed))