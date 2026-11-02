while True:
    marks = int(input("Enter marks (0-100): "))

    if 0 <= marks <= 100:
        print("Valid Marks:", marks)
        break
    else:
        print("Invalid marks! Please enter marks between 0 and 100.")
