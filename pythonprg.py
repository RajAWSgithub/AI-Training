def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    try:
        value = int(input("Enter a number to print its 1-10 multiplication table: "))
        print_multiplication_table(value)
    except ValueError:
        print("Please enter a valid integer.")
        print("GitHub")