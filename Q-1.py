student_lst = ["anushka",("Virat",),"Hazel",("Yuvraj",)]
girls_count,boys_count = 0,0

for i in student_lst:
    if isinstance(i, tuple):
        boys_count = boys_count + 1
    else:
        girls_count = girls_count+1 

print(f"number of boys are {boys_count}")
print(f"number of girls are {girls_count}")
