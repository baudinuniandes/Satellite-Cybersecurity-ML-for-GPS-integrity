"""
Monitorea en tiempo real la integridad de señal GPS recibida por USB, usando el modelo RandomForest preentrenado.
Además controla dos LEDs vía GPIO:
  - GPIO17: LED encendido si señal íntegra
  - GPIO12: LED encendido si señal anómala o sin fix GPS

Uso:
  python3 realtime_gps_integrity.py

Salida consola:
  YYYY-MM-DDThh:mm:ssZ → True|False

True  = señal íntegra (LED en GPIO17)
False = señal anómala o sin fix (LED en GPIO12)

Requisitos de instalación en Raspberry Pi:
  sudo apt update
  sudo apt install -y gpsd gpsd-clients python3-gpsd-py3 python3-rpi.gpio
  pip3 install gpsd-py3 numpy joblib scikit-learn
"""

import time
from datetime import datetime
import numpy as np
import joblib
import gpsd
import RPi.GPIO as GPIO
from math import radians, sin, cos, sqrt, atan2, degrees

# Configuración GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_LED_OK = 17      # Señal íntegra
GPIO_LED_ALERT = 12   # Señal anómala o no fix
GPIO.setup(GPIO_LED_OK, GPIO.OUT)
GPIO.setup(GPIO_LED_ALERT, GPIO.OUT)

# Ruta al modelo RF
MODEL_FILE = 'rf_continuity_model.pkl'  # Tener presente que para la ejecucion en la Raspberry debe ir la ruta completa, para esta ejecucion se uso el mismo direcctorio

# Funciones

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    φ1, φ2 = radians(lat1), radians(lat2)
    Δφ = radians(lat2 - lat1)
    Δλ = radians(lon2 - lon1)
    a = sin(Δφ/2)**2 + cos(φ1)*cos(φ2)*sin(Δλ/2)**2
    d = 2 * R * atan2(sqrt(a), sqrt(1-a))
    y = sin(Δλ) * cos(φ2)
    x = cos(φ1)*sin(φ2) - sin(φ1)*cos(φ2)*cos(Δλ)
    θ = (degrees(atan2(y, x)) + 360) % 360
    return d, θ


def load_model():
    try:
        m = joblib.load(MODEL_FILE)
        print(f"[INFO] Modelo RF cargado desde '{MODEL_FILE}'")
        return m
    except Exception as e:
        print(f"[ERROR] No se pudo cargar el modelo: {e}")
        exit(1)

# Se puede realizar pruebas de conexion y funcionamiento del GPS antes de ejecutar este script
def connect_gpsd():
    try:
        gpsd.connect()
        print("[INFO] Conectado a gpsd")
    except Exception as e:
        print(f"[ERROR] No se pudo conectar a gpsd: {e}")
        exit(1)


def parse_features(lat, lon, prev):
    return np.array([haversine(prev[0], prev[1], lat, lon)], dtype=np.float32)


def update_leds(ok):
    if ok:
        GPIO.output(GPIO_LED_OK, GPIO.HIGH)
        GPIO.output(GPIO_LED_ALERT, GPIO.LOW)
    else:
        GPIO.output(GPIO_LED_OK, GPIO.LOW)
        GPIO.output(GPIO_LED_ALERT, GPIO.HIGH)


def main():
    model = load_model()
    connect_gpsd()

    prev = None
    print("[INFO] Iniciando monitor GPS (Ctrl+C para salir)...")
    try:
        while True:
            try:
                pkt = gpsd.get_current()
            except UserWarning:
                # GPS no activo
                update_leds(False)
                print("[WARN] GPS not active")
                time.sleep(1)
                continue

            if pkt.mode >= 2 and pkt.lat is not None and pkt.lon is not None:
                lat, lon = pkt.lat, pkt.lon
                if prev is not None:
                    X = parse_features(lat, lon, prev)
                    lab = model.predict(X)[0]
                    ok = bool(lab == 1)
                    ts = datetime.utcnow().isoformat(timespec="seconds") + "Z"
                    print(f"{ts} → {ok}")
                    update_leds(ok)
                prev = (lat, lon)
            else:
                # Sin fix GPS válido
                update_leds(False)
                print("[WARN] Sin fix GPS válido")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Monitor detenido. Limpiando GPIO...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
