
# while 1
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# while 2

i = 1

while i <= 10:
    print(i)
    i += 1

# while 3


while True:
    print("Executando para sempre")

# while 4

while True:
    senha = input("Digite a senha: ")

    if senha == "123":
        print("Acesso permitido")
        break

# while 5

i = 0

while i < 10:
    if i == 5:
        break
    print(i)
    i += 1

# while 6

i = 0

while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)

# while 7

i = 0

while i < 3:
    print(i)
    i += 1
else:
    print("Loop terminou")

# while 8

i = 1

while i <= 3:
    j = 1

    while j <= 3:
        print(i, j)
        j += 1

    i += 1

# while 9

nomes = ["Ana", "Pedro", "Lucas"]

i = 0

while i < len(nomes):
    print(nomes[i])
    i += 1

# while 10

idade = 0

while idade >= 0 and idade < 18:
    idade = int(input("Digite sua idade: "))

while True:
    pass


