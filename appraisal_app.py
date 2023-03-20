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
    st.header("Property Details")

    try:
        # Display address
        st.subheader("Address")
        property_data = house_data['property']
        address_data = house_data['address']
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

            st.subheader("Year Built")
            st.write(property_data.get('year_built', 'N/A'))

            st.subheader("Living Area (sq.ft)")
            st.write(property_data.get('sqft', 'N/A'))

        with col2:
            st.subheader("Lot Area (sq.ft)")
            st.write(property_data.get('lot_size', 'N/A'))

            st.subheader("Assessed Value")
            st.write(property_data.get('value', 'N/A'))

            st.subheader("Tax Assessment")
            st.write(property_data.get('tax_assessment', 'N/A'))

    except KeyError as e:
        st.error(f"Failed to display data. Missing field: {e}")

def app():
    st.set_page_config(page_title="House Canary Property Details", page_icon=":house_with_garden:")

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
