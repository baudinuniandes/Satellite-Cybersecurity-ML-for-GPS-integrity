# === IMPORTS Y CARGA DE DATOS ===
import pandas as pd
import numpy as np
import joblib
from math import radians, sin, cos, sqrt, atan2, degrees
from google.colab import files

# === SUBIR CSV ===
print("Sube aquí tu archivo gps_valid.csv (datos íntegros sin spoofing)")
uploaded = files.upload()  # Selecciona gps_valid.csv

# Nombre del CSV subido
CSV_FILE = "gps_valid.csv"

# Cargar y parsear
df = pd.read_csv(CSV_FILE, parse_dates=["UTC"])
# Separar Lat/Lon
df[["Lat","Lon"]] = df["Position"].str.split(",", expand=True).astype(float)
df = df.sort_values("UTC").reset_index(drop=True)

print(f"Datos cargados: {len(df)} filas")
# === CÁLCULO DE FEATURES DE CONTINUIDAD ===
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # radio terrestre en metros
    φ1, φ2 = radians(lat1), radians(lat2)
    Δφ = radians(lat2 - lat1)
    Δλ = radians(lon2 - lon1)
    a = sin(Δφ/2)**2 + cos(φ1)*cos(φ2)*sin(Δλ/2)**2
    d = 2 * R * atan2(sqrt(a), sqrt(1-a))
    y = sin(Δλ) * cos(φ2)
    x = cos(φ1)*sin(φ2) - sin(φ1)*cos(φ2)*cos(Δλ)
    θ = (degrees(atan2(y, x)) + 360) % 360
    return d, θ

def compute_continuity_features(df):
    dists, bears = [], []
    for i in range(1, len(df)):
        d, b = haversine(
            df.loc[i-1,"Lat"], df.loc[i-1,"Lon"],
            df.loc[i  ,"Lat"], df.loc[i  ,"Lon"]
        )
        dists.append(d)
        bears.append(b)
    return pd.DataFrame({
        "dist":    np.array(dists, dtype=np.float32),
        "bearing": np.array(bears, dtype=np.float32)
    })

cont_df = compute_continuity_features(df)
y_clean = np.ones(len(cont_df), dtype=int)

print(f"{len(cont_df)} muestras de continuidad calculadas")

# === GENERACIÓN DE ANOMALÍAS SINTÉTICAS ===
SEED = 42
ANOMALY_RATIO = 0.2

np.random.seed(SEED)
n = len(cont_df)
n_anom = int(n * ANOMALY_RATIO)
# Seleccion de indices del dataset original
idx = np.random.choice(n, n_anom, replace=False)

# Creacion de un arreglo con valores de spoofing generados
cont_anom_features = []
for j in idx:
    # Toma de datos del dataset original
    d_orig, b_orig = cont_df.loc[j, "dist"], cont_df.loc[j, "bearing"]
    lat0, lon0 = df.loc[j, "Lat"], df.loc[j, "Lon"] # Uso de la funcion Haversine para carcualar valores de latitud y longitud

    # Generacion de parametros aleatorios fuera de ruta entre 3 y 25 NM
    jump_d = np.random.uniform(5_000, 50_000)
    jump_b = np.random.uniform(0, 360)

    # El calculo asume que se tiene un salto a una nueva posicion, simulando un spoofing
    # La anomalia estaria en el punto generado (df.loc[j])
    φ = radians(lat0)
    Δφ = (jump_d * cos(radians(jump_b))) / 6371000
    Δλ = (jump_d * sin(radians(jump_b))) / (6371000 * cos(φ))
    lat1 = lat0 + degrees(Δφ)
    lon1 = lon0 + degrees(Δλ)

    '''
    Calcular las características con la funcion  Haversine para el punto anómalo en relación con el punto anterior, asumiendo que el punto anterior es el que está en el índice j-1 en el DataFrame original (df).
    Se usara la interpretación de que el salto modifica la ubicación del punto j y que la anomalía se detecta en la característica de continuidad entre j-1 y el j modificado.
    Esto significa que el cálculo con la funcion Haversine debe realizarse entre `df.loc[j-1]` y la nueva ubicación `(lat1, lon1)`.
    Las características `dist` y `bearing` en el índice `i` dentro de `cont_df` corresponden a la continuidad entre `df.loc[i-1]` y `df.loc[i]`.
    Si queremos introducir una anomalía en el índice `j` de `cont_df`, deberíamos modificar las características de continuidad entre `df.loc[j-1]` y una nueva ubicación para `df.loc[j]`.

    Las características anómalas deberían calcularse entre `df.loc[j]` y una nueva ubicación para `df.loc[j+1]`.
    El código original usaba `df.loc[j]` como punto de inicio del salto y aplicaba el salto para obtener un nuevo punto (lat1, lon1).
    Luego calculaba Haversine entre `df.loc[j]` y este nuevo punto. Este cálculo no reemplaza directamente el valor original en `cont_df[j]` (que es entre `df[j]` y `df[j+1]`).

    Supongamos entonces que el objetivo es crear puntos de spoofing. Un paso anómalo en el índice `j` de `cont_df` significa que la transición desde `df.loc[j]` hacia `df.loc[j+1]` es anómala.
    Deberíamos tomar `df.loc[j]` como punto de partida y aplicar un salto para encontrar una nueva ubicación para el siguiente punto (que sería el punto anómalo `df.loc[j+1]`).
    '''

    lat_start, lon_start = df.loc[j, "Lat"], df.loc[j, "Lon"]

    φ_start = radians(lat_start)
    Δφ = (jump_d * cos(radians(jump_b))) / 6371000
    Δλ = (jump_d * sin(radians(jump_b))) / (6371000 * cos(φ_start))
    lat_anom_next = lat_start + degrees(Δφ)
    lon_anom_next = lon_start + degrees(Δλ)

    # Calcular las características de Haversine para este paso anómalo (entre df.loc[j] y la nueva ubicación para df.loc[j+1])
    d_anom, b_anom = haversine(lat_start, lon_start, lat_anom_next, lon_anom_next)
    cont_anom_features.append([d_anom, b_anom])

# Se convierte el listado de anomalias en un numpy array
cont_anom_features = np.array(cont_anom_features, dtype=np.float32)

y_anom = np.zeros(n_anom, dtype=int)

# Se combinan los datos del dataset entre integros 1 y anomalos o spoofing 0
X = np.vstack([cont_df.values, cont_anom_features])
y = np.concatenate([y_clean, y_anom])

print(f"Dataset combinado: {X.shape[0]} muestras ({len(y_clean)} íntegros + {n_anom} anómalos)")
