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