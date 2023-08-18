nome = input('Escreva seu nome: ')
sobrenome = input('Escreva seu sobrenome: ')
idade = int(input('Digite sua idade: '))
ano_nasc = 2023 - idade

print(f'Olá {nome} {sobrenome}, você tem {idade} e nasceu em {ano_nasc}, pelos meus cálculos: ')

if idade >= 18: 
    print('Você é maior de idade!')
else:
    print('Eres una criancita de mierda!')