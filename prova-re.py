import re

d_atualizar = ["atualizar", "mudar", "atualizo"]

d_acompanhar = ["onde", "status", "acompanhar", "rastrear"]

def extrair_intencao(mensagem):
    padrao = r'(onde|status|rastrear|acompanhar|atualizar|atualizo|mudar)'

    resultado = re.search(padrao, mensagem, re.IGNORECASE)
    if resultado:
        return resultado.group()
    else:
        return None

def realizar_acao(intencao):
    if intencao in d_atualizar:
        print("O usuário quer saber como atualizar o pagamento")
    elif intencao in d_acompanhar:
        print("O usuário quer acompanhar seu pedido")
    else:
        print("Intenção não reconhecida")

# Testando a função
mensagens = [
    "Como posso atualizar meu cartão de crédito?", 
    "Preciso mudar a forma de pagamento, o que fazer?", 
    "Quero atualizar minhas informações de pagamento", 
    "Método de pagamento desatualizado, como proceder para atualizar?",
    "onde vejo o status do meu pedido?", 
    "Como faço para rastrear meu pedido?", 
    "Quero saber onde está meu pedido, como faço?", 
    "status de entrega, como consultar?"

]

while(True):
#for msg in mensagens:
    frase = input("Digite uma intenção (Aperte CTRL + C para sair!): ")
    intencao = extrair_intencao(frase)
    if intencao:
        realizar_acao(intencao)
    else:
        print(f"Não foi possível extrair intenções da mensagem: '{frase}'")
