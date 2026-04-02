## **2. Hash Map / Dictionary**

# **Q4. Count frequency of elements in a list**


# Example: [1, 2, 2, 3, 1] → Output: {1:2, 2:2, 3:1}
# Hint: Use a dictionary and iterate over list



def freq(lists):
    my_dict = {}
    for num in lists:
        if num in my_dict:
            my_dict[num] += 1
        else:
            my_dict[num] = 1

    return my_dict




if __name__ == '__main__':
    lists = [1, 2, 2, 3, 1]
    result = freq(lists)
    print(result)