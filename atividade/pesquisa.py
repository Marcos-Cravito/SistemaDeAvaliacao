# Contadores do resultado.
quantidade_excelente = 0
quantidade_bom = 0
quantidade_ruim = 0

# Para testar com outra quantia de pessoa basta trocar o valor dentro de range(x)
for pessoa in range(3):
    print("\nEntrevistado", pessoa + 1)

    # Não aceita um nome vazio.
    while True:
        print("Digite seu nome:")
        nome = input().strip() #strip é pra evitar que aja espaços do nome caso o usuário insira

        if nome.replace(" ", "").isalpha(): #o isalpha aqui reconhece se o texto escrito tem só texto(pra evitar que o usuário insira números ou outras coisas)
            break
        else:
            print("O nome não pode ficar vazio.")

    # Aceita apenas idades a partir de 18 anos.
    while True:
        print("Digite sua idade:")

        try:
            idade = int(input())

            if idade < 18 or idade >= 120:
                print("É necessário ter 18 anos ou menos de 120.")
            else:
                break
        except ValueError:
            print("Digite a idade usando apenas números inteiros.")

    # Repete até receber uma das três opções.
    while True:
        print("Qual sua opinião sobre o atendimento?")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")
        opiniao = input().strip()

        if opiniao in ("1", "2", "3"):
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")

    # Funções para cada opinião.
    def excelente():
        print("Você avaliou o atendimento como EXCELENTE.")

    def bom():
        print("Você avaliou o atendimento como BOM.")

    def ruim():
        print("Você avaliou o atendimento como RUIM.")

    # Verifica a opinião e conta as respostas.
    if opiniao == "1":
        excelente()
        quantidade_excelente += 1
    elif opiniao == "2":
        bom()
        quantidade_bom += 1
    elif opiniao == "3":
        ruim()
        quantidade_ruim += 1

# Mostra o resultado final.
print("\nRESULTADO DA PESQUISA")
print("Respostas EXCELENTE:", quantidade_excelente)
print("Respostas BOM:", quantidade_bom)
print("Respostas RUIM:", quantidade_ruim)