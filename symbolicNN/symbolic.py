import numpy as np
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import torch.optim as optim
import matplotlib.pyplot as plt
import sympy as sp
import os
import argparse

# Constants
EPOCHS = 1000
INPUT_DIM = 4
HIDDEN_DIM = 16
NUM_CLASSES = 3
MODEL_PATH = "iris_model.pth"


def load_data():
    iris_dataset = load_iris()
    X, y = iris_dataset.data, iris_dataset.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

class FeedForward(nn.Module):
    def __init__(self, sparsity = 0.3):
        super(FeedForward, self).__init__()
        layers = []
        total_size = [INPUT_DIM] + [HIDDEN_DIM, HIDDEN_DIM] + [NUM_CLASSES]
        for i in range(len(total_size) - 1):
            layers.append(nn.Linear(total_size[i], total_size[i+1]))
            layers.append(nn.ReLU() if i < len(total_size) - 2 else nn.Identity())
        
        self.model = nn.Sequential(*layers)
        self.sparsity = sparsity
        self.apply_sparsity()
    
    def apply_sparsity(self):
        with torch.no_grad():
            for layer in self.model:
                if isinstance(layer, nn.Linear):
                    mask = torch.rand(layer.weight.size()) > self.sparsity
                    layer.weight.data *= mask
    
    def forward(self, x):
        return self.model(x)

def train(plot_curve=False):
    
    model = FeedForward()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.003)
    
    X_train, X_test, y_train, y_test = load_data()
    print("Model Training started...")
    
    train_loss = []
    
    for epoch in range(EPOCHS):
        
        inputs = torch.tensor(X_train, dtype=torch.float32)
        target = torch.tensor(y_train, dtype=torch.long)  
        output = model(inputs)
        loss = criterion(output, target)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        train_loss.append(loss.item())  
        
        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{EPOCHS}], Loss: {loss.item():.4f}')
            
    if plot_curve:
        plt.figure(figsize=(10, 6))
        plt.plot(train_loss, label='Training Loss', marker='o')
        plt.title("Training Loss Curve")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.legend()
        plt.grid(True)
        plt.savefig("train_loss.png")
        
    print("Saving the trained model")
    torch.save(model.state_dict(), MODEL_PATH)
    
def inference():
    
    model = FeedForward()
    model.load_state_dict(torch.load(MODEL_PATH))
    X_train, X_test, y_train, y_test = load_data()
    train_predictions, test_predictions = [], []
    model.eval()
    
    X_train_tensor = torch.tensor(X_train, dtype = torch.float32)
    X_test_tensor = torch.tensor(X_test, dtype = torch.float32)
    
    with torch.no_grad():
        train_output = model(X_train_tensor)
        test_output = model(X_test_tensor)
        _, train_prediction = torch.max(train_output.data, 1)
        _, test_prediction = torch.max(test_output.data, 1) # calculates the class
        
        train_predictions.append(train_prediction)
        test_predictions.append(test_prediction)
    
    train_accuracy = np.sum(train_predictions == y_train) / len(y_train)
    test_accuracy = np.sum(test_predictions == y_test) / len(y_test)
    
    print("Train Accuracy : {}".format(train_accuracy))
    print("Test Accuracy : {}".format(test_accuracy))
        

def create_eqn(input_values):
    
    print("Constructing the symbolic equation")
    model = FeedForward()
    model.load_state_dict(torch.load(MODEL_PATH))
    
    W, b = [], []
    for layer in model.model:
        if isinstance(layer, nn.Linear):
            W.append(sp.Matrix(layer.weight.detach().numpy()))
            b.append(sp.Matrix(layer.bias.detach().numpy()))
    
    x = sp.symbols('x0:4')  
    X = sp.Matrix([x[0], x[1], x[2], x[3]])
    
    # Construct the symbolic equation
    z1 = W[0]*X + b[0]
    a1 = sp.Matrix([sp.Max(0, z1[i]) for i in range(z1.rows)])
    z2 = W[1]*a1 + b[1]
    a2 = sp.Matrix([sp.Max(0, z2[i]) for i in range(z2.rows)])
    output = W[2]*a2 + b[2]
    
    # Substitute input values and evaluate
    x_subs = {x[i]: input_values[i] for i in range(4)}
    output_evaluated = output.subs(x_subs)
    output_numerical = [output_evaluated[i].evalf() for i in range(output.rows)]
    
    index = np.argmax(np.max(output_numerical))
    
    return output_numerical, index

if __name__ == "__main__":
    
    train(plot_curve=True)
    
    inference()

    parser = argparse.ArgumentParser()
    parser.add_argument("--x1", type = float, default = 0.1)
    parser.add_argument("--x2", type = float, default = 0.1)
    parser.add_argument("--x3", type = float, default = 0.1)
    parser.add_argument("--x4", type = float, default = 0.1)
    args = parser.parse_args()
    
    inputs = [args.x1, args.x2, args.x3, args.x4]
    
    res, index = create_eqn(inputs)
    
    print("Predicted output: {}".format(res))
    print("Class predictied: {}".format(index))
