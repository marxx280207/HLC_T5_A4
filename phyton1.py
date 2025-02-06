def iterativo(n):
     resultado = 1
     for i in range(2, n + 1):
         resultado *= i
     return resultado
 
def recursivo(n):
     if n == 0 or n == 1:
         return 1
     else:
         return n * recursivo(n - 1)
     

print(iterativo(5)),print((recursivo(6)))