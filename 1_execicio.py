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