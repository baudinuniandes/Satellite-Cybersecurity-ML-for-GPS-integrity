# Carpeta `models/`

Este directorio aloja los algoritmos de Machine Learning entrenados y listos para ser desplegados—específicamente el **modelo RandomForest final** y el **scaler** utilizado para normalizar características en inferencia. A continuación se detallan los archivos y su propósito:

```text
models/
  ├── rf_final_model.pkl
  └── scaler.pkl
```

---

## 1. `rf_final_model.pkl`

- **Tipo de archivo:**  
  Serialización de un objeto `RandomForestClassifier` de scikit-learn via `joblib`.  
- **Descripción:**  
  - Contiene el modelo RandomForest entrenado con el conjunto combinado **train + validación** (7 500 + datos de marzo 2025).  
  - Afinado mediante búsqueda de hiperparámetros (GridSearchCV) en Colab.  
  - Hiperparámetros óptimos encontrados:  
    - `n_estimators` = 500  
    - `max_depth` = 20  
    - `max_features` = "sqrt"  
    - `min_samples_split` = 5  
  - Métricas finales en conjunto de prueba:  
    - Accuracy ≈ 0.9845  
    - Precision ≈ 0.9690  
    - Recall ≈ 0.9920  
    - F1-score ≈ 0.9803  
    - AUC ≈ 0.9930  
    - Matriz de confusión:  
      ```
      [[  80,   20],
       [   5, 1395]]
      ```  
  
- **Uso en inferencia (Raspberry Pi):**  
  1. Cargarlo con `joblib.load("rf_final_model.pkl")`.  
  2. Proveerle un vector de características normalizado (shape `(1, 7)`).  
  3. Llamar a `model.predict(X_scaled)` para obtener `1` (íntegro) o `0` (anómalo).  
- **Ejemplo de carga en código Python:**
  ```python
  import joblib
  model = joblib.load("models/rf_final_model.pkl")
  y_pred = model.predict(X_scaled)  # X_scaled: array con 7 columnas normalizadas

## 2. `scaler.pkl`

- **Tipo de archivo:**  
  - Serialización de un objeto StandardScaler de scikit-learn via joblib.
- **Descripción:**  
  - Ajustado sobre los datos de entrenamiento originales (train_data.csv) en Google Colab.
  - Normaliza las 7 características de entrada (Latitude, Longitude, Altitude, Speed, Direction, hour, minute) antes de pasar al modelo RF.
  - Estadísticas (media y desviación estándar) basadas en la distribución de las 7 columnas en el conjunto de entrenamiento limpio.
- **Uso en inferencia (Raspberry Pi):**
  - Cargarlo con joblib.load("scaler.pkl").
  - Para cada nuevo vector de features X_raw (shape (1, 7)), llamar a X_scaled = scaler.transform(X_raw).
  - Pasar X_scaled a model.predict(...).
 
- **Ejemplo de carga en código Python:**
  ```python
  import joblib
  scaler = joblib.load("models/scaler.pkl")
  X_scaled = scaler.transform(X_raw)  # X_raw: array 2D (1, 7)

- **Notas Adicionales**
  Integridad de archivos:
  - Ambos .pkl se generaron en Google Colab utilizando joblib.dump(...) en la celda final del notebook 01_training_pipeline.ipynb.
  - Verificar que la versión de scikit-learn en Raspberry Pi coincide (o sea compatible) con la usada en Colab (preferiblemente scikit-learn 1.2.x).

