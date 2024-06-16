# Task 1: Sum of Squares
def sum_of_squares(arr):
    return sum(x ** 2 for x in arr)

# Task 2: Filter and Sum
def filter_and_sum(arr):
    avg = sum(arr) / len(arr)
    return sum(x for x in arr if x >= avg)

# Task 3: Sort by Frequency
def sort_by_frequency(arr):
    freq_dict = {}
    for num in arr:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    return sorted(arr, key=lambda x: (-freq_dict[x], x))

# Task 4: Find Missing Number
def find_missing_number(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)

# Task 5: Longest Consecutive Sequence
def longest_consecutive(arr):
    num_set = set(arr)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length

# Task 6: Rotate Array
def rotate_array(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

# Task 7: Array of Products
def array_of_products(arr):
    result = []
    left_product = 1
    for num in arr:
        result.append(left_product)
        left_product *= num
    right_product = 1
    for i in range(len(arr) - 1, -1, -1):
        result[i] *= right_product
        right_product *= arr[i]
    return result

# Task 8: Maximum Subarray Sum
def max_subarray_sum(arr):
    max_sum = curr_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

# Task 9: Spiral Order Matrix
def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
    return result

# Task 10: K Closest Points to Origin
def k_closest_points(points, k):
    return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]
