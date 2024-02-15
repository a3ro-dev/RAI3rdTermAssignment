class PatternProblems:
    """
    A class that contains methods to print various number patterns.
    """

    @staticmethod
    def normalAsterickRightAngledTriangle(n):
        for i in range(n):
            print(i*"*")

    @staticmethod
    def normalCharacterRightAngledTriangle(n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65+j), end="")
            print()

    @staticmethod
    def normalNumeralRightAngledTriangle(n):
        for i in range(n):
            char = str(i)
            print(char*i)

    @staticmethod
    def normalCountingRightAngledTriangle(n):
        counter = 0
        for i in range(n):
            for j in range(i+1):
                print(counter, end='')
                counter =+ 1
            print()

    @staticmethod
    def leftSidedNumericalRightAngledTriangle(n):
        for i in range(1, n+1):
            print(f"{' '*(n-i)}{''.join(str(j) for j in range(1, i+1))}")

    @staticmethod
    def upsideDownAstericksRightAngledTriangle(n):
        for i in range(n):
            print("*"*(n-i))
    
    @staticmethod
    def normalPyramid(n):
        for i in range(n):
            print(f"{' '*(n-i-1)}{'*'*(2*i+1)}")

PatternProblems.normalPyramid(6)