##Devin Thomas
# Jun 1, 2024


def main() -> None:
    sales_tax_factor: float = 1.0825
    album_price: float = float(input("Enter the price of the album: "))
    headphones_price: float = float(input("Enter the price of the headphones: "))
    discount_price: float = album_price - 2.99

    total_price: float = (discount_price + headphones_price) * sales_tax_factor

    print(f"Total cost after discounts and tax: ${total_price:.2f}.")


if __name__ == '__main__':
    main()
