# Devin Thomas
# Jun 1, 2024


def main() -> None:
    choice = menu()
    if choice == "1":
        print("Connecting to an account agent...")
    elif choice == "2":
        message = input("Enter your message: ")
        print(f"Your message says: {message}")
        print("Message sent")
    elif choice == "3":
        print("Returning to main menu...")
    else:
        print(f"You chose {choice}\n")
        print("Invalid input\n")


def menu():
    print("Press 1 when you are ready to")
    print("connect to an account agent, or")
    print("press 2 to leave a message, or")
    return input("press 3 to return to the main menu: ")


if __name__ == '__main__':
    main()
