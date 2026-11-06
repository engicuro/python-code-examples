"""Program to create a lap timer."""

def create_a_lap_timer():
    """Create a simple lap timer that records lap times."""
    print("Lap Timer Demo")
    print("=" * 40)

    # Simulate lap times
    lap_times = [5.23, 10.87, 16.45, 22.10]
    start_time = time.time()

    for lap_num, elapsed in enumerate(lap_times, 1):
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed % 1) * 100)
        print(f"Lap {lap_num}: {minutes:02d}:{seconds:02d}.{milliseconds:02d}")

    print(f"\nTotal time: {elapsed:.2f} seconds")

if __name__ == "__main__":
    create_a_lap_timer()
