# program to:Write a function that accepts *args to calculate the product of all
# numbers provided. Add error handling to manage non-numeric
# inputs

def calculate_product(*args):
    product = 1
    try:
        for num in args:
            if not isinstance(num, (int, float)):
                raise ValueError(f"invalid input: {num} is not a number.")
            product *= num
        return product
    except ValueError as e:
        return str(e)

if __name__ == "__main__":
    user_input = input("enter numbers separated by space: ")
    try:
        numbers = [float(x) for x in user_input.split()]
        result = calculate_product(*numbers)
        print(f"product: {result}")
    except ValueError:
        print("invalid input! please enter only numeric values.")
