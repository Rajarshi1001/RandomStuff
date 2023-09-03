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

# define paths and paremeters for training
LEARNING_RATE = 0.009
WEIGHT_DECAY = 0.008
BATCH_SIZE = 64
EPOCHS = 1000
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
csv_file = 'data.csv'
root_dir = 'images'


# fetching training data via scraping
def create_data():
    url = "https://height-weight-chart.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    # print(soup.prettify())
    pattern = "\d{3}-\d{3}.html"
    res = soup.find_all('a', {"href": re.compile(pattern)})
    print(res[0].img["src"])
    results = ["https://height-weight-chart.com/" + res[i].img["src"] for i in range(len(res))]
    weights = [int(str(res[i].img["title"].split(","))[9:12])*0.4532 for i in range(len(res))]


    folder_name = "images"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for idx, img_url in enumerate(results):
        img_resp = requests.get(img_url, stream=True)
        img_resp.raise_for_status()
        img_path = os.path.join(folder_name, f'image_{idx}.jpg')
        with open(img_path, 'wb') as img_file:
            for chunk in img_resp.iter_content(chunk_size=8192):
                img_file.write(chunk)

    images = os.listdir("images")
    print("Total {} training images obtained".format(len(images)))
    weights = weights
    data = pd.DataFrame({"image": images, "weight" : weights})
    weights = np.array(weights)
    # saving the train dataframe to disk
    data.to_csv("data.csv")

# creation of custom pytorch dataset
class WeightDataset(Dataset):
    
    def __init__(self, csv_file, root_dir, transform=None):
        self.data_frame = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.data_frame)

    def __getitem__(self, idx):
        img_name = os.path.join(root_dir, self.data_frame.iloc[idx, 1])
        image = Image.open(img_name)
        label = self.data_frame.iloc[idx, 2]

        if self.transform:
            image = self.transform(image)

        return image, float(label)


# Define data transformations
data_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.RandomGrayscale(p=0.2),
    transforms.RandomHorizontalFlip(p=0.2),
    transforms.RandomVerticalFlip(p=0.2),
#     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def trainmodel():

    dataset = WeightDataset(csv_file=csv_file, root_dir=root_dir, transform=data_transform)
    trainloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)
    # model = WeightModel(NUM_CLASSES).to(device)  
    model = SimpleCNN().to(device)
    optimizer = Adam(model.parameters(), lr=LEARNING_RATE)
    criterion = nn.MSELoss()


    for epoch in range(EPOCHS):
        model.train()
        running_loss = 0.0
        for batch_idx, (images, targets) in enumerate(trainloader):
            images = images.to(device).float()
            targets = targets.to(device).float()
            output = model(images)
            loss = criterion(output, targets)
            optimizer.zero_grad()
            loss.backward()
            clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
            running_loss += loss.item()

        avg_loss = running_loss / len(trainloader)
        print(f"Epoch [{epoch+1}/{EPOCHS}], Avg Loss: {avg_loss:.4f}")

    # saving the model state dict to disk
    torch.save(model.state_dict(), "model.pth")

if __name__ == "__main__":
    create_data()
    trainmodel()