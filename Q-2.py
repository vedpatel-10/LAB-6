std_details = [(209,"ved",18),(208,"taksh",19),(177,"Reyan",18)]
roll = []
name = []
age = []

for i in std_details :
    X,Y,Z = i
    roll.append(X)
    name.append(Y)
    age.append(Z)

print("List of roll numbers:", roll)
print("List of name:", name) 
print("List of age:", age) 

#OUTPUT:
# List of roll numbers: [209, 208, 177]
# List of name: ['ved', 'taksh', 'Reyan']
# List of age: [18, 19, 18]  
