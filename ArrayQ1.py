# Q1. Find the second largest number in a list

# Example: [4, 1, 7, 7, 5] → Output: 5
# Hint: Track the largest and second largest while iterating

def second_largest(elements):
    size = len(elements)
    if size < 2:
        return None
    largest = float('-inf')
    second_large = float('-inf')
    for i in range(size):
        if elements[i] > largest:
            second_large = largest
            largest = elements[i]
        elif second_large < elements[i] and elements[i] != largest:
            second_large = elements[i]
    return second_large if second_large != float("-inf") else None




if __name__ == "__main__":
    elements = [1, 2, 3,4,3,7,7,5]
    result = second_largest(elements)
    print(result)