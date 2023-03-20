import streamlit as st
import requests
import pandas as pd
import base64

def get_house_data(address, zipcode, api_key, api_secret):
    url = f"https://api.housecanary.com/v2/property/details?address={address}&zipcode={zipcode}"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{api_key}:{api_secret}".encode("ascii")).decode("ascii")
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data. Status code: {response.status_code}. Response text: {response.text}")
        return None

def display_house_data(house_data):
    st.header("Property Details")

    try:
        # Display address
        st.subheader("Address")
        property_data = house_data['result']['property']
        address_data = property_data['address']
        st.markdown(f"{address_data['line1']}, {address_data['city']}, {address_data['state']} {address_data['zipcode']}")

        # Display property details in columns
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Property Type")
            st.write(property_data['property_type'])

            st.subheader("Bedrooms")
            st.write(property_data.get('bedrooms', 'N/A'))

            st.subheader("Bathrooms")
            st.write(property_data.get('bathrooms', 'N/A'))

        with col2:
            st.subheader("Year Built")
            st.write(property_data['year_built'])

            st.subheader("Living Area (sq.ft)")
            st.write(property_data.get('living_area', 'N/A'))

            st.subheader("Lot Area (sq.ft)")
            st.write(property_data.get('lot_area', 'N/A'))

    except KeyError as e:
        st.error(f"Failed to display data. Missing field: {e}")


st.title("House Canary Web App")

address = st.text_input("Enter the address:")
zipcode = st.text_input("Enter the zipcode:")

api_key = "test_QXKKXWIHFL71J1D524Z1"
api_secret = "xVRYZEOZqBmheOYmFJsFDphFd6vFTRGL"

if st.button("Fetch Data"):
    house_data = get_house_data(address, zipcode, api_key, api_secret)
    if house_data:
        display_house_data(house_data)
    else:
        st.error("Failed to fetch data. Please try again.")
