# Perceptron: Implementação e Análise

## Introdução
Este repositório contém a implementação de um perceptron, um dos fundamentos dos algoritmos de aprendizado de máquina. O perceptron é um modelo de aprendizado supervisionado e serve como um bloco de construção para redes neurais mais complexas. Este código oferece uma visão prática sobre como perceptrons funcionam e são treinados, além de abordar suas limitações, como a incapacidade de resolver a operação lógica XOR.

## Características Principais
- **Implementação Clássica do Perceptron**: Código escrito em Python que demonstra a arquitetura básica e a funcionalidade de um perceptron.
- **Treinamento e Teste**: Funções para treinar o perceptron com dados de entrada e testar sua precisão em classificar dados.
- **Visualização de Resultados**: Capacidade de visualizar a linha de decisão criada pelo perceptron em um conjunto de dados bidimensionais.

## Como Utilizar
### Pré-requisitos
- Python 3.x
- Bibliotecas Python: numpy (para operações matemáticas)

### Instalação
1. Clone o repositório para sua máquina local.
2. Instale as dependências necessárias usando o comando `pip install numpy`.

### Execução
Para executar o perceptron, utilize o seguinte comando no terminal:
```
python perceptron_oficial.py
```

### Exemplos de Uso
No arquivo `perceptron_oficial.py`, você encontrará exemplos de como inicializar, treinar e testar o perceptron com seus próprios dados.

## Limitações: O Caso da Porta XOR
Uma limitação importante do perceptron é sua incapacidade de resolver operações lógicas não lineares, como a XOR (exclusive or). Isso ocorre porque a função de decisão de um perceptron é linear e a XOR, por natureza, requer a separação dos dados de forma não linear. Essa limitação ilustra a necessidade de estruturas mais complexas, como redes neurais multicamadas, para resolver tais problemas.

