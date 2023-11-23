
import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.weights = np.zeros(input_size + 1)  # Incluindo o bias no vetor de pesos
        self.learning_rate = learning_rate
        self.epochs = epochs
    
    def activation_function(self, x):
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return self.activation_function(summation)

    def train(self, training_inputs, labels):
        for _ in range(self.epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)

# Dados de treinamento para diferentes portas lógicas, exceto XOR
training_data = {
    'AND': {
        'inputs': np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
        'labels': np.array([0, 0, 0, 1])
    },
    'OR': {
        'inputs': np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
        'labels': np.array([0, 1, 1, 1])
    },
    'NAND': {
        'inputs': np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
        'labels': np.array([1, 1, 1, 0])
    }
}

# Treinando e avaliando o perceptron para cada tipo de porta lógica
for logic_gate, data in training_data.items():
    perceptron = Perceptron(input_size=2)
    perceptron.train(data['inputs'], data['labels'])

    # Exibindo as predições
    print(f"Predições para a porta {logic_gate}:")
    for input_value in data['inputs']:
        prediction = perceptron.predict(input_value)
        print(f"Input: {input_value}, Predição: {prediction}")
    print("\n")
