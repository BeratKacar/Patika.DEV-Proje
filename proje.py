
def flatten(lst):
    flat = []
    for i in lst:
        if isinstance(i, list):
            flat.extend(flatten(i))
        else:
            flat.append(i)
    return flat

# Kullanıcıdan girdi al
user_input = input("Listeyi girin: ")  # Örn: [1, [2, 'abc'], 3]

# String'i listeye çevir
nested_list = ast.literal_eval(user_input)

# Flatten işlemi
flat_list = flatten(nested_list)
print(flat_list)