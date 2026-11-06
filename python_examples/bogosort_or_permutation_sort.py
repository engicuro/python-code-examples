"""Program to implement BogoSort (permutation sort)."""

# Use a simple LCG-based pseudo-random number generator to avoid external imports
class _SimpleRNG:
    def __init__(self, seed=42):
        self.seed = seed

    def randint(self, a, b):
        self.seed = (self.seed * 1103515245 + 12345) % (2**31)
        return a + (self.seed % (b - a + 1))

_rng = _SimpleRNG()

def bogosort_or_permutation_sort():
    """Sort an array using BogoSort (inefficient but fun)."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]

    def is_sorted(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    def shuffle(a):
        n = len(a)
        for i in range(n - 1, 0, -1):
            j = _rng.randint(0, i)
            a[i], a[j] = a[j], a[i]

    def bogosort(arr):
        attempts = 0
        while not is_sorted(arr):
            shuffle(arr)
            attempts += 1
        return arr, attempts

    print(f"Original array: {arr}")
    sorted_arr, attempts = bogosort(arr.copy())
    print(f"Sorted array: {sorted_arr}")
    print(f"Number of shuffles: {attempts}")
    return sorted_arr

if __name__ == "__main__":
    bogosort_or_permutation_sort()
