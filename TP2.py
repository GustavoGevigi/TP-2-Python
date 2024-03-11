from datetime import datetime

def menu():
    print("1. Criar um registro")
    print("2. Consultar um registro pelo ID")
    print("3. Listar os registros")
    print("4. Modificar um registro")
    print("5. Apagar um registro")
    print("6. Sair")
    return input("Escolha uma opção: ")

def solicitar_nome():
    nome_completo = input("Digite o nome completo: ")
    return nome_completo.title()

def solicitar_data_nascimento():
    while True:
        data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
        try:
            data_valida = datetime.strptime(data_nascimento, "%d-%m-%Y")
            return data_valida.strftime("%d-%m-%Y")
        except ValueError:
            print("Data inválida. Tente novamente.")

def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    soma = 0
    peso = 10
    for digito in cpf[:-2]:
        soma += int(digito) * peso
        peso -= 1

    resto = soma % 11
    digito_verificador1 = 0 if resto < 2 else 11 - resto

    soma = 0
    peso = 11
    for digito in cpf[:-1]:
        soma += int(digito) * peso
        peso -= 1

    resto = soma % 11
    digito_verificador2 = 0 if resto < 2 else 11 - resto

    return int(cpf[-2]) == digito_verificador1 and int(cpf[-1]) == digito_verificador2

def formatar_cpf(cpf):
    if validar_cpf(cpf):
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    else:
        return False

def solicitar_dados_cadastrais():
    nome = solicitar_nome()
    data_nascimento = solicitar_data_nascimento()

    while True:
        cpf = input("Digite o CPF: ")
        if validar_cpf(cpf):
            cpf_formatado = formatar_cpf(cpf)
            break
        else:
            print("CPF inválido. Tente novamente.")

    email = input("Digite o endereço de email: ")

    return [nome, data_nascimento, cpf_formatado, email]

def imprimir_registro_por_id(registros, id):
    if id < len(registros):
        print(registros[id])
    else:
        print("ID não encontrado.")

def imprimir_registros_ordenados(registros):
    for registro in sorted(registros, key=lambda x: x[0]):
        print(registro)

def remover_registro(registros, id):
    if id < len(registros):
        del registros[id]
        print("Registro removido com sucesso.")
    else:
        print("ID não encontrado.")

def modificar_registro(registros):
    id = int(input("Digite o ID do registro a ser modificado: "))
    registro = registros[id]

    print("Escolha o campo a ser modificado:")
    for i, campo in enumerate(registro):
        print(f"{i + 1}. {campo}")

    campo_escolhido = int(input()) - 1
    novo_valor = input(f"Digite o novo valor para {registro[campo_escolhido]}: ")

    registro[campo_escolhido] = novo_valor

    return id, registro

def modificar_valor_registro(registro, campo, novo_valor):
    registro[campo] = novo_valor
    return registro

def modificar_registro_lista(registros, id, novo_registro):
    if id < len(registros):
        registros[id] = novo_registro
        return registros
    else:
        print("ID não encontrado.")
        return registros

registros = []

while True:
    escolha = menu()

    if escolha == "1":
        novo_registro = solicitar_dados_cadastrais()
        registros.append(novo_registro)
        print("Registro criado com sucesso.")
    elif escolha == "2":
        id_consulta = int(input("Digite o ID do registro a ser consultado: "))
        imprimir_registro_por_id(registros, id_consulta)
    elif escolha == "3":
        imprimir_registros_ordenados(registros)
    elif escolha == "4":
        id_modificacao, novo_registro = modificar_registro(registros)
        registros = modificar_registro_lista(registros, id_modificacao, novo_registro)
        print("Registro modificado com sucesso.")
    elif escolha == "5":
        id_remocao = int(input("Digite o ID do registro a ser removido: "))
        remover_registro(registros, id_remocao)
    elif escolha == "6":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
