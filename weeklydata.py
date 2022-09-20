from time import timezone
import pandas as pd
from pytrends.request import TrendReq
from datetime import timedelta, date
import csv
pytrend = TrendReq(hl="en-US", tz=360)
# Get Google Keyword Suggestions
keyword = ['bitcoin']


def weekly(year):
     data = []
     start_date =  date(year, month=1, day=1)
     end_date = date(year, month=12, day=31)
     timeframe = str(start_date) + ' ' + str(end_date) 

     pytrend.build_payload(keyword, timeframe=timeframe)

     df_monthly = pytrend.interest_over_time()

     x = df_monthly.head(10000)
     data.append(x)
     with open('weekly.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
     


x = 2015
while x < 2023:
    weekly(x)
    x = x + 1
