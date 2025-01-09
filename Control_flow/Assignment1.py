# program to:Write a program to classify numbers as prime, composite, or
# neither (for negative or zero values). Ensure it handles invalid
# inputs gracefully

def classify_number():
    # to handle the exception if the user entered the wrng value 
    try:
        number = int(input("enter a number: "))

        if number <= 0:
            print(f"{number} is neither prime nor composite.")
        elif number == 1:
            print("1 is neither prime nor composite.")
        else:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    print(f"{number} is a composite number.")
                    return
            print(f"{number} is a prime number.")
    except ValueError:
        print("invalid input! please enter an integer.")

def main():
    while True:
        print("\nnumber classifier")
        print("1. classify a number")
        print("2. exit")
        choice = input("choose an option (1/2): ")
        if choice == '1':
            classify_number()
        elif choice == '2':
            print("exiting... goodbye!")
            break
        else:
            print("invalid choice! please choose 1 or 2.")

if __name__ == "__main__":
    main()
