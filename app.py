import streamlit as st
import os
from dotenv import load_dotenv
import requests
import pandas as pd

#load_dotenv()
API_KEY = st.secrets['api_key']

def main():
    st.title("Open Weather API")
    st.text("Inserisci città")
    city_name = st.text_input("Città")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
    result = requests.get(url)
    json = result.json()
    temperatura =json['main']["temp"] - 273.15
    temperatura = round(temperatura,2)
    vento = json["wind"]["speed"]
    umidità = json['main']["humidity"]
    pressione = json['main']["pressure"]
    lat = json["coord"]["lat"]
    lon = json["coord"]["lon"]
    
    if st.button("Cerca"):
        a, b = st.columns(2)
        c, d = st.columns(2)

        a.metric("Temperature",f"{temperatura} °C" ,delta=None)
        b.metric("Wind",f"{vento} m/sec" , delta=None)

        c.metric("Humidity",f"{umidità} %" ,delta= None)
        d.metric("Pressure",f"{pressione} hPa" ,delta= None)
        
        st.map(pd.DataFrame({'lat':[lat],'lon':[lon]},columns=['lat','lon']))

if __name__ == "__main__":
    main()