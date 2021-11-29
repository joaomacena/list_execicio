print(f'# 2. Faça um Programa que leia uma string e diga quantas consoantes foram lidas. Imprima as consoantes.')

class Cont_consoantes:
    def read_Consoant(self, text:str):
        vogal = "AEIOU"
        print(text.upper())
        contar = list(filter(lambda i: i not in vogal, text.upper()))
       
        return f'{contar} com o total de {len(contar)} consoantes'

ler_1 = Cont_consoantes()
print(ler_1.read_Consoant("Faça um Programa que leia uma string e diga quantas consoantes foram lidas. Imprima as consoantes"))

