
# Day 3: Personalized Welcome Message
# Using Python f-strings

print("=" * 60)
print("             PERSONALIZED WELCOME SYSTEM")
print("=" * 60)

name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
course = input("Enter your course: ")
goal = input("Enter your career goal: ")

print("\n" + "*" * 60)
print(f"Hello, {name}! Welcome to Python Programming.")
print("*" * 60)

print(f"\nDear {name},")
print(f"We are happy to welcome you from {city}.")
print(f"You are currently {age} years old.")
print(f"You are studying {course}.")
print(f"Your career goal is to become a {goal}.")

print("\n--- Your Personalized Message ---")

if age < 18:
    print(f"{name}, keep learning and building your skills!")
elif age <= 25:
    print(f"{name}, this is a great time to develop your career!")
else:
    print(f"{name}, keep growing and achieving your goals!")

print(f"\nBest wishes for your future, {name}!")
print("Keep practicing Python every day.")
print("=" * 60)
