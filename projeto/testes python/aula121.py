pessoa = {
    'nome': 'Pedro',
    'sobrenome': 'Teixeira',
    'nome': 'Pedro',
    'sobrenome': 'Azevedo',
}

print(list(pessoa.values()))

for valor in pessoa.values():
    print(valor) #para listar o valor 'Pedro' e 'Azevedo'
    
for chave, valor in pessoa.items():
    print(chave,':', valor)