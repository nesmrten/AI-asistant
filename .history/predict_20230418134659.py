import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image

# Define the neural network model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = nn.functional.relu(nn.functional.max_pool2d(self.conv1(x), 2))
        x = nn.functional.relu(nn.functional.max_pool2d(self.conv2(x), 2))
        x = x.view(-1, 320)
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return nn.functional.log_softmax(x, dim=1)

# Load the trained model
model = Net()
model.load_state_dict(torch.load('mnist_cnn.pt'))

# Set the model to evaluation mode
model.eval()

# Load the image and apply the same preprocessing as we did for the training dataset
img = Image.open('test_image.png').convert('L')
img = transforms.Resize((28, 28))(img)
img = transforms.ToTensor()(img)
img = transforms.Normalize((0.1307,), (0.3081,))(img)
img = img.unsqueeze(0)

# Make a prediction and print the result
with torch.no_grad():
    output = model(img)
    prediction = output.argmax(dim=1, keepdim=True)
    print("Prediction:", prediction.item())
