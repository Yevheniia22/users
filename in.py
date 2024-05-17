import tkinter as tk
from tkinter import messagebox

def calculate_balance():
    initial_balance = float(initial_balance_entry.get())
    annual_interest_rate = float(annual_interest_rate_entry.get())
    years = int(years_entry.get())

    if initial_balance <= 0 or annual_interest_rate <= 0 or years <= 0:
        messagebox.showerror("Помилка", "Введено некоректні дані. Перевірте, що всі значення є додатніми числами.")
        return

    balance = initial_balance
    for year in range(1, years + 1):
        interest = balance * (annual_interest_rate / 100)
        balance += interest

    result_label.config(text=f"Сума на рахунку через {years} років буде: {balance:.2f}")

# Створення вікна
root = tk.Tk()
root.title("Калькулятор зростання суми на рахунку")

# Створення елементів у вікні
initial_balance_label = tk.Label(root, text="Початкова сума на рахунку:")
initial_balance_label.grid(row=0, column=0, padx=10, pady=10)

initial_balance_entry = tk.Entry(root)
initial_balance_entry.grid(row=0, column=1, padx=10, pady=10)

annual_interest_rate_label = tk.Label(root, text="Річний відсоток (%):")
annual_interest_rate_label.grid(row=1, column=0, padx=10, pady=10)

annual_interest_rate_entry = tk.Entry(root)
annual_interest_rate_entry.grid(row=1, column=1, padx=10, pady=10)

years_label = tk.Label(root, text="Кількість років:")
years_label.grid(row=2, column=0, padx=10, pady=10)

years_entry = tk.Entry(root)
years_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Розрахувати", command=calculate_balance)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
