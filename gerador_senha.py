import random
import string
import os

def gerar_senha(tamanho=12, incluir_numeros=True, incluir_especiais=True):
    caracteres = string.ascii_letters
    
    if incluir_numeros:
        caracteres += string.digits
    
    if incluir_especiais:
        caracteres += string.punctuation
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def salvar_e_abrir_senha(nome_usuario, uso, senha):
    with open("senhas.txt", "a") as arquivo:
        arquivo.write(f"Usuário: {nome_usuario} | Uso: {uso} | Senha: {senha}\n")
    print(f"Senha salva para {nome_usuario} ({uso}) no arquivo 'senhas.txt'!")
    os.startfile("senhas.txt")  # Para Windows
    # Para Linux: os.system("xdg-open senhas.txt")
    # Para Mac: os.system("open senhas.txt")

# Interação com o usuário
nome_usuario = input("Digite seu nome de usuário: ")
uso_senha = input("Para que esta senha será usada? (ex: E-mail, Banco): ")
print("\nGerando uma senha para você...")

while True:
    senha_gerada = gerar_senha()
    print(f"Sua senha gerada é: {senha_gerada}")
    aceita = input("Você gostou desta senha? (s/n): ").lower()
    
    if aceita == "s":
        confirmacao = input("Deseja salvar esta senha? (s/n): ").lower()
        if confirmacao == "s":
            salvar_e_abrir_senha(nome_usuario, uso_senha, senha_gerada)
            break
        else:
            print("Senha não salva. Programa encerrado.")
            break
    else:
        print("Ok, gerando outra senha...\n")
