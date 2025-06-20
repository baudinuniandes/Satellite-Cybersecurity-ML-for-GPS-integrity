# Carpeta `scripts/`

Este directorio aloja los scripts de python necesarios para ejecutar desde la Raspberry Pi el modelo de detección de anomalías y el script de generación de datos de spoofing simulado. A continuación se detallan los archivos y su propósito:
```text
models/
  ├── generate_spoofing.py
  └── realtime_gps_integrity.py
```

---

## 1. `generate_spoofing.py`

- **Tipo de archivo:**  
 Archivo de Python para ejecutar desde un entorno de Python 3.5 o superior.  
- **Descripción:**  
  - Recibe un documento .cvs con datos íntegros, por ejemplo el mismo dataset usado para entrenamiento.
  - Realiza puntos fuera de curso con base en movimientos aleatorios con cambio de rumbo y con una distancia entre 5 y 50 kilómetros, de forma aleatoria de un punto inicial del dataset original y crea un nuevo archivo con puntos de spoofing simulado.


## 2. `realtime_gps_integrity.py`

- **Tipo de archivo:**  
 Archivo de Python para ejecutar desde un entorno de Python 3.5 o superior.  
- **Descripción:**  
  - Utiliza el modelo pre entrenado con la finalidad de realizar una calificación de señales de GPS correctas y señales spoofing o anómalas.
  - El modelo seleccionado es el rf_best_model.pkl entrenado con el algoritmo de Random Forest Classifier.
  - Usa señales de GPS en tiempo real, recibidas mediante antena receptora conectada a la Raspberry Pi
  - Envía señal a actuadores tipo led, con la finalidad de dar una señal visual en caso de detectar señales anómalas.
