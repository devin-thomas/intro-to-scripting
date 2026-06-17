# Devin Thomas
# Jun 1, 2024


def main() -> None:
    age = int(input("Enter your age: "))
    favorite_color: str = input("Enter your favorite primary color: ")

    primary_colors = ["blue", "red", "yellow"]

    color_error = "Error: Color must be blue, red or yellow."
    age_error = "Error: Age must not be negative"

    if age < 0 and favorite_color.lower() not in primary_colors:
        print(age_error)
        print(color_error)
    elif age < 0 and favorite_color.lower() in primary_colors:
        print(age_error)
    elif age >= 0 and favorite_color.lower() not in primary_colors:
        print(color_error)
    else:
        print("Thank you for entering valid information.")


if __name__ == '__main__':
    main()
