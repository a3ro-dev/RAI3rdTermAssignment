
# try:
#     lastReading = float(input("Enter the last reading: "))
#     firstReading = float(input("Enter the first reading: "))
#     rate = float(input("Enter the rate for rupee/unit: "))
#     if lastReading < firstReading:
#         raise ValueError("Last reading cannot be less than the first reading.")
#     if lastReading == firstReading:
#         raise ValueError("Last reading cannot be equal to the first reading.")
#     if lastReading > firstReading:
#         difference = lastReading - firstReading
#         print(f"Difference: {difference} units")
#         amount = difference * rate
#         print(f"Amount: {amount}Rs.")
#     else:
#         print("Invalid readings. Please check the values entered.")
# except ZeroDivisionError:
#     print("Rate cannot be zero.")   
# except ValueError as e:
#     print(e)

# # ------------------------------------------------------------------------------------------------------------------------

# salary = int(input("Enter the salary: "))
# yearOfService = int(input("Enter the year of service: "))
# if salary < 0:
#     print("Salary cannot be negative.")
# elif salary == 0:
#     print("Salary cannot be zero.")
# elif salary > 0:
#     if yearOfService < 0:
#         print("Year of service cannot be negative.")
#     elif yearOfService == 0:
#         print("Year of service cannot be zero.")
#     elif yearOfService >= 5:
#         print("You are eligible for a bonus.")
#         print("Bonus: 5% of salary")
#         print("Bonus amount: ", (salary * 0.05))

# ----------------------------------------------------------------------------------------------------------------------------

ls = [1,8,7,2,21,15]
ascending = sorted(ls)
print(ascending)
reverse = ls[::-1]
print(reverse)
ls.append(8)
ls.insert(19, 3)
ls.remove(15)
print(ls)
