def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
    else:
        return price
    
    # Prompting the user for input
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Printing the final price
    if final_price == original_price:
        print(f"No discount applied. The original_price is: {final_price:.2f}")
    else:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
 
    