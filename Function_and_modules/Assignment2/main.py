from math_operations import MathOperations

def perform_operations():
    math_ops = MathOperations()

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Matrix Multiplication")
        print("4. Exit")
        
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {math_ops.add(a, b)}")
        
        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {math_ops.subtract(a, b)}")
        
        elif choice == '3':
            matrix1 = []
            matrix2 = []
            
            rows1 = int(input("Enter number of rows for first matrix: "))
            cols1 = int(input("Enter number of columns for first matrix: "))
            print("Enter elements for first matrix:")
            for i in range(rows1):
                row = [int(x) for x in input(f"Enter row {i+1}: ").split()]
                matrix1.append(row)

            rows2 = int(input("Enter number of rows for second matrix: "))
            cols2 = int(input("Enter number of columns for second matrix: "))
            print("Enter elements for second matrix:")
            for i in range(rows2):
                row = [int(x) for x in input(f"Enter row {i+1}: ").split()]
                matrix2.append(row)

            result = math_ops.matrix_multiply(matrix1, matrix2)
            print("Matrix Multiplication Result:")
            if isinstance(result, list):
                for row in result:
                    print(row)
            else:
                print(result)
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid input. Please choose again.")

if __name__ == "__main__":
    perform_operations()
