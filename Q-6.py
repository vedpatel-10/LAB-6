original_tuple = (1, 2, 3, 4)
modified_tuple = original_tuple[:2] + (99,) + original_tuple[3:]
print("Modified tuple:", modified_tuple)

#OUTPUT:
# Modified tuple: (1, 2, 99, 4)
