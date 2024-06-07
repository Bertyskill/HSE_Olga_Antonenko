def find_two_items_by_sum(arr, s):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == s:
                return [i, j]

    return []

print(find_two_items_by_sum([1, 2, 3, 4, 5], 6))
print(find_two_items_by_sum([], 1))
print(find_two_items_by_sum([1], 1))
print(find_two_items_by_sum([1, 2], 1))
print(find_two_items_by_sum([1, 2], 3))
print(find_two_items_by_sum([1, 2, 3], 5))
print(find_two_items_by_sum([1, 2, 1, 2, 1], 3))