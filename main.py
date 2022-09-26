from random import randint
from time import sleep

cromossomos = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
]
iten = [1, 3, 5, 6, 3, 1, 2]

    #caneta: 2,
    #estojo: 3,
    #livro: 6,
    #caderno: 6,
    #calculadora: 4,
    #borracha: 1,
    #provas: 2'''

lista_peso = []
lista_itens = []
lista_fitness = []


penalidade = 0.2

# fitness = peso * quantiadade de itens

def aleatorio():
  for cromossomo in cromossomos: # pega a lista (cromossomo) da lista de litas (cromossomos)
    for alelo in range(len(cromossomo)): # pega o alelo do cromossomo pego e gera um valor aleatório para ele entre 0 e 1
      cromossomo[alelo] = randint(0, 1)
    print(cromossomo)
    

def coloca_item():
  print('CHAMOU COLOCA ITEM')
  for i, cromossomo in enumerate(cromossomos): # pega o index e a lista do cromossomos 
    peso = 0
    for alelo in range(len(cromossomo)):
      if cromossomo[alelo] == 1:
        peso += iten[alelo]
    lista_itens.append(cromossomo.count(1)) #  conta quantos 'itens' (1) tem no cromossomo
    lista_peso.append(peso)
    lista_fitness.append(cromossomo.count(1) * peso)
    print(f'o Peso do cromossomo {i} -> {peso}')
  aplica_penalidade()
  
  
def aplica_penalidade():
  print('CHAMOU APLICAR PENALIDADE')
  for i, cromossomo in enumerate(cromossomos): # pega o index e a lista do cromossomos 
    if lista_peso[i] > 15:
      print(f'Cromossomo {i} penalizado (peso: {lista_peso[i]} \n fitness: {lista_fitness[i]}) -> {lista_fitness[i] * penalidade}')
      lista_fitness[i] *= penalidade
  print(f'Nova lista de Fitness: {lista_fitness}')
      

def torneio():
  aux = 0
  # primeiro FOR para percorrer a lista de fitness duas vezes e achar os maiores valores
  while True:
    win01 = 0
    win02 = 0
    lose01 = 10000
    lose02 = 10000
    print(f'=-=-=-=-=-=-=-=-=-=-==--=-=-=-=-CICLO: {aux}-=-=-=-=-=-=-=-=-=-=-==--=-=-=-=- ')
    if len(set(lista_fitness)) == 1:
      print('FINALIZADO!')
      break  
    for c in range(2):
      for i, fit in enumerate(lista_fitness):
        if fit >= win01:
          win01 = fit
        elif fit > win02:
          win02 = fit
        if fit <= lose01:
          lose01 = fit
        elif fit <= lose02:
          lose02 = fit

    # FAZER O LOOP PEGAR OS NOVO ARRAY DE CROMOSSOMOS
    print(f'Cromossomo ANTIGO: {cromossomos}')
    print(f'lista do Fitness: {lista_fitness}')
    print(f'lista do Peso: {lista_peso}')
    print(f'lista do Itens: {lista_itens}')
    print(30*'--')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-= RANKING =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-')
    print(f'N°1: {win01} -> Index: {lista_fitness.index(win01)}') # tem o valor do vencedor 1 e seu Index
    print(f'N°2: {win02} -> Index: {lista_fitness.index(win02)}') # tem o valor do vencedor 2 e seu Index
    print(f'N°6: {lose02} -> Index: {lista_fitness.index(lose02)}') # tem o valor fitness do pior cromossomo e seu Index
    print(f'N°7: {lose01} -> Index: {lista_fitness.index(lose01)}') # tem o valor fitness do pior cromossomo e seu Index

    cromossomo_win01 = cromossomos[lista_fitness.index(win01)]
    cromossomo_win02 = cromossomos[lista_fitness.index(win02)]
    cromossomo_lose01 = cromossomos[lista_fitness.index(lose01)]
    cromossomo_lose02 = cromossomos[lista_fitness.index(lose02)]

    print('-----------------------------------------------------------------------------------------------')
    
    print(f'Melhor Cromossomo (N°1): {cromossomo_win01}') # Mostra o melhor cromossomo
    print(f'Segundo Melhor Cromossomo (N°2): {cromossomo_win02}') # Mostra o segundo melhor cromossomo
    print(f'Segundo Pior Cromossomo (N°6): {cromossomo_lose02}') # Mostra o segundo pior cromossomo
    print(f'Pior Cromossomo (N°7): {cromossomo_lose01}') # Mostra o pior cromossomo
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-')

    # faz a mistura dos melhores cromossomos e susbtitui nos piores cromossomos
    for i in range (3):
      #print('TO NO RANGE I')
      #print(f'ANTIGO VALOR DE N°7 NA POSIÇÃO {i} VALE {cromossomos[lista_fitness.index(lose01)][i]}')
      cromossomos[lista_fitness.index(lose01)][i] = cromossomos[lista_fitness.index(win01)][i]
      #print(f'NOVO VALOR DE N°7 NA POSIÇÃO {i} VALE {cromossomos[lista_fitness.index(lose01)][i]}')
      cromossomos[lista_fitness.index(lose02)][i] = cromossomos[lista_fitness.index(win02)][i]
    for j in range (3, 7, 1):
      #print('TO NO RANGE J')
      #print(f'ANTIGO VALOR DE N°7 NA POSIÇÃO {j} VALE {cromossomos[lista_fitness.index(lose01)][j]}')
      cromossomos[lista_fitness.index(lose01)][j] = cromossomos[lista_fitness.index(win02)][j]
      #print(f'NOVO VALOR DE N°7 NA POSIÇÃO {j} VALE {cromossomos[lista_fitness.index(lose01)][j]}')
      cromossomos[lista_fitness.index(lose02)][j] = cromossomos[lista_fitness.index(win01)][j]
    
    print(f'O novo cromossomo N°7: {cromossomos[lista_fitness.index(lose01)]}')
    print(f'O novo cromossomo N°6: {cromossomos[lista_fitness.index(lose02)]}')
    print(f'Cromossomo novo: {cromossomos}')

    lista_fitness.clear()
    lista_itens.clear()
    lista_peso.clear()

    coloca_item()

    aux += 1

    if aux > 40:
      print('ENTREI NO CICLO 40 - ALTERANDO OS ALENOS DO PIOR CROMOSSOMO')
      for alelo in range(len(cromossomos[lista_fitness.index(lose01)])):
        cromossomos[lista_fitness.index(lose01)][alelo] = randint(0, 1)
      aux = 0
    



aleatorio()
coloca_item()

print(30*'--')
print(lista_fitness)
print(cromossomos)
print(30*'--')

torneio()