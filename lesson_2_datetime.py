from datetime import datetime

now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print(now)

print(current_day)
print(current_month)
print(current_year)

print(now.hour)
print(now.minute)
print(now.second)

# Дата в дургом формате
print('%s-%s-%s' % (now.month, now.day, now.year))
print('%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
