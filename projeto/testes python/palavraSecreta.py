"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os 

keyword = 'onibus'
letra_correta = ''
tentativas = 0

while True:
    letra = input('Digite um letra: ')
    tentativas += 1
    
    if len(letra) > 1:
        print('Ooops! Digite apenas uma letra!')
        continue
    
    if letra in keyword:
        letra_correta += letra
        
    palavra = ''    
    
    for letra_secreta in keyword:
        if letra_secreta in letra_correta:
            palavra += letra_secreta
        else:
            palavra += ('*')
            
    print('A palavra formada é: ',palavra)
    
    if palavra == keyword:
        os.system('cls')
        print('Você descobriu qual é a palavra secreta!')
        print('A palavra formada era: ', keyword)
        print('Seu número de tentativas foi: ',tentativas)
        letra_correta = ''
        tentativas = 0