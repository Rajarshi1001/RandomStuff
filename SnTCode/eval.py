import torch 
import numpy as np
import pandas as pd
import torch.nn.functional as F
import torch.nn as nn
import matplotlib.pyplot as plt
import os
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
from bs4 import BeautifulSoup
import requests 
import regex as re
import csv
from sklearn.metrics import mean_squared_error
from torch.nn.utils import clip_grad_norm_
import torchvision.models as models
from torch.optim import Adam
from model import SimpleCNN, WeightModel
from train import create_data, trainmodel, WeightDataset


# Define data transformations
data_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.RandomGrayscale(p=0.2),
    transforms.RandomHorizontalFlip(p=0.2),
    transforms.RandomVerticalFlip(p=0.2),
#     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# evaluation on train data
DATA_DIR = "images"
train_images = os.listdir(DATA_DIR)
print(len(train_images))
model_path = 'model.pth'
model = SimpleCNN()  # Replace with your model class
model.load_state_dict(torch.load(model_path))
model.eval()
pred_weights = []

for idx, img in enumerate(train_images):
    img_path = os.path.join(DATA_DIR, img)
    image = Image.open(img_path)
    image = data_transform(image)  
    image = image.unsqueeze(0)  

    with torch.no_grad():
        output = model(image)
#         print(output)
        pred_weights.append(output.cpu().detach().numpy().astype("float")[0])


# calculating the RMSE % in training data
pred_weights = np.array(pred_weights)
weights = np.array(weights)
rmse_per = np.sqrt(mean_squared_error(pred_weights, weights))/(np.max(weights) - np.min(weights))
print("RMSE% score for training data: {}".format(rmse_per*100))

# Inference

DATA_DIR = "Dataset"
test_images = os.listdir(DATA_DIR)
print(len(test_images))

model_path = 'model.pth'
model = SimpleCNN()
model.load_state_dict(torch.load(model_path))
model.eval()
pred_weights = []

for idx, img in enumerate(test_images):
    img_path = os.path.join(DATA_DIR, img)
    image = Image.open(img_path)
    image = data_transform(image)  # No need to unsqueeze(1) here
    image = image.unsqueeze(0)  # Add batch dimension

    with torch.no_grad():
        output = model(image)
#         print(output)
        pred_weights.append(output.cpu().detach().numpy().astype("float")[0])
        with open("sample_submission.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([img, np.round(output.cpu().detach().numpy().astype("float")[0])])