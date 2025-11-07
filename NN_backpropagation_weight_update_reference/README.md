# 🧠 Neural Network Backpropagation & Weight Update — Quick Reference

This repository provides a concise overview of **Neural Network Backpropagation**, including the key equations, steps, and update rules for training feedforward networks.

---

## 📘 Overview

**Backpropagation** is the core algorithm used to train neural networks by minimizing the **loss function** through **gradient descent**.  
It propagates the error backward from the output layer to the input layer and updates the weights to reduce prediction error.

---

## 🧩 Key Steps in Backpropagation

1. **Forward Pass**
   - Compute the output of each neuron layer by layer.
   - Store activations and weighted sums for later use.
   - Example:
   - $$
     \[
     z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}
     \]
     \[
     a^{[l]} = f(z^{[l]})
     \]
   $$

2. **Compute Loss**
   - Example (Mean Squared Error):
     \[
     L = \frac{1}{2m} \sum_i (y_i - \hat{y}_i)^2
     \]

3. **Backward Pass (Error Propagation)**
   - Compute gradients layer-by-layer from the output backward:
     \[
     \delta^{[L]} = (\hat{y} - y) \odot f'(z^{[L]})
     \]
     \[
     \delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \odot f'(z^{[l]})
     \]

4. **Compute Gradients**
   - For each layer:
     \[
     \frac{\partial L}{\partial W^{[l]}} = \frac{1}{m} \delta^{[l]} (a^{[l-1]})^T
     \]
     \[
     \frac{\partial L}{\partial b^{[l]}} = \frac{1}{m} \sum \delta^{[l]}
     \]

5. **Weight & Bias Update**
   - Update using **Gradient Descent**:
     \[
     W^{[l]} := W^{[l]} - \eta \frac{\partial L}{\partial W^{[l]}}
     \]
     \[
     b^{[l]} := b^{[l]} - \eta \frac{\partial L}{\partial b^{[l]}}
     \]
   - Where:
     - \( \eta \) = learning rate
     - \( \frac{\partial L}{\partial W^{[l]}} \), \( \frac{\partial L}{\partial b^{[l]}} \) = gradients

---

## ⚙️ Simplified Example (Single Neuron)

**Given:**
\[
y = f(Wx + b)
\]
**Loss:**
\[
L = \frac{1}{2}(y_{true} - y)^2
\]
**Updates:**
\[
\frac{dL}{dW} = (y - y_{true}) \cdot f'(z) \cdot x
\]
\[
W := W - \eta \frac{dL}{dW}
\]
\[
b := b - \eta (y - y_{true}) \cdot f'(z)
\]

---

## 🧮 Activation Functions & Derivatives

| Function | \( f(x) \) | Derivative \( f'(x) \) |
|-----------|-------------|------------------------|
| Sigmoid | \( \frac{1}{1 + e^{-x}} \) | \( f(x)(1 - f(x)) \) |
| Tanh | \( \tanh(x) \) | \( 1 - f(x)^2 \) |
| ReLU | \( \max(0, x) \) | \( 1 \text{ if } x>0 \text{ else } 0 \) |
| Leaky ReLU | \( \max(\alpha x, x) \) | \( 1 \text{ if } x>0 \text{ else } \alpha \) |
| Softmax | \( \frac{e^{x_i}}{\sum e^{x_j}} \) | Used with cross-entropy loss |

---

## 🧠 Gradient Descent Variants

| Method | Update Rule | Description |
|--------|--------------|-------------|
| **Batch GD** | Use all samples per update | Stable but slow |
| **Stochastic GD** | Use one sample per update | Noisy but fast |
| **Mini-Batch GD** | Small subsets | Best trade-off |
| **Momentum** | Add velocity term | Speeds convergence |
| **Adam** | Adaptive learning rates | Common in deep learning |

---

## 📊 Pseudocode Summary

```python
for epoch in range(epochs):
    # Forward pass
    A = forward(X, W, b)
    loss = compute_loss(A, Y)
    
    # Backward pass
    gradients = backprop(A, Y, W, b)
    
    # Weight update
    for l in layers:
        W[l] -= lr * gradients['dW'][l]
        b[l] -= lr * gradients['db'][l]

