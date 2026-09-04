# Function 1: Discount Calculator
def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

# Subukan ang discount function
shirt_price = calculate_discount(1000, 20)
shoes_price = calculate_discount(2500, 10)

print(f"Shirt Final Price: ₱{shirt_price}")
print(f"Shoes Final Price: ₱{shoes_price}")

def get_grade_status(average):
    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"

print(get_grade_status(85))
print(get_grade_status(60))