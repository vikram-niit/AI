import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the saved model
model = load_model('models/mnist_model.h5')
print("✅ Model loaded successfully!")

# 2. Load the MNIST test dataset
(_, _), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 3. Preprocess the data (same as during training)
x_test = x_test.reshape(-1, 28*28).astype("float32") / 255.0

# 4. Evaluate the model on the test set
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"📊 Test accuracy: {test_acc:.4f}")

# 5. Make predictions on new or test images
predictions = model.predict(x_test[:5])

# 6. Show predictions
for i in range(5):
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Predicted: {np.argmax(predictions[i])}, Actual: {y_test[i]}")
    plt.axis('off')
    plt.show()
