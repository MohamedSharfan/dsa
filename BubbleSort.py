def bubble_sort(numbers_list):
    size = len(numbers_list)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1):
            if numbers_list[j] > numbers_list[j + 1]:
                temp = numbers_list[j]
                numbers_list[j] = numbers_list[j + 1]
                numbers_list[j + 1] = temp
                swapped = True
        if not swapped:
            break



if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]

    bubble_sort(elements)
    print(elements)