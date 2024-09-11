''' Estatistica fórmula - RETA DE REGRESSÃO LINEAR '''

lista = [50.5, 51.5, 52.1, 54.5, 56.2]         # Lista de valores

n = len(lista)                                 # Número de elementos
SOMA_X = 0                                     # Soma de X
SOMA_Y = 0                                     # Soma de Y
SOMA_X2 = 0                                    # Soma de X^2
SOMA_XY = 0                                    # Soma de X*Y

for i in range(1, n +1):
    SOMA_X += i
    SOMA_X2 += i**2
    SOMA_Y += lista[i - 1]
    SOMA_XY += i*lista[i - 1]
    
print(f"Ʃx: {SOMA_X}\n")
print(f"Ʃy: {SOMA_Y}\n")
print(f"Ʃx²: {SOMA_X2}\n")
print(f"Ʃxy: {SOMA_XY}\n")

a = (n*SOMA_XY - SOMA_X*SOMA_Y) / (n*SOMA_X2 - SOMA_X**2)

b = (SOMA_Y*SOMA_X2 - SOMA_X*SOMA_XY) / (n*SOMA_X2 - SOMA_X**2)

print(f'a = {a}\n')
print(f'b = {b}\n')

if a > 0 and b > 0:
    print(f"y = {b} + {a}.x\n")

elif a < 0 and b > 0:
    print(f"y = {b} - {abs(a)}.x\n")

elif a > 0 and b < 0:
    print(f"y = - {abs(b)} + {a}.x\n")

elif a < 0 and b < 0:
    print(f"y = - {abs(b)} - {abs(a)}.x\n")

else:
    print(f"invalido")

