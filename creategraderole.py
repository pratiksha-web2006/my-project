# Time of Day Message

time = int(input("Enter current hour (0-23): "))

if time >= 5 and time < 12:
    print("Good Morning!")
elif time >= 12 and time < 17:
    print("Good Afternoon!")
elif time >= 17 and time < 21:
    print("Good Evening!")
elif time >= 0 and time < 24:
    print("Good Night!")
else:
    print("Invalid time!")
