#--- Exercício 4  - Funções
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável de nome da empresa (passada por parametro)
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita com base em uma variável que contenha o caracter a ser multiplicado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console

nome_empresa = input("Nome da empresa: ")
separacao = "-"

def cabecalho():
    print(separacao*10 , nome_empresa, separacao*10)

def rodape():
    print(separacao*10, f"{nome_empresa} agradece a preferência", separacao*10)

cabecalho()
rodape()
