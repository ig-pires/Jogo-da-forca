import random

palavras = ['abacaxi', 'computador', 'internet', 'cachorro', 'gato', 'teclado', 'linha', 'monitor', 'musica', 'idade', 'fruta', 'janela', 'palavra']
palavra = random.choice(palavras)
ocultar = ['_'] * len(palavra)
erro = []
vidas = 5

print("Bem-vindo ao Jogo da Forca!")
print("A palavra tem {} letras.".format(len(palavra)))

while vidas > 0 and '_' in ocultar:
    print('\nPalavra: {}'.format(' '.join(ocultar)))
    print('Erros: {}'.format(', '.join(erro)))
    print('Vidas restantes: {}'.format(vidas))

    tentativa = input('Digite uma letra: ').lower()

    if tentativa in palavra:
        for i in range(len(palavra)):
            if palavra[i] == tentativa:
                ocultar[i] = tentativa
        print('Certo!')
    else:
        if tentativa not in erro:
            erro.append(tentativa)
            vidas -= 1
        print('Errado!')
if '_' not in ocultar:
    print('\nVocê ganhou!')
else:
    print('\nVocê perdeu!')
