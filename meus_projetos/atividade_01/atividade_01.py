# Questão 01
mensagem = "Alunos - PLP Unifavip 2022.2"
print("Questão 01:")
print(mensagem)
print("-" * 30)

# Questão 02
numero = input("Questão 02 - Informe um número: ")
print("Número informado:", numero)
print("-" * 30)

# Questão 03
num01 = float(input("Questão 03 - Digite o número 01: "))
num02 = float(input("Digite o número 02: "))
soma = num01 + num02
print("Soma dos valores:", soma)
print("-" * 30)

# Questão 04
nota01 = float(input("Questão 04 - Digite a nota 01: "))
nota02 = float(input("Digite a nota 02: "))
nota03 = float(input("Digite a nota 03: "))
nota04 = float(input("Digite a nota 04: "))
media = (nota01 + nota02 + nota03 + nota04) / 4
print("Média das notas:", media)
print("-" * 30)

# Questão 05
metro = float(input("Questão 05 - Valor em metros: "))
centimetros = metro * 100
print(f"{metro} metros equivale a {centimetros} centímetros")
print("-" * 30)

# Questão 06
num = int(input("Questão 06 - Digite um número inteiro: "))
dobro = num * 2
print(f"Dobro de {num} é {dobro}")
print("-" * 30)

# Questão 07
num = float(input("Questão 07 - Digite um número: "))
cubo = num ** 3
print(f"Cubo de {num} é {cubo}")
print("-" * 30)

# Questão 08
raio = float(input("Questão 08 - Digite o raio do círculo: "))
area = 3.14159 * raio ** 2
print(f"Área do círculo: {area:.2f}")
print("-" * 30)

# Questão 09
largura = float(input("Questão 09 - Largura do terreno: "))
comprimento = float(input("Comprimento do terreno: "))
area_terreno = largura * comprimento
print(f"Área do terreno: {area_terreno}")
print("-" * 30)

# Questão 10
base = float(input("Questão 10 - Base do triângulo: "))
altura = float(input("Altura do triângulo: "))
area_triangulo = (base * altura) / 2
print(f"Área do triângulo: {area_triangulo}")
print("-" * 30)

# Questão 11
salario = float(input("Questão 11 - Salário do funcionário: "))
novo_salario = salario * 1.15
print(f"Novo salário com 15% de aumento: {novo_salario}")
print("-" * 30)

# Questão 12
preco = float(input("Questão 12 - Preço do produto: "))
desconto = preco * 0.10
preco_final = preco - desconto
print(f"Preço final com 10% de desconto: {preco_final}")
print("-" * 30)

# Questão 13
fahrenheit = float(input("Questão 13 - Temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"Temperatura em Celsius: {celsius:.2f}°C")
print("-" * 30)

# Questão 14
celsius = float(input("Questão 14 - Temperatura em Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperatura em Fahrenheit: {fahrenheit:.2f}°F")
print("-" * 30)

# Questão 15
peso = float(input("Questão 15 - Peso da pessoa (kg): "))
altura = float(input("Altura da pessoa (m): "))
imc = peso / altura ** 2
print(f"IMC da pessoa: {imc:.2f}")
print("-" * 30)

# Questão 16
valor_hora = float(input("Questão 16 - Valor recebido por hora: "))
horas_trabalhadas = float(input("Horas trabalhadas no mês: "))
salario_mes = valor_hora * horas_trabalhadas
print(f"Salário do mês: {salario_mes}")
print("-" * 30)

# Questão 17
qtd_produtos = int(input("Questão 17 - Quantidade de produtos vendidos: "))
preco_unitario = float(input("Preço unitário de cada produto: "))
total_venda = qtd_produtos * preco_unitario
print(f"Total da venda: {total_venda}")
print("-" * 30)

# Questão 18
distancia_km = float(input("Questão 18 - Distância em km: "))
velocidade_kmh = float(input("Velocidade média em km/h: "))
tempo_h = distancia_km / velocidade_kmh
print(f"Tempo estimado de viagem: {tempo_h:.2f} horas")
print("-" * 30)

# Questão 19
valor_casa = float(input("Questão 19 - Valor da casa: "))
salario = float(input("Salário do comprador: "))
anos = int(input("Quantos anos deseja financiar: "))
prestacao = valor_casa / (anos * 12)
if prestacao > salario * 0.3:
    print("Financiamento não aprovado.")
else:
    print("Financiamento aprovado.")
print(f"Prestação mensal: {prestacao:.2f}")
print("-" * 30)

# Questão 20
numero = int(input("Questão 20 - Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")
print("-" * 30)

print("Todas as questões foram executadas com sucesso!")

# Questão 21
cidades = []

while len(cidades) < 6:
    cidade = input(f"Digite o nome da cidade {len(cidades)+1}: ").strip()
    opcao = input("Deseja adicionar algo ao nome da cidade? (S/N): ").upper().strip()
    if opcao == "S":
        complemento = input("Digite o que deseja adicionar: ").strip()
        cidade = cidade + " " + complemento
    if cidade in cidades:
        print("Essa cidade já foi inserida! Digite outra.")
    else:
        cidades.append(cidade)

print("\nCidades cadastradas:")
for c in cidades:
    print(c)

cidade_mais_longa = max(cidades, key=len)
print(f"\nA cidade com o nome mais extenso é: {cidade_mais_longa}")
print("-" * 30)

# Questão 22
letra = input("Questão 22 - Digite uma letra: ").upper().strip()
if letra in ["A", "E", "I", "O", "U"]:
    print("Vogal")
else:
    print("Consoante")
print("-" * 30)

# Questão 23
nota1 = float(input("Questão 23 - Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
print("-" * 30)

# Questão 24
palavra1 = input("Questão 24 - Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
palavra3 = input("Digite a terceira palavra: ")
palavras = [palavra1, palavra2, palavra3]
maior = max(palavras, key=len)
print(f"A maior palavra é '{maior}' e tem {len(maior)} caracteres.")
print("-" * 30)

# Questão 25
num1 = float(input("Questão 25 - Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
print("-" * 30)

# Questão 26
preco1 = float(input("Questão 26 - Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))
mais_barato = min(preco1, preco2, preco3)
print(f"O produto mais barato custa R$ {mais_barato:.2f}")
print("-" * 30)

# Questão 27
num1 = float(input("Questão 27 - Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
numeros = [num1, num2, num3]
numeros.sort(reverse=True)
print("Números em ordem decrescente:", numeros)
print("-" * 30)

# Questão 28
turno = input("Questão 28 - Digite seu turno (M-matutino, V-vespertino, N-noturno): ").upper().strip()
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
print("-" * 30)

# Questão 29
salario = float(input("Questão 29 - Digite o salário atual: "))
if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5
valor_aumento = salario * (percentual / 100)
novo_salario = salario + valor_aumento
print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual aplicado: {percentual}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
print("-" * 30)

# Questão 30
valor_hora = float(input("Questão 30 - Digite o valor da hora: "))
horas = float(input("Digite a quantidade de horas trabalhadas: "))
salario_bruto = valor_hora * horas
if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.20
inss = salario_bruto * 0.03
fgts = salario_bruto * 0.11
total_descontos = ir + inss
salario_liquido = salario_bruto - total_descontos
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"(-) IR: R$ {ir:.2f}")
print(f"(-) INSS: R$ {inss:.2f}")
print(f"FGTS: R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
print("-" * 30)

# Questão 31
respostas_sim = 0
perguntas = [
    "Telefonou para a vítima? (S/N) ",
    "Esteve no local do crime? (S/N) ",
    "Mora perto da vítima? (S/N) ",
    "Devia para a vítima? (S/N) ",
    "Já trabalhou com a vítima? (S/N) "
]
for p in perguntas:
    resposta = input(p).upper().strip()
    if resposta == "S":
        respostas_sim += 1
if respostas_sim == 2:
    print("Suspeita")
elif respostas_sim == 3 or respostas_sim == 4:
    print("Cúmplice")
elif respostas_sim == 5:
    print("Assassino")
else:
    print("Inocente")
print("-" * 30)

print("Todas as questões 21 a 31 foram executadas com sucesso!")
