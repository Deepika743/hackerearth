if __name__ == '__main__':
    # Read input string
    s = input()

    # Define a custom sorting key
    def custom_sort(char):
        if char.islower():
            return (0, char)
        elif char.isupper():
            return (1, char)
        elif char.isdigit() and int(char) % 2 == 1:
            return (2, char)
        else:
            return (3, char)

    # Sort the string using the custom sorting key
    sorted_string = ''.join(sorted(s, key=custom_sort))

    # Print the sorted string
    print(sorted_string)
