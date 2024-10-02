def calculate_assessment_value(actual_value):
    """Calculate the assessment value (60% of actual value)."""
    return actual_value * 0.60

def calculate_property_tax(assessment_value):
    """Calculate the property tax ($0.72 for each $100 of assessment value)."""
    tax_per_100 = 0.72
    return (assessment_value / 100) * tax_per_100

def main():
   
    try:
        actual_value = float(input("Enter the actual value of the property: $"))
        
        # Calculate assessment value and property tax
        assessment_value = calculate_assessment_value(actual_value)
        property_tax = calculate_property_tax(assessment_value)
        
        # Display results
        print(f"\nAssessment Value: ${assessment_value:.2f}")
        print(f"Property Tax: ${property_tax:.2f}")
        
    except ValueError:
        print("Please enter a valid numeric value.")

if __name__ == "__main__":
    main()
