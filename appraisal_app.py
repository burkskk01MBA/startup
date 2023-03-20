import streamlit as st
import requests
import base64
import pydeck as pdk
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")


def get_coordinates(address):
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)


def get_house_data(address, zip_code, api_key, api_secret):
    url = f"https://api.housecanary.com/v2/property/details?address={address}&zipcode={zip_code}"
    auth_str = f"{api_key}:{api_secret}"
    auth_bytes = auth_str.encode('ascii')
    auth_base64 = base64.b64encode(auth_bytes).decode('ascii')
    headers = {"Authorization": f"Basic {auth_base64}"}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    return response_json["property/details"][0]["property"]


def display_map(coordinates):
    st.subheader("Property Location")
    map_data = pdk.Layer(
        "ScatterplotLayer",
        data={"coordinates": [coordinates]},
        get_position="coordinates",
        get_radius=100,
        get_fill_color=[255, 0, 0],
        pickable=True,
    )
    view_state = pdk.ViewState(latitude=coordinates[0], longitude=coordinates[1], zoom=15)
    st.pydeck_chart(pdk.Deck(mapbox_key=MAPBOX_API_KEY, layers=[map_data], initial_view_state=view_state))


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
    MAPBOX_API_KEY = "pk.eyJ1IjoiYnVya3NrazAxIiwiYSI6ImNsZmhkcm14NDAzb3EzdHBtdXhhZm9vMjYifQ.EGOxDJvYrc-9toE0BQ6N5g"  # Replace this with your Mapbox API key

    try:
        house_data = get_house_data(address, zip_code, api_key, api_secret)
        full_address = f"{address}, {house_data['address']['city']}, {house_data['address']['state']} {house_data['address']['zip']}"
        coordinates = get_coordinates(full_address)
        display_map(coordinates)
        display_house_data(house_data)
    except Exception as e:
        st.error(f"Error: Could not retrieve property details. {str(e)}")
