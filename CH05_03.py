def calculate_min_insurance(replacement_cost):
    """Calculate the minimum insurance amount (80% of the replacement cost)."""
    return replacement_cost * 0.80

def main():
    # Get user input
    try:
        replacement_cost = float(input("Enter the replacement cost of the building: $"))
        
        # Calculate minimum insurance
        min_insurance = calculate_min_insurance(replacement_cost)
        
        # Display the result
        print(f"The minimum amount of insurance you should buy is: ${min_insurance:.2f}")
        
    except ValueError:
        print("Please enter a valid numeric value.")

if __name__ == "__main__":
    main()
