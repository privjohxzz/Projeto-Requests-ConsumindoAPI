import requests

print("Nosso Cardápio Especial! 🍕🍔🥤\n")

print("pratos🍽️")
pratos = [
    "pizza - R$ 30",
    "hamburguer - R$ 25",
    "feijoada - R$ 40"
]

for prato in pratos:
    print(prato)

print("\nbebidas🥤")
bebidas = [
    "Coca Cola - R$ 5",
    "agua - R$ 3",
    "suco de laranja - R$ 7,5"
]

for bebida in bebidas:
    print(bebida)

print("\nmesas 🪑")
mesas_disponiveis = [
    "mesa 1", "mesa 2", "mesa 3", "mesa 4", 
    "mesa 5", "mesa 6", "mesa 7", "mesa 8", 
    "mesa 9", "mesa 10"
]

for mesa in mesas_disponiveis:
    print(mesa)

pedido_prato = input("\nEscolha o prato (ex: pizza, hamburguer, feijoada): ")
pedido_bebida = input("Escolha a bebida (ex: Coca Cola, agua, suco de laranja): ")
pedido_mesa = input("Escolha a mesa (ex: mesa 1, mesa 2, etc.): ")


pedido = {
    'prato': pedido_prato,
    'bebida': pedido_bebida,
    'mesa': pedido_mesa
}

response = requests.post('https://68c9623cceef5a150f649f73.mockapi.io/API/restaurante', json=pedido)

pedidosfeito = input("deseja conferir pedidos ja feitos? ex:(sim/nao): ")

if pedidosfeito == "sim":
    pratosDaAPI=requests.get('https://68c9623cceef5a150f649f73.mockapi.io/API/restaurante')
    print(pratosDaAPI.json())

else:
    print("ok!")

alteracao = input('deseja realaizar a alteraçao do seu pedido?: ex:(sim/nao):')

if alteracao == 'sim':
    pratosDaAPI=requests.get('https://68c9623cceef5a150f649f73.mockapi.io/API/restaurante')
    print(pratosDaAPI.json())
    id= input('digite o id do seu pedido: ')

    
    pedido_prato = input("\nEscolha o prato (ex: pizza, hamburguer, feijoada): ")
    pedido_bebida = input("Escolha a bebida (ex: Coca Cola, agua, suco de laranja): ")
    pedido_mesa = input("Escolha a mesa (ex: mesa 1, mesa 2, etc.): ")
    pedidonovo={
        'prato': pedido_prato,
        'bebida': pedido_bebida,
        'mesa': pedido_mesa
    }
    print("novo pedido realizado")
else:
    print("ok!")

requests.put(f'https://68c9623cceef5a150f649f73.mockapi.io/API/restaurante/{id}',pedidonovo)




excluir = input("deseja excluir algum pedido ?: ex: (sim/nao):")

if excluir == 'sim':
    pratosDaAPI=requests.get('https://68c9623cceef5a150f649f73.mockapi.io/API/restaurante')
    print(pratosDaAPI.json())
    id= input('digite o id do seu pedido: ')
    print('excluido com sucesso')
else:
    print('ok!')
requests.delete(f'https://68c9623cceef5a150f649f73.mockapi.io/API/restaurante/{id}')