import ast

a = ast.literal_eval(input()) 
a.reverse()
for i in range(len(a)):
    a[i].reverse()
print(a)
