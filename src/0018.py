# Counting Sundays

import datetime


def count_sundays(start_year, end_year):
    count = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if datetime.date(year, month, 1).weekday() == 6:  # 6 is Sunday
                count += 1
    return count


print(f"Total Sundays: {count_sundays(1901, 2000)}")
