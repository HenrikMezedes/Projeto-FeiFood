 FEIFood – Sistema de Delivery em Python

O **FEIFood** é um sistema de entrega de comida feito totalmente em Python, utilizando manipulação de arquivos (`.txt`) para armazenar usuários, cardápio e pedidos.  
O projeto funciona no terminal e simula um aplicativo de delivery, com as funções principais de um sistema real.

---

Funcionalidades

 **Sistema de Usuários**
- Criar conta
- Login
- Senhas salvas em arquivo (`usuarios.txt`)

 **Cardápio**
- Exibido por categorias
- Cada item possui:
  - Código  
  - Nome  
  - Preço  
  - Categoria  
  - Nota média (baseada nas avaliações)

 **Carrinho**
- Adicionar itens
- Remover itens
- Calcular total automático

**Pedidos**
- Finalizar pedido
- Listar pedidos anteriores
- Cada pedido contém:
  - Número
  - Cliente
  - Itens
  - Valor total
  - Data e hora
  - Situação
  - Avaliação

**Avaliações**
- Sistema de avaliação de 1 a 5 estrelas
- Ao avaliar um pedido:
  - A avaliação é registrada no pedido
  - A nota do item no cardápio é atualizada automaticamente (média)

---

Estrutura dos Arquivos

O programa cria automaticamente 3 arquivos na mesma pasta:
FEIFood
├── usuarios.txt
├── cardapio.txt
└── pedidos.txt



---

Tecnologias Utilizadas

- **Python 3**
- Manipulação de arquivos (`open`, `readlines`, `write`)
- Estruturas de dados: listas e dicionários
- Formatação com f-strings

---

 Exemplo de Cardápio no arquivo
 
1|Hambúrguer|22.50|Lanches|5
2|Pizza Calabresa|38.90|Pizzas|4
3|Suco de Laranja|7.50|Bebidas|5


