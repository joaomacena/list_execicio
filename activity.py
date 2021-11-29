from typing import Counter, List
import random
from datetime import timedelta,datetime

print(f'# 1. Faça um Programa que leia 4 notas de alunos e, ao final, mostre na tela as notas lidas e a respectiva média.')


class Alunos:
    def __init__(self, name_student, classroom, time):
        self.name_student = name_student
        self.classroom = classroom
        self.time= time
    
    def __str__(self):
        return f'Nome do estudante: {self.name_student} \nSala: {self.classroom}\nTime: {self.time}'


class Test:    
    def __init__(self,aluno):
        self.aluno = aluno
        self.nota = []
    
    def tests_score(self, nota):
        self.nota.append(nota)

    def media(self):
        media = 0
        for i in range(len(self.nota)):
            media += self.nota[i]
            print(f'{i} - nota da prova: {self.nota[i]}')
        print(f'media :{media/4}')
        return (media/4)

    def __str__(self):
        print(20*"_")
        return f'{self.aluno} \nNotas {self.nota}'

aluno1 = Alunos("João","labs","foundation")
print(aluno1)
provas2 = Test(aluno1)
provas2.tests_score(12)
provas2.tests_score(10)
provas2.tests_score(12)
provas2.tests_score(11)
print(provas2)
provas2.media()

print(f'# 2. Faça um Programa que leia uma string e diga quantas consoantes foram lidas. Imprima as consoantes.')

class Cont_consoantes:
    def read_Consoant(self, text:str):
        vogal = "AEIOU"
        print(text.upper())
        contar = list(filter(lambda i: i not in vogal, text.upper()))
       
        return f'{contar} com o total de {len(contar)} consoantes'

ler_1 = Cont_consoantes()
print(ler_1.read_Consoant("Faça um Programa que leia uma string e diga quantas consoantes foram lidas. Imprima as consoantes"))


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

print(f'''
# 4. Faça um Programa que peça duas notas de 5 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.
# ''')

class Alunos_4:
    def __init__(self,name,clasroom,score1,score2):
        self.name = name
        self.clasroom = clasroom
        self.score1 = score1
        self.score2 = score2
        self.media = ((self.score1+self.score2)/2)


    def __str__(self):
        return f'nome do aluno {self.name} da sala {self.clasroom} com as notas {self.score1},{self.score2}  e media {self.media}'

    

class sistema_4:
    def __init__(self):
        self.alunos = []

    def add_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def resumo(self):
        for i in filter(lambda x: x[1].media >= 7.0 ,enumerate(self.alunos)):
             print(f'nº {i[0]} - {i[1]}')
        print("--------")
        return f'total de alunos {len(self.alunos)}'
    
        

aluno_4_A = Alunos_4('joao1','A',10,7)
print("sistema_4 ",aluno_4_A)
aluno_4_B = Alunos_4('joao2','A',6,6)
aluno_4_C = Alunos_4('joao3','A',6,6)
aluno_4_D = Alunos_4('joao4','B',8,7)
aluno_4_E = Alunos_4('joao5','B',8,8)

aluno_4 = sistema_4()
aluno_4.add_aluno(aluno_4_A)
aluno_4.add_aluno(aluno_4_B)
aluno_4.add_aluno(aluno_4_C)
aluno_4.add_aluno(aluno_4_D)
aluno_4.add_aluno(aluno_4_E)

print(aluno_4.resumo())

print(f'''
# 5. Faça um Programa que leia as idades e alturas de 10 alunos e determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.''')

class Aluno_5:
    def __init__(self,nome,idade,altura):
        self.nome=nome
        self.idade=idade
        self.altura=altura
    
    def __str__(self):
        return f'Nome: {self.nome} Idade: {self.idade} Altura: {self.altura}'


class Sistema_5:
    def __init__(self):
        self.alunos = []
    
    def add_alunos(self, aluno):
        return self.alunos.append(aluno)
 
    def medias_alturas(self):
        #print((lambda j : print(j.altura) ,self.alunos))
        return sum(list(map(lambda x:x.altura,self.alunos)))/10

    def list_medias(self):
        media = self.medias_alturas()
        
        for i in list(filter(lambda x:x[1].altura >media, enumerate(self.alunos))) :
            print(f'Nº {i[0]} - {i[1]}')
        return f'Lista de alunos maiores que media de {media} de atura'

    def idade_maior(self):
        return f'Quantiade de alunos maior que 13 é de {len(list(filter(lambda x:x.idade >= 13,self.alunos)))}'
            

aluno_5_a = Aluno_5('jose1',13,1.30)
aluno_5_b = Aluno_5('jose2',10,1.70)
aluno_5_c = Aluno_5('jose3',13,1.80)
aluno_5_d = Aluno_5('jose4',10,1.70)
aluno_5_e = Aluno_5('jose5',10,1.10)
aluno_5_f = Aluno_5('jose6',16,1.70)
aluno_5_g = Aluno_5('jose7',10,1.40)
aluno_5_h = Aluno_5('jose8',14,1.70)
aluno_5_i = Aluno_5('jose9',13,1.10)
aluno_5_j = Aluno_5('jose10',13,1.99)

aluno_5 = Sistema_5()
aluno_5.add_alunos(aluno_5_a)
aluno_5.add_alunos(aluno_5_b)
aluno_5.add_alunos(aluno_5_c)
aluno_5.add_alunos(aluno_5_d)
aluno_5.add_alunos(aluno_5_e)
aluno_5.add_alunos(aluno_5_f)
aluno_5.add_alunos(aluno_5_g)
aluno_5.add_alunos(aluno_5_h)
aluno_5.add_alunos(aluno_5_i)
aluno_5.add_alunos(aluno_5_j)

print(aluno_5.medias_alturas())
print(aluno_5.list_medias())
print(aluno_5.idade_maior())

print(f'''
# 6. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após
# isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que
# mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
''')

'''
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho', 'Agosto',
'Setembro','Outubro', 'Novembro','Dezembro']
temperatura = []
for temp in range(len(meses)):
    temperatura.append(float(input(f'Digite a temperatura do mês de {meses[temp]}')))
media = sum(temperatura ) / len(temperatura)
print(f'A média do ano {media}')
for i in range(len(temperatura)):
    if temperatura[i] > media:
        print(str( i + 1) + '-' + meses[i] )
'''    

print(f'''
# 7. Crie uma classe para representar datas com as seguintes regras:
# a. deve ter três atributos: o dia, o mês e o ano;
# b. deve ter um construtor que inicializa os três atributos e verifica a validade dos valores fornecidos;
# c. encapsule cada um dos atributos;
# d. forneça o método __str__ para retornar uma representação da data como string. Considere que a data
# deve ser formatada mostrando o dia, o mês e o ano separados por barra (/);
# e. forneça uma operação para avançar uma data para o dia seguinte.
''')

class Data():
    """ def get_datetime():
        x = datetime.datetime.now()
        print(x.strftime("%x")) """
    def __init__(self, dia=0, mes=0, ano=0):
        if dia == 0:
            dia = datetime.today().day
        self.__dia = dia
        if mes == 0:
            mes = datetime.today().month
        self.__mes = mes
        if ano == 0:
            ano = datetime.today().year
        self.__ano = ano
    def __str__(self):
        return '{}/{}/{}'.format(self.__dia,self.__mes,self.__ano)
    def dia_seguinte(self):
        date = datetime(self.__ano, self.__mes, self.__dia, 0, 0, 0) + timedelta(days=1)
        self.__dia = date.day
        self.__mes = date.month
        self.__ano = date.year
data = Data(28, 11, 2021)
print("Data atual = ",data)
data.dia_seguinte()
print("Dia seguinte = ", data)
date = Data()

print(f'''
# 8. Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia dinheiro para a vítima?"
# e. "Já trabalhou com a vítima?"
# No final, o programa deve emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
# responder positivamente a 2 questões ela deve ser classificada como "Suspeita"; entre 3 e 4, como "Cúmplice", e 5 como
# "Assassino". Caso contrário, ele será classificado como "Inocente".
''')

def crimePerguntas():
    quantidade_positivo = 0
    status = {2: "Suspeito(a)",
              3: "Cúmplice",
              4: "Cúmplice",
              5: "Assassino"}
    lista_perguntas = ["Telefonou para a vítima?",
                       "Esteve no local do crime?",
                       "Mora perto da vítima?",
                       "Devia para a vítima?",
                       "Já trabalhou com a vítima?"]
    for index in range(len(lista_perguntas)):
        print(lista_perguntas[index] + " (sim ou não)")
        resposta = input('Resposta: ')
        if resposta.lower() == 'sim':
            quantidade_positivo += 1
    if quantidade_positivo in status:
        print(status[quantidade_positivo])
    else:
        print("Inocente")
crimePerguntas()


# 9. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a
# entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada
# de dados, faça:
# a. mostre a quantidade de valores que foram lidos;
# b. exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c. exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# d. calcule e mostre a soma dos valores;
# e. calcule e mostre a média dos valores;
# f. calcule e mostre a quantidade de valores acima da média calculada;
# g. calcule e mostre a quantidade de valores abaixo de sete;
# h. encerre o programa com uma mensagem.

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

print(f'''
# 12. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome
# do mês por extenso.
# Ex: Data de Nascimento: 29/10/1973
# Você nasceu em 29 de Outubro de 1973.
''')

def date_month_year():
    meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho",
    "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    dia, mês, ano = input("Digite a data de Nascimento no formato dd/mm/aaa: ").split('/')
    print('Voce nasceu em {} de {} de {}'.format(dia, meses[int(mês) -1], ano))
date_month_year()


# 13. Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
# vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação
# são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram
# ignorados. Faça um programa que leia uma sequência de caracteres e diga se esta é um palíndromo ou não.
# 14. Faça um programa que solicite dois valores e imprima todos os pares entre o menor valor e o maior valor. Caso
# os números digitados sejam iguais, enviar mensagem ao usuário e imprimir os pares de 1 a 10 como exemplo.
# 15. Faça um programa que peça dois números (base e expoente) e calcule e mostre o primeiro número elevado ao
# segundo número. Não utilize a função de potência nativa da linguagem.
# 16. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada
# eleitor votar e ao final mostrar o número de votos de cada candidato.
# 17. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O
# usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50
# 18. Implemente uma classe chamada Carro de acordo com as seguintes regras:
# a. um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de
# combustível no tanque;
# b. o consumo é especificado no construtor e o nível de combustível inicial é 0;
# c. forneça um método andar( ) que simula o ato de dirigir o veículo por uma certa distância, reduzindo o
# nível de combustível no tanque de gasolina;
# d. forneça um método obterGasolina( ), que retorna o nível atual de combustível;
# e. forneça um método adicionarGasolina( ), para abastecer o tanque.