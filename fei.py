usuarios = {}
cardapio = []
pedidos = []
usuario_logado = None
carrinho = []

def carregar_usuarios():
    global usuarios
    usuarios = {}
    
    arquivo = open("usuarios.txt", "r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()
    
    for linha in linhas:
        linha = linha.strip()
        if linha and ":" in linha:
            partes = linha.split(":")
            nome = partes[0]
            senha = partes[1]
            usuarios[nome] = senha

def salvar_usuarios():
    arquivo = open("usuarios.txt", "w", encoding="utf-8")
    for nome, senha in usuarios.items():
        arquivo.write(f"{nome}:{senha}\n")
    arquivo.close()

def carregar_cardapio():
    global cardapio
    cardapio = []
    
    arquivo = open("cardapio.txt", "r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()
    
    for linha in linhas:
        linha = linha.strip()
        if linha and "|" in linha:
            partes = linha.split("|")
            if len(partes) == 5:
                item = {
                    "codigo": int(partes[0]),
                    "nome": partes[1],
                    "preco": float(partes[2]),
                    "categoria": partes[3],
                    "nota": float(partes[4])
                }
                cardapio.append(item)

def salvar_cardapio():
    arquivo = open("cardapio.txt", "w", encoding="utf-8")
    for item in cardapio:
        linha = f"{item['codigo']}|{item['nome']}|{item['preco']}|{item['categoria']}|{item['nota']}\n"
        arquivo.write(linha)
    arquivo.close()

def carregar_pedidos():
    global pedidos
    pedidos = []
    
    arquivo = open("pedidos.txt", "r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()
    
    for linha in linhas:
        linha = linha.strip()
        if linha and "|" in linha:
            partes = linha.split("|")
            if len(partes) >= 6:
                itens_pedido = []
                itens_texto = partes[2]
                if itens_texto:
                    lista_itens = itens_texto.split(";")
                    for item_texto in lista_itens:
                        if item_texto:
                            dados_item = item_texto.split(",")
                            if len(dados_item) == 5:
                                item = {
                                    "codigo": int(dados_item[0]),
                                    "nome": dados_item[1],
                                    "preco": float(dados_item[2]),
                                    "categoria": dados_item[3],
                                    "nota": float(dados_item[4])
                                }
                                itens_pedido.append(item)
                
                pedido = {
                    "numero": int(partes[0]),
                    "cliente": partes[1],
                    "itens": itens_pedido,
                    "valor_total": float(partes[3]),
                    "data": partes[4],
                    "situacao": partes[5],
                    "avaliacao": int(partes[6]) if partes[6] != "Nenhuma" else None
                }
                pedidos.append(pedido)

def salvar_pedidos():
    arquivo = open("pedidos.txt", "w", encoding="utf-8")
    for pedido in pedidos:
        texto_itens = ""
        for item in pedido["itens"]:
            texto_itens += f"{item['codigo']},{item['nome']},{item['preco']},{item['categoria']},{item['nota']};"
        
        avaliacao_texto = str(pedido["avaliacao"]) if pedido["avaliacao"] is not None else "Nenhuma"
        linha = f"{pedido['numero']}|{pedido['cliente']}|{texto_itens}|{pedido['valor_total']}|{pedido['data']}|{pedido['situacao']}|{avaliacao_texto}\n"
        arquivo.write(linha)
    arquivo.close()

def carregar_tudo():
    carregar_usuarios()
    carregar_cardapio()
    carregar_pedidos()

def salvar_tudo():
    salvar_usuarios()
    salvar_cardapio()
    salvar_pedidos()

def mostrar_cabecalho():
    print("\n" + "="*60)
    print("              FEIFOOD - ENTREGA DE COMIDA")
    print("="*60)

def tela_principal():
    carregar_tudo()
    
    while True:
        mostrar_cabecalho()
        print("\nOla! Bem-vindo ao FEIFood!")
        print("\nO que voce gostaria de fazer?")
        print("1 - Entrar na minha conta")
        print("2 - Criar uma conta nova")
        print("3 - Sair do aplicativo")
        
        escolha = input("\nDigite o numero da sua escolha: ")
        
        if escolha == "1":
            entrar_conta()
        elif escolha == "2":
            criar_conta()
        elif escolha == "3":
            print("\nObrigado por usar o FEIFood! Volte sempre!")
            break
        else:
            print("\nOpcao invalida! Por favor, escolha 1, 2 ou 3.")

def entrar_conta():
    global usuario_logado
    
    mostrar_cabecalho()
    print("\nENTRAR NA CONTA")
    
    nome_usuario = input("\nSeu nome de usuario: ")
    senha_usuario = input("Sua senha: ")
    
    if nome_usuario in usuarios and usuarios[nome_usuario] == senha_usuario:
        print(f"\nLogin feito com sucesso! Bem-vindo(a), {nome_usuario}!")
        usuario_logado = nome_usuario
        menu_cliente()
    else:
        print("\nUsuario ou senha incorretos!")
        input("\nPressione Enter para tentar novamente...")

def criar_conta():
    mostrar_cabecalho()
    print("\nCRIAR NOVA CONTA")
    
    novo_usuario = input("\nEscolha um nome de usuario: ")
    
    if novo_usuario in usuarios:
        print("Este nome de usuario ja esta sendo usado!")
        return
    
    nova_senha = input("Crie uma senha: ")
    confirmar_senha = input("Digite a senha novamente para confirmar: ")
    
    if nova_senha != confirmar_senha:
        print("As senhas nao sao iguais!")
        return
    
    usuarios[novo_usuario] = nova_senha
    salvar_usuarios()
    print(f"\nConta criada com sucesso! Bem-vindo(a) ao FEIFood, {novo_usuario}!")
    input("\nPressione Enter para fazer login...")

def menu_cliente():
    while True:
        mostrar_cabecalho()
        print(f"\nOla, {usuario_logado}!")
        print("\nO que voce gostaria de fazer hoje?")
        print("1 - Ver cardapio e fazer pedido")
        print("2 - Ver meu carrinho")
        print("3 - Ver meus pedidos anteriores")
        print("4 - Avaliar um pedido")
        print("5 - Sair da minha conta")
        
        escolha = input("\nDigite o numero da sua escolha: ")
        
        if escolha == "1":
            fazer_pedido()
        elif escolha == "2":
            ver_carrinho()
        elif escolha == "3":
            ver_pedidos_anteriores()
        elif escolha == "4":
            avaliar_pedido()
        elif escolha == "5":
            print("\nSaindo da sua conta...")
            break
        else:
            print("\nOpcao invalida! Escolha um numero de 1 a 5.")

def fazer_pedido():
    while True:
        mostrar_cabecalho()
        print("\nFAZER PEDIDO")
        
        categorias_disponiveis = []
        for item in cardapio:
            if item["categoria"] not in categorias_disponiveis:
                categorias_disponiveis.append(item["categoria"])
        
        print("\nEscolha uma categoria:")
        for numero, categoria in enumerate(categorias_disponiveis, 1):
            print(f"{numero} - {categoria}")
        
        print(f"{len(categorias_disponiveis) + 1} - Ver meu carrinho")
        print(f"{len(categorias_disponiveis) + 2} - Finalizar pedido")
        print(f"{len(categorias_disponiveis) + 3} - Voltar ao menu")
        
        escolha = input(f"\nDigite sua escolha (1-{len(categorias_disponiveis) + 3}): ")
        
        if escolha.isdigit():
            numero_escolha = int(escolha)
            
            if 1 <= numero_escolha <= len(categorias_disponiveis):
                categoria_escolhida = categorias_disponiveis[numero_escolha - 1]
                mostrar_itens_categoria(categoria_escolhida)
            elif numero_escolha == len(categorias_disponiveis) + 1:
                ver_carrinho()
            elif numero_escolha == len(categorias_disponiveis) + 2:
                finalizar_pedido()
                if not carrinho:
                    return
            elif numero_escolha == len(categorias_disponiveis) + 3:
                return
            else:
                print("\nOpcao invalida!")
        else:
            print("\nPor favor, digite um numero!")
        
        input("\nPressione Enter para continuar...")

def mostrar_itens_categoria(categoria):
    mostrar_cabecalho()
    print(f"\n{categoria.upper()}")
    
    itens_categoria = []
    for item in cardapio:
        if item["categoria"] == categoria:
            itens_categoria.append(item)
    
    if not itens_categoria:
        print("Nenhum item encontrado nesta categoria!")
        input("\nPressione Enter para voltar...")
        return
    
    print("\nItens disponiveis:")
    for numero, item in enumerate(itens_categoria, 1):
        estrelas = "*" * int(item["nota"])
        print(f"{numero} - {item['nome']:25} R$ {item['preco']:6.2f} {estrelas}")
    
    print(f"\n{len(itens_categoria) + 1} - Voltar para categorias")
    
    escolha = input(f"\nDigite o numero do item (1-{len(itens_categoria) + 1}): ")
    
    if escolha.isdigit():
        numero_item = int(escolha)
        if 1 <= numero_item <= len(itens_categoria):
            item_escolhido = itens_categoria[numero_item - 1]
            carrinho.append(item_escolhido)
            print(f"\n{item_escolhido['nome']} adicionado ao carrinho!")
        elif numero_item == len(itens_categoria) + 1:
            return
        else:
            print("\nOpcao invalida!")
    else:
        print("\nPor favor, digite um numero!")
    
    input("\nPressione Enter para continuar...")

def ver_carrinho():
    mostrar_cabecalho()
    print("\nMEU CARRINHO")
    
    if not carrinho:
        print("\nSeu carrinho esta vazio!")
        input("\nPressione Enter para voltar...")
        return
    
    total = 0
    for numero, item in enumerate(carrinho, 1):
        print(f"{numero} - {item['nome']:25} R$ {item['preco']:6.2f}")
        total += item["preco"]
    
    print("-" * 40)
    print(f"TOTAL: R$ {total:.2f}")
    
    print("\nO que voce gostaria de fazer?")
    print("1 - Remover um item")
    print("2 - Finalizar pedido")
    print("3 - Continuar comprando")
    
    escolha = input("\nDigite sua escolha: ")
    
    if escolha == "1":
        remover_item_carrinho()
    elif escolha == "2":
        finalizar_pedido()
    elif escolha == "3":
        return
    else:
        print("\nOpcao invalida!")

def remover_item_carrinho():
    if not carrinho:
        return
    
    numero = input("Digite o numero do item que quer remover: ")
    if numero.isdigit():
        posicao = int(numero) - 1
        if 0 <= posicao < len(carrinho):
            item_removido = carrinho.pop(posicao)
            print(f"\n{item_removido['nome']} removido do carrinho!")
        else:
            print("\nNumero invalido!")
    else:
        print("\nPor favor, digite um numero!")

def finalizar_pedido():
    global carrinho, pedidos
    
    if not carrinho:
        print("\nSeu carrinho esta vazio!")
        return
    
    mostrar_cabecalho()
    print("\nFINALIZAR PEDIDO")
    
    valor_total = 0
    print("\nRESUMO DO SEU PEDIDO:")
    for item in carrinho:
        print(f"  - {item['nome']:25} R$ {item['preco']:6.2f}")
        valor_total += item["preco"]
    
    print("-" * 40)
    print(f"VALOR TOTAL: R$ {valor_total:.2f}")
    
    confirmar = input("\nTem certeza que quer finalizar este pedido? (S/N): ").upper()
    
    if confirmar == "S":
        from datetime import datetime
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        novo_pedido = {
            "numero": len(pedidos) + 1,
            "cliente": usuario_logado,
            "itens": carrinho.copy(),
            "valor_total": valor_total,
            "data": data_hora,
            "situacao": "Entregue",
            "avaliacao": None
        }
        
        pedidos.append(novo_pedido)
        salvar_pedidos()
        
        print(f"\nPEDIDO CONFIRMADO!")
        print(f"Numero do pedido: #{novo_pedido['numero']}")
        print(f"Cliente: {usuario_logado}")
        print(f"Valor total: R$ {valor_total:.2f}")
        print(f"Data: {data_hora}")
        print("\nSeu pedido esta sendo preparado!")
        print("Aguarde a entrega!")
        
        carrinho = []
        
        avaliar = input("\nGostaria de avaliar o pedido agora? (S/N): ").upper()
        if avaliar == "S":
            avaliar_pedido_especifico(novo_pedido["numero"])
    else:
        print("\nPedido cancelado. Seus itens continuam no carrinho.")
    
    input("\nPressione Enter para continuar...")

def ver_pedidos_anteriores():
    mostrar_cabecalho()
    print("\nMEUS PEDIDOS ANTERIORES")
    
    meus_pedidos = []
    for pedido in pedidos:
        if pedido["cliente"] == usuario_logado:
            meus_pedidos.append(pedido)
    
    if not meus_pedidos:
        print("\nVoce ainda nao fez nenhum pedido!")
        input("\nPressione Enter para voltar...")
        return
    
    print(f"\nVoce fez {len(meus_pedidos)} pedido(s) no total:")
    
    for i in range(len(meus_pedidos)-1, -1, -1):
        pedido = meus_pedidos[i]
        print(f"\nPedido #{pedido['numero']} - {pedido['data']}")
        print(f"Situacao: {pedido['situacao']}")
        for item in pedido["itens"]:
            print(f"   - {item['nome']:25} R$ {item['preco']:6.2f}")
        print(f"Total: R$ {pedido['valor_total']:.2f}")
        
        if pedido["avaliacao"]:
            estrelas = "*" * pedido["avaliacao"]
            print(f"Avaliacao: {estrelas} ({pedido['avaliacao']}/5)")
        else:
            print("Avaliacao: Ainda nao avaliado")
    
    input("\nPressione Enter para voltar...")

def avaliar_pedido():
    mostrar_cabecalho()
    print("\nAVALIAR PEDIDO")
    
    pedidos_sem_avaliacao = []
    for pedido in pedidos:
        if pedido["cliente"] == usuario_logado and pedido["avaliacao"] is None:
            pedidos_sem_avaliacao.append(pedido)
    
    if not pedidos_sem_avaliacao:
        print("\nTodos os seus pedidos ja foram avaliados!")
        input("\nPressione Enter para voltar...")
        return
    
    print("\nPedidos aguardando sua avaliacao:")
    for pedido in pedidos_sem_avaliacao:
        print(f"#{pedido['numero']} - {pedido['data']} - R$ {pedido['valor_total']:.2f}")
    
    numero = input("\nDigite o numero do pedido que quer avaliar: ")
    if numero.isdigit():
        numero_pedido = int(numero)
        avaliar_pedido_especifico(numero_pedido)
    else:
        print("\nPor favor, digite um numero!")

def avaliar_pedido_especifico(numero_pedido):
    pedido_encontrado = None
    for pedido in pedidos:
        if pedido["numero"] == numero_pedido and pedido["cliente"] == usuario_logado:
            pedido_encontrado = pedido
            break
    
    if not pedido_encontrado:
        print("\nPedido nao encontrado!")
        return
    
    mostrar_cabecalho()
    print(f"\nAVALIAR PEDIDO #{numero_pedido}")
    print(f"Data do pedido: {pedido_encontrado['data']}")
    
    print("\nItens do seu pedido:")
    for item in pedido_encontrado["itens"]:
        print(f"   - {item['nome']}")
    
    print("\nComo foi sua experiencia com este pedido?")
    print("1 - * (Ruim)")
    print("2 - ** (Regular)")
    print("3 - *** (Bom)")
    print("4 - **** (Muito Bom)")
    print("5 - ***** (Excelente)")
    
    nota = input("\nDigite sua nota (1-5 estrelas): ")
    if nota.isdigit():
        nota_numero = int(nota)
        if 1 <= nota_numero <= 5:
            pedido_encontrado["avaliacao"] = nota_numero
            
            for item_pedido in pedido_encontrado["itens"]:
                for item_cardapio in cardapio:
                    if item_cardapio["nome"] == item_pedido["nome"]:
                        item_cardapio["nota"] = (item_cardapio["nota"] + nota_numero) / 2
                        break
            
            salvar_pedidos()
            salvar_cardapio()
            
            estrelas = "*" * nota_numero
            print(f"\nAvaliacao registrada: {estrelas} ({nota_numero}/5)")
            
            if nota_numero >= 4:
                print("Obrigado pela excelente avaliacao!")
            elif nota_numero >= 3:
                print("Obrigado pela boa avaliacao!")
            else:
                print("Obrigado pelo feedback! Vamos melhorar!")
                
        else:
            print("\nA avaliacao deve ser entre 1 e 5!")
    else:
        print("\nPor favor, digite um numero!")
    
    input("\nPressione Enter para voltar...")

def iniciar_sistema():
    print("Iniciando FEIFood...")
    tela_principal()

if __name__ == "__main__":
    iniciar_sistema()