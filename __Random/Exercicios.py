'''Escreva um programa que peça ao usuário para digitar
 seu nome e, em seguida, imprima uma mensagem de boas-vindas com o nome fornecido.'''

'''nome=input("Digite seu nome")
print("Seja bem vindo" , nome)'''

'''Crie duas variáveis, numero1 e numero2, e atribua a elas valores inteiros.
 Calcule a soma, subtração, multiplicação e divisão dessas variáveis e imprima os resultados.'''

'''num1= 10
num2 = 12

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print("Aqui está a soma", soma)
print("Aqui está a subtração", subtracao)
print("Aqui está a multiplicacao", multiplicacao)
print("Aqui está a divisão", divisao)'''

'''Crie uma variável chamada saldo com o valor 500.50 (float). Em seguida, crie uma variável saque com o valor 200.25 (float).
 Subtraia o saque do saldo e imprima o saldo final formatado para duas casas decimais.'''

'''saldo = 500.50
saque = 200.25

subtracao = saldo - saque 
print("este é o resultado:", subtracao)'''

'''Declare uma variável booleana chamada **tem_carteira_de_motorista** e atribua a ela o valor True. Imprima uma 
mensagem que diga "Pode dirigir" se a variável for verdadeira e "Não pode dirigir" caso contrário.'''

'''tem_carteira_de_motorista = True
if tem_carteira_de_motorista:
    print("Pode dirigir")
else:   
    print("Não pode dirigir")'''

'''Crie duas variáveis:

idade_ana = 25
idade_beto = 30
Use operadores de 
comparação para verificar se a idade de Ana é menor que a de Beto e imprima o resultado booleano.'''

'''idade_ana = 25  
idade_beto = 30
if idade_ana < idade_beto:
    print("A idade de Ana é menor que a de Beto")
else:
    print("A idade de Ana não é menor que a de Beto")'''

'''Receba um número inteiro do usuário e use o operador d
e módulo (%) para verificar se o número é par ou ímpar. Imprima o resultado.
Obs:  Não estudamos ainda os condicionais, mas pesquise se necessário e tente resolver.'''

'''numero=int(input("Digite um número inteiro: \n"))
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")'''

'''Crie duas variáveis booleanas:

chovendo = True
guarda_chuva = False
Use operadores lógicos para 
verificar se uma pessoa vai se molhar (se está chovendo E ela não tem guarda-chuva).'''

chovendo = True
guarda_chuva = False
if chovendo and not guarda_chuva:
    print("A pessoa vai se molhar")
else:
    print("A pessoa não vai se molhar")

'''Calcule a potência de 2 elevado a 10 e imprima o resultado.'''
resultado = 2 ** 10
print("O resultado é:", resultado)

'''Converta a string "2026" para um tipo inteiro e armazene-a em uma variável chamada ano. Em seguida, some 1 a essa variável e imprima o novo ano.'''
ano = int("2026")
novo_ano = ano + 1
print("O novo ano é:", novo_ano)

'''Crie a string:

frase = " Python é uma linguagem poderosa e estou aprendendo com a DSA ".

Remova os espaços em branco do início e do fim da string e imprima a nova string.'''
'''frase = " Python é uma linguagem poderosa e estou aprendendo com a DSA "
nova_frase = frase.strip()
print("A nova frase é:", nova_frase)'''

'''Na string do exercício anterior (já sem os espaços), converta toda a frase para letras maiúsculas.'''
frase = " Python é uma linguagem poderosa e estou aprendendo com a DSA "
nova_frase = frase.upper()
print("A frase em maiúscula é:", nova_frase)

'''Escreva um programa que peça ao usuário para digitar sua altura em metros (ex: 1.75) e seu peso em quilogramas (ex: 68.5). Calcule o Índice de Massa Corporal (IMC) usando a fórmula IMC = peso / (altura * altura) e imprima o resultado formatado com duas casas decimais.
'''
altura = float(input("Digite sua altura em metros (ex: 1.75): "))
peso = float(input("Digite seu peso em quilogramas (ex: 68.5): "))
imc = peso / (altura * altura)
print("Seu imc é:", imc)

'''faça um jogo de pedra papel e tesoura com dois jogadores'''
jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ")
jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ")
if jogador1 == jogador2:
    print("Empate!")
elif (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "papel" and jogador2 == "pedra") or (jogador1 == "tesoura" and jogador2 == "papel"):
    print("Jogador 1 vence!")
else:
    print("Jogador 2 vence!")


''' agora faça o jogo com um menu inicial o jogador 1 faz a escolha e o jogador faz outra coloca as opções validas depois faz o jogo e mantem em um loop ate que o usuario escolha sair'''
while True:
    print("Menu:")
    print("1. Jogar Pedra, Papel ou Tesoura")
    print("2. Sair")
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == "1":
        jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ")
        jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ")
        
        if jogador1 == jogador2:
            print("Empate!")
        elif (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "papel" and jogador2 == "pedra") or (jogador1 == "tesoura" and jogador2 == "papel"):
            print("Jogador 1 vence!")
        else:
            print("Jogador 2 vence!")
    elif escolha == "2":
        print("Saindo do jogo. Até a próxima!")
        break
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")



'''Escreva uma função que receba os valores de três lados de um triângulo e o classifique como "Equilátero" (todos os lados iguais), "Isósceles" (dois lados iguais) ou "Escaleno" (todos os lados diferentes).'''
def classificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"
lado1 = float(input("Digite o valor do lado 1 do triângulo: "))
lado2 = float(input("Digite o valor do lado 2 do triângulo: "))
lado3 = float(input("Digite o valor do lado 3 do triângulo: "))
resultado = classificar_triangulo(lado1, lado2, lado3)
print("O triângulo é:", resultado)

###
## Escrever o que eu aprendi no projeto desenvolvido 

'''Escreva uma função que recebe um número inteiro e exibe a tabuada de multiplicação desse número, do 1 ao 10.'''
def tabuada(numero):
    for i in range (1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
numero = int(input("Digite um número inteiro para ver a tabuada: "))
tabuada(numero)
print("Aqui está a tabuada do número", numero)


'''Você recebeu um dicionário com os nomes dos alunos e suas respectivas notas. Escreva uma função que calcula a média da turma e retorna uma lista com os nomes dos alunos que tiveram nota acima da média.'''
def alunos_acima_da_media(alunos_notas):
    media = sum(alunos_notas.values()) / len(alunos_notas)
    alunos_acima = [aluno for aluno, nota in alunos_notas.items() if nota > media]
    return alunos_acima
alunos_notas = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Eve": 70
}
alunos_acima = alunos_acima_da_media(alunos_notas)
print("Alunos com nota acima da média:", alunos_acima)

'''resultado obtido no curso da DSA'''
def dsa_alunos_acima_da_media(turma):
    
    """
    Calcula a média da turma e retorna os alunos com nota superior à média.
    """
    
    if not turma:
        return "Dicionário de turma vazio."

    # Calcula a soma de todas as notas
    soma_notas = sum(turma.values())
    
    # Calcula a média
    media = soma_notas / len(turma)
    print(f"A média da turma é: {media:.2f}")

    # Itera sobre o dicionário para encontrar alunos acima da média
    aprovados = []
    
    for aluno, nota in turma.items():
        if nota > media:
            aprovados.append(aluno)

    return aprovados

# Dados de exemplo
notas_turma = {"Ana": 8.5, "Bruno": 6.0, "Carla": 9.5, "Marcelo": 7.0, "Eliane": 5.5}

# Chama a função
print(f"Alunos acima da média: {dsa_alunos_acima_da_media(notas_turma)}")


# testando try/except
try:
    numero = int(input("Digite um número: \n"))
    resultado = 10 / numero
    print("O resultado é", resultado)
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")

