
def binary_search_first(numbers_list, number_to_find):
    left = 0
    right = len(numbers_list)-1
    mid = 0
    result = -1
    while left <= right:
        mid = (right + left) // 2
        if numbers_list[mid] == number_to_find:
            result = mid
            right = mid - 1

        elif numbers_list[mid] < number_to_find:
            left = mid + 1
        else:
            right = mid - 1
    return result


def binary_search_last(numbers_list, number_to_find):
    left = 0
    right = len(numbers_list)-1
    mid = 0
    result = -1
    while left <= right:
        mid = (right + left) // 2
        if numbers_list[mid] == number_to_find:
            result = mid
            left = mid + 1

        elif numbers_list[mid] < number_to_find:
            left = mid + 1
        else:
            right = mid - 1
    return result


if __name__ == '__main__':
    numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15

    result = binary_search_first(numbers_list, number_to_find)
    results= binary_search_last(numbers_list, number_to_find)
    print(list(range(result,results + 1)))