# Program to :Create a real-world problem-solving program, such as calculating
# monthly loan payments based on principal, rate of interest, and
# tenure.

def calculate_loan_payment():
    try:
        principal = float(input("Enter the loan principal amount: "))
        annual_rate = float(input("Enter the annual interest rate (in %): "))
        tenure_years = int(input("Enter the loan tenure (in years): "))

        if principal <= 0 or annual_rate < 0 or tenure_years <= 0:
            print("Please enter positive values for principal, interest rate, and tenure.")
            return

        monthly_rate = annual_rate / 12 / 100
        tenure_months = tenure_years * 12

        if monthly_rate == 0:
            emi = principal / tenure_months
        else:
            emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
                  ((1 + monthly_rate) ** tenure_months - 1)

        print(f"\nMonthly Loan Payment (EMI): {emi:.2f}")
        total_payment = emi * tenure_months
        print(f"Total Payment Over {tenure_years} Years: {total_payment:.2f}")
        print(f"Total Interest Paid: {total_payment - principal:.2f}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

def main():
    while True:
        print("\nLoan Payment Calculator")
        print("1. Calculate Loan Payment")
        print("2. Exit")
        choice = input("Choose an option (1/2): ")
        if choice == '1':
            calculate_loan_payment()
        elif choice == '2':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1 or 2.")

if __name__ == "__main__":
    main()
