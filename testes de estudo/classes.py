#Para criar uma classe utilizamos a palavra-chave "class":
class MyClass:
  x = 5
  
#Agora podemos usar a classe "MyClass" para criar objetos:
p1 = MyClass()
print(p1.x)

#Agora vamos falar sobre a função "__init__", os exemplos que usei acima são de classes e objetos em sua forma
#mais simplista, e não são tão utilizados em aplicações reais. Para entender o significado de classes precisamos
#entender a função "__init__". As classes tem essa função pois executam o comando assim que são chamadas. Exemplo:

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
p1 = Pessoa("Pedro", 19)
print(p1.nome)
print(p1.idade)

#A função "__init__()" serve para atribuir valores às propriedades do objeto ou outras operações necessárias quando
#o objeto está sendo criado.