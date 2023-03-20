import streamlit as st
import requests


def get_house_data(address, api_key, api_secret):
    url = f"https://api.housecanary.com/v2/property/details?address={address}&zipcode={zipcode}"
    response = requests.get(url, auth=(api_key, api_secret))
    return response.json()["property/details"]["result"]


def app():
    st.title("House Value Estimator")
    st.write("Enter the address and zipcode of the house you want to get an estimate for:")
    address = st.text_input("Address:")
    zipcode = st.text_input("Zipcode:")

    if st.button("Get estimate"):
        api_key = "test_ZHR10MHG9YVB19SPIKG9"
        api_secret = "vDy4m18y7oNi9u3zFFXqk4fJmSV8X6GW"

        house_data = get_house_data(address, zipcode, api_key, api_secret)

        st.write(f"Estimated value: ${house_data['avm']['value']}")


if __name__ == "__main__":
    app()
