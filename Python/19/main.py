import datetime

start_date = datetime.date(1901, 1, 1)
end_date = datetime.date(2000, 12, 31)

sundays_on_first = 0

# Iterate over all the months in the 20th century
current_date = start_date
while current_date <= end_date:
    # Check if the first day of the month is a Sunday
    if current_date.day == 1 and current_date.weekday() == 6:
        sundays_on_first += 1
    # Move to the first day of the next month
    if current_date.month == 12:
        current_date = datetime.date(current_date.year + 1, 1, 1)
    else:
        current_date = datetime.date(current_date.year, current_date.month + 1, 1)

print(sundays_on_first)
