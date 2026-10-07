# Sistema de Controle de Inventário de Equipamentos
lista = []

# Função para preencher o inventário
def preeccherinventario(lista):
    resposta = "S"
    while resposta == "S":
        equipamento = [
            input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            input("Departamento: ")
        ]
        lista.append(equipamento)
        resposta = input("Digite (S) para continuar: ").upper()

# Função para exibir o inventário
def exibirinventario(lista):
    print("\n=== Inventário ===")
    for elemento in lista:
        print(f"Nome: {elemento[0]}")
        print(f"Valor: R$ {elemento[1]:.2f}")
        print(f"Serial: {elemento[2]}")
        print(f"Departamento: {elemento[3]}")
        print("-" * 30)


# Função para localizar o equipamento por nome
def localizarpornome(lista):
    busca = input("\nDigite o nome do equipamento que deseja localizar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print(f"\nEquipamento encontrado!")
            print(f"Valor: R$ {elemento[1]:.2f}")
            print(f"Serial: {elemento[2]}")


# Função para depreciar o equipamento
def depreciarpornome(lista):
    depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print(f"Valor antigo: R$ {elemento[1]:.2f}")
            elemento[1] *= 0.90
            print(f"Novo valor: R$ {elemento[1]:.2f}")


# Função para excluir o serial do equipamento
def excluirporserial(lista):
    serial = (input("\nDigite o serial do equipamento para remover: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
            print("Equipamento removido!")
            break


# Função para resumir os valores
def resumirvalores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])

    if len(valores) > 0:
        print(f"\nEquipamento mais caro: R$ {max(valores):.2f}")
        print(f"Equipamento mais barato: R$ {min(valores):.2f}")
        print(f"Valor total do inventário: R$ {sum(valores):.2f}")
    else:
        print("\nO inventário está vazio.")
