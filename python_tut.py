INR_to_USD = 0.012
INR_to_RUB = 1.03
INR_to_GBP = 0.0093

def convert_currency(amount, to_currency):
    if to_currency == "USD":
        return amount * INR_to_USD
    elif to_currency == "RUB":
        return amount * INR_to_RUB
    elif to_currency == "GBP":
        return amount * INR_to_GBP
    else:
        return None

def main():
    try:
        amount = float(input("Enter the amount in INR: "))
        to_currency = input("Enter the target currency (USD or RUB or GBP): ").upper()

        converted_amount = convert_currency(amount, to_currency)
        if converted_amount is not None:
            print(f"{amount:.2f} INR is equivalent to {converted_amount:.2f} {to_currency}.")
        else:
            print("Invalid target currency.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric amount.")

if __name__ == "__main__":
    main()