import streamlit as st
import requests
import base64


def get_house_data(address, zip_code, api_key, api_secret):
    url = f"https://api.housecanary.com/v2/property/details?address={address}&zipcode={zip_code}"
    auth_str = f"{api_key}:{api_secret}"
    auth_bytes = auth_str.encode('ascii')
    auth_base64 = base64.b64encode(auth_bytes).decode('ascii')
    headers = {"Authorization": f"Basic {auth_base64}"}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    return response_json["property/details"][0]["result"]


def display_house_data(house_data):
    st.subheader("Property Details")
    st.write("Address:", house_data["address"]["line1"])
    st.write("City:", house_data["address"]["city"])
    st.write("State:", house_data["address"]["state"])
    st.write("Zip Code:", house_data["address"]["zip"])
    st.write("County:", house_data["address"]["county"])
    st.write("Year Built:", house_data["property"]["year_built"])
    st.write("Living Area (sq ft):", house_data["property"]["living_area_sq_ft"])
    st.write("Bedrooms:", house_data["property"]["bedrooms"])
    st.write("Bathrooms:", house_data["property"]["bathrooms"])
    st.write("Lot Size (sq ft):", house_data["property"]["lot_sq_ft"])


# Main Streamlit app code
st.title("Home Equalizer Appraisal App")

with st.sidebar:
    st.subheader("Enter Property Information")
    address = st.text_input("Address")
    zip_code = st.text_input("Zip Code")
    get_data_button = st.button("Get Property Details")

if get_data_button:
    api_key = "test_ZHR10MHG9YVB19SPIKG9"
    api_secret = "vDy4m18y7oNi9u3zFFXqk4fJmSV8X6GW"

    try:
        house_data = get_house_data(address, zip_code, api_key, api_secret)
        display_house_data(house_data)
    except Exception as e:
        st.error(f"Error: Could not retrieve property details. {str(e)}")
