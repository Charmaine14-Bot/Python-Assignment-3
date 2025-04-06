def calculate_discount(price, discount_percentage):
    # Calculate the discount amount
    discount_amount = price * (discount_percentage / 100)
    # Calculate the final price after discount
    final_price = price - discount_amount
    return discount_amount, final_price

# Prompting the user for input
original_price = float(input("Enter the original price in ZAR: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the discount and final price
discount_amount, final_price = calculate_discount(original_price, discount_percentage)

# Printing the calculations in detail
print("\n--- Discount Calculation Details ---")
print(f"Original Price: ZAR {original_price:.2f}")
print(f"Discount Percentage: {discount_percentage:.2f}%")
print(f"Discount Amount: ZAR {discount_amount:.2f}")
print(f"Final Price after Discount: ZAR {final_price:.2f}")

