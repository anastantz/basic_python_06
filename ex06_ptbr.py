# Programa que lê um número e mostra o seu dobro, triplo e raiz quadrada

numero = float(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print(f"Analisando o número {numero}:")
print(f"O dobro é {dobro}.")
print(f"O triplo é {triplo}.")
print(f"A raiz quadrada é {raiz_quadrada:.2f}.")