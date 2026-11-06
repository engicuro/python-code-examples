"""Program to find yesterday's, today's, and tomorrow's date."""

def find_yesterdays_todays_and_tomorrows_date():
    """Find yesterday's, today's, and tomorrow's dates."""
    # Using a fixed reference date since we can't use datetime
    today_year, today_month, today_day = 2025, 1, 1

    # Calculate yesterday
    y, m, d = today_year, today_month, today_day - 1
    if d < 1:
        m -= 1
        if m < 1:
            m = 12
            y -= 1
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        d = days_in_month[m]
    yesterday = (y, m, d)

    # Calculate tomorrow
    y, m, d = today_year, today_month, today_day + 1
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if d > days_in_month[m]:
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1
    tomorrow = (y, m, d)

    print(f"Yesterday: {yesterday[0]:04d}-{yesterday[1]:02d}-{yesterday[2]:02d}")
    print(f"Today:     {today_year:04d}-{today_month:02d}-{today_day:02d}")
    print(f"Tomorrow:  {tomorrow[0]:04d}-{tomorrow[1]:02d}-{tomorrow[2]:02d}")

    return yesterday, (today_year, today_month, today_day), tomorrow

if __name__ == "__main__":
    find_yesterdays_todays_and_tomorrows_date()
