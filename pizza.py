# Cria um dicionário vazio para armazenar os nomes e sabores de pizza
pizzas = {}

# Coleta os dados de 2 pessoas (mas é só mudar se quiser mais)
for i in range(2):
    nome = input("Digite seu nome: ") # Pede o nome da pessoa
    sabor = input("Digite seu sabor de pizza: ") # Pede o sabor de pizza

    pizzas[nome] = sabor # Associa o nome ao sabor dentro do dicionário

# Exibe as informações formatadas
for key,values in pizzas.items():
    print(f"-{key.title()}: {values.lower()}")