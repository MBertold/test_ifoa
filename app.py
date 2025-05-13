import streamlit as st
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv('api_key')

def main():
    st.title("Open Weather API")
    st.text("Inserisci città")
    city_name = st.text_input("Città")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
    result = requests.get(url)
    json = result.json()
    if st.button("Cerca"):
        a, b = st.columns(2)
        c, d = st.columns(2)

        a.metric("Temperature", json['main']["temp"],None , border=True)
        b.metric("Wind", "4 mph", None, border=True)

        c.metric("Humidity", json['main']["humidity"], None, border=True)
        d.metric("Pressure", json['main']["pressure"], None, border=True)

if __name__ == "__main__":
    main()