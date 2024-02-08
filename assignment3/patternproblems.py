class PatternProblems:
    """
    A class that contains methods to print various number patterns.
    """

    def print_pattern1(self, n):
        """
        Prints a number pattern where each line contains the number repeated 'i' times.

        Args:
            n (int): The number of lines to print.

        Example:
            >>> pattern = PatternProblems()
            >>> pattern.print_pattern1(5)
            1
            22
            333
            4444
            55555
        """
        for i in range(n+1):
            char = str(i)
            print(char * i)

    def print_pattern2(self, n):
        """
        Prints a number pattern where each line contains the number repeated 'n-i' times.

        Args:
            n (int): The number of lines to print.

        Example:
            >>> pattern = PatternProblems()
            >>> pattern.print_pattern2(5)
            0
            11
            222
            3333
            44444
        """
        for i in range(n):
            char = str(i)
            print(char * (n-i))

    def print_pattern3(self, n):
        """
        Prints a number pattern where each line contains the number repeated 'i' times, with leading spaces.

        Args:
            n (int): The number of lines to print.

        Example:
            >>> pattern = PatternProblems()
            >>> pattern.print_pattern3(5)
                1
               22
              333
             4444
            55555
        """
        for i in range(n+1):
            char = str(i)
            print(' ' * (n-i) + char * i)

    def print_pattern4(self, n):
        """
        Prints a number pattern where each line contains numbers from 1 to 'i'.

        Args:
            n (int): The number of lines to print.

        Example:
            >>> pattern = PatternProblems()
            >>> pattern.print_pattern4(5)
            1
            12
            123
            1234
            12345
        """
        for i in range(1, n+1):
            print(''.join(map(str, range(1, i+1))))

    def print_pattern5(self, n):
        """
        Prints a pattern of alphabets up to the given number 'n'.

        Parameters:
        - n (int): The number of alphabets to print.

        Returns:
        None
        """
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(n+1):
            print(alphabet[:i+1])
