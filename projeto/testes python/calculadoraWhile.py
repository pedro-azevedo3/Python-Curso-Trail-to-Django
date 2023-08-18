# Calculadora com While
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite um outro número: ')
    operador = input('Digite o operador (+,-,/,*): ')
    
    numeros_validos = None
    
    num1_float = 0
    num2_float = 0
    
    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = False
        
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue #Para retornar ao início do while.
    
    operadores_validos = '+-/*'
    
    if operador not in operadores_validos:
        print('Operador inválido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    if operador == '+':
        print(num1_float + num2_float)
    elif operador == '-':
        print(num1_float - num2_float)
    elif operador == '*':
        print(num1_float * num2_float)
    elif operador == '/':
        print(num1_float / num2_float)
          
    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break