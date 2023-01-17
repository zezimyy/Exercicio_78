numeros = [int(input("digite um numero: ")), int(input("digite um numero: ")), int(input("digite um numero: ")), int(input("digite um numero: ")), int(input("digite um numero: "))]
posicao = 0

menor_numero = min(numeros)

for numero in numeros:
  numero_ind = numero
  if numero_ind == menor_numero:
    print()
    print("o menor numero está na {}° posição".format(posicao + 1))
    print()
    posicao = 0
  else:
    posicao +=1

maior_numero = max(numeros)

for numero in numeros:
  numero_ind = numero
  if numero_ind == maior_numero:
    print()
    print("o maior numero está na {}° posição".format(posicao + 1))
    print()
  else:
    posicao +=1
  