from perceptron import Perceptron
from utils import load_dataset, plot_data, plot_decision_boundary
import numpy as np
from itertools import combinations
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
dataset_path = "datasets/dataset.txt"

# Define class indices based on dataset structure
class_indices = {
    0: (0, 500),  # First 500 examples → Class 1
    1: (500, 1000),  # Next 500 examples → Class 2
    2: (1000, 2000)  # Last 1000 examples → Class 3
}


# One-Against-One Training with Accuracy & Confusion Matrix
def train_oao_classifiers(dataset_path):
    classifiers = {}

    for class1, class2 in combinations(class_indices.keys(), 2):
        print(f"\nTraining on class{class1 + 1} vs class{class2 + 1}...")

        # Load both datasets
        X1_train, X1_test, Y1_train, Y1_test = load_dataset(dataset_path, class_indices[class1])
        X2_train, X2_test, Y2_train, Y2_test = load_dataset(dataset_path, class_indices[class2])

        # Merge datasets for binary classification
        X_train = np.vstack((X1_train, X2_train))
        X_test = np.vstack((X1_test, X2_test))
        Y_train = np.hstack((np.zeros(len(X1_train)), np.ones(len(X2_train))))
        Y_test = np.hstack((np.zeros(len(X1_test)), np.ones(len(X2_test))))

        # Train perceptron
        perceptron = Perceptron(input_size=X_train.shape[1], lr=0.1, epochs=100)
        perceptron.train(X_train, Y_train)

        classifiers[(class1, class2)] = perceptron

        # Predictions
        Y_pred_train = np.array([round(perceptron.predict(x)) for x in X_train])
        Y_pred_test = np.array([round(perceptron.predict(x)) for x in X_test])

        # Evaluation Metrics
        train_accuracy = accuracy_score(Y_train, Y_pred_train) * 100
        test_accuracy = accuracy_score(Y_test, Y_pred_test) * 100

        print(f"Training Accuracy: {train_accuracy:.2f}%")
        print(f"Testing Accuracy: {test_accuracy:.2f}%")
        print("Confusion Matrix (Test Set):")
        print(confusion_matrix(Y_test, Y_pred_test))

        # Plot results
        plot_data(X_train, Y_train, X_test, Y_test, dataset_name=f"class{class1 + 1} vs class{class2 + 1}")
        plot_decision_boundary(perceptron, X_train, Y_train)
        perceptron.plot_errors()

    return classifiers


# Train OAO classifiers
classifiers = train_oao_classifiers(dataset_path)
