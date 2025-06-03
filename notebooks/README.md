# Carpeta `notebooks/`

Este directorio contiene los cuadernos de Jupyter (Google Colab) donde se desarrollan, entrenan y evalúan los modelos de Machine Learning para detección de integridad GPS. Cada notebook está documentado con referencias a las fuentes académicas utilizadas y sigue la metodología de limpieza, generación de anomalías, afinación de hiperparámetros y evaluación.

notebooks/
├── 01_training_pipeline.ipynb

└── 02_model_selection_and_evaluation.ipynb

---

## 1. `01_training_pipeline.ipynb`

- **Propósito:**  
  Implementar todo el flujo de entrenamiento paso a paso en Google Colab:
  1. Limpieza de datos (Aceves-Fernandez, 2023, p.86)  
  2. Transformación y extracción de features de navegación (Barua et al., 2024, pp.120–123)  
  3. Generación de etiquetas sintéticas de spoofing/jamming (Sarang, 2023, p.43)  
  4. División en conjuntos de entrenamiento, validación y prueba (Amr, 2020, p.54)  
  5. Normalización con `StandardScaler`  
  6. Búsqueda de hiperparámetros para RandomForest con `GridSearchCV`  
  7. Cálculo de métricas básicas (accuracy, precision, recall, f1, AUC, confusion matrix)

- **Secciones Principales:**  
  1. **Instalación de Dependencias:**  
     - `pip install pandas numpy scikit-learn joblib xgboost lightgbm`  
  2. **Carga de Datos (`train_data.csv`, `val_data.csv`, `test_data.csv`):**  
     - Lectura con `pd.read_csv(…, parse_dates=["UTC"])`  
     - Verificación de forma y primeras filas  
  3. **Limpieza de Datos:**  
     - Eliminación de duplicados y valores nulos en columnas críticas (`Latitude`, `Longitude`, `Altitude`, `Speed`, `Direction`)  
  4. **Ingeniería de Features:**  
     - Extracción de componentes `hour` y `minute` desde `UTC`  
     - Construcción del DataFrame con columnas:  
       `["Latitude", "Longitude", "Altitude", "Speed", "Direction", "hour", "minute"]`  
  5. **Generación de Etiquetas Sintéticas:**  
     - Si el CSV no contiene `Label`, inyecta anomalías en el 20 % de las filas:  
       - Desplazamiento gaussiano en latitud/longitud (spoofing)  
       - Outliers en altitud y velocidad (jamming)  
     - Referencia: Sarang (2023, p.43)  
  6. **Normalización de Features:**  
     - Ajuste de `StandardScaler` sobre `X_train`  
     - Transformación de `X_val` y `X_test`  
  7. **GridSearchCV para RandomForest:**  
     - Parámetros a explorar:  
       - `n_estimators`: [200, 500, 1000]  
       - `max_depth`: [None, 10, 20, 30]  
       - `max_features`: ['sqrt', 'log2']  
       - `min_samples_split`: [2, 5, 10]  
     - Configuración: `cv=3`, `scoring="roc_auc"`, `n_jobs=-1`  
     - Referencia: Sarang (2023, p.48) y Amr (2020, pp.95–97)  
  8. **Resultados de GridSearchCV:**  
     - Mejores hiperparámetros (`best_params_`) y métrica ROC AUC (`best_score_`)  
  9. **Evaluación en Validación:**  
     - Cálculo de métricas (accuracy, precision, recall, f1, AUC) sobre `X_val`  
     - Matriz de confusión y Curva ROC (RocCurveDisplay.from_predictions)  
  10. **Guardado de Modelo y Scaler:**  
      - `joblib.dump(final_model, "rf_final_model.pkl")`  
      - `joblib.dump(scaler, "scaler.pkl")`

---

## 2. `02_model_selection_and_evaluation.ipynb`

- **Propósito:**  
  Profundizar en la comparación de métricas y justificación de la elección del RandomForest final. Proporciona análisis gráfico y estadístico de distintos modelos (RF, XGB, LightGBM, MLP, SVM, IsolationForest).

- **Secciones Principales:**  
  1. **Carga de Results de Entrenamiento:**  
     - Importa resúmenes de métricas obtenidos en `01_training_pipeline.ipynb` para RF, XGB, LGBM, MLP, SVM e IsolationForest.  
  2. **Comparación de Métricas por Modelo:**  
     - Tabla comparativa de `accuracy`, `precision`, `recall`, `f1-score`, `AUC` para cada clasificador.  
     - Referencia: Amr (2020, p.95) sobre buenas prácticas en comparación de clasificadores.  
  3. **Visualización de Curvas ROC:**  
     - Muestra ROC curves lado a lado para todos los modelos usando `RocCurveDisplay`.  
     - Análisis de AUC para cada uno.  
  4. **Matriz de Confusión Extendida:**  
     - Matrices para cada modelo, con anotaciones de falsos positivos vs. falsos negativos.
  5. **Selección del Modelo Final:**  
     - Justificación basada en métricas, balance entre detección de anomalías (recall clase 0) y baja tasa de falsos positivos (precision clase 0).  
     - Observación de tiempos de inferencia (valor clave para Raspberry Pi).  
     - Decisión: **RandomForestClassifier** como modelo óptimo (mejor AUC, buen trade-off velocidad vs. precisión).  
  6. **Ejemplos de Inferencia Simulada:**  
     - Carga del modelo `rf_final_model.pkl` y `scaler.pkl`.  
     - Predicción sobre un pequeño subconjunto simulado de datos “en tiempo real”.  
     - Verificación de consistencia con valores esperados (params threshold, etc.).  
  7. **Conclusión y Próximos Pasos:**  
     - Plan de despliegue en Raspberry Pi (inferencia con tlfte/cpu).  
     - Posibles mejoras: quantization, pruning, ensambles mixtos.

---

## Notas Generales

- Ambos notebooks están listos para correr directamente en Google Colab y contienen **celdas de texto** y **celdas de código** que implementan los pasos descritos en la metodología.  
- La numeración de las celdas y los comentarios en cada bloque de código facilitan la trazabilidad entre lo que se hace en el notebook.  
- Asegúrate de subir los archivos CSV (`train_data.csv`, `val_data.csv`, `test_data.csv`) a Colab antes de ejecutar las celdas de carga de datos.  
- Los notebooks generan el modelo final (`rf_final_model.pkl`) y el scaler (`scaler.pkl`) en la raíz del entorno de Colab para que luego puedan ser descargados o usados directamente en Raspberry Pi.

