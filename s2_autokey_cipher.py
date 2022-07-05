def char_range(c1,c2):
    alpha = ""
    for c in range(ord(c1), ord(c2)+1):
        alpha += chr(c)
    return alpha

def clear_text(m, alpha):
    aux = ''
    for c in m:
        if c in alpha:
            aux+=c
    return aux

def encrypt (m, k):  
    return autokey_cipher(m, k, 'encriptar')

def decrypt(m, k):
    return autokey_cipher(m, k, 'decriptar')

def autokey_cipher (m, k, a):
    c = ""
    k_index = 0
    key = k.upper()
    for i in m:
        letter = alpha.find(i.upper())
        if a == 'encriptar':
             letter += alpha.find(key[k_index]) 
             key += i.upper() 

        elif a == 'decriptar':
             letter -= alpha.find(key[k_index])
             key += alpha[letter] 

        letter %= len(alpha)
        k_index += 1
       
        c += alpha[letter]
    return c


message = input('Escreva sua mensagem: ')
key = input('Escreva sua chave: ')
a = input('Você deseja "encriptar" ou "decriptar"? ')
alpha = char_range("A","Z") 
if a == 'encriptar':
    print(encrypt(clear_text(message, alpha), key))
elif a == 'decriptar':
    print(decrypt(clear_text(message, alpha), key))
   
