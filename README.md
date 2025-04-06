# Calculating Percentage Using Python

This Python script calculates the discount amount and the final price after applying a discount percentage to an original price. It prompts the user for the original price and discount percentage, performs the calculations, and displays the results in detail.

## Example Code

```python
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
```

## How It Works

1. The user is prompted to enter the original price and the discount percentage.
2. The `calculate_discount` function computes:
   - The discount amount.
   - The final price after applying the discount.
3. The results are displayed in a detailed format.

## Example Usage

```
Enter the original price in ZAR: 1000
Enter the discount percentage: 15

--- Discount Calculation Details ---
Original Price: ZAR 1000.00
Discount Percentage: 15.00%
Discount Amount: ZAR 150.00
Final Price after Discount: ZAR 850.00
```