# Devin Thomas
# Jun 1, 2024


def main() -> None:
    user_num = int(input("Enter a whole number and we can sum all integers up to this value: "))
    if user_num >= 1:
        print(f"The total of 1-{user_num} = {sum_up_to(user_num)}")


def sum_up_to(last_number):
    result = last_number / 2
    sum = last_number + 1
    return int(sum * result)


if __name__ == '__main__':
    main()
