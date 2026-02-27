from datetime import datetime, timedelta
#1. Write a Python program to subtract five days from current date.
t = datetime.now()
ans = t - timedelta(days = 5)
print(ans)

#2. Write a Python program to print yesterday, today, tomorrow.
today = datetime.now().date()
yest = today - timedelta(days = 1)
tomr = today + timedelta(days=1)
print(today, yest, tomr)

#3. Write a Python program to drop microseconds from datetime.
now = datetime.now()
micr = now.replace(microsecond = 0)
print(micr)

#4. Write a Python program to calculate two date difference in seconds.
date1 = datetime(2026, 2, 28, 14, 30, 58)
date2 = datetime(2008, 8, 26, 4, 1, 23)
diff = date1 - date2
sec = diff.total_seconds()
print(sec)

