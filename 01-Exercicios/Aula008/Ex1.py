#--- Exercício 1  - Funções
#--- Escreva uma função para cadastro de pessoa:
#---       a função deve receber três parâmetros, nome, sobrenome e idade
#---       a função deve salvar os dados da pessoa em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
#---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
#---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada
#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve retornar todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibir uma pessoa específica:
#        a função deve retornar uma pessoa cadastrada na função do ex1 filtrando por id

# pessoa = {"id": id, "nome": nome, "sobrenome" : sobrenome}}
# pessoas = [pessoa1, pessoa2]

pessoas = []
pessoa = {}
id_pessoa = 0

def cadastro_Pessoa(nome, sobrenome, idade):
    global id_pessoa
    id_pessoa += 1
    pessoa = {"id_pessoa": id_pessoa}
    pessoa['nome'] = nome
    pessoa['sobrenome'] = sobrenome
    pessoa['idade'] = idade
    pessoas.append(pessoa)
    dados_cadastrados_pessoa = [nome, sobrenome, idade]
    return id_pessoa
         
def mostrar_Dados():
    for i in pessoas:
        print(f"ID: {i['id_pessoa']}")
        print(f"Nome: {i['nome']}")
        print(f"Sobrenome: {i['sobrenome']}")
        print(f"Idade: {i['idade']}")

def pesquisa_Pessoa():
    id_especifico = input("Insira o ID a ser pesquisado: ")
    arquivo = open("cadastro.txt", 'r')
    if (int(id_especifico) < len(pessoas) or (int(id_especifico) > 0)):
        if id_pessoa == (int(id_especifico)):
            mostrar_Dados()
        else:
            print("Id não encontrado")

    for linha in arquivo:
        limpa_linha = linha.strip()
        lista_dados = limpa_linha.split(',')
        if id_especifico == lista_dados[0]:
            print(f"""Dados do Arquivo:
            ID: {lista_dados[0]}
            Nome: {lista_dados[1]}
            Sobrenome: {lista_dados[2]}
            Idade: {lista_dados[3]}""")
            
    arquivo.close()
            