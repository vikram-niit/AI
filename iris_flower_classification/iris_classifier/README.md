# 🌸 Iris Flower Classification – Streamlit App

This project is a simple and interactive Iris Flower Classification web app built using Streamlit and Scikit-Learn.
It allows users to input flower measurements and instantly get a predicted Iris species using a trained Decision Tree Classifier.

## 🚀 Features

- Interactive sliders to input flower measurements
- Machine learning model trained on the classic Iris dataset
- Real-time prediction displayed in the UI
-Includes a separate script to train and evaluate the model

## 📁 Project Structure
project/
├── app.py            # Streamlit application for classification
├── iris_model.py     # Script to train/test the classifier
├── requirements.txt  # # Python dependencies required to run this project
└── README.md         # Documentation

## 🧠 Model Information

The app uses the built-in Iris dataset from Scikit-Learn.
The ML model is a DecisionTreeClassifier, trained using all four flower measurements:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

iris_model.py also includes:

- Train/test split
- Model training
- Accuracy calculation

## 🛠️ Installation & Setup
1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2️⃣ Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3️⃣ Install dependencies

Create a requirements.txt like:
```nginx
streamlit
scikit-learn
numpy
```
Then install:
```bash
pip install -r requirements.txt
```

▶️ Run the Streamlit App

Start the web app using:
```bash
streamlit run app.py
```
Then open the URL shown in your terminal.

📊 Example Output (from iris_model.py)
Running:
```bash
python iris_model.py
```

will print something like:
```makefile
Accuracy: 0.97

```

## 🌼 About the Iris Dataset

The Iris dataset is a famous machine learning dataset containing 150 samples of Iris flowers across 3 species:
- Iris-setosa
- Iris-versicolor
- Iris-virginica

Each sample includes four measurements used for classification.
