# Documentação do Projeto Ollama

## Visão Geral
O `ollama.py` é um script Python para interagir com uma API de geração de texto, utilizando as bibliotecas `requests`, `json` e `gradio`.

## Dependências
- Python 3.x
- Bibliotecas: `requests`, `json`, `gradio`

```python
import requests
import json
import gradio as gr
```

## Configuração
- URL da API: `http://localhost:11434/api/generate`

```python
url = "http://localhost:11434/api/generate"
```

## Cabeçalhos HTTP
- Definição de cabeçalhos para a solicitação JSON.

```python
headers = {
    'Content-Type': 'application/json',
}
```

## Histórico de Conversação
- Uma lista para armazenar o histórico de conversas.

```python
conversation_history = []
```

## Função `generate_response`
- Esta função gerencia a adição de prompts ao histórico e a comunicação com a API.

```python
def generate_response(prompt):
    conversation_history.append(prompt)
    full_prompt = "\n".join(conversation_history)
    data = {
        "model": "mistral",
        "stream": False,
        "prompt": full_prompt,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # Processamento da resposta aqui
```

## Uso e Exemplos
- Para usar o script, execute-o em um ambiente Python com as dependências instaladas. ( python3 chatbot.py)
- A função `generate_response` pode ser chamada com um prompt de texto para interagir com a API.

## Considerações Adicionais
- O script pressupõe a disponibilidade da API e a utilização do modelo `mistral`.
- Tratamento de erros e exceções pode ser necessário para uso em ambientes de produção.
-  O principal problema parece ser que o script não consegue estabelecer uma conexão com o URL http://localhost:11434/api/generate. Isso resulta em um ConnectionRefusedError, indicando que a tentativa de conectar ao servidor local na porta 11434 falhou. Porém a essencia prevalece. 

### Vídeo Demonstrativo

[Vídeo no Drive](https://drive.google.com/file/d/1kvdwlwi6Yxnrn9ys2TWg9rmGCriVHrwW/view?usp=sharing)

Tambem disponível no [repositório](https://github.com/Gabi-Barretto/M8-Individual/blob/main/Ponderada%205/M%C3%ADdia/ponderada5.mp4)!

