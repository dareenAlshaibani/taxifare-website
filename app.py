import streamlit as st
import requests

# API URL
url = 'https://taxifare.lewagon.ai/predict'  # Replace with your API URL if you have one

# User Interface
st.title("TaxiFareModel Frontend")
st.markdown("Get a taxi fare estimate in NYC!")

# Input fields
pickup_date = st.date_input("Pickup date", min_value="2025-04-20")
pickup_time = st.time_input("Pickup time", value="11:19")
pickup_longitude = st.number_input("Pickup Longitude", value=-73.99)
pickup_latitude = st.number_input("Pickup Latitude", value=40.75)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.99)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.75)
passenger_count = st.number_input("Passenger Count", value=1)

# Send data to API
if st.button("Get Estimate"):
    params = {
        'pickup_datetime': f"{pickup_date} {pickup_time}",
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }

    response = requests.get(url, params=params)

    # Log the response for debugging
    st.write("API Response:", response.json())

    if response.status_code == 200:
        # Change 'prediction' to 'fare'
        fare = response.json().get('fare')

        # Check if the fare is None
        if fare is not None:
            st.success(f"Estimated fare: ${fare:.2f}")
        else:
            st.error("Fare not available. Please check your inputs.")
    else:
        st.error("Error in API request!")
