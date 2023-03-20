import streamlit as st
import requests
import base64

# Function to fetch data from House Canary API
def get_house_data(address, zipcode, api_key, api_secret):
    url = f"https://api.housecanary.com/v2/property/details?address={address}&zipcode={zipcode}"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{api_key}:{api_secret}".encode("ascii")).decode("ascii")
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["property/details"]["result"]
    else:
        st.error("Failed to fetch data. Please try again.")
        return None

# Function to display data
def display_house_data(house_data):
    st.subheader("Property Details")

    try:
        # Display address
        st.write(f"**Address:** {house_data['address_info']['address']}, {house_data['address_info']['city']}, {house_data['address_info']['state']} {house_data['address_info']['zipcode']}")

        # Display property details
        st.write(f"**Property Type:** {house_data['property']['property_type']}")
        st.write(f"**Bedrooms:** {house_data['property'].get('number_of_bedrooms', 'N/A')}")
        st.write(f"**Bathrooms:** {house_data['property'].get('total_bath_count', 'N/A')}")
        st.write(f"**Year Built:** {house_data['property'].get('year_built', 'N/A')}")
        st.write(f"**Living Area (sq.ft):** {house_data['property'].get('building_area_sq_ft', 'N/A')}")
        st.write(f"**Lot Area (sq.ft):** {house_data['property'].get('site_area_acres', 'N/A')}")
        st.write(f"**Assessed Value:** {house_data['property'].get('assessed_value', 'N/A')}")

    except KeyError as e:
        st.error(f"Failed to display data. Missing field: {e}")

def app():
    st.title("House Canary Property Details")

    # Add a sidebar for user input
    st.sidebar.header("Input Property Information")

    address = st.sidebar.text_input("Address", "123 Main St")
    zipcode = st.sidebar.text_input("Zipcode", "12345")

    api_key = "test_QXKKXWIHFL71J1D524Z1"
    api_secret = "xVRYZEOZqBmheOYmFJsFDphFd6vFTRGL"

    fetch_button = st.sidebar.button("Fetch Property Details")

    if fetch_button:
        # Fetch data
        house_data = get_house_data(address, zipcode, api_key, api_secret)

        if house_data:
            display_house_data(house_data)

    # Add a footer
    st.markdown("---")
    st.markdown("This web app is using data from the House Canary API. For more information, please visit their [website](https://www.housecanary.com/).")

if __name__ == "__main__":
    app()
