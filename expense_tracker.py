import json
import datetime

FILE_NAME = "expenses.json"

# Load or initialize data
def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Add a new expense
def add_expense():
    try:
        amount = float(input("Enter amount spent: ₹"))
        category = input("Enter category (Food, Travel, Bills, etc.): ").capitalize()
        note = input("Enter short description: ")
        date = input("Enter date (YYYY-MM-DD) [leave blank for today]: ")
        if not date:
            date = str(datetime.date.today())
        
        expense = {
            "amount": amount,
            "category": category,
            "note": note,
            "date": date
        }

        data = load_data()
        data.append(expense)
        save_data(data)

        print("✅ Expense recorded successfully!\n")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.\n")

# View all expenses
def view_expenses():
    data = load_data()
    if not data:
        print("No expenses recorded yet.\n")
        return

    print("\n🧾 All Expenses:")
    for i, exp in enumerate(data, 1):
        print(f"{i}. ₹{exp['amount']} - {exp['category']} - {exp['note']} ({exp['date']})")
    print()

# Show total spending
def show_summary():
    data = load_data()
    total = sum(exp["amount"] for exp in data)
    print(f"\n📊 Total Expenses: ₹{total:.2f}")
    
    category_totals = {}
    for exp in data:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    print("📂 Breakdown by Category:")
    for cat, amt in category_totals.items():
        print(f"   - {cat}: ₹{amt:.2f}")
    print()

# Main menu
def main():
    while True:
        print("===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
