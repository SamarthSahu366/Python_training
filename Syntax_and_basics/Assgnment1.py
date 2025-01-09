
# program to :Write a program to calculate the area and perimeter of different
# geometric shapes(square, rectangle, parallelogram, triangle, circle)
# based on user input. The program should include error handling for
# invalid inputs.

import math

def calculate_shape_properties():
    print("\nSelect a shape to calculate area and perimeter:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Parallelogram")
    print("4. Triangle")
    print("5. Circle")

    # exception handling if the user does not enter the value btw 1 to 5 
    try:
        choice = int(input("Enter your choice (1-5): "))
        
        if choice == 1:
            side = float(input("Enter the side length of the square: "))
            area = side ** 2
            perimeter = 4 * side
            print(f"Area: {area}, Perimeter: {perimeter}")
        
        elif choice == 2:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = length * width
            perimeter = 2 * (length + width)
            print(f"Area: {area}, Perimeter: {perimeter}")
        
        elif choice == 3:
            base = float(input("Enter the base length of the parallelogram: "))
            height = float(input("Enter the height of the parallelogram: "))
            side = float(input("Enter the side length of the parallelogram: "))
            area = base * height
            perimeter = 2 * (base + side)
            print(f"Area: {area}, Perimeter: {perimeter}")
        
        elif choice == 4:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            side1 = float(input("Enter the length of the first side of the triangle: "))
            side2 = float(input("Enter the length of the second side of the triangle: "))
            side3 = float(input("Enter the length of the third side of the triangle: "))
            area = 0.5 * base * height
            perimeter = side1 + side2 + side3
            print(f"Area: {area}, Perimeter: {perimeter}")
        
        elif choice == 5:
            radius = float(input("Enter the radius of the circle: "))
            area = math.pi * radius ** 2
            perimeter = 2 * math.pi * radius
            print(f"Area: {area}, Perimeter: {perimeter}")
        else:
            print("Invalid choice! Please choose a number between 1 and 5.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    
def main():
    while True:
        print("\nChoose an option:")
        print("1. Calculate area and perimeter of a shape")
        print("2. Exit")

        # exception handling if the user enter the value other than 1 or 2 
        try:
            choice = int(input("Enter your choice (1-2): "))
            if choice == 1:
                calculate_shape_properties()
            elif choice == 2:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice! Please select a number between 1 and 2.")
        except ValueError:
            print("Invalid input! Please enter a number  1 or 2.")

# to check the assignment.py run directly or imported as disccussed in the meet today
if __name__ == "__main__":
    main()
