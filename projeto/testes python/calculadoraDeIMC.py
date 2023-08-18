nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura ** 2)

print(f'Olá {nome}, você tem {altura} e pesa {peso}kg, seu IMC é de: {imc:.2f}')