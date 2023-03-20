import requests
import base64
import streamlit as st
import pandas as pd

# Get HouseCanary API credentials
api_key = "test_QXKKXWIHFL71J1D524Z1"
api_secret = "xVRYZEOZqBmheOYmFJsFDphFd6vFTRGL"

# Define function to fetch data from HouseCanary API
def get_house_data(address, zipcode, api_key, api_secret):
    url = f"https://api.housecanary.com/v2/property/details?address={address}&zipcode={zipcode}"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{api_key}:{api_secret}".encode("ascii")).decode("ascii")
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Display the structure of the JSON object
        print(pd.json_normalize(response.json()))

        # Return the property details
        return response.json()["property/details"]["result"]
    else:
        st.error("Failed to fetch data. Please try again.")
        return None

# Define function to display house data
def display_house_data(house_data):
    property_data = house_data['property/details']['result']['property']
    assessment_data = house_data['property/details']['result']['assessment']
    
    st.subheader("Property Details")
    st.markdown(f"**Address**: {property_data['address']['line1']}, {property_data['address']['city']}, {property_data['address']['state']} {property_data['address']['zipcode']}")
    st.write(f"**Built Year**: {property_data['year_built']}")
    st.write(f"**Building Area**: {property_data['building_area_sq_ft']} sq. ft.")
    st.write(f"**Site Area**: {property_data['site_area_acres']} acres")
    st.write(f"**Building Quality Score**: {property_data['building_quality_score']}")
    st.write(f"**Assessed Value**: {assessment_data['total_assessed_value']}")
    st.write(f"**Tax Amount**: {assessment_data['tax_amount']}")
    
# Define the Streamlit app
def app():
    st.set_page_config(page_title="HouseCanary Appraisal", page_icon=":house:")
    st.title("HouseCanary Appraisal")
    st.markdown("Enter the address and zipcode of the property to get an appraisal.")
    
    # Get user input
    address = st.text_input("Address")
    zipcode = st.text_input("Zipcode")
    
    # Fetch data from HouseCanary API
    if st.button("Get Appraisal"):
        house_data = get_house_data(address, zipcode, api_key, api_secret)
        if house_data is not None:
            display_house_data(house_data)
        
if __name__ == "__main__":
    app()
