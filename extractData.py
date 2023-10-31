import pandas as pd
from datetime import datetime
import os

files = os.listdir('downloads')
files = [f'downloads/{file}' for file in files]
dates = []
temps = []
press = []
winds = []

for file_path in files:
    with open(file_path, 'r', encoding='UTF-8') as file:
        content = file.readlines()
    for l in content:
        date = l[15:23]
        day = int(date[6:])
        month = int(date[4:6])
        year = int(date[:4])
        dates.append(datetime(year, month, day))

        wind = l[65:69]
        wind_corrected = float(wind) / 10
        winds.append(wind_corrected)

        pres = l[99:104]
        pres_corrected = float(pres) / 10
        press.append(pres_corrected)

        temp = l[87:92]
        if temp[0] == '+':
            temp_corrected = float(temp[1:]) / 10
        else:
            temp_corrected = float(temp[1:]) / (-10)
        temps.append(temp_corrected)

data = {
    "DATE": dates,
    "TEMP": temps,
    "PRESS": press,
    "WIND_SPEED": winds
}
df = pd.DataFrame(data)
condition1 = (df['TEMP'] > 99.9)
df.loc[condition1, "TEMP"] = None
condition2 = (df['PRESS'] == 9999.9)
df.loc[condition2, "PRESS"] = None
condition3 = (df['WIND_SPEED'] == 999.9)
df.loc[condition3, "WIND_SPEED"] = None
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
print(df.tail(10))
df.to_csv('data.csv', index=False)