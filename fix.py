
# =====================================================
# DAY 5: FINAL PYTHON PROJECT
# Project Name: Personal Welcome and Profile System
# Description: Collects user information and displays
# a personalized profile with useful calculations.
# =====================================================

def display_header():
    """Display the application header."""
    print("\n" + "=" * 60)
    print("          PERSONAL WELCOME SYSTEM")
    print("=" * 60)


def get_user_information():
    """Collect and return information from the user."""
    print("\nPlease enter your details.")

    name = input("Enter your name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    while True:
        try:
            age = int(input("Enter your age: "))
            if 1 <= age <= 120:
                break
            print("Please enter an age between 1 and 120.")
        except ValueError:
            print("Please enter a valid whole number.")

    city = input("Enter your city: ").strip()
    course = input("Enter your course: ").strip()
    hobby = input("Enter your hobby: ").strip()
    goal = input("Enter your future goal: ").strip()

    return name, age, city, course, hobby, goal


def display_profile(details):
    """Display the personalized user profile."""
    name, age, city, course, hobby, goal = details

    print("\n" + "-" * 60)
    print("                 YOUR PROFILE")
    print("-" * 60)

    print(f"Welcome, {name}!")
    print(f"Age           : {age}")
    print(f"City          : {city}")
    print(f"Course        : {course}")
    print(f"Hobby         : {hobby}")
    print(f"Future Goal   : {goal}")

    print("\n--- Personalized Message ---")
    print(f"Hello {name}, welcome to Python programming!")

    if age < 18:
        print("Keep learning and exploring new skills.")
    elif age <= 25:
        print("Build your skills and work towards your dreams.")
    else:
        print("Keep growing and learning something new.")

    print(f"\nYour age after 5 years will be {age + 5}.")
    print(f"We wish you success in becoming a {goal}!")

    print("-" * 60)


def show_menu():
    """Display the main menu."""
    while True:
        display_header()
        print("1. Create Your Profile")
        print("2. About This Project")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            details = get_user_information()
            display_profile(details)

        elif choice == "2":
            print("\nAbout This Project")
            print("This project is created using Python.")
            print("Concepts used:")
            print("- Variables and data types")
            print("- User input and output")
            print("- f-strings")
            print("- Conditional statements")
            print("- Functions")
            print("- Exception handling")
            print("- Input validation")

        elif choice == "3":
            print("\nThank you for using this program!")
            print("Keep practicing Python. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

        input("\nPress Enter to return to the menu...")


# Start the application
if __name__ == "__main__":
    show_menu()
