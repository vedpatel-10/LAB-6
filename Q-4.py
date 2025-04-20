import operator
menu = [("Pizza",120),("Burger",80),("Coffee", 50),("Lemonade",30),("Sandwich",50)]

print(sorted(menu, key = operator.itemgetter(1), reverse=True))

#OUTPUT:
# [('Pizza', 120), ('Burger', 80), ('Coffee', 50), ('Sandwich', 50), ('Lemonade', 30)]
