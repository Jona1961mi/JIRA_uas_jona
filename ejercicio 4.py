#suma de numeros
def sumas_vari(*numeros):
    total=0

    for numero in numeros:
        total += numero
    return total

print (sumas_vari(1,2,3,4,15))