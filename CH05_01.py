def km_to_mi(kilometers):
    
    return kilometers * 0.6214
def main():
    try:
        kilometers = float(input("Enter distance in kilometers: "))
        
        miles = km_to_mi(kilometers)
        
        print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
