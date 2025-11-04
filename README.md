🍽️ API de Pedidos do Restaurante

Bem-vindo à API de Pedidos do Restaurante!
Este projeto tem como objetivo gerenciar pedidos de clientes de forma simples e prática.
Você poderá criar, listar, atualizar e deletar pedidos através de requisições HTTP.

📋 Sumário

Cardápio

Como Registrar um Pedido

Exemplo de Requisição

Pedidos para Teste

Rotas da API

Próximos Passos

🍕 Cardápio
🥘 Pratos
Prato	Descrição	Preço
🍕 Pizza Margherita	Molho de tomate, queijo mozzarella e manjericão.	R$ 30
🍔 Hambúrguer Suculento	Queijo cheddar, alface, tomate e molho especial.	R$ 25
🍲 Feijoada Tradicional	Acompanha arroz, farofa, couve e laranja.	R$ 40
🍹 Bebidas
Bebida	Descrição	Preço
🥤 Coca-Cola	Refrigerante clássico e gelado.	R$ 5
🍊 Suco de Laranja	Natural, sem conservantes.	R$ 7,50
💧 Água Mineral	Pura e refrescante.	R$ 3
📲 Como Registrar um Pedido

Para registrar um pedido, use o método POST no endpoint /pedidos.

🧾 Exemplo de Pedido

A mesa 1 fez o pedido de:

Prato: 🍔 Hambúrguer Suculento

Bebida: 🥤 Coca-Cola

Mesa: 1

Exemplo de Requisição

Método: POST
Endpoint: /pedidos

Corpo da Requisição (JSON):

{
  "nome": "Hambúrguer Suculento",
  "bebida": "Coca-Cola",
  "mesa": 1
}

🍽 Pedidos para Teste

Aqui estão 5 pedidos que você pode usar para testar a API:

Mesa	Prato	Bebida
1	🍕 Pizza Margherita	🥤 Coca-Cola
2	🍔 Hambúrguer Suculento	🍊 Suco de Laranja
3	🍲 Feijoada Tradicional	💧 Água Mineral
4	🍕 Pizza Margherita	🥤 Coca-Cola
5	🍔 Hambúrguer Suculento	🥤 Coca-Cola
⚙️ Rotas da API
Método	Endpoint	Descrição
POST	/pedidos	Criar um novo pedido
GET	/pedidos	Listar todos os pedidos
PUT	/pedidos/{id}	Atualizar um pedido específico
DELETE	/pedidos/{id}	Deletar um pedido específico
🚀 Próximos Passos

Realize os pedidos da Mesa 1 até a Mesa 5 utilizando o método POST /pedidos.

Teste a API para garantir que os pedidos estão sendo criados corretamente.

Utilize os métodos PUT e DELETE para simular atualizações ou exclusões.

💡 Dica

Use ferramentas como Postman ou Insomnia para testar os endpoints da API.
Assim, você poderá visualizar as requisições e respostas com facilidade.
