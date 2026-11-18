import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

# Class labels
classes = [
    'Potato Early Blight',
    'Tomato Blight',
    'Tomato Healthy'
]

# Create ResNet18 model
model = models.resnet18(pretrained=False)

# Modify final layer
num_features = model.fc.in_features

model.fc = nn.Linear(num_features, len(classes))

# Load trained weights
model.load_state_dict(
    torch.load(
        'plant_disease_detection/model/plant_disease_model.pth',
        map_location=torch.device('cpu')
    )
)

# Evaluation mode
model.eval()

# Image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# Prediction function
def predict_disease(image_path):

    image = Image.open(image_path).convert('RGB')

    image = transform(image)

    image = image.unsqueeze(0)

    with torch.no_grad():

        outputs = model(image)

        _, predicted = torch.max(outputs, 1)

        prediction = classes[predicted.item()]

    return prediction