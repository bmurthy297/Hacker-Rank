# Calendar Module : https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
month, day, year = map(int, input().split())  

print(calendar.day_name[calendar.weekday(year, month, day)].upper())


# Alternative solution using datetime module
import datetime

month, day, year = map(int, input().split())
weekday = datetime.date(year, month, day).strftime('%A')
print(weekday.upper())