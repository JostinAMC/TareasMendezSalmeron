#Aaron Salmeron Gamboa 2020168052
#Jostin Mendez Castro 2020034338

import math  #Libreria de matematicas para añadir irracional PI


def divide_string(frase, operacion):
    # Se define nombre funcion y parametros de entrada
    if isinstance(frase, str) is True:  # Se verifica que sea un String
        if isinstance(operacion, int) is True:
            # Se verifica que el valor de operacion sea un int
            tamaño = len(frase)  # Se mide el tamño de la frase

            # Variable que almacenaran la nueva divicion del string
            mayusculas = ''
            minusculas = ''
            primer_mitad = ''
            segunda_mitad = ''
            if operacion == 1:  # Se selecciona la operacion 1
                for i in range(tamaño):
                    # Un ciclo para revisar cada elemento del string
                    if ((ord(frase[i]) >= 65 and ord(frase[i]) <= 90) or
                            (ord(frase[i]) >= 48 and ord(frase[i]) <= 57)):
                        # Verifica mayuscula y se añade a la nueva division
                        mayusculas = mayusculas + frase[i]
                    else:
                        minusculas = minusculas + frase[i]  # Suma minusculas
                print(frase, 'se convierte en', mayusculas, 'y', minusculas)
                return mayusculas + ' ' + minusculas
            elif operacion == 2:  # Se selecciona la operacion 2
                if tamaño % 2 != 0:  # Se verifica si es impar
                    for i in range(int(tamaño/2)+1):
                        # Mitad de ciclos del tamaño total para dividir
                        primer_mitad = primer_mitad + frase[i]
                        if i < int(tamaño/2)+1 and i > 0:
                            # Evita el ultimo ciclo
                            (segunda_mitad == segunda_mitad +
                                frase[int(tamaño/2)+i])
                else:
                    for i in range(int(tamaño/2)):
                        # Mitad de ciclo para separar string
                        primer_mitad = primer_mitad + frase[i]
                        segunda_mitad = segunda_mitad + frase[int(tamaño/2)+i]
                print(frase, 'se convierte en',
                      primer_mitad, 'y', segunda_mitad)
                return primer_mitad + '  ' + segunda_mitad
            # Imprime cada uno de los erros
            else:
                print('Error 003')
                return 'Error 003'
        else:
            print('Error 002')
            return 'Error 002'
    else:
        print('Error 001')
        return 'Error 001'


def mesure_area(valor):  # Se define la funcion y variables
    if isinstance(valor, int) is True:  # Revisa que sea un entero
        area_circulo = (valor**2)*math.pi  # Calcula las areas correspondietes
        area_cuadrado = valor**2
        print('Area del Circulo de radio', valor, 'es de', area_circulo,
              '\nArea del Cudrado de lado', valor, 'es de', area_cuadrado)
        return str(area_circulo) + ' ' + str(area_cuadrado)
    else:
        print('Error 002')
        return 'Error 002'  # Imprime error

# sCodigos de Error Unico
        # 001 No es una variable string
        # 002 No es una varible int
        # 003 No es una operacion valido
