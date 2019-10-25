a = input()
a_list = list(a)
b = input()
b_list = list(b)
c = input()
for i in range(len(a)):
    if c[i] == "1":
        a_list[i] = b_list[i]
for i in range(len(a)):
    print(a_list[i], end="")
print()
        
