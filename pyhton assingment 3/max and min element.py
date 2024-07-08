def find_max_min(lst):
    if not lst:
        return None, None  

    max_element = lst[0]
    min_element = lst[0]

    for num in lst:
        if num > max_element:
            max_element = num
        if num < min_element:
            min_element = num

    return max_element, min_element

my_list = [2,55,65,70,80,90,100,105,109]
max_num, min_num = find_max_min(my_list)

print(f"Maximum element in the list: {max_num}")
print(f"Minimum element in the list: {min_num}")
