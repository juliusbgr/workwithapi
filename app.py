import streamlit as st
import requests
import pandas as pd

# Title and Description
st.title("🌌 People in Space & ISS Tracker")
st.markdown("""
This app shows real-time data of astronauts currently in space and the location of the **International Space Station (ISS)**.  
Data is fetched from [Open Notify API](http://open-notify.org/).
""")

# Fetching people in space
people_url = 'http://api.open-notify.org/astros.json'
people_response = requests.get(people_url).json()

num_people = people_response['number']
people = people_response['people']

# Display number of people and names
st.subheader("🧑‍🚀 People Currently in Space")
st.write(f"**Total people in space:** {num_people}")
st.write("**Names:**")
for person in people:
    st.write(f"- {person['name']} ({person['craft']})")

# Fetching ISS location
iss_url = 'http://api.open-notify.org/iss-now.json'
iss_response = requests.get(iss_url).json()

latitude = float(iss_response['iss_position']['latitude'])
longitude = float(iss_response['iss_position']['longitude'])

# Display ISS location
st.subheader("🛰️ Current ISS Location")
st.write(f"Latitude: {latitude}")
st.write(f"Longitude: {longitude}")

# Show ISS location on map
st.markdown("Below is the current location of the ISS on the globe 🌍.")
iss_location_df = pd.DataFrame([[latitude, longitude]], columns=['lat', 'lon'])
st.map(iss_location_df)
