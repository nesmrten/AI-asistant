from models import Net
import torch
import torchvision.transforms as transforms
from PIL import Image
import sys

# Define the device for the model
device = torch.device('cpu')

# Load the pretrained model
model = Net().to(device)
model.load_state_dict(torch.load('mnist_cnn_model.pt', map_location=device))

# Set the model to evaluation mode
model.eval()

# Load the input image
input_image = sys.argv[1]
image = Image.open(input_image).convert('L')

# Preprocess the image
transform = transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])
image = transform(image).unsqueeze(0)

# Make a prediction
with torch.no_grad():
    output = model(image.to(device))
    prediction = output.argmax(dim=1).item()

# Print the prediction
print(prediction)
