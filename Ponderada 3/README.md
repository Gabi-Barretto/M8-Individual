## Descrição
O script `teste-re.py` é uma ferramenta de processamento de texto em Python que utiliza expressões regulares para extrair coordenadas tridimensionais de mensagens textuais. As coordenadas são interpretadas nos eixos x, y e z e podem ser formatos de número inteiro ou decimal.

## Função `extrair_coordenadas`
A função principal `extrair_coordenadas` busca padrões específicos no texto que correspondem às coordenadas espaciais. Ela é capaz de detectar coordenadas com os seguintes formatos:
- `x: <number> y: <number> z: <number>`
- `x <number> y <number> z <number>`
- Incluindo números negativos e decimais.

Se as coordenadas são encontradas, a função retorna uma tupla de floats `(x, y, z)`. Caso contrário, retorna uma tupla `(None, None, None)`.

## Casos de Teste
O script inclui um conjunto de casos de teste que demonstram sua utilização e validam sua precisão. Para cada caso de teste, o script imprime as coordenadas encontradas ou uma mensagem de erro se as coordenadas não puderem ser extraídas.

## Possíveis Cenários de Aplicação
Este script pode ser utilizado em diversos cenários, como:
- Análise de dados geoespaciais ou astronômicos onde as coordenadas são frequentemente utilizadas.
- Extração e análise de coordenadas a partir de dados de sensores ou registros de localização.
- Jogos de realidade virtual ou aumentada onde a posição espacial precisa ser rastreada e interpretada.
- Robótica e automação para interpretar posições e movimentos em um espaço tridimensional.
- Simulações físicas ou de engenharia que envolvem a modelagem de objetos no espaço.

## Como Usar
1. Clone o repositório ou faça download do `teste-re.py`.
2. Execute o script em um ambiente Python com a mensagem de texto contendo as coordenadas como input.
3. A função `extrair_coordenadas` pode ser importada e utilizada em outros scripts Python como um módulo.

## Vídeo Demonstrativo



## Requisitos
- Python 3.x
