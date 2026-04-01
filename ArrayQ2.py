

#Q2 Merge two sorted lists without using sort

# Example: [1, 3, 5], [2, 4, 6] → Output: [1, 2, 3, 4, 5, 6]
# Hint: Use two pointers to iterate through both lists


# def merge_arrays(a, b):
#     ab = []
#     for item in a:
#         ab.append(item)
#     for item in b:
#         ab.append(item)
#     size = len(ab)
#     for i in range(size):
#         for j in range(size - 1):
#             if ab[j] > ab[j + 1]:
#                 ab[j], ab[j + 1] = ab[j + 1], ab[j]
#     return ab

def merge_arrays(a, b):
    ab = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ab.append(a[i])
            i += 1
        else:
            ab.append(b[j])
            j += 1

    while i < len(a):
        ab.append(a[i])
        i += 1
    while j < len(b):
        ab.append(b[j])
        j += 1
    return ab


if __name__ == '__main__':
    a = [1, 3, 5]
    b = [2, 4, 6]
    result = merge_arrays(a, b)
    print(result)
