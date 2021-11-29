print(f'''
# 11. Faça um programa completo utilizando classes e métodos que:
# a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel.
# ii. valorLitro
# iii. quantidadeCombustivel
# b. Possua no mínimo esses métodos:

# i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a
# quantidade de litros que foi colocada no veículo

# ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e
# mostra o valor a ser pago pelo cliente.

# iii. alterarValor( ) – altera o valor do litro do combustível.

# iv. alterarCombustivel( ) – altera o tipo do combustível.

# v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

# c. OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível
# total na bomba.
''')

class bombaCombustível:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def abastecerPorValor(self,valor):
        litros = valor/self.valorLitro
        self.alterarQuantidadeCombustivel(litros)
        return print(f'A quantidade em litros de combustível {litros:.2f} do tipo {self.tipoCombustivel}')
        
    def abastecerPorLitro(self,litros_abstecer):
        valor = litros_abstecer*self.valorLitro
        self.alterarQuantidadeCombustivel(litros_abstecer)
        return print(f'o valor a ser pago pelo cliente {valor:.2f}')
    
    def alterarValor(self, valor_novo):
        self.valorLitro = valor_novo
        return self.valorLitro

    def alterarCombustivel(self,valor, tipo):
        self.tipoCombustivel = tipo
        self.alterarValor(valor)
        return print(f'A bonba foi alterada para o valor {self.valorLitro} com o tipo de conbistivel {self.tipoCombustivel}')

    def alterarQuantidadeCombustivel(self,litros):
        self.quantidadeCombustivel =(self.quantidadeCombustivel - litros)
        return print(f'Quantiade de conbustivel restante  {self.quantidadeCombustivel:.2f}')


bomba1 = bombaCombustível('gasolina',5.43,100)
print(30*'-')
bomba1.abastecerPorValor(50)
print(30*'-')
bomba1.abastecerPorLitro(50)
print(30*'-')
bomba1.alterarValor(7.30)
print(30*'-')
bomba1.abastecerPorValor(20)
print(30*'-')
bomba1.alterarCombustivel(2,"etanol")
print(30*'-')
bomba1.abastecerPorValor(50)