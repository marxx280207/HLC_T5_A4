def potencia(base, exponente):
    if exponente == 0 or exponente == 1:
         return 1
    return base * potencia(base, exponente - 1)
base = int(input("Introduce la base "))
exponente = int(input("Introduce el exponente "))
     
 
print(potencia(base, exponente))