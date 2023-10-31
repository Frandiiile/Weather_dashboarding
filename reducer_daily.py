import sys

current_date = None
temp_total = 0.0
press_total = 0.0
wind_speed_total = 0.0
count = 0
temp_max = float('-inf')
temp_min = float('inf')
press_max = float('-inf')
press_min = float('inf')
wind_speed_max = float('-inf')
wind_speed_min = float('inf')

# Input comes from the standard input (stdin)
for line in sys.stdin:
    columns = line.strip().split(',')
    if len(columns) == 4:
        try:
            date, temp, press, wind_speed = columns[0], float(columns[1]), float(columns[2]), float(columns[3])
        except ValueError:
            # Handle lines with invalid data (e.g., non-numeric temperature)
            continue
        
        # If the current 'DATE' is the same as the previous one, accumulate the values
        if current_date == date:
            temp_total += temp
            press_total += press
            wind_speed_total += wind_speed
            count += 1  # Increment the count for each valid line

            # Track max and min values
            temp_max = max(temp_max, temp)
            temp_min = min(temp_min, temp)
            press_max = max(press_max, press)
            press_min = min(press_min, press)
            wind_speed_max = max(wind_speed_max, wind_speed)
            wind_speed_min = min(wind_speed_min, wind_speed)
        else:
            # If the 'DATE' changes, calculate the averages and emit the result
            if current_date:
                avg_temp = temp_total / count
                avg_press = press_total / count
                avg_wind_speed = wind_speed_total / count
                result_line = current_date + "," + str(avg_temp) + "," + str(avg_press) + "," + str(avg_wind_speed) + "," + str(temp_min) + "," + str(temp_max) + "," + str(press_min) + "," + str(press_max) + "," + str(wind_speed_min) + "," + str(wind_speed_max)
                print(result_line)
            current_date = date

# Output the last 'DATE' with its averages
if current_date:
    avg_temp = temp_total / count
    avg_press = press_total / count
    avg_wind_speed = wind_speed_total / count
    result_line = current_date + "," + str(avg_temp) + "," + str(avg_press) + "," + str(avg_wind_speed) + "," + str(temp_min) + "," + str(temp_max) + "," + str(press_min) + "," + str(press_max) + "," + str(wind_speed_min) + "," + str(wind_speed_max)
    print(result_line)