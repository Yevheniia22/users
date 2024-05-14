def calculate_growth(principal, interest_rate, years):
    if principal <= 0 or interest_rate <= 0 or years <= 0:
        return None, "Початкова сума, відсоткова ставка та кількість років повинні бути додатніми числами."

    amount = principal * ((1 + interest_rate / 100) ** years)
    return amount, None

def main():
    principal = float(input("Введіть початкову суму: "))
    interest_rate = float(input("Введіть річний відсоток (%): "))
    years = int(input("Введіть кількість років: "))

    amount, error = calculate_growth(principal, interest_rate, years)

    if error:
        print(error)
    else:
        print(f"Сума на рахунку через {years} років складе {amount:.2f}.")

if __name__ == "__main__":
    main()
