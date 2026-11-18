import torch
from torchvision import transforms, models
from PIL import Image
import torch.nn as nn
import os

# Device
device = torch.device("cpu")

# Classes
class_names = [
    "Tomato Early Blight",
    "Tomato Healthy",
    "Tomato Late Blight"
]

# Load ResNet18 model
model = models.resnet18(weights=None)

# Change final layer
model.fc = nn.Linear(model.fc.in_features, 3)

# Model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "plant_disease_model.pth"
)

# Load weights
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))

# Evaluation mode
model.eval()

# Image transforms
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict_disease(img_path):

    # Open image
    img = Image.open(img_path).convert("RGB")

    # Transform
    img = transform(img)

    # Add batch dimension
    img = img.unsqueeze(0)

    # Prediction
    with torch.no_grad():

        outputs = model(img)

        _, predicted = torch.max(outputs, 1)

    index = predicted.item()

    print("Predicted Index:", index)

    result = class_names[index]

    return result