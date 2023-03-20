import streamlit as st
import requests
import base64

# Functions for fetching data and displaying it
# ...

def app():
    st.title("House Canary Property Details")

    # Add a sidebar for user input
    st.sidebar.header("Input Property Information")

    address = st.sidebar.text_input("Address", "123 Main St")
    zipcode = st.sidebar.text_input("Zipcode", "12345")

    api_key = "test_QXKKXWIHFL71J1D524Z1"
    api_secret = "xVRYZEOZqBmheOYmFJsFDphFd6vFTRGL"

    st.sidebar.button("Fetch Property Details")

    # Fetch data
    house_data = get_house_data(address, zipcode, api_key, api_secret)

    if house_data:
        display_house_data(house_data)

    # Add a footer
    st.markdown("---")
    st.markdown("This web app is using data from the House Canary API. For more information, please visit their [website](https://www.housecanary.com/).")

if __name__ == "__main__":
    app()

