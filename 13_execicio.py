# 13. Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
# vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação
# são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram
# ignorados. Faça um programa que leia uma sequência de caracteres e diga se esta é um palíndromo ou não.




def palindro():
    frase = str(input("digite uma frase :")).strip().upper()
    palavra = frase.split()
    junto = ''.join(palavra)
    inverso = ''
    
    for letra in range(len(junto)-1,-1,-1):
        inverso += junto[letra]
    
    if junto == inverso:
        print('é um palíndromo')

    else:
        print('Não é palíndromo')
    
    
palindro()