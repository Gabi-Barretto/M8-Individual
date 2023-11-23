import numpy as np

class Perceptron:
    def __init__(self, weights, threshold):
        self.weights = np.array(weights)
        self.threshold = threshold
        self.bias = -self.threshold  # Ajustando o bias para usar 0 como limiar na função de ativação

    def activation_function(self, x):
        return 1 if x >= 0 else 0  # Função de ativação com limiar em 0

    def predict(self, inputs):
        linear_output = np.dot(inputs, self.weights) + self.bias
        y_predicted = self.activation_function(linear_output)
        return y_predicted

# Definindo os dados de entrada
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Definindo os perceptrons para as portas AND, OR e NAND
and_perceptron = Perceptron(weights=[1, 1], threshold=2)
or_perceptron = Perceptron(weights=[1, 1], threshold=1)
nand_perceptron = Perceptron(weights=[-2, -2], threshold=-3)


# Testando os perceptrons
and_results = [and_perceptron.predict(input) for input in inputs]
or_results = [or_perceptron.predict(input) for input in inputs]
nand_results = [nand_perceptron.predict(input) for input in inputs]


print("AND Results:", and_results)
print("OR Results:", or_results)
print("NAND Results:", nand_results)

