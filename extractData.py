from operator import index
import pandas as pd
from datetime import datetime
file_path = 'downloads/601010-99999-1980'
with open(file_path, 'r', encoding='UTF-8') as file:
    content = file.readlines()
dates=[]
temps=[]
press=[]
winds=[]
for l in content:
     date = l[15:23]
     day = int(date[6:])
     month = int(date[4:6])
     year = int(date[:4])
     dates.append(datetime(year,month,day))

     wind= l[65:69]
     wind_corrected = float(wind)/10
     winds.append(wind_corrected)   

     pres = l[99:104]
     pres_corrected = float(pres)/10
     press.append(pres_corrected)   

     temp = l[87:92]
     if temp[0] == '+':
         temp_corrected = float(temp[1:])/10
     else:
         temp_corrected = float(temp[1:])/(-10)
     temps.append(temp_corrected)

    


data= {
    "DATE": dates,
    "TEMP": temps,
    "PRESS": press,
    "WIND_SPEED": winds
}
df_1901=pd.DataFrame(data)
condition1=(df_1901['TEMP']==99.9)      
df_1901.loc[condition1,"TEMP"]=None
condition2=(df_1901['PRESS']==9999.9)      
df_1901.loc[condition2,"PRESS"]=None
condition3=(df_1901['WIND_SPEED']==999.9)
df_1901.loc[condition3,"WIND_SPEED"]=None
df_1901.dropna(inplace=True)
df_1901=df_1901.reset_index(drop=True)       
print(df_1901.tail())