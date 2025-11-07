\# 🧠 Neural Network Backpropagation \& Weight Update — Quick Reference



This repository provides a concise overview of \*\*Neural Network Backpropagation\*\*, including the key equations, steps, and update rules for training feedforward networks.



---



\## 📘 Overview



\*\*Backpropagation\*\* is the core algorithm used to train neural networks by minimizing the \*\*loss function\*\* through \*\*gradient descent\*\*.  

It propagates the error backward from the output layer to the input layer and updates the weights to reduce prediction error.



---



\## 🧩 Key Steps in Backpropagation



1\. \*\*Forward Pass\*\*

&nbsp;  - Compute the output of each neuron layer by layer.

&nbsp;  - Store activations and weighted sums for later use.

&nbsp;  - Example:

&nbsp;    \\\[

&nbsp;    z^{\[l]} = W^{\[l]} a^{\[l-1]} + b^{\[l]}

&nbsp;    \\]

&nbsp;    \\\[

&nbsp;    a^{\[l]} = f(z^{\[l]})

&nbsp;    \\]



2\. \*\*Compute Loss\*\*

&nbsp;  - Example (Mean Squared Error):

&nbsp;    \\\[

&nbsp;    L = \\frac{1}{2m} \\sum\_i (y\_i - \\hat{y}\_i)^2

&nbsp;    \\]



3\. \*\*Backward Pass (Error Propagation)\*\*

&nbsp;  - Compute gradients layer-by-layer from the output backward:

&nbsp;    \\\[

&nbsp;    \\delta^{\[L]} = (\\hat{y} - y) \\odot f'(z^{\[L]})

&nbsp;    \\]

&nbsp;    \\\[

&nbsp;    \\delta^{\[l]} = (W^{\[l+1]})^T \\delta^{\[l+1]} \\odot f'(z^{\[l]})

&nbsp;    \\]



4\. \*\*Compute Gradients\*\*

&nbsp;  - For each layer:

&nbsp;    \\\[

&nbsp;    \\frac{\\partial L}{\\partial W^{\[l]}} = \\frac{1}{m} \\delta^{\[l]} (a^{\[l-1]})^T

&nbsp;    \\]

&nbsp;    \\\[

&nbsp;    \\frac{\\partial L}{\\partial b^{\[l]}} = \\frac{1}{m} \\sum \\delta^{\[l]}

&nbsp;    \\]



5\. \*\*Weight \& Bias Update\*\*

&nbsp;  - Update using \*\*Gradient Descent\*\*:

&nbsp;    \\\[

&nbsp;    W^{\[l]} := W^{\[l]} - \\eta \\frac{\\partial L}{\\partial W^{\[l]}}

&nbsp;    \\]

&nbsp;    \\\[

&nbsp;    b^{\[l]} := b^{\[l]} - \\eta \\frac{\\partial L}{\\partial b^{\[l]}}

&nbsp;    \\]

&nbsp;  - Where:

&nbsp;    - \\( \\eta \\) = learning rate

&nbsp;    - \\( \\frac{\\partial L}{\\partial W^{\[l]}} \\), \\( \\frac{\\partial L}{\\partial b^{\[l]}} \\) = gradients



---



\## ⚙️ Simplified Example (Single Neuron)



\*\*Given:\*\*

\\\[

y = f(Wx + b)

\\]

\*\*Loss:\*\*

\\\[

L = \\frac{1}{2}(y\_{true} - y)^2

\\]

\*\*Updates:\*\*

\\\[

\\frac{dL}{dW} = (y - y\_{true}) \\cdot f'(z) \\cdot x

\\]

\\\[

W := W - \\eta \\frac{dL}{dW}

\\]

\\\[

b := b - \\eta (y - y\_{true}) \\cdot f'(z)

\\]



---



\## 🧮 Activation Functions \& Derivatives



| Function | \\( f(x) \\) | Derivative \\( f'(x) \\) |

|-----------|-------------|------------------------|

| Sigmoid | \\( \\frac{1}{1 + e^{-x}} \\) | \\( f(x)(1 - f(x)) \\) |

| Tanh | \\( \\tanh(x) \\) | \\( 1 - f(x)^2 \\) |

| ReLU | \\( \\max(0, x) \\) | \\( 1 \\text{ if } x>0 \\text{ else } 0 \\) |

| Leaky ReLU | \\( \\max(\\alpha x, x) \\) | \\( 1 \\text{ if } x>0 \\text{ else } \\alpha \\) |

| Softmax | \\( \\frac{e^{x\_i}}{\\sum e^{x\_j}} \\) | Used with cross-entropy loss |



---



\## 🧠 Gradient Descent Variants



| Method | Update Rule | Description |

|--------|--------------|-------------|

| \*\*Batch GD\*\* | Use all samples per update | Stable but slow |

| \*\*Stochastic GD\*\* | Use one sample per update | Noisy but fast |

| \*\*Mini-Batch GD\*\* | Small subsets | Best trade-off |

| \*\*Momentum\*\* | Add velocity term | Speeds convergence |

| \*\*Adam\*\* | Adaptive learning rates | Common in deep learning |



---



\## 📊 Pseudocode Summary



```python

for epoch in range(epochs):

&nbsp;   # Forward pass

&nbsp;   A = forward(X, W, b)

&nbsp;   loss = compute\_loss(A, Y)

&nbsp;   

&nbsp;   # Backward pass

&nbsp;   gradients = backprop(A, Y, W, b)

&nbsp;   

&nbsp;   # Weight update

&nbsp;   for l in layers:

&nbsp;       W\[l] -= lr \* gradients\['dW']\[l]

&nbsp;       b\[l] -= lr \* gradients\['db']\[l]



