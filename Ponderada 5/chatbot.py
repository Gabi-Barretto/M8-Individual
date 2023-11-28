import tkinter as tk
import openai

# Função para obter a chave de API da OpenAI a partir do arquivo
def obter_chave_api():
    try:
        with open('api.txt', 'r') as arquivo:
            chave_api = arquivo.read().strip()
        return chave_api
    except FileNotFoundError:
        raise Exception("O arquivo api_key.txt não foi encontrado. Certifique-se de criar o arquivo e adicionar sua chave de API.")

# Configure sua chave de API da OpenAI aqui
openai.api_key = obter_chave_api()

# Função para obter a resposta do chatbot
def chatbot_responder(pergunta):
    resposta = openai.Completion.create(
        engine="text-davinci-003",  # Escolha o modelo adequado da OpenAI (davinci é poderoso, mas você pode escolher outros)
        prompt=pergunta,
        max_tokens=50  # Ajuste o número de tokens conforme necessário
    )
    return resposta.choices[0].text

# Função para responder à pergunta do usuário
def responder_pergunta():
    pergunta = entrada.get()
    resposta = chatbot_responder(pergunta)
    resposta_label.config(text=resposta)

# Configurar a janela
janela = tk.Tk()
janela.title("Chatbot de Segurança Industrial")

# Criar widgets
entrada = tk.Entry(janela, width=50)
botao = tk.Button(janela, text="Enviar Pergunta", command=responder_pergunta)
resposta_label = tk.Label(janela, text="Resposta aparecerá aqui.")

# Colocar widgets na janela
entrada.pack()
botao.pack()
resposta_label.pack()

# Iniciar a interface gráfica
janela.mainloop()
