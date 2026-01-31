import datetime

now = datetime.datetime.now()
today_date = datetime.date.today()

print(today_date)
print(now)

formatted_date = now.strftime("%y/%m/%d %H:%M:%S %p")
print(formatted_date)
