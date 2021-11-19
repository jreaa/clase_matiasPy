#ejercicio es hacer un palindromo
def verifyPalindromo(value):
    if(value):
        return("La palabra es un palindromo")
    else:
        return("la palabra no es un palindromo")
    
def palindromo():
    palabra = input("Por favor ingresa una palabra: ")
    palabraFormat1 = palabra.replace(' ', '')
    palabraFormat2 = palabraFormat1[::-1]

    if(palabraFormat1 == palabraFormat2):
        return verifyPalindromo(True)
    else:
        return verifyPalindromo(False)


if __name__ == '__main__':
    print(palindromo())