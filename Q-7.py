tpl = (1,23,32,45,441,21)
i = 2                                        # want to remove 32 from tuple
new_tpl = tpl[0:i] + tpl[3:]
print(new_tpl)

#OUTPUT:
# (1, 23, 45, 441, 21)
