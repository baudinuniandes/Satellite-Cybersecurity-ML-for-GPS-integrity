# Satellite Cybersecurity: Machine Learning to preserve GPS integrity signals of Colombian Air Space Force aircraft 🚀🔐
# Ciberseguridad Satelital: Machine Learning para preservar integridad de señales GPS en aeronaves de la FAC 🚀🔐

Bienvenido al repositorio “**Ciberseguridad Satelital para sistemas de posicionamiento global GPS**”, un proyecto que combina principios de ciberseguridad, la potencia de la Inteligencia Artificial, dominio espacial y operaciones aéreas para garantizar que las aeronaves de la Fuerza Aeroespacial Colombiana (FAC) reciban señales GPS **íntegras** y libres de interferencias maliciosas. En un mundo donde actores adversarios crean simuladores hiperpoderosos para falsificar datos satelitales, nuestra misión es diseñar, entrenar y desplegar un modelo de Machine Learning que detecten posibles ataques de spoofing y jamming en tiempo real. 

## Resumen 🌎 
El estudio aborda temas de ciberseguridad satelital en el uso del GPS por parte de la Fuerza Aeroespacial Colombiana, enfocándose en el segmento de usuario del sistema satelital, mediante la aplicación de metodologías observacional y experimental para identificar vulnerabilidades, amenazas y ataques posibles, donde se destaca el spoofing como ataque crítico a la integridad de los datos GPS. Como respuesta, se diseñó un modelo de aprendizaje automático basado en Random Forest, entrenado con datos reales y simulados, que permite detectar señales anómalas en tiempo real a bordo de aeronaves, el modelo fue implementado en una Raspberry Pi, validado en simulaciones y pruebas de campo, con la finalidad de mejorar la resiliencia y seguridad operacional frente a ciberataques al sistema satelital.

## Palabras clave 🔗
Ciberseguridad satelital, GPS, Machine Learning, Navigation Warfare, Spoofing, SPARTA

## Abstract 🌎   
The target of this study is satellite cybersecurity in the GPS uses by the Colombian Aerospace Force, focusing on the user segment of the satellite system. It applies observational and experimental methodologies to identify vulnerabilities, threats, and potential attacks, highlighting spoofing as a critical threat to the integrity of GPS data. As a response, a machine learning model based on Random Forest was designed, trained with real and simulated data, enabling real-time detection of anomalous signals aboard aircraft. The model was implemented on a Raspberry Pi, validated through simulations and field tests, with the aim of enhancing resilience and operational safety against cyberattacks targeting the satellite system.

## Keywords 🔗
Satellite Cybersecurity, GPS, Machine Learning, Navigation Warfare, Spoofing, SPARTA.

## 🌌 ¿Por qué es importante la Ciberseguridad Satelital?

- **Dependencia crítica de GNSS:** Los sistemas de navegación GPS son vitales para la aviación militar y civil. Un ataque no detectado podría desviar aeronaves hacia áreas peligrosas o interrumpir operaciones esenciales.  
- **Amenazas avanzadas:** Hoy en día existen equipos capaces de replicar señales GPS con precisión casi perfecta. Sin defensas robustas, nuestras plataformas quedarían vulnerables a falsificaciones y bloqueos deliberados.  
- **Protección de vidas y misiones:** Un GPS confiable no solo guía aviones, sino que respalda misiones de búsqueda y rescate, vigilancia y transporte de carga crítica. Asegurar la integridad de la señal satelital es salvaguardar vidas y operaciones estratégicas.

## 📁 ¿Qué encontrarás en este repositorio?

```text
├── data/                            
│   ├── train_data.csv               # 7 500 muestras reales + etiquetas sintéticas de spoofing
│   ├── val_data.csv                 # Datos de validación (vuelo marzo 2025) + etiquetas
│   └── test_data.csv                # Datos de prueba independientes + etiquetas
│
├── notebooks/
│   ├── training_pipeline.ipynb      # Notebook de Google Colab: limpieza, generación de anomalías, GridSearch, métricas
│   └── model_selection_and_evaluation.ipynb  # Análisis detallado de métricas, curvas ROC y selección final de RF
│
├── models/
│   ├── rf_final_model.pkl           # Modelo RandomForest entrenado con train+val
│   └── scaler.pkl                   # StandardScaler para normalización de features
│
├── scripts/
│   ├── train_continuity_model.py    # Script de entrenamiento de RF (continuidad GPS) en PC
│   ├── realtime_gps_status.py       # Script de Raspberry Pi: clasificación en tiempo real + control LED
│   └── generate_spoofing.py         # Herramienta auxiliar para inyectar datos spoofing sintético en CSV
│
└── README.md                        # Esta introducción creativa y descripción del proyecto
