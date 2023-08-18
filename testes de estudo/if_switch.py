"""
If/Switch

No Python não temos o switch, porém podemos inventalo utilizando classes.

O python suporta as condições lógicas usuais da matemática:

Igual a: a == b
Diferentes: a != b
Menor que: a < b
Menor ou igual a: a <= b
Maior que: a > b
Maior ou igual a: a >= b

Essas condições podem ser usadas de várias maneiras, mais comumente em "instruções if" e loops.

Uma "instrução if" é escrita usando a palavra-chave if .
"""

a = 33
b = 200
if b > a:
  print("b é maior que a")
  
"""
Elif
A palavra-chave elif é a maneira de Python dizer "se as condições anteriores não forem verdadeiras, 
tente esta condição".

Exemplo:
"""
a = 33
b = 33
if b > a:
  print("b é maior que a")
elif a == b:
  print("a e b são iguais")
  
"""
Else
A palavra-chave else captura qualquer coisa que não seja capturada pelas condições anteriores.

Exemplo:
"""

a = 200
b = 33
if b > a:
  print("b é maior que a")
elif a == b:
  print("a e b são iguais")
else:
  print("a é maior que b")
  

#Podemos encurtar o uso do if:

if a > b: print("a is greater than b")

#Podemos encurtar o uso do elif:
a = 2
b = 330
print("A") if a > b else print("B")

#O operador lógico "and" é um operador lógico e é usado para combinar instruções condicionais:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("As duas condições são True")
  
#O operador lógico "or" é usado para combinar declarações condicionais:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("Pelo menos uma condição é verdadeira True")
  
#O operador lógico "not" é usado para inventar o resultado da instrução condicional:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
