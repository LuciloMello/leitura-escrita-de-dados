import os
os.system('cls')

nome_arquivo = "dados.txt"

while True:
    print("Escolha uma opção:")
    print("1. Ler o arquivo")
    print("2. Escrever no arquivo")
    print("3. Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        try:
            with open(nome_arquivo, "r") as arquivo:
                conteudo = arquivo.read()
                if conteudo:
                    print("Conteúdo do arquivo:")
                    print(conteudo)
                else:
                    print("O arquivo está vazio.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
    elif opcao == "2":
        try:
            with open(nome_arquivo, "r") as arquivo:
                numeros = [int(num.strip()) for num in arquivo if num.strip().isdigit()]
        except FileNotFoundError:
            numeros = []
        
        novo_numero = int(input("Digite um número: "))
        if not numeros or novo_numero > max(numeros):
            with open(nome_arquivo, "a") as arquivo:
                arquivo.write(str(novo_numero) + "\n")
            print("Número adicionado.")
        else:
            print("O número não é maior que os existentes.")
    elif opcao == "3":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida.")