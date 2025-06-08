import streamlit as st
import requests
import pandas as pd

st.title("🌌 People in Space & ISS Tracker")
st.markdown("""
This app shows real-time data of astronauts currently in space and the location of the **International Space Station (ISS)**.  
Data is fetched from [Open Notify API](http://open-notify.org/).
""")

def fetch_json(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching data from {url}: {e}")
        return None

people_response = fetch_json('http://api.open-notify.org/astros.json')

if people_response:
    num_people = people_response['number']
    people = people_response['people']

    st.subheader("🧑‍🚀 People Currently in Space")
    st.write(f"**Total people in space:** {num_people}")
    st.write("**Names:**")
    for person in people:
        st.write(f"- {person['name']} ({person['craft']})")

iss_response = fetch_json('http://api.open-notify.org/iss-now.json')

if iss_response:
    latitude = float(iss_response['iss_position']['latitude'])
    longitude = float(iss_response['iss_position']['longitude'])

    st.subheader("🛰️ Current ISS Location")
    st.write(f"Latitude: {latitude}")
    st.write(f"Longitude: {longitude}")

    st.markdown("Below is the current location of the ISS on the globe 🌍.")
    iss_location_df = pd.DataFrame([[latitude, longitude]], columns=['lat', 'lon'])
    st.map(iss_location_df)
