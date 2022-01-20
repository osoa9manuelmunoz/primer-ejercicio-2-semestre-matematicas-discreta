def convertir_base(numero,base):
    conversion = "0123456789ABCDEF"


    if numero < base:
        return conversion[numero]
    
    else:
        return convertir_base(numero//base, base) + conversion[numero % base]


numero = int(input("ingrese numero base 10:  "))
base = int(input("ingrese base que desea calcular del numero en base 10: "))
resultado = convertir_base(numero,base)
print(resultado)












