if __name__ == '__main__':
    # Read input values
    n, m = map(int, input().split())

    # Read the data into a list of tuples
    data = [tuple(map(int, input().split())) for _ in range(n)]

    # Read the index for sorting
    k = int(input())

    # Sort the data based on the k-th attribute
    sorted_data = sorted(data, key=lambda x: x[k])

    # Print the sorted data
    for row in sorted_data:
        print(' '.join(map(str, row)))
