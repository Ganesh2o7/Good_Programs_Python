import numpy as np
from perceptron import Perceptron
from utils import load_dataset, plot_data, plot_decision_boundary
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
dataset_path = "datasets/class3.txt"
X_train, X_test, Y_train, Y_test = load_dataset(dataset_path)

# Train Perceptron with Backpropagation
perceptron = Perceptron(input_size=X_train.shape[1], lr=0.1, epochs=100)
perceptron.train(X_train, Y_train)

# Predictions
Y_pred_train = np.array([round(perceptron.predict(x)) for x in X_train])
Y_pred_test = np.array([round(perceptron.predict(x)) for x in X_test])

# Evaluation
train_accuracy = accuracy_score(Y_train, Y_pred_train) * 100
test_accuracy = accuracy_score(Y_test, Y_pred_test) * 100

print(f"Training Accuracy: {train_accuracy:.2f}%")
print(f"Testing Accuracy: {test_accuracy:.2f}%")
print("Confusion Matrix (Test Set):")
print(confusion_matrix(Y_test, Y_pred_test))

# Visualization
plot_data(X_train, Y_train, X_test, Y_test, dataset_name=dataset_path)
plot_decision_boundary(perceptron, X_train, Y_train)
perceptron.plot_errors()
