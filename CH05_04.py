def calculate_total_monthly_cost(expenses):
    """Calculate the total monthly cost from a list of expenses."""
    return sum(expenses)

def calculate_total_annual_cost(monthly_cost):
    """Calculate the total annual cost based on the monthly cost."""
    return monthly_cost * 12

def main():
   
    try:
        loan_payment = float(input("Enter your monthly loan payment: $"))
        insurance = float(input("Enter your monthly insurance cost: $"))
        gas = float(input("Enter your monthly gas cost: $"))
        oil = float(input("Enter your monthly oil cost: $"))
        tires = float(input("Enter your monthly tire cost: $"))
        maintenance = float(input("Enter your monthly maintenance cost: $"))
        
      
        expenses = [loan_payment, insurance, gas, oil, tires, maintenance]
        
     
        total_monthly_cost = calculate_total_monthly_cost(expenses)
        total_annual_cost = calculate_total_annual_cost(total_monthly_cost)
        
      
        print(f"\nTotal Monthly Cost: ${total_monthly_cost:.2f}")
        print(f"Total Annual Cost: ${total_annual_cost:.2f}")
        
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
