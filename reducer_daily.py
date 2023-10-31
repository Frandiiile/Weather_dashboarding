import sys

current_date = None
temp_total = 0.0
press_total = 0.0
wind_speed_total = 0.0
count = 0
temps_today = []
press_today = []
wind_today = []
# Input comes from the standard input (stdin)
for line in sys.stdin:
    columns = line.strip().split(',')
    if len(columns) == 4:
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
            temps_today.append(temp)
            press_today.append(press)
            wind_today.append(wind_speed)
            count += 1  # Increment the count for each valid line
        else:
            # If the 'DATE' changes, calculate the averages and emit the result
            if current_date:
                avg_temp = temp_total / count
                avg_press = press_total / count
                avg_wind_speed = wind_speed_total / count
                min_temp = min(temps_today) if temps_today else 0.0
                max_temp = max(temps_today) if temps_today else 0.0
                min_press = min(press_today) if press_today else 0.0
                max_press = max(press_today) if press_today else 0.0
                min_wind = min(wind_today) if wind_today else 0.0
                max_wind = max(wind_today) if wind_today else 0.0
                result_line = current_date + "," + str(avg_temp) + "," + str(avg_press) + "," + str(avg_wind_speed) + "," + str(min_temp) + "," + str(max_temp) + "," + str(min_press) + "," + str(max_press) + "," + str(min_wind) + "," + str(max_wind)
                print(result_line)
            current_date = date
            temps_today = []
            press_today = []
            wind_today = []

# Output the last 'DATE' with its averages
if current_date:
    avg_temp = temp_total / count
    avg_press = press_total / count
    avg_wind_speed = wind_speed_total / count
    min_temp = min(temps_today) if temps_today else 0.0
    max_temp = max(temps_today) if temps_today else 0.0
    min_press = min(press_today) if press_today else 0.0
    max_press = max(press_today) if press_today else 0.0
    min_wind = min(wind_today) if wind_today else 0.0
    max_wind = max(wind_today) if wind_today else 0.0
    result_line = current_date + "," + str(avg_temp) + "," + str(avg_press) + "," + str(avg_wind_speed) + "," + str(min_temp) + "," + str(max_temp) + "," + str(min_press) + "," + str(max_press) + "," + str(min_wind) + "," + str(max_wind)
    print(result_line)
