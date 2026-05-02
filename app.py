import streamlit as st
import pickle
import numpy as np
import os

model_path = os.path.join(os.getcwd(), "model.pkl")
model = pickle.load(open(model_path, "rb"))

st.title("🌱 Easy Crop Recommendation App")

temp = st.number_input("🌡️ Temperature (°C)", min_value=0.0)
humidity = st.number_input("💧 Humidity (%)", min_value=0.0)
rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0.0)

soil = st.selectbox("🌍 Soil Type", ["Sandy", "Loamy", "Clay", "Black"])

if soil == "Sandy":
    N, P, K = 40, 40, 40
elif soil == "Loamy":
    N, P, K = 80, 50, 50
elif soil == "Clay":
    N, P, K = 60, 60, 60
else:
    N, P, K = 90, 60, 60

ph = 6.5

if st.button("🌾 Recommend Crop"):
    data = np.array([[N, P, K, temp, humidity, rainfall, ph]])
    result = model.predict(data)
    st.success(f"🌱 Best Crop: {result[0]}")
