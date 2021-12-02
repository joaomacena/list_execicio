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