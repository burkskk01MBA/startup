import streamlit as st
import requests
import pandas as pd


def get_house_data(address, zipcode, api_key, api_secret):
    url = f"https://api.housecanary.com/v2/property/details?address={address}&zipcode={zipcode}"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{api_key}:{api_secret}".encode("ascii")).decode("ascii")
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

    st.title("House Canary Web App")

address = st.text_input("Enter the address:")
zipcode = st.text_input("Enter the zipcode:")

api_key = "test_QXKKXWIHFL71J1D524Z1"
api_secret = "xVRYZEOZqBmheOYmFJsFDphFd6vFTRGL"

if st.button("Fetch Data"):
    house_data = get_house_data(address, zipcode, api_key, api_secret)
    if house_data:
        st.write(house_data)
    else:
        st.error("Failed to fetch data. Please try again.")
