# Q5. First non-repeating character in a string

# Example: "swiss" → Output: "w"
# Hint: Count frequencies first, then iterate string to find first with count 1

def non_rep_char(str):
    my_dict = {}
    for char in str:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    for char in str:
        if my_dict[char] == 1:
            return char
    return None


if __name__ == '__main__':
    str = "swiss"
    result = non_rep_char(str)
    print(result)