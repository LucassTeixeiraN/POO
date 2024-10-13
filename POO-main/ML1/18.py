'''O número 3025 possui a interessante característica:
30 + 25 = 55
55 ** 2 = 3025
Faça um programa que procure todos os números de 4 algarismos que possuem essa
característica.'''
def caracteristica():
  numeros = []
  for num in range(1000, 10000):  # números de 4 algarismos
      str_num = str(num)
      soma_primeiros_algarismos = int(str_num[0] + str_num[1])
      soma_ultimos_algarismos = int(str_num[2] + str_num[3])
      soma = soma_primeiros_algarismos + soma_ultimos_algarismos
      
      if soma ** 2 == num:
          numeros.append(num)
  print(f"Numeros com a caracteristica: {numeros}")
  
caracteristica()
