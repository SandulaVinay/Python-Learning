# ------------------------------
# ☕ COFFEE MACHINE SIMULATION ☕
# ------------------------------

# 🔧 Initial Resources (in ml or grams)
total_milk = 1000       # Total milk available
total_water = 1000      # Total water available
total_coffee = 750      # Total coffee available
total_money = 0         # Total earnings (in Rs.)

# 📋 Coffee Menu Dictionary with Recipes and Prices
coffee_menu = {
    "latte": {
        "milk_required": 200,
        "water_required": 200,
        "coffee_required": 100,
        "cost": 20
    },
    "espresso": {
        "milk_required": 250,
        "water_required": 150,
        "coffee_required": 50,
        "cost": 25
    },
    "cappuccino": {
        "milk_required": 200,
        "water_required": 200,
        "coffee_required": 100,
        "cost": 30
    }
}

# ☕ Function to Process Drink Orders
def process_order(selected_drink, payment_amount):
    global total_milk, total_water, total_coffee, total_money

    drink_details = coffee_menu[selected_drink]
    payment_amount = int(payment_amount)

    if (drink_details["milk_required"] <= total_milk and
        drink_details["water_required"] <= total_water and
        drink_details["coffee_required"] <= total_coffee):

        if payment_amount >= drink_details["cost"]:
            change = payment_amount - drink_details["cost"]

            # Deduct used ingredients
            total_milk -= drink_details["milk_required"]
            total_water -= drink_details["water_required"]
            total_coffee -= drink_details["coffee_required"]
            total_money += drink_details["cost"]

            print(f"\n✅ Please enjoy your {selected_drink}.")
            print(f"💰 Change: {change} rs\n")
        else:
            print(f"\n❌ Insufficient money!")
            print(f"➡️ Cost of the drink: {drink_details['cost']} rs")
            print(f"➡️ Amount you gave: {payment_amount} rs\n")
    else:
        print("\n❌ Insufficient ingredients to make the drink.\n")

# 👤 User Interaction Loop
def start_coffee_machine():
    while True:
        user_selection = input("🔸 Enter your drink (latte/espresso/cappuccino) or type 'admin': ").lower()

        # Admin Mode
        if user_selection == "admin":
            admin_command = input("🔧 Type 'report' to check resources or 'off' to stop the machine: ").lower()
            if admin_command == "report":
                print(f"\n📊 RESOURCE REPORT")
                print(f"Milk: {total_milk} ml")
                print(f"Water: {total_water} ml")
                print(f"Coffee: {total_coffee} g")
                print(f"Money Collected: {total_money} rs\n")
            elif admin_command == "off":
                print("\n🔌 Turning off machine. Goodbye!\n")
                break
            else:
                print("\n❗ Invalid admin command.\n")

        # Customer Mode
        elif user_selection in coffee_menu:
            drink_cost = coffee_menu[user_selection]["cost"]
            print(f"\n💡 {user_selection.capitalize()} costs {drink_cost} rs.")
            user_payment = input("💵 Please enter the amount you're paying: ")
            process_order(user_selection, user_payment)

        # Invalid Entry
        else:
            print("\n❗ Invalid drink selection. Try: latte, espresso, or cappuccino.\n")

# ▶️ Program Start
start_coffee_machine()
