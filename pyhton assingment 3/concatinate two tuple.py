def concatenate_tuples(tuple1, tuple2):
    list1 = list(tuple1)
    list2 = list(tuple2)
    
    concatenated_list = list1 + list2
    
    concatenated_tuple = tuple(concatenated_list)
    
    return concatenated_tuple

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

concatenated_tuple = concatenate_tuples(tuple1, tuple2)
print("Concatenated tuple:", concatenated_tuple)
