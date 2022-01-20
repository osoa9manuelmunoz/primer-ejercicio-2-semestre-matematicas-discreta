def convertir_base(numero,base): 
    conversion = "0123456789ABCDEF"  #es una lista en la cual identifica las bases nesarias para este ejercicio 

    if numero < base:              
        return conversion[numero]  #se utiliza la lista "conversion" en la cual dentro de la lista se realiza la operacion con el numero
    
    else:                                                                     
        return convertir_base(numero//base, base) + conversion[numero % base] #aqui se convierte el numero entero  a base mediante la division + lo que saca el residuo de este 

numero = int(input("ingrese numero base 10:  "))
base = int(input("ingrese base que desea calcular del numero en base 10: "))
resultado = convertir_base(numero,base)                                      
print("el resultado de la base deseado es: ",resultado)  # se genera el resultado de la operacion en donde el usuario eligio el numero para calcular  a la base deseada                    












