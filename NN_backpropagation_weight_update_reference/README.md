# 🧠 Neural Network Backpropagation & Weight Update — Quick Reference

This repository provides a concise overview of **Neural Network Backpropagation**, including the key equations, steps, and update rules for training feedforward networks.

---

## 📘 Overview

**Backpropagation** is the algorithm used to train neural networks by minimizing the **loss function** through **gradient descent**.  
It propagates the error backward from the output layer to the input layer and updates weights to reduce prediction error.

---

## 🧩 Key Steps in Backpropagation

### 1. Forward Pass
Compute the output of each neuron layer by layer.

**Equations:**
- <b>z<sup>[l]</sup> = W<sup>[l]</sup> a<sup>[l−1]</sup> + b<sup>[l]</sup></b>  
- <b>a<sup>[l]</sup> = f(z<sup>[l]</sup>)</b>

---

### 2. Compute Loss
Example (Mean Squared Error):

<b>L = (1 / 2m) Σ<sub>i</sub> (y<sub>i</sub> − ŷ<sub>i</sub>)²</b>

---

### 3. Backward Pass (Error Propagation)

Compute gradients layer-by-layer from the output backward:

- <b>δ<sup>[L]</sup> = (ŷ − y) ⊙ f′(z<sup>[L]</sup>)</b>  
- <b>δ<sup>[l]</sup> = (W<sup>[l+1]</sup>)ᵀ δ<sup>[l+1]</sup> ⊙ f′(z<sup>[l]</sup>)</b>

---

### 4. Compute Gradients

- <b>∂L/∂W<sup>[l]</sup> = (1/m) · δ<sup>[l]</sup> (a<sup>[l−1]</sup>)ᵀ</b>  
- <b>∂L/∂b<sup>[l]</sup> = (1/m) Σ δ<sup>[l]</sup></b>

---

### 5. Weight & Bias Update

- <b>W<sup>[l]</sup> ← W<sup>[l]</sup> − η · ∂L/∂W<sup>[l]</sup></b>  
- <b>b<sup>[l]</sup> ← b<sup>[l]</sup> − η · ∂L/∂b<sup>[l]</sup></b>

Where:
- η = learning rate  
- ∂L/∂W, ∂L/∂b = gradients

---

## ⚙️ Simplified Example (Single Neuron)

Given:  
<b>y = f(Wx + b)</b>

Loss:  
<b>L = ½ (y<sub>true</sub> − y)²</b>

Updates:  
- <b>dL/dW = (y − y<sub>true</sub>) · f′(z) · x</b>  
- <b>W ← W − η (dL/dW)</b>  
- <b>b ← b − η (y − y<sub>true</sub>) · f′(z)</b>

---

## 🧮 Activation Functions & Derivatives

| Function | f(x) | f′(x) |
|-----------|-------|-------|
| **Sigmoid** | 1 / (1 + e<sup>−x</sup>) | f(x)(1 − f(x)) |
| **Tanh** | tanh(x) | 1 − f(x)² |
| **ReLU** | max(0, x) | 1 if x > 0 else 0 |
| **Leaky ReLU** | max(αx, x) | 1 if x > 0 else α |
| **Softmax** | e<sup>xᵢ</sup> / Σ e<sup>xⱼ</sup> | Used with cross-entropy |

---

## 🧠 Gradient Descent Variants

| Method | Update Rule | Description |
|--------|--------------|-------------|
| **Batch GD** | All samples per update | Stable but slow |
| **Stochastic GD** | One sample per update | Noisy but fast |
| **Mini-Batch GD** | Small subsets | Best trade-off |
| **Momentum** | Add velocity term | Faster convergence |
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
