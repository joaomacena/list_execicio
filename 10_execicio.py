print(f'''
# 10. Implemente a classe Funcionário com um nome e um salário. Escreva um construtor com dois parâmetros
# (nome e salário) e métodos para devolver nome e salário. Crie o método aumentar_salario(percentual_aumento)
# que aumente o salário do funcionário em uma certa porcentagem. Escreva um pequeno programa que teste sua
# classe.
''')

class Funcionário:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario =salario

    def __str__(self) -> str:
        print(20*'-')
        return f"nome: {self.nome} salario: {self.salario}"

    def aumentar_salario(self,percentual_aumento):
        aumento = self.salario*(percentual_aumento/100)
        self.salario += aumento
        return self.salario


funcinario1 = Funcionário('jose',1000.00)

print(funcinario1)

funcinario1.aumentar_salario(50)

print(funcinario1)