import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("crop_data.csv")

X = data[['N','P','K','temperature','humidity','rainfall','ph']]
y = data['label']

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model created!")
