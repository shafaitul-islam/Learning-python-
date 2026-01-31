from datetime import datetime,timedelta
import pytz

today = datetime.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

now = datetime.today()
new_time = now + timedelta(hours=5, minutes=30)
print(today,tomorrow,yesterday)
print(now,new_time)

date1 = datetime(2025,12,25)
date2 = datetime(2026,1,31)
print(date2-date1)
dhaka_time = datetime.now(pytz.timezone("Asia/Dhaka"))
print(dhaka_time)
print(dhaka)

