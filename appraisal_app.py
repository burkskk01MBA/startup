import streamlit as st
import requests


def get_house_data(address, zip_code, api_key, api_secret):
    # Make API request to HouseCanary endpoint and return result
    url = f"https://api.housecanary.com/v2/property/details?property={address}&zipcode={zip_code}"
    headers = {"HouseCanary-Api-Key": api_key, "HouseCanary-Api-Secret": api_secret}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    st.write(response_json)  # Display the entire API response
    return response_json["property/details"][0]["result"]


# Main Streamlit app code
st.title("HouseCanary Property Details")

# Get user input
address = st.text_input("Enter Address")
zip_code = st.text_input("Enter Zip Code")

# Button to trigger API request and show results
if st.button("Get Property Details"):
    # Get API credentials (you can replace with your own if you have them)
    api_key = "test_ZHR10MHG9YVB19SPIKG9"
    api_secret = "vDy4m18y7oNi9u3zFFXqk4fJmSV8X6GW"
    
    # Make API request and display results
    try:
        house_data = get_house_data(address, zip_code, api_key, api_secret)
        st.write(house_data)
    except Exception as e:
        st.write(f"Error: Could not retrieve property details. {str(e)}")
