def char_range(c1,c2):
    lista = []
    for c in range(ord(c1), ord(c2)+1):
        lista += chr(c)
    return lista

def clear_text(m, alpha):
    aux = ''
    for c in m:
        if c in alpha:
            aux+=c
    return aux
        

m = input()
alpha = char_range('a', 'z')
clean_m = clear_text(m.lower(),alpha)
print(clean_m)
