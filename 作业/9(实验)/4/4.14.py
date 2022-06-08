from datetime import datetime

now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
month = now.month
print(month)
if month == 12:
    print('12月')
