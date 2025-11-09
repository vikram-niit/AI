# 🧠 MNIST Image Classifier

A simple neural network that classifies handwritten digits (0–9) from the MNIST dataset.  
Built with **TensorFlow/Keras**, this project demonstrates how to train, evaluate, and save a neural network model.

---

## 🚀 Features
- Loads and preprocesses the MNIST dataset automatically  
- Builds and trains a fully connected neural network (MLP)  
- Evaluates accuracy on the MNIST test set  
- Saves the trained model in `.h5` format  
- Reloads the model for inference or further training  

---

## 🧩 Project Structure
mnist_image_classifier/
├── models/ # Saved model files (.h5)
├── mnist_classifier.py # Main training script
├── requirements.txt # Dependencies
└── README.md # Project documentation

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/mnist_image_classifier.git
cd mnist_image_classifier
```

## 2. (Optional) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```
Or manually:
```bash
pip install tensorflow numpy matplotlib
```

## 🧠 Usage
### 🔹 Train and Save the Model

Run the training script:
```bash
python mnist_classifier.py
```

During training, you 'll see logs like:
```yaml
Epoch 1/5
1688/1688 [==============================] - 5s 3ms/step - loss: 0.2978 - accuracy: 0.9142
...
Test accuracy: 0.9754
✅ Model saved successfully at models/mnist_model.h5

```
The trained model will be saved in the models/ folder.

## 🔹 Load and Use the Saved Model

In a Python shell or new script:
```python
from tensorflow.keras.models import load_model
import numpy as np

# Load the model
model = load_model('models/mnist_model.h5')

# Example: predict on a single image
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_test = x_test.reshape(-1, 28*28) / 255.0

pred = model.predict(x_test[:1])
print("Predicted digit:", np.argmax(pred))
```

## 🖼️ Model Architecture
## Layer	Type	Output Shape	Activation
---
Input	Flatten	(784,)	—
Dense	Fully Connected	(128,)	ReLU
Dense	Fully Connected	(64,)	ReLU
Output	Fully Connected	(10,)	Softmax

## 📊 Example Results
```yaml
Epoch 5/5
1688/1688 [==============================] - 4s 2ms/step - loss: 0.0902 - accuracy: 0.9735
Test accuracy: 0.9754
✅ Model saved successfully at models/mnist_model.h5
```
