import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def load_dataset(file_path, class_range, test_size=0.3):
    """Load dataset and extract specific class samples."""
    data = np.loadtxt(file_path)

    # Extract subset of dataset
    start, end = class_range
    subset = data[start:end]

    # Assign class labels (0 or 1 for binary classification)
    labels = np.zeros(len(subset))

    # Split dataset into 70% train, 30% test
    X_train, X_test, Y_train, Y_test = train_test_split(subset, labels, test_size=test_size, random_state=42)
    return X_train, X_test, Y_train, Y_test

def plot_data(X_train, Y_train, X_test, Y_test, dataset_name):
    """Scatter plot of training and testing data separately."""
    plt.scatter(X_train[:, 0], X_train[:, 1], c=Y_train, cmap="bwr", edgecolors='k')
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title(f"Training Data: {dataset_name}")
    plt.show()

    plt.scatter(X_test[:, 0], X_test[:, 1], c=Y_test, cmap="bwr", edgecolors='k')
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title(f"Testing Data: {dataset_name}")
    plt.show()

def plot_decision_boundary(perceptron, X, Y):
    """Plot decision boundary for perceptron."""
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = np.array([perceptron.predict(np.array([a, b])) for a, b in zip(xx.ravel(), yy.ravel())])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.3, cmap="bwr")
    plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap="bwr")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("Decision Boundary with Sigmoid Activation")
    plt.show()
