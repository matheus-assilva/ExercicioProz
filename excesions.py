import datetime

def validar_ano(ano):
    if ano.isdigit():
        ano = int(ano)
        if 1922 <= ano <= 2021:
            return True
    return False

nome = input("Digite seu nome completo: ")

ano_nascimento = input("Digite seu ano de nascimento: ")
while not validar_ano(ano_nascimento):
    print("Erro: ano inválido. Por favor, insira um ano entre 1922 e 2021.")
    ano_nascimento = input("Digite seu ano de nascimento: ")

ano_atual = datetime.datetime.now().year
idade = ano_atual - int(ano_nascimento)

print(f"Nome: {nome}\nIdade: {idade}")