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

    print(response.json())

    if response.status_code == 200:
        try:
            return response.json()["property/details"]["result"]
        except KeyError as e:
            st.error(f"Failed to display data. Missing field: {e}")
            return None
    else:
        st.error("Failed to fetch data. Please try again.")
        return None

# Function to display data
def display_house_data(house_data):
    st.header("Property Details")

    try:
        # Display address
        st.subheader("Address")
        property_data = house_data['property']
        address_data = house_data['address_info']
        st.markdown(f"{address_data['address']}, {address_data['city']}, {address_data['state']} {address_data['zipcode']}")

        # Display property details in columns
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Property Type")
            st.write(property_data['property_type'])

            st.subheader("Bedrooms")
            st.write(property_data.get('number_of_bedrooms', 'N/A'))

            st.subheader("Bathrooms")
            st.write(property_data.get('total_bath_count', 'N/A'))

            st.subheader("Year Built")
            st.write(property_data.get('year_built', 'N/A'))

        with col2:
            st.subheader("Living Area (sq.ft)")
            st.write(property_data.get('building_area_sq_ft', 'N/A'))

            st.subheader("Lot Area (sq.ft)")
            st.write(property_data.get('site_area_acres', 'N/A'))

            st.subheader("Assessed Value")
            st.write(property_data.get('assessed_value', 'N/A'))

    except KeyError as e:
        st.error(f"Failed to display data. Missing field: {e}")

def app():
    st.title("House Canary Property Details")

    # Add a sidebar for user input
    st.sidebar.header("Input Property Information")

    address = st.sidebar.text_input("Address", "123 Main St")
    zipcode = st.sidebar.text_input("Zipcode", "12345")

    api_key = "test_AQ5GSA1A96947PDOJJXE"
    api_secret = "zxkVIQ9O3g3YkFVEZTOIs4TvCmb00kd3"

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
