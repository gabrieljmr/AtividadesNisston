import string

def e_palindromo(frase):
    frase = frase.lower()
    frase = ''.join(frase.split())
    frase = frase.translate(str.maketrans('', '', string.punctuation))     
    return frase == frase[::-1]

entrada = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

if e_palindromo(entrada):
    print(f"'{entrada}' é um palíndromo.")
else:
    print(f"'{entrada}' não é um palíndromo.")