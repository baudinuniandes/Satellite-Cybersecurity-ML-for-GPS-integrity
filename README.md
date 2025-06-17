# Ciberseguridad Satelital: Machine Learning para preservar integridad de señales GPS en aeronaves de la FAC 🚀🔐

Bienvenido al repositorio “**Ciberseguridad Satelital Machine Learning para integridad de sistemas de posicionamiento global (GPS)**”, este repositorio es parte del trabajo de investigación realizado en la Maestria de Ciberseguridad y Ciberdefensa, para la obtención del titulo de Magister, este proyecto que combina principios de ciberseguridad, la potencia de la Inteligencia Artificial, dominio espacial y operaciones aéreas para garantizar que las aeronaves de la Fuerza Aeroespacial Colombiana (FAC) reciban señales GPS **íntegras** y libres de interferencias maliciosas. Se tendra el marco conceptual en el articulo titulado **"Ciberseguridad Satelital: Machine Learning para preservar integridad de señales GPS en aeronaves de la FAC"** y aca podra encontrar el diseño y la implementación del diseño de machine learning propuesto. 

## Resumen 🌎 
El estudio aborda temas de ciberseguridad satelital en el uso del GPS por parte de la Fuerza Aeroespacial Colombiana, enfocándose en el segmento de usuario del sistema satelital, mediante la aplicación de metodologías observacional y experimental para identificar vulnerabilidades, amenazas y ataques posibles, donde se destaca el spoofing como ataque crítico a la integridad de los datos GPS. Como respuesta, se diseñó un modelo de aprendizaje automático basado en Random Forest, entrenado con datos reales y simulados, que permite detectar señales anómalas en tiempo real a bordo de aeronaves, el modelo fue implementado en una Raspberry Pi, validado en simulaciones y pruebas de campo, con la finalidad de mejorar la resiliencia y seguridad operacional frente a ciberataques al sistema satelital.

## Palabras clave 🔗
Ciberseguridad satelital, GPS, Machine Learning, Navigation Warfare, Spoofing, SPARTA

## Abstract 🌎   
The target of this study is satellite cybersecurity in the GPS uses by the Colombian Aerospace Force, focusing on the user segment of the satellite system. It applies observational and experimental methodologies to identify vulnerabilities, threats, and potential attacks, highlighting spoofing as a critical threat to the integrity of GPS data. As a response, a machine learning model based on Random Forest was designed, trained with real and simulated data, enabling real-time detection of anomalous signals aboard aircraft. The model was implemented on a Raspberry Pi, validated through simulations and field tests, with the aim of enhancing resilience and operational safety against cyberattacks targeting the satellite system.

## Keywords 🔗
Satellite Cybersecurity, GPS, Machine Learning, Navigation Warfare, Spoofing, SPARTA.

## 🌌 ¿Por qué es importante la Ciberseguridad Satelital?

- **Amenazas avanzadas:** Hoy en día existen equipos capaces de replicar señales GPS con precisión casi perfecta. Sin defensas robustas, nuestras plataformas quedarían vulnerables a falsificaciones y bloqueos deliberados.  
- **Protección de vidas y misiones:** Un GPS confiable no solo es necesario para la navegación, sino que respalda misiones de búsqueda y rescate, vigilancia y transporte de carga crítica. Asegurar la integridad de la señal satelital es salvaguardar vidas y operaciones estratégicas.
- **Dependencia crítica de GNSS:** Los sistemas de navegación GPS son vitales para la aviación militar y civil. Un ataque no detectado podría desviar aeronaves hacia áreas peligrosas o interrumpir operaciones esenciales.
- **Vulnerabilidad del segmento de usuario:** El segmento de usuario del sistema satelital GPS carece de control directo sobre los satélites o estaciones terrestres, lo que lo hace inherentemente vulnerable a amenazas y ataques.
- **Riesgos operacionales del spoofing:** Un ataque de spoofing exitoso conlleva riesgos severos, como el desvío de aeronaves, colisiones marítimas o terrestres, y la afectación a infraestructuras críticas dependientes de la sincronización GNSS.

## 🕵️  Elementos importantes de la investigación
- **Frameworks para la gestión de riesgos:** Marcos de referencia como SPARTA facilitan el modelado de técnicas y tácticas de ciberataques espaciales y la aplicación de contramedidas de protección.
- **Estrategias de mitigación específicas:** La fortificación del segmento de usuario requiere medidas como autenticación robusta, cifrado ligero, infraestructura de llave pública y monitoreo en tiempo real.
- **Machine Learning para Detección de Anomalías:** La aplicación de algoritmos de aprendizaje automático, como Random Forest, permite clasificar señales GPS anómalas (spoofing) para verificar su integridad en tiempo real a bordo de aeronaves.
- **Modelo Random Forest:** Un modelo basado en Random Forest, entrenado con datos de vuelos reales y simulados de spoofing, demostró una precisión del 98.72% en la detección de señales anómalas.
- **Implementación práctica en borde:** El modelo de ML fue implementado y validado en una Raspberry Pi, demostrando su viabilidad técnica para procesar y verificar la integridad de señales GPS en un entorno de procesamiento en borde.
- **Contribución a la Seguridad Operacional:** La implementación del modelo ML en el segmento de usuario mejora la resiliencia y la seguridad operacional al permitir la detección activa de ataques como el spoofing, evitando la toma de decisiones erróneas por parte de la tripulación.

## 📁 ¿Qué encontrarás en este repositorio?

```text
├── data/                            
│   ├── test_data.csv                      # 3032 muestras reales + etiquetas sintéticas de spoofing
│   ├── train_data.csv                     # 7245 muestras reales + etiquetas sintéticas de spoofing
│   └── val_data.csv                       # 1272 muestras reales + etiquetas sintéticas de spoofing
│
├── notebooks/
│   ├── rf_model_design.ipynb                # Notebook de Google Colab: limpieza, generación de anomalías, GridSearch, métricas
│   └── model_selection_and_evaluation.ipynb # Análisis detallado de métricas, curvas ROC y selección final de RF
│
├── models/
│   ├── rf_final_model.pkl           # Modelo RandomForest entrenado con train+val
│   └── scaler.pkl                   # StandardScaler para normalización de features
│
├── scripts/
│   ├── realtime_gps_status.py       # Script de Raspberry Pi: clasificación en tiempo real + control LED
│   └── generate_spoofing.py         # Herramienta auxiliar para inyectar datos spoofing sintético en CSV
│
└── README.md                        # Esta introducción creativa y descripción del proyecto
