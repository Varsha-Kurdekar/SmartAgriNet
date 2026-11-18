import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("irrigation_dataset.csv")

X = data[['Temperature','Humidity','Soil_Moisture','Rainfall']]
y = data['Irrigation']

model = RandomForestClassifier()

model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved")