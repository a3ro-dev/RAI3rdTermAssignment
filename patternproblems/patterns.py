import threading
import os

class Patterns:
    def __init__(self, n):
        """
        Initialize the Patterns class with the number of rows for the patterns.
        """
        self.n = n

    def triangle(self):
        """
        Print a right-angled triangle pattern of '*' with height of n.
        """
        print(f"\nTriangle Pattern: A right-angled triangle of '*' with height of {self.n}.")
        for i in range(self.n):
            print("*" * (i+1))

    def pyramid(self):
        """
        Print a pyramid pattern of '*' with height of n.
        """
        print(f"\nPyramid Pattern: A pyramid of '*' with height of {self.n}.")
        for i in range(self.n):
            print(' ' * (self.n - i - 1) + '*' * (2 * i + 1))

    def numberPyramid(self):
        """
        Print a pyramid pattern of numbers with height of n.
        """
        print(f"\nNumber Pyramid Pattern: A pyramid of numbers with height of {self.n}.")
        for i in range(self.n):
            print(" " * (self.n - i - 1), end="")
            for j in range(i + 1):
                print(j + 1, end="")
            for j in range(i, 0, -1):
                print(j, end="")
            print()

def main():
    """
    Main function to run the program. It keeps running until the user chooses to exit.
    """
    try:
        n = int(input("Enter the size of the pattern: "))
        patterns = Patterns(n)

        while True:
            print("\n1. Triangle Pattern")
            print("2. Pyramid Pattern")
            print("3. Number Pyramid Pattern")
            print("4. Exit")

            choice = int(input("\nChoose the pattern you want to print: "))

            if choice == 1:
                threading.Thread(target=patterns.triangle).start()
            elif choice == 2:
                threading.Thread(target=patterns.pyramid).start()
            elif choice == 3:
                threading.Thread(target=patterns.numberPyramid).start()
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")

            input("\nPress Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()