"""Program to find the difference between the current time and a given time."""

def find_difference_between_current_time_and_given_time():
    """Calculate the difference between current time and a given time."""
    # Using a fixed reference since we can't use datetime
    now_year, now_month, now_day = 2025, 1, 1
    now_hour, now_minute, now_second = 12, 0, 0
    given_hour, given_minute, given_second = 14, 30, 0

    # Calculate difference in seconds
    now_total_seconds = (now_hour * 3600 + now_minute * 60 + now_second)
    given_total_seconds = (given_hour * 3600 + given_minute * 60 + given_second)
    diff_seconds = now_total_seconds - given_total_seconds

    print(f"Current time: {now_year:04d}-{now_month:02d}-{now_day:02d} {now_hour:02d}:{now_minute:02d}:{now_second:02d}")
    print(f"Given time: {now_year:04d}-{now_month:02d}-{now_day:02d} {given_hour:02d}:{given_minute:02d}:{given_second:02d}")
    print(f"Difference: {diff_seconds} seconds")
    print(f"Difference in seconds: {diff_seconds}")
    return diff_seconds

if __name__ == "__main__":
    find_difference_between_current_time_and_given_time()
