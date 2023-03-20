import requests
import streamlit as st

# HouseCanary API credentials
api_key = "test_ZHR10MHG9YVB19SPIKG9"
api_secret = "vDy4m18y7oNi9u3zFFXqk4fJmSV8X6GW"

# HouseCanary endpoint for getting property details
url = "https://api.housecanary.com/v2/property/details"

# Function to get property details for the given address using HouseCanary API
def get_house_data(address, api_key, api_secret):
    # Define headers and query parameters for the API request
    headers = {"Authorization": f"Basic {api_key}:{api_secret}"}
    params = {"address": address, "zipcode": "", "state": "", "city": ""}

    # Send a GET request to the HouseCanary API
    response = requests.get(url, headers=headers, params=params)

    # Parse the JSON response and return the property details
    return response.json()["property/details"]["result"]

# Streamlit app
def app():
    # Set the page title and layout
    st.set_page_config(page_title="HouseCanary Property Details", page_icon=":house_with_garden:")
    
    # Set the app title and subtitle
    st.title("HouseCanary Property Details")
    st.subheader("Enter the address to get the property details:")
    
    # Get the user's input address
    address = st.text_input("Address", value="", max_chars=100)

    # Display the property details when the user submits the address
    if st.button("Submit"):
        # Call the function to get the property details
        house_data = get_house_data(address, api_key, api_secret)

        # Display the property details in a table
        st.write("## Property Details")
        st.table(house_data)

# Run the app
if __name__ == "__main__":
    app()
