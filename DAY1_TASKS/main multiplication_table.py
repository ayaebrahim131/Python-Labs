
from multiplication_table import print_multiplication_table

def main():
    print("=== Multiplication Table Generator ===")
    print("Enter a number to see its multiplication table (0 to exit)\n")
    
    while True:
        try:
            num = int(input("Please enter a number: "))
            
            if num == 0:
                print("\nThank you for using the program. Goodbye!")
                break
                
            if not print_multiplication_table(num):
                print("Please enter a positive number!")
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()