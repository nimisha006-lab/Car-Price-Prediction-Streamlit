import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Used Car Price Prediction")

st.markdown("""
Predict the estimated selling price of a used car based on its specifications.
Fill in the details below and click **Predict Price**.
""")

st.write("Enter the car details below to predict its selling price.")

# -------------------------------
# 🚘 Car Information
# -------------------------------
st.subheader("🚘 Car Information")

col1, col2 = st.columns(2)

with col1:
    car_name = st.selectbox(
        "Car Name",
        encoders["car_name"].classes_
    )

    model_name = st.selectbox(
        "Model",
        encoders["model"].classes_
    )

with col2:
    brand = st.selectbox(
        "Brand",
        encoders["brand"].classes_
    )

# -------------------------------
# ⚙️ Vehicle Specifications
# -------------------------------
st.subheader("⚙️ Vehicle Specifications")

col1, col2 = st.columns(2)

with col1:
    vehicle_age = st.number_input(
        "Vehicle Age (years)",
        min_value=0,
        step=1
    )

    mileage = st.number_input(
        "Mileage (km/l)",
        min_value=0.0
    )

    max_power = st.number_input(
        "Max Power (BHP)",
        min_value=0.0
    )

with col2:
    km_driven = st.number_input(
        "Kilometers Driven",
        min_value=0
    )

    engine = st.number_input(
        "Engine (CC)",
        min_value=0
    )

    seats = st.number_input(
        "Number of Seats",
        min_value=1,
        step=1
    )

# -------------------------------
# 📋 Additional Details
# -------------------------------
st.subheader("📋 Additional Details")

col1, col2 = st.columns(2)

with col1:
    fuel_type = st.selectbox(
        "Fuel Type",
        encoders["fuel_type"].classes_
    )

    seller_type = st.selectbox(
        "Seller Type",
        encoders["seller_type"].classes_
    )

with col2:
    transmission_type = st.selectbox(
        "Transmission Type",
        encoders["transmission_type"].classes_
    )

st.divider()

if st.button("Predict Price"):
    car_name = encoders["car_name"].transform([car_name])[0]
    brand = encoders["brand"].transform([brand])[0]
    model_name = encoders["model"].transform([model_name])[0]
    seller_type = encoders["seller_type"].transform([seller_type])[0]
    fuel_type = encoders["fuel_type"].transform([fuel_type])[0]
    transmission_type = encoders["transmission_type"].transform([transmission_type])[0]

    input_data = pd.DataFrame({
        "car_name": [car_name],
        "brand": [brand],
        "model": [model_name],
        "vehicle_age": [vehicle_age],
        "km_driven": [km_driven],
        "seller_type": [seller_type],
        "fuel_type": [fuel_type],
        "transmission_type": [transmission_type],
        "mileage": [mileage],
        "engine": [engine],
        "max_power": [max_power],
        "seats": [seats]
    })

    prediction = model.predict(input_data)

    st.success("✅ Prediction Complete!")

    st.metric(
        label="Estimated Selling Price",
        value=f"₹ {prediction[0]:,.0f}"
    )

    st.balloons()