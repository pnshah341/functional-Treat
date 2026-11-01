"""
Project: Data Analyzer and Transformer
Author: Prince Shah
"""

DATA = []
DATA_TYPE = ""
DATA_SUMMARY = {}


def input_data():
    """Input data in 1D or 2D list."""
    global DATA, DATA_TYPE, DATA_SUMMARY

    print("\n1. 1D Array")
    print("2. 2D Array")

    choice = input("Choose array type: ")

    if choice == "1":
        values = input("Enter data for a 1D array (separated by spaces): ")
        DATA = list(map(int, values.split()))
        DATA_TYPE = "1D"

    elif choice == "2":
        rows = int(input("Enter number of rows: "))
        DATA = []

        for i in range(rows):
            values = input("Enter row " + str(i + 1) + ": ")
            DATA.append(list(map(int, values.split())))

        DATA_TYPE = "2D"

    else:
        print("Invalid choice!")
        return

    DATA_SUMMARY = {}
    print("\nData has been stored successfully!")


def flatten_data():
    """Convert 2D list into 1D list."""
    if DATA_TYPE == "2D":
        return [x for row in DATA for x in row]
    return DATA[:]


def calculate_total(*args):
    """Calculate total using multiple arguments."""
    return sum(args)


def calculate_average(numbers):
    """Calculate average of dataset."""
    return sum(numbers) / len(numbers)


def show_summary(**kwargs):
    """Display dataset summary using keyword arguments."""
    for key, value in kwargs.items():
        print("- " + key + ": " + str(value))


def display_summary():
    """Display basic statistics using built-in functions."""
    global DATA_SUMMARY

    if not DATA:
        print("Please input data first!")
        return

    numbers = flatten_data()

    total = calculate_total(*numbers)
    average = calculate_average(numbers)

    DATA_SUMMARY = {
        "Total elements": len(numbers),
        "Minimum value": min(numbers),
        "Maximum value": max(numbers),
        "Sum of all values": total,
        "Average value": round(average, 2)
    }

    print("\nData Summary:")
    show_summary(**DATA_SUMMARY)


def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def calculate_factorial():
    """Take input and display factorial."""
    n = int(input("\nEnter a number to calculate its factorial: "))

    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print("\nFactorial of", n, "is:", factorial(n))


def filter_data():
    """Filter values using lambda, map and filter."""
    if not DATA:
        print("Please input data first!")
        return

    threshold = int(input("\nEnter a threshold value to filter out data above this value: "))

    numbers = flatten_data()

    transformed = list(map(lambda x: x, numbers))
    result = list(filter(lambda x: x >= threshold, transformed))

    print("\nFiltered Data (values >= " + str(threshold) + "):")
    print(", ".join(map(str, result)))


def sort_data():
    """Sort 1D or 2D list data."""
    if not DATA:
        print("Please input data first!")
        return

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        reverse = False
    elif choice == "2":
        reverse = True
    else:
        print("Invalid choice!")
        return

    if DATA_TYPE == "1D":
        DATA.sort(reverse=reverse)
        print("\nSorted Data:")
        print(", ".join(map(str, DATA)))

    else:
        sorted_rows = [
            sorted(row, reverse=reverse)
            for row in DATA
        ]

        print("\nSorted 2D Data:")
        for row in sorted_rows:
            print(row)


def return_statistics(numbers):
    """Return minimum, maximum, sum and average."""
    return (
        min(numbers),
        max(numbers),
        sum(numbers),
        calculate_average(numbers)
    )


def display_statistics():
    """Display statistics using multiple return values."""
    if not DATA:
        print("Please input data first!")
        return

    numbers = flatten_data()

    minimum, maximum, total, average = return_statistics(numbers)

    print("\nDataset Statistics:")
    print("- Minimum value:", minimum)
    print("- Maximum value:", maximum)
    print("- Sum of all values:", total)
    print("- Average value:", round(average, 2))


def main():
    """Display the main menu and control the program."""

    print("Welcome to the Data Analyzer and Transformer Program")

    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit")

        choice = input("Please enter your choice: ")

        if choice == "1":
            input_data()

        elif choice == "2":
            display_summary()

        elif choice == "3":
            calculate_factorial()

        elif choice == "4":
            filter_data()

        elif choice == "5":
            sort_data()

        elif choice == "6":
            display_statistics()

        elif choice == "7":
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
