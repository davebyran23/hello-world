def calculate_meal_cost(meal_cost, tip_percent, tax_percent):
    # Calculate tip and tax amounts
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    
    # Calculate total cost
    total_cost = meal_cost + tip + tax
    
    return round(total_cost)

def main():
    # Get input from user
    meal_cost = float(input("Enter the cost of the meal: "))
    tip_percent = int(input("Enter the tip percentage: "))
    tax_percent = int(input("Enter the tax percentage: "))
    money = float(input("Enter the amount of money you have: "))
    
    # Calculate total cost
    total_cost = calculate_meal_cost(meal_cost, tip_percent, tax_percent)
    
    # Check if user can afford the meal
    if money >= total_cost:
        print(f"You can afford the meal! The total cost is ${total_cost}")
    else:
        print(f"You cannot afford the meal. The total cost is ${total_cost}")

if __name__ == "__main__":
    main() 