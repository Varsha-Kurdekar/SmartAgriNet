import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("dataset.csv")

# Rename columns
data.columns = [
    'temperature',
    'humidity',
    'soil_moisture',
    'rainfall',
    'nitrogen',
    'potassium',
    'phosphorous'
]

# Create target column
data['irrigation'] = data['soil_moisture'].apply(
    lambda x: 1 if x < 50 else 0
)

# Features and target
X = data[['temperature', 'humidity', 'soil_moisture', 'rainfall']]
y = data['irrigation']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully as model.pkl")