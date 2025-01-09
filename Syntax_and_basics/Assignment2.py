# program to :Develop a program to take user input for multiple numbers, store
# them in a list, and compute basic statistical metrics like mean,
# median, mode, and standard deviation


def calculate_statistics():
    try:
        numbers = list(map(float, input("\nEnter numbers separated by space: ").split()))
        if not numbers:
            print("No numbers entered!")
            return
        mean = sum(numbers) / len(numbers)
        print(f"Mean: {mean}")
        numbers.sort()
        n = len(numbers)
        median = numbers[n // 2] if n % 2 != 0 else (numbers[n // 2 - 1] + numbers[n // 2]) / 2
        print(f"Median: {median}")
        number_counts = {num: numbers.count(num) for num in set(numbers)}
        mode = [num for num, count in number_counts.items() if count == max(number_counts.values())]
        if len(mode) == len(set(numbers)):
            print("Mode: No unique mode")
        else:
            print(f"Mode: {mode}")
        variance = sum((x - mean) ** 2 for x in numbers) / (n - 1) if n > 1 else 0
        stdev = variance ** 0.5
        print(f"Standard Deviation: {stdev}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

def main():
    while True:
        choice = input("\n1. Calculate Statistics\n2. Exit\nChoose an option (1/2): ")
        if choice == '1':
            calculate_statistics()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
