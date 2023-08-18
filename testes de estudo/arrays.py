#Nesse exemplo vamos utilizar marcas de carro para fazer o array.

carro_marcas = ["Ford","Renault","Fiat","Volkswagen","BMW"]

print(carro_marcas)

#Agora, para acessar os elementos de um array, utilizamos o index number de um array. 
#O index number, ou seja, o começo de um array é o número 0. Então, no nosso exemplo o número 0 é Ford.

print(carro_marcas[0])

#Para checarmos quantos elementos tem no meu array utilizamos o atributo "len".
print(len(carro_marcas)) #Neste caso temos 5 elementos.

#Para listarmos em sequência todos os elementos de um array podemos fazer um loop.
for x in carro_marcas:
    print(x)
    
#Para adicionarmos elementos em um array utilizamos o atributo "append()":
carro_marcas.append("Honda")
print(carro_marcas)

#Para removermos elementos de um array utilizamos o atributo "pop()";

carro_marcas.pop(0)
print(carro_marcas)

#Você também pode remover elementos utilizando o atributo remove():
carro_marcas.remove("Fiat")
print(carro_marcas)

#Outros métodos são: insert(), copy(), reverse(), sort(), index(), clear(), count(), extend()...