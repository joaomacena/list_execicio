import random

print(f'''
# 3. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no
# vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores.
# ''')

class List_numero:
    def read_number(self, numeros):
        par = list(filter(lambda i : i%2== 0,numeros))
        impar = list(filter(lambda i : i%2!= 0,numeros))
        return f'''lista de numero inseridos {numeros} \n
lista de numeros pares encontrados {par} \n 
lista de numeros impares encontrados {impar}
         '''
#print(random.sample(range(0, 1000), 20))         
lista1 = List_numero()
print(lista1.read_number(random.sample(range(0, 1000), 20)))
