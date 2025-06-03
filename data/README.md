# Carpeta `data/`

Este directorio contiene todos los conjuntos de datos utilizados para entrenar, validar y probar nuestro modelo de integridad GPS en tiempo real. A continuación se describen los archivos y su propósito:

---

├── data/        

│   ├── train_data.csv               # 7 500 muestras reales + etiquetas sintéticas de spoofing

│   ├── val_data.csv                 # Datos de validación (vuelo marzo 2025) + etiquetas

│   └── test_data.csv                # Datos de prueba independientes + etiquetas


## 1. `train_data.csv`

- **Descripción:**  
  conjunto principal de entrenamiento. Contiene ~7 500 registros recolectados de FlightRadar24, correspondientes a 13 vuelos diferentes de aeronaves de la FAC.  
- **Columnas esperadas:**  
  - `UTC`         : marca de tiempo en formato ISO 8601 (ej. `2024-10-23T14:56:23Z`)  
  - `Callsign`    : identificador de la aeronave (ej. `GAF665`)  
  - `Latitude`    : latitud en grados decimales (ej. `33.824123`)  
  - `Longitude`   : longitud en grados decimales (ej. `35.495888`)  
  - `Altitude`    : altitud en metros (ej. `1200`)  
  - `Speed`       : velocidad en nudos (ej. `250`)  
  - `Direction`   : rumbo/heading en grados (0–359)  
  - `Label`       : etiqueta de integridad (`1` = íntegro, `0` = no íntegro/spoofing).  
- **Uso:**  
  - Entrenar el `RandomForestClassifier` (continuidad GPS).  
  - Como base para inyectar anomalías sintéticas (spoofing/jamming) si no contiene `Label`.  
  
---

## 2. `val_data.csv`

- **Descripción:**  
  conjunto de validación completamente independiente. Corresponde a datos reales de un vuelo de la FAC en marzo de 2025.  
- **Columnas esperadas:**  
  - Mismas que `train_data.csv`.  
  - Si no existe `Label`, se generan etiquetas sintéticas siguiendo el mismo criterio (20 % spoofing).  
- **Uso:**  
  - Afinar hiperparámetros del modelo (GridSearchCV).  
  - Evaluar rendimiento durante el entrenamiento (no se usa para ajustar pesos del RandomForest).  
 
---

## 3. `test_data.csv`

- **Descripción:**  
  conjunto de prueba final. Datos recogidos en tiempo real (o simulados) que nunca se usaron en entrenamiento ni validación.  
- **Columnas esperadas:**  
  - Mismas que `train_data.csv`.  
  - Si no existe `Label`, se generan etiquetas sintéticas (20 % spoofing).  
- **Uso:**  
  - Evaluación final del modelo afinado.  
  - Cálculo de métricas definitivas: Accuracy, Precision, Recall, F1, AUC, Matriz de Confusión.  
  - Simula comportamiento en datos nuevos no vistos.

---

## Estructura de un registro de ejemplo

```csv
UTC,Callsign,Latitude,Longitude,Altitude,Speed,Direction,Label
2024-10-23T14:56:23Z,GAF665,33.824123,35.495888,1200,250,188,1
2024-10-23T14:56:29Z,GAF665,33.823837,35.495720,1195,255,190,1
...

