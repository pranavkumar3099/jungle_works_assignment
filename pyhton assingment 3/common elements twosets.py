def find_common_elements(set1, set2):
    common_elements = set1.intersection(set2)
    return common_elements

set1 = {100, 205, 465, 666, 990, 1000, 1050}
set2 = {300, 205, 540, 666, 760, 1050, 990}

common_elements = find_common_elements(set1, set2)
print("Common elements:", common_elements)
