"""Program to convert time from 12-hour format to 24-hour format."""

def convert_time_from_12_hour_to_24_hour_format():
    """Convert time from 12-hour AM/PM format to 24-hour format."""
    test_times = ["02:30 PM", "11:45 AM", "12:00 PM", "12:00 AM", "07:15 PM"]

    def convert_12_to_24(time_str):
        parts = time_str.strip().split()
        if len(parts) != 2:
            return "Invalid format"
        time_part, period = parts
        period = period.upper()

        h_m = time_part.split(':')
        if len(h_m) != 2:
            return "Invalid format"
        hour = int(h_m[0])
        minute = h_m[1]

        if period == 'PM' and hour != 12:
            hour += 12
        elif period == 'AM' and hour == 12:
            hour = 0

        return f"{hour:02d}:{minute}"

    for t in test_times:
        result = convert_12_to_24(t)
        print(f"{t} -> {result}")

if __name__ == "__main__":
    convert_time_from_12_hour_to_24_hour_format()
