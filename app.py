import streamlit as st
import requests
from datetime import datetime

st.title("🚕 TaxiFareModel Frontend")
st.markdown("Get a taxi fare estimate in NYC!")

# --- Input fields ---
st.subheader("📝 Enter ride details:")

# Date and time input
pickup_date = st.date_input("Pickup date", value=datetime.today())
pickup_time = st.time_input("Pickup time", value=datetime.now().time())
pickup_datetime = datetime.combine(pickup_date, pickup_time).isoformat()

# Coordinates and passenger count
pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)
passenger_count = st.slider("Passenger Count", min_value=1, max_value=8, value=1)

# --- Prediction ---
if st.button("Predict fare"):
    url = 'https://taxifare.lewagon.ai/predict'  # 🔁 Replace with your own API if available

    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json()["fare"]
        st.success(f"💵 Estimated fare: ${prediction:.2f}")
    else:
        st.error("Something went wrong with the API call.")
