import tkinter as tk
from tkinter import messagebox

# Expanded list of stock options
STOCK_OPTIONS = {
    "Apple": "AAPL",
    "Google": "GOOGL",
    "Tesla": "TSLA",
    "Airtel": "AIRTEL",
    "Jio": "JIO",
    "Infosys": "INFY",
    "TCS": "TCS",
    "Reliance": "RELIANCE",
    "Microsoft": "MSFT",
    "Amazon": "AMZN"
}

portfolio = {}

def add_or_modify_stock():
    selected = stock_var.get()
    symbol = STOCK_OPTIONS.get(selected)
    shares = entry_shares.get()
    price_input = entry_price.get()

    if not symbol or not shares.isdigit() or not price_input.replace(".", "", 1).isdigit():
        messagebox.showerror("Error", "Invalid stock, number of shares, or price.")
        return

    shares = int(shares)
    price = float(price_input)

    portfolio[symbol] = {"shares": shares, "price": price}
    update_portfolio()

def remove_stock():
    selected = stock_var.get()
    symbol = STOCK_OPTIONS.get(selected)
    if symbol in portfolio:
        del portfolio[symbol]
        update_portfolio()
    else:
        messagebox.showwarning("Warning", "Stock not found in portfolio.")

def update_portfolio():
    output.delete(1.0, tk.END)
    total_value = 0
    total_shares = 0

    output.insert(tk.END, "📊 Current Portfolio Status:\n\n")
    for stock_name, symbol in STOCK_OPTIONS.items():
        if symbol in portfolio:
            shares = portfolio[symbol]["shares"]
            price = portfolio[symbol]["price"]
            value = shares * price
            output.insert(tk.END, f"{stock_name} ({symbol}): {shares} shares @ ${price:.2f} = ${value:.2f}\n")
            total_value += value
            total_shares += shares
        else:
            output.insert(tk.END, f"{stock_name} ({symbol}): 0 shares\n")

    output.insert(tk.END, "\n" + "-"*40 + "\n")
    output.insert(tk.END, f"📈 Total Shares Owned: {total_shares}\n")
    output.insert(tk.END, f"💰 Total Portfolio Value: ${total_value:.2f}\n")

# GUI setup
window = tk.Tk()
window.title("Stock Portfolio Tracker")

tk.Label(window, text="Select Stock:").pack()
stock_var = tk.StringVar(value=list(STOCK_OPTIONS.keys())[0])
tk.OptionMenu(window, stock_var, *STOCK_OPTIONS.keys()).pack(pady=5)

tk.Label(window, text="Enter Number of Shares:").pack()
entry_shares = tk.Entry(window)
entry_shares.pack(pady=5)

tk.Label(window, text="Enter Price per Share:").pack()
entry_price = tk.Entry(window)
entry_price.pack(pady=5)

tk.Button(window, text="Add/Update Stock", command=add_or_modify_stock).pack(pady=5)
tk.Button(window, text="Remove Stock", command=remove_stock).pack(pady=5)

output = tk.Text(window, height=22, width=60)
output.pack(pady=10)

update_portfolio()

window.mainloop()
