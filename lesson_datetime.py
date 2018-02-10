from datetime import datetime
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

print(now)
print(current_day)
print(current_month)
print(current_year)

# Дата в дургом формате rgrtrtrt
print('%s-%s-%s' % (now.month, now.day, now.year))
