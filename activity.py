# from typing import Counter, List

# # 9. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a
# # entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada
# # de dados, faça:
# # a. mostre a quantidade de valores que foram lidos;
# # b. exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# # c. exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# # d. calcule e mostre a soma dos valores;
# # e. calcule e mostre a média dos valores;
# # f. calcule e mostre a quantidade de valores acima da média calculada;
# # g. calcule e mostre a quantidade de valores abaixo de sete;
# # h. encerre o programa com uma mensagem.








# # 13. Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
# # vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação
# # são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram
# # ignorados. Faça um programa que leia uma sequência de caracteres e diga se esta é um palíndromo ou não.

#import re

#txt = "chove chuva chove sem parar"

#Retorna os caracteres NÃO dígitos(números de 0-9), se existir

#x = re.findall(r"\D", txt)

#print('x6 = ',x)


# def palindro():
#     frase = str(input("digite uma frase :")).strip().upper()
#     palavra = frase.split()
#     junto = ''.join(palavra)
#     inverso = ''
    
#     for letra in range(len(junto)-1,-1,-1):
#         inverso += junto[letra]
    
#     if junto == inverso:
#         print('é um palíndromo')

#     else:
#         print('Não é palíndromo')
    
    
# palindro()

# # 14. Faça um programa que solicite dois valores e imprima todos os pares entre o menor valor e o maior valor. Caso
# # os números digitados sejam iguais, enviar mensagem ao usuário e imprimir os pares de 1 a 10 como exemplo.

# # 15. Faça um programa que peça dois números (base e expoente) e calcule e mostre o primeiro número elevado ao
# # segundo número. Não utilize a função de potência nativa da linguagem.

# # 16. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada
# # eleitor votar e ao final mostrar o número de votos de cada candidato.

# # 17. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O
# # usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# # Tabuada de 5:
# # 5 X 1 = 5
# # 5 X 2 = 10
# # ...
# # 5 X 10 = 50

# 18. Implemente uma classe chamada Carro de acordo com as seguintes regras:
# a. um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de
# combustível no tanque;
# b. o consumo é especificado no construtor e o nível de combustível inicial é 0;
# c. forneça um método andar( ) que simula o ato de dirigir o veículo por uma certa distância, reduzindo o
# nível de combustível no tanque de gasolina;
# d. forneça um método obterGasolina( ), que retorna o nível atual de combustível;
# e. forneça um método adicionarGasolina( ), para abastecer o tanque.

class Carro:
    def __init__(self,km,litros):
        self.consumo_de_combustível= self.consumo_combustível(km,litros)
        self.nivel_combustivel = 0

    def consumo_combustível(self, medida_km, litros):
        return(medida_km/litros)
    
    def andar(self,medida_km):
        nivel_atual = self.nivel_combustivel-(medida_km /self.consumo_de_combustível)
        self.nivel_combustivel = nivel_atual
        return print(f'o carro andou {medida_km} km(s) e esta com {self.nivel_combustivel} litros no tanque')

    def obterGasolina(self):
        return print(f'- o nivel de cobustivel atual é de {self.nivel_combustivel} em litros')

    def adicionarGasolina(self, add_gasolina):
        self.nivel_combustivel += add_gasolina
        return print(f'foi adincinado {self.nivel_combustivel} litros de combustivel ')

    def __str__(self):
        return f' - o carro tem o consumo {self.consumo_de_combustível} e nivel do tanque {self.nivel_combustivel}'


carro1 = Carro(10,1)
carro1.obterGasolina()
carro1.adicionarGasolina(50)
carro1.obterGasolina()
carro1.andar(20)
carro1.obterGasolina()
carro1.andar(30)
print(carro1)


