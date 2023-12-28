def getTotalX(a, b):
    count = 0
    max_a = max(a)
    min_b = min(b)

    for num in range(max_a, min_b + 1):
        if all(num % factor == 0 for factor in a) and all(factor % num == 0 for factor in b):
            count += 1

    return count

# Example usage:
if __name__ == "__main__":
    n, m = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    result = getTotalX(arr_a, arr_b)
    print(result)
