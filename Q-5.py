lst = [(21,13,"fd"),(),(3,),(),("had",53,2)]

for i in lst:
    if not(bool(i)):
        lst.remove(i)

print(lst)        

#OUTPUT:
# [(21, 13, 'fd'), (3,), ('had', 53, 2)]
