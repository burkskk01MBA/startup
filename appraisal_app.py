import streamlit as st
import requests

def get_house_data(address, zipcode, api_key, api_secret):
    endpoint = "https://api.housecanary.com/v2/property/details"
    payload = {
        "address": address,
        "zipcode": zipcode
    }
    headers = {
        "X-API-KEY": api_key,
        "X-API-SECRET": api_secret,
        "Content-Type": "application/json"
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    return response.json()["property/details"]["result"]

def app():
    st.title("Real Estate Appraisal")

    st.markdown("""
    This web app fetches a real estate appraisal using HouseCanary's API.
    """)

    address = st.text_input("Enter the address of the property")
    zipcode = st.text_input("Enter the zipcode of the property")

    if st.button("Get appraisal"):
        api_key = "test_AQ5GSA1A96947PDOJJXE"
        api_secret = "zxkVIQ9O3g3YkFVEZTOIs4TvCmb00kd3"
        house_data = get_house_data(address, zipcode, api_key, api_secret)

        st.write(f"Property value: {house_data['avm']['value']}")
        st.write(f"Last sale date: {house_data['lastSaleDate']}")
        st.write(f"Last sale amount: {house_data['lastSaleAmount']}")
        st.write(f"Year built: {house_data['yearBuilt']}")
        st.write(f"Number of bedrooms: {house_data['bedrooms']}")
        st.write(f"Number of bathrooms: {house_data['bathrooms']}")

if __name__ == "__main__":
    app()
