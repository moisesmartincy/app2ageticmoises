import streamlit as st
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Dashboard - Teledetección Forestal", layout="wide")

st.title("🛰️ Sistema de Monitoreo de Incendios Forestales - Análisis Bolivia")

@st.cache_data(ttl=60)
def get_alertas_data():
    try:
        res = requests.get(f"{API_URL}/api/alertas")
        if res.status_code == 200:
            return res.json()
    except Exception as e:
        pass
    return None

# Barra lateral
with st.sidebar:
    st.header("Controles")
    if st.button("Ejecutar Análisis Satelital", type="primary"):
        with st.spinner("Procesando imágenes satelitales..."):
            try:
                response = requests.post(f"{API_URL}/api/procesar_imagen")
                if response.status_code == 200:
                    st.success("Análisis completado. Nuevos focos detectados.")
                    get_alertas_data.clear() # Clear cache to fetch new data
                else:
                    st.error("Error al procesar la imagen.")
            except Exception as e:
                st.error(f"Error de conexión con la API: {e}")
    st.markdown("---")
    st.info("Este dashboard visualiza un Mapa de Calor (Heatmap) de los focos de incendio en Bolivia.")

# Crear mapa base centrado en Bolivia
m = folium.Map(location=[-16.2902, -63.5887], zoom_start=6)

# Cargar y dibujar Alertas de Incendio como Mapa de Calor
alertas_data = get_alertas_data()

if alertas_data:
    heat_data = []
    if alertas_data.get('features'):
        for feature in alertas_data['features']:
            geom = feature['geometry']
            props = feature['properties']
            if geom and geom['type'] == 'Point':
                lon, lat = geom['coordinates']
                # Folium HeatMap requiere formato [lat, lon, weight]
                # Usaremos la temperatura como weight (peso)
                heat_data.append([lat, lon, props.get('temperatura_estimada', 50)])

        # Añadir HeatMap al mapa
        HeatMap(
            heat_data,
            name="Mapa de Calor de Incendios",
            radius=15,
            blur=10,
            max_zoom=1,
        ).add_to(m)

        # Añadir control de capas
        folium.LayerControl().add_to(m)
else:
    st.warning("Esperando a que la API termine de arrancar o procesar datos...")

# Mostrar el mapa en Streamlit
st_data = st_folium(m, width=1200, height=700)
