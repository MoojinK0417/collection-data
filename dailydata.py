from time import timezone
from tkinter import N
import pandas as pd
from pytrends.request import TrendReq
from datetime import timedelta, date
import csv
pytrend = TrendReq(hl="en-US", tz=360)
# Get Google Keyword Suggestions
keyword = ['bitcoin']



def daily(year,month):
     
     data = []

     start_date =  date(year, month-1, day=1)
     end_date = date(year, month, day=1)
     timeframe = str(start_date) + ' ' + str(end_date) 

     pytrend.build_payload(keyword, timeframe=timeframe)

     df_monthly = pytrend.interest_over_time()

     x = df_monthly.head(1000000)
     data.append(x)
     with open('daily.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
     
        



z = 2015
y = 2

while z < 2023:

    while y < 13:
     daily(z,y)
     y = y + 1
    
    z = z + 1
    y = 2


