import ast
def flatten(lst):
    flat = []
    for i in lst:
        if isinstance(i, list):
            flat.extend(flatten(i))
        else:
            flat.append(i)
    return flat

# Kullanıcıdan girdi al
user_input = input()  

# String'i listeye çevir
nested_list = ast.literal_eval(user_input)

# Flatten işlemi
flat_list = flatten(nested_list)
print(flat_list)