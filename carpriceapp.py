
import streamlit as st
import pickle
import pandas as pd

with open('car_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('car_columns.pkl', 'rb') as columns_file:
    columns = pickle.load(columns_file)

st.title('Car Selling Price Prediction App')

year = st.number_input('Year of Manufacture', min_value=2000, max_value=2024, value=2015, step=1)
present_price = st.number_input('Present Showroom Price (in Lakhs)', min_value=0.5, value=5.0, step=0.1)
kms_driven = st.number_input('Kilometers Driven', min_value=100, value=30000, step=500)
owner = st.selectbox('Number of Previous Owners', [0, 1, 2, 3])
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
seller_type = st.selectbox('Seller Type', ['Dealer', 'Individual'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
if st.button('Predict Selling Price'):

    input_data = pd.DataFrame({
        'Year': [year],
        'Present_Price': [present_price],
        'Kms_Driven': [kms_driven],
        'Owner': [owner],
        'Fuel_Type_Diesel': [1 if fuel_type == 'Diesel' else 0],
        'Fuel_Type_Petrol': [1 if fuel_type == 'Petrol' else 0],
        'Seller_Type_Individual': [1 if seller_type == 'Individual' else 0],
        'Transmission_Manual': [1 if transmission == 'Manual' else 0],
    })

    for col in columns:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[columns]

    predicted_price = model.predict(input_data)

    st.success(f'Predicted Selling Price: Rs. {predicted_price[0]:.2f} Lakhs')
