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