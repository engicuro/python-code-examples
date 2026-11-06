"""Program to solve the Tower of Hanoi problem."""

def program_for_tower_of_hanoi():
    """Solve the Tower of Hanoi puzzle using recursion."""
    n = 3

    def hanoi(n, source, auxiliary, target):
        if n == 1:
            print(f"Move disk 1 from {source} to {target}")
            return 1
        moves = 0
        moves += hanoi(n - 1, source, target, auxiliary)
        print(f"Move disk {n} from {source} to {target}")
        moves += 1
        moves += hanoi(n - 1, auxiliary, source, target)
        return moves

    print(f"Tower of Hanoi with {n} disks:")
    total_moves = hanoi(n, 'A', 'B', 'C')
    print(f"\nTotal moves: {total_moves}")
    return total_moves

if __name__ == "__main__":
    program_for_tower_of_hanoi()
