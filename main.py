from fastapi import FastAPI
import random

app = FastAPI(title="Sistema de Teledetección API - Mock Mode")

@app.get("/api/alertas")
def get_alertas():
    # Simular una cantidad considerable de puntos de calor (incendios) en Bolivia
    # Bolivia bounding box aproximado: Lat -22 a -10, Lon -69 a -57
    features = []
    for i in range(150): # 150 puntos de calor simulados
        lat = random.uniform(-22.0, -10.0)
        lon = random.uniform(-69.0, -57.0)
        temp = random.uniform(45.0, 100.0)
        riesgo = "ALTO" if temp > 70 else "MEDIO"

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]
            },
            "properties": {
                "temperatura_estimada": temp,
                "nivel_riesgo": riesgo
            }
        }
        features.append(feature)

    return {
        "type": "FeatureCollection",
        "features": features
    }

@app.post("/api/procesar_imagen")
def procesar_imagen_satelital():
    return {"mensaje": "Análisis ejecutado. El mapa se recargará con nuevos datos."}
