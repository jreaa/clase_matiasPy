"""
and 

or 

< 

>

<=

>=

comparacion
"=="

asignacion
"="

<>
nombre = "pedro"
nombre2 = "jose"

nombre = nombre2

============================================================================

#Condicionales:

#permisos para entrar

matias = int(input("Por fa matias dame tu edad: "))
persona_especial = False
#edadDeMatias = int(matias)

if matias >= 18 and matias < 21: #if es la primera condicion a ejecutrar
    print("Matia es mayor de edad!")
    print("Pero Matias no puede beber")
elif matias >= 21 or persona_especial: #elif son condiciones anidadas al primer if
    print("Matia es mayor de edad!")
    print("Puede beber!!")
else: #else no es mas que la negacion a tus condiciones
    print("No es mayor de edad!!")
    print("No puedes entrar!!")

============================================================================
"""

#Modularidad - (Funciones)

def nombreDeLaFuncion(texto):
    print(texto)

def permisosDeEntrada(persona, persona_especial, nombre):
    if persona >= 18 and persona < 21: #if es la primera condicion a ejecutrar
        print(f'{nombre} es una persona mayor de edad!')
        print(f'Pero {nombre} no puede beber')
    elif persona >= 21 or persona_especial: #elif son condiciones anidadas al primer if
        print(f'{nombre} es una persona mayor de edad!')
        print("Puede beber!!")
    else: #else no es mas que la negacion a tus condiciones
        print("No es mayor de edad!!")
        print("No puedes entrar!!")

if __name__ == '__main__':
    #texto = "Hola mundo desde el main!!"
    #nombreDeLaFuncion(texto)
    nombre_matias = input("Dame tu nombre: ")
    matias = int(input(f'Por fa {nombre_matias} dame tu edad: '))
    matias_persona_especial = True
    permisosDeEntrada(matias, matias_persona_especial, nombre_matias)

    nombre_pedro = input("Dame tu nombre: ")
    pedro = int(input(f'Por fa {nombre_pedro} dame tu edad: '))
    pedro_persona_especial = True
    permisosDeEntrada(pedro, pedro_persona_especial, nombre_pedro)
    #edadDeMatias = int(matias)
