\# Models Directory



This folder is intended to store \*\*trained machine learning models\*\* for the MNIST Image Classifier project.



---



\## 📁 Purpose



\- Keep all saved models (`.h5` files, TensorFlow SavedModel folders, etc.) in one place.

\- Maintain the project directory structure in Git without committing large files.



---



\## ⚡ Usage



1\. \*\*Saving a trained model\*\*  

&nbsp;  Models are saved here after training. For example, in `mnist\_classifier.py`:



&nbsp;  ```python

&nbsp;  import os

&nbsp;  model.save('models/mnist\_model.h5')

&nbsp;  ```



2\. Loading a saved model

&nbsp;  Models in this folder can be loaded for evaluation or inference:

&nbsp;  ```python

&nbsp;  	from tensorflow.keras.models import load\_model

&nbsp;	model = load\_model('models/mnist\_model.h5')



&nbsp;  ```



Notes

Do not commit large model files to Git. Instead, use cloud storage or provide a download link in the main README.md.



