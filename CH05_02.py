def calculate_state_tax(amount, state_tax_rate):
    """Calculate the state sales tax."""
    return amount * state_tax_rate

def calculate_county_tax(amount, county_tax_rate):
    """Calculate the county sales tax."""
    return amount * county_tax_rate

def calculate_total_tax(state_tax, county_tax):
    """Calculate the total sales tax."""
    return state_tax + county_tax

def main():
    # Get user input
    try:
        purchase_amount = float(input("Enter the purchase amount: "))
        state_tax_rate = float(input("Enter the state sales tax rate (as a decimal): "))
        county_tax_rate = float(input("Enter the county sales tax rate (as a decimal): "))
        
        # Calculate taxes
        state_tax = calculate_state_tax(purchase_amount, state_tax_rate)
        county_tax = calculate_county_tax(purchase_amount, county_tax_rate)
        total_tax = calculate_total_tax(state_tax, county_tax)
        
        # Display results
        print(f"\nPurchase Amount: ${purchase_amount:.2f}")
        print(f"State Sales Tax: ${state_tax:.2f}")
        print(f"County Sales Tax: ${county_tax:.2f}")
        print(f"Total Sales Tax: ${total_tax:.2f}")
        
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
