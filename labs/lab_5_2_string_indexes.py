# Devin Thomas
# Jun 1, 2024


def main() -> None:
    company_name: str = "Campbell's"
    letter: str = company_name[0]
    print(letter)

    company_name = "Alamo Colleges"
    print(company_name[company_name.index("g")])  # programmatically find "g" and print it


if __name__ == '__main__':
    main()
