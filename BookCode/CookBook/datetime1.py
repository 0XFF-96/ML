from datetime import datetime, date, timedelta

import calendar 

def get_month_range(start_date=None):

    if start_date is None:
        start_date = date.today().replace(day=1)
        _, dasy_in_month = calendar.monthrange(start_date.year, start_date.month)
        end_date = start_date + timedelta(days=days_in_month)

        return (start_date, end_date)


