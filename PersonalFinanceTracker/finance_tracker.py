import pandas as pd
import matplotlib.pyplot as plt
import csv
from collections import defaultdict

def add_transaction(date, category, amount, description=""):
    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Transaction added successfully!")

def view_transactions():
    print("Date        | Category   | Amount  | Description")
    print("-" * 40)
    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]:<12} | {row[1]:<10} | ${row[2]:<7} | {row[3]}")

def summarize_by_category():
    category_totals = defaultdict(float)
    
    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            category = row[1]
            amount = float(row[2])
            category_totals[category] += amount

    print("Category    | Total Amount")
    print("-" * 25)
    for category, total in category_totals.items():
        print(f"{category:<10} | ${total:.2f}")

def plot_spending_by_category():
    data = pd.read_csv("expenses.csv", names=["Date", "Category", "Amount", "Description"])
    category_totals = data.groupby("Category")["Amount"].sum()
    category_totals.plot(kind="bar", title="Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.show()

def plot_monthly_spending():
    data = pd.read_csv("expenses.csv", names=["Date", "Category", "Amount", "Description"])
    data["Date"] = pd.to_datetime(data["Date"])
    data["Month"] = data["Date"].dt.to_period("M")
    monthly_totals = data.groupby("Month")["Amount"].sum()
    monthly_totals.plot(kind="line", title="Monthly Spending Over Time")
    plt.xlabel("Month")
    plt.ylabel("Total Amount")
    plt.show()

def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add a Transaction")
        print("2. View All Transactions")
        print("3. Summarize by Category")
        print("4. Plot Spending by Category")
        print("5. Plot Monthly Spending Over Time")
        print("6. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (e.g., Food, Rent): ")
            amount = input("Enter amount: ")
            description = input("Enter description (optional): ")
            add_transaction(date, category, float(amount), description)
        
        elif choice == "2":
            view_transactions()
        
        elif choice == "3":
            summarize_by_category()
        
        elif choice == "4":
            plot_spending_by_category()
        
        elif choice == "5":
            plot_monthly_spending()
        
        elif choice == "6":
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
