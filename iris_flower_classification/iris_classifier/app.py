import streamlit as st
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Load dataset and train model
data = load_iris()
X = data.data
y = data.target
model = DecisionTreeClassifier()
model.fit(X, y)

# Streamlit app
st.title("🌸 Iris Flower Classification App")

st.write("Enter the flower measurements below:")

# Input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)

# Predict button
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    flower_name = data.target_names[prediction]
    st.success(f"🌼 Predicted Species: **{flower_name.capitalize()}**")
