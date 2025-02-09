"Q2:"

string: str = str(input("Enter the string: "))
search: str = str(input("Enter the search string: "))
words = string.split()
if search in words:
    print("String Name Found")
else:
    print("String Name Not Found")