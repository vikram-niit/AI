import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("train.csv")
# print(f"df.head(10): {df.head(10)}")
# print(f"df.columns: {df.columns}")
# print(f"df.shape: {df.shape}")
df_test = pd.read_csv("test.csv")
# print(f"df_test.head(10): {df_test.head(10)}")
# print(f"df_test.columns: {df_test.columns}")
# print(f"df_test.shape: {df_test.shape}")

# Perform EDA on the dataset

# Check for missing values
df.isnull().sum()

# Summary statistics
df.describe(include='all')

# Data types of each column
df.dtypes

# Explore categorical features
for col in ['Survived', 'Pclass', 'Sex', 'Embarked']:
  print(f"Value counts for {col}:")
  print(df[col].value_counts())
  df[col].value_counts().plot(kind='bar')
  plt.title(f'Distribution of {col}')
  plt.show()

# Explore numerical features
for col in ['Age', 'SibSp', 'Parch', 'Fare']:
  print(f"Descriptive statistics for {col}:")
  print(df[col].describe())
  df[col].plot(kind='hist', bins=20, title=f'Distribution of {col}')
  plt.gca().spines[['top', 'right']].set_visible(False)
  plt.show()

# Analyze relationships between features
pd.plotting.scatter_matrix(df[['Age', 'Fare', 'SibSp', 'Parch']], figsize=(10, 10))
plt.show()

# Correlation matrix
correlation_matrix = df.select_dtypes(include=['number']).corr()
plt.figure(figsize=(10, 8))
import seaborn as sns
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Survival rate by Pclass
df.groupby('Pclass')['Survived'].mean().plot(kind='bar')
plt.title('Survival Rate by Pclass')
plt.show()

# Survival rate by Sex
df.groupby('Sex')['Survived'].mean().plot(kind='bar')
plt.title('Survival Rate by Sex')
plt.show()

# Survival rate by Embarked
df.groupby('Embarked')['Survived'].mean().plot(kind='bar')
plt.title('Survival Rate by Embarked')
plt.show()

# Load the training data
df = pd.read_csv("train.csv")

# Feature engineering (example: combining SibSp and Parch)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Select features and target variable
features = ['Pclass', 'Sex', 'Age', 'Fare', 'FamilySize']
target = 'Survived'

# Preprocess data
df = df.dropna(subset=['Age', 'Embarked'])  # Drop rows with missing values for these columns
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1}) # Encode sex as numerical
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True) # One-hot encode Embarked

# Now features list includes the one-hot encoded Embarked features
features = features + ['Embarked_Q', 'Embarked_S']

# Split data into training and testing sets
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a RandomForestClassifier (you can experiment with other models)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Example prediction for a new passenger
new_passenger = pd.DataFrame({'Pclass': [3], 'Sex': [0], 'Age': [25], 'Fare': [7.25], 'FamilySize': [1], 'Embarked_Q': [0], 'Embarked_S': [1]})
prediction = model.predict(new_passenger)
print(f"Prediction for new passenger: {prediction[0]}") #0 = did not survive, 1 = survived

# Predictions on the test dataset
# Preprocess the test data in the same way as the training data
df_test['FamilySize'] = df_test['SibSp'] + df_test['Parch'] + 1
df_test['Sex'] = df_test['Sex'].map({'male': 0, 'female': 1})
df_test['Age'].fillna(df_test['Age'].median(), inplace=True) #Impute missing ages
df_test['Fare'].fillna(df_test['Fare'].median(),inplace=True) #Impute missing fares
df_test = pd.get_dummies(df_test, columns=['Embarked'], drop_first=True)

# Ensure the test data has the same columns as the training data
for col in ['Embarked_Q', 'Embarked_S']:
    if col not in df_test.columns:
        df_test[col] = 0

# Make predictions on the test set
test_features = ['Pclass', 'Sex', 'Age', 'Fare', 'FamilySize', 'Embarked_Q', 'Embarked_S']
predictions = model.predict(df_test[test_features])

# Create the results DataFrame
results_df = pd.DataFrame({'PassengerId': df_test['PassengerId'], 'Survived': predictions})

results_df.to_csv("results.csv", index=False)

