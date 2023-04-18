import torch
import torchvision.transforms as transforms
from PIL import Image

# Define the transform to normalize the image
transform = transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.Grayscale(),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Load the image and apply the transform
img = Image.open('R.png')
img = transform(img).unsqueeze(0)

# Load the model
model = Net()
model.load_state_dict(torch.load('mnist_cnn.pt', map_location=torch.device('cpu')))
model.eval()

# Make a prediction
with torch.no_grad():
    output = model(img)

# Get the predicted class
pred = output.argmax(dim=1, keepdim=True)

# Print the predicted class
print("Predicted class:", pred.item())
