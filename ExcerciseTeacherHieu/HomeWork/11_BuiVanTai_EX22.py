def tower_of_hanoi(n, source, target, auxiliary):
    """
    Recursive function to solve Tower of Hanoi puzzle.

    Args:
        n (int): Number of disks.
        source (str): Name of the source rod.
        target (str): Name of the target rod.
        auxiliary (str): Name of the auxiliary rod.
    """
    if n > 0:
        # Move n-1 disks from source to auxiliary rod
        tower_of_hanoi(n - 1, source, auxiliary, target)

        print(f"Move disk {n} from {source} to {target}")

        tower_of_hanoi(n - 1, auxiliary, target, source)


while True:
    try:
        n = int(input("Enter the number of disks: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer greater than 0.")

print(f"Solving Tower of Hanoi with {n} disks...")
tower_of_hanoi(n, "Source", "Target", "Auxiliary")
print("Tower of Hanoi puzzle solved!")
