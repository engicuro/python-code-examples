"""Program to calculate the area of a circle given its radius."""

def find_area_of_a_circle():
    """Calculate the area of a circle."""
    import math
    radius = 5
    area = math.pi * radius ** 2

    print(f"Radius: {radius}")
    print(f"Area of circle: {area:.4f}")
    return area

if __name__ == "__main__":
    find_area_of_a_circle()
