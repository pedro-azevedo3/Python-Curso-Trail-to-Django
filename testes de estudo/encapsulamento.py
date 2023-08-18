"""
Herança e Encapsulameto:    

Encapsulamento é um dos pilares da programação orientada a objetos, segundo o qual procuramos esconder
de clientes (usuários da classe) todas as informações que não são necessárias ao uso da classe.

Por exemplo, suponha que precisássemos criar uma classe para armazenar informações de funcionários
de uma empresa, como ilustrado no exemplo abaixo:
"""
class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome
        self.cargo
        self.valor_hora_trabalhada
        self.horas_trabalhadas = 0
        self.salario = 0
    def registra_hora_trabalhada(self):
        self.horas_trabalhadas += 1
    def calcula_salario(self):
        self.salario = self.horas_trabalhadas *self.valor_hora_trabalhada    
    
"""
Na classe acima, o salário de um funcionário é calculados com base no valor por hora trabalhada e na 
quantidade de horas trabalhadas. A classe acima é razoável, mas possui alguns problemas. Informações 
sigilosas de funcionários, como salário, são expostas a clientes da classe, o que nem sempre é desejável.
Além disso, clientes da classe podem simplesmente alterar o salário final de um funcionário sem utilizar
a função calcula salário. Por exemplo, na implementação acima, nada impede que um cliente da classe faça 
algo como "f.salario = 1000000", o que alteraria o salário final do funcionário sem que este seja atrelado
ao número de horas trabalhadas. O mesmo problema acontece com a variável "horas_trabalhadas".

O que desejamos é ENCAPSULAR (esconder) as informações de salário do funcionário. Como fazer isso?

Bom, existe a palavra-chave "private" para indicar que um dado ou método não é visível fora da classe. Em python,
existe uma convenção de que dados ou métodos cujo nome começa com "__" (dois underscores), não deveriam ser acessados
fora da classe, como ilustrado no exemplo abaixo:
"""

class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0  #Mudamos para que ela comece com dois underscores
        self.__salario = 0 #Também mudamos essa aqui.

    def registra_hora_trabalhada(self):
        self.horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada
        
"""
Além disso, o encapsulamento permite que a implementação das funcionalidades da classe seja alterada sem que 
o código que usa a classe precise mudar. Em outras palavras, dado que a interface da classe (o que é exposto
aos clientes) não mude, o programador tem liberdade de mudar a implementação da funcionalidade que a classe
oferece. Por exemplo, caso a forma de cálculo do salário mude, basta que o programador altere a implementação
do método "calcula_salario()" e clientes da classe continuarão a usar o método precisar sofrer alterações.

Porém, dado que essa forma de encapsulamento é somente um indicativo de que dados e métodos cujo nome começa 
com "__" não devem (mas podem) ser acessados, ainda assim podemos alterar a variável salário, conforme mostrado
no exemplo abaixo:
"""

pedro = Funcionario('Pedro','Desenvolvedor', 50)
pedro.__salario = 100000
print(pedro.__salario)

"""
Como impedir esse tipo de alteração?

Python possui outro mecanismo garantir que certas variáveis de uma classe não sejam alteradas. Esse mecanismo
consiste do uso do decorador "@property", que nos permite restringir acesso a variáveis de uma classe. Exemplo
abaixo ilustra o uso desse mecanismo:
"""
class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0
        self.__horas_trabalhadas = 0

    @property
    def salario(self): 
        return self.__salario

    @salario.setter
    def salario(self, novo_salario): 
        raise ValueError("Impossivel alterar salario diretamente. Use a funcao calcula_salario().")

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

pedro = Funcionario('Pedro', 'Desenvolvedor', 50)
pedro.salario = 100000 
