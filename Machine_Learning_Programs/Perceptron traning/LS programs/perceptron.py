import numpy as np
import matplotlib.pyplot as plt


class Perceptron:
    def __init__(self, input_size, lr=0.01, epochs=100):
        self.lr = lr
        self.epochs = epochs
        self.weights = np.random.randn(input_size + 1)  # +1 for bias
        self.errors = []  # Track errors per epoch

    def activation(self, x):
        """Sigmoid activation function."""
        return 1 / (1 + np.exp(-x))

    def predict(self, x):
        """Predict using the current weights with sigmoid activation."""
        x = np.insert(x, 0, 1)  # Add bias term
        return self.activation(np.dot(self.weights, x))

    def train(self, X, Y):
        """Train perceptron using sigmoid activation and backpropagation."""
        for _ in range(self.epochs):
            total_error = 0
            for i in range(len(X)):
                x_i = np.insert(X[i], 0, 1)  # Add bias term
                y_pred = self.predict(X[i])
                error = Y[i] - y_pred

                # Backpropagation update
                self.weights += self.lr * error * y_pred * (1 - y_pred) * x_i
                total_error += abs(error)

            self.errors.append(total_error / len(Y))  # Store average error per epoch

    def plot_errors(self):
        """Plot Average Error vs. Epochs"""
        plt.plot(range(1, len(self.errors) + 1), self.errors, marker='o')
        plt.xlabel("Epochs")
        plt.ylabel("Average Error")
        plt.title("Error Reduction Over Epochs")
        plt.show()
