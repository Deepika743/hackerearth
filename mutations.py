def mutate_string(s, position, character):
    # Convert the string to a list
    string_list = list(s)

    # Modify the character at the specified position
    string_list[position] = character

    # Join the list back into a string
    mutated_string = ''.join(string_list)

    return mutated_string

# Example usage:
if __name__ == "__main__":
    s = input().strip()  # Read the original string
    position, character = map(str, input().strip().split())  # Read the position and character
    position = int(position)  # Convert the position to an integer

    result = mutate_string(s, position, character)
    print(result)
