# 1. Main Data Structure (Alkansya)
account = {
    "owner": "Student",
    "balance": 1000.0,
    "history": []
}

# 2. Function para sa Deposit
def deposit(acc, amount):
    acc["balance"] += amount
    acc["history"].append(f"Deposited ₱{amount}")

# 3. Function para sa Withdraw
def withdraw(acc, amount):
    if acc["balance"] >= amount:
        acc["balance"] -= amount
        acc["history"].append(f"Withdrew ₱{amount}")
    else:
        print(f"\n⚠️ Cannot withdraw ₱{amount}: Insufficient funds!")

# 4. Function para sa Report
def display_summary(acc):
    print("\n--- BANK ACCOUNT SUMMARY ---")
    print(f"Owner: {acc['owner']}")
    print(f"Current Balance: ₱{acc['balance']}")

    print("\n--- TRANSACTION HISTORY ---")
    for item in acc["history"]:
        print(f"- {item}")


# --- Testing the Functions ---
deposit(account, 500)
withdraw(account, 200)
withdraw(account, 2000)  # Mag-e-error dahil kulang ang pera
display_summary(account)