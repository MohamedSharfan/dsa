# Q3. Find all pairs with a given sum

# Example: [2, 4, 3, 5, 7], target = 7 → Output: [(2, 5), (4, 3)]
# Hint: Use a set or dictionary for faster lookup


def find_sum_pairs(a, target):
    result = set()
    k = l = 0
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if (a[i] + a[j]) == target:
                result.add((a[i], a[j]))
    return result


if __name__ == '__main__':
    a = [2, 4, 3, 5, 7]
    target = 7
    result = find_sum_pairs(a, target)
    print(result)