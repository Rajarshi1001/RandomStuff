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


# model definitions
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()

        self.conv_layers = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1),  # 224x224
            nn.GELU(),
            nn.MaxPool2d(kernel_size=2, stride=2),  # 112x112
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1), 
            nn.GELU(),
            nn.MaxPool2d(kernel_size=2, stride=2),  # 56x56
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1),
            nn.GELU(),
            nn.MaxPool2d(kernel_size=2, stride=2)   # 28x28
        )
        self.fc_layers = nn.Sequential(
            nn.Linear(64 * 28 * 28, 512),  
            nn.ReLU(),
            nn.Linear(512, 1),
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = x.view(x.size(0), -1) 
        x = self.fc_layers(x)
        return x.view(-1)  

class WeightModel(nn.Module):
    def __init__(self, num_classes):
        super(WeightModel, self).__init__()
        self.resnet50 = models.resnet50(pretrained=True)
        self.resnet50.fc = nn.Linear(self.resnet50.fc.in_features, num_classes)

    def forward(self, x):
        return self.resnet50(x)
