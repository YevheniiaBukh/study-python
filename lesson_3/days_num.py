days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = input("Enter the number of the day (1-7):")

if 1 <= int(day) <= 7:
   print(days[int(day) - 1])
else:
    print("Wrong input")