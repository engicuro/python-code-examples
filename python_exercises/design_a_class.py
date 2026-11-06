"""Design a Class - Exercise."""

class Student:
    """A simple Student class."""

    def __init__(self, name, age, grade):
        """Initialize a student with name, age, and grade."""
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        """Display student information."""
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def is_passing(self):
        """Check if the student is passing (grade >= 60)."""
        return self.grade >= 60

def design_a_class():
    """Demonstrate class design."""
    student1 = Student("Alice", 20, 85)
    student2 = Student("Bob", 22, 55)

    student1.display_info()
    print(f"Is passing: {student1.is_passing()}")

    student2.display_info()
    print(f"Is passing: {student2.is_passing()}")

if __name__ == "__main__":
    design_a_class()
