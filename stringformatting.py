def print_formatted(number):
    width = len(bin(number)[2:])  # Calculate the width based on the binary representation

    for i in range(1, number + 1):
        decimal_value = str(i)
        octal_value = oct(i)[2:]
        hexadecimal_value = hex(i)[2:].upper()
        binary_value = bin(i)[2:]

        print(f"{decimal_value:>{width}} {octal_value:>{width}} {hexadecimal_value:>{width}} {binary_value:>{width}}")

# Example usage:
if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
