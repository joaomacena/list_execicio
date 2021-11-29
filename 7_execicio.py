from datetime import timedelta,datetime


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