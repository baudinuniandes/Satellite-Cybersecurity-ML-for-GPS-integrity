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

## 🔥  Amenazas comunes a los Sistemas Satelitales

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Esquema Gráfico de Seguridad Espacial</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f0f4f8; /* Light blue-gray background */
            color: #334155; /* Darker text for readability */
        }
        .segment-card {
            background-color: #ffffff;
            border-radius: 1rem; /* Rounded corners */
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* Soft shadow */
            padding: 1.5rem;
            margin: 1rem;
            border: 1px solid #e2e8f0; /* Light border */
        }
        .threat-item {
            display: flex;
            align-items: flex-start;
            margin-bottom: 0.5rem;
        }
        .threat-icon {
            margin-right: 0.75rem;
            color: #ef4444; /* Red for threats */
            font-size: 1.25rem;
        }
        .component-icon {
            margin-right: 0.75rem;
            color: #3b82f6; /* Blue for components */
            font-size: 1.25rem;
        }
        .transversal-threats {
            background-color: #fef3c7; /* Light yellow background */
            border: 2px dashed #f59e0b; /* Orange dashed border */
            border-radius: 1rem;
            padding: 1.5rem;
            margin: 2rem 1rem; /* More margin to stand out */
            text-align: center;
            position: relative; /* For arrow positioning */
        }
        .transversal-threats::before,
        .transversal-threats::after {
            content: '';
            position: absolute;
            width: 0;
            height: 0;
            border-style: solid;
        }
        /* Arrows for transversal threats */
        .arrow-up-left {
            position: absolute;
            top: -1.5rem;
            left: 10%;
            font-size: 2rem;
            color: #f59e0b;
        }
        .arrow-up-right {
            position: absolute;
            top: -1.5rem;
            right: 10%;
            font-size: 2rem;
            color: #f59e0b;
        }
        .arrow-down-left {
            position: absolute;
            bottom: -1.5rem;
            left: 10%;
            font-size: 2rem;
            color: #f59e0b;
        }
        .arrow-down-right {
            position: absolute;
            bottom: -1.5rem;
            right: 10%;
            font-size: 2rem;
            color: #f59e0b;
        }
        .level-indicator {
            display: inline-block;
            width: 1rem;
            height: 1rem;
            border-radius: 50%;
            margin-left: 0.5rem;
        }
        .level-high { background-color: #ef4444; } /* Red */
        .level-medium { background-color: #f59e0b; } /* Orange */
        .level-low { background-color: #22c55e; } /* Green */
    </style>
</head>
<body class="p-4 md:p-8">

    <div class="max-w-6xl mx-auto">
        <h1 class="text-4xl font-extrabold text-center mb-10 text-gray-800">Esquema Gráfico de Seguridad Espacial</h1>

        <div class="segment-card">
            <h2 class="text-2xl font-bold mb-4 text-indigo-700"><i class="fas fa-satellite-dish component-icon"></i> Segmento Espacial</h2>
            <p class="text-lg mb-4 text-gray-700">Satélites y componentes internos:</p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                    <h3 class="text-xl font-semibold mb-2 text-gray-800">Sistema de Bus:</h3>
                    <ul class="list-none pl-0">
                        <li class="flex items-center mb-2"><i class="fas fa-compass component-icon"></i> Control de actitud</li>
                        <li class="flex items-center mb-2"><i class="fas fa-broadcast-tower component-icon"></i> Comunicación</li>
                        <li class="flex items-center mb-2"><i class="fas fa-solar-panel component-icon"></i> Energía</li>
                        <li class="flex items-center mb-2"><i class="fas fa-rocket component-icon"></i> Propulsión</li>
                        <li class="flex items-center mb-2"><i class="fas fa-thermometer-half component-icon"></i> Control térmico</li>
                    </ul>
                </div>

                <div>
                    <h3 class="text-xl font-semibold mb-2 text-gray-800">Carga Útil (Payload):</h3>
                    <ul class="list-none pl-0">
                        <li class="flex items-center mb-2"><i class="fas fa-map-marked-alt component-icon"></i> Navegación</li>
                        <li class="flex items-center mb-2"><i class="fas fa-wifi component-icon"></i> Comunicaciones</li>
                        <li class="flex items-center mb-2"><i class="fas fa-flask component-icon"></i> Aplicaciones científicas</li>
                    </ul>
                </div>
            </div>

            <div class="mt-6">
                <h3 class="text-xl font-semibold mb-2 text-gray-800">Amenazas:</h3>
                <ul class="list-none pl-0">
                    <li class="threat-item"><i class="fas fa-bug threat-icon"></i> Vulnerabilidades de software (firmware/kernel/BIOS) <span class="level-indicator level-high"></span></li>
                    <li class="threat-item"><i class="fas fa-user-slash threat-icon"></i> Errores humanos <span class="level-indicator level-medium"></span></li>
                    <li class="threat-item"><i class="fas fa-user-secret threat-icon"></i> Acceso no autorizado desde tierra <span class="level-indicator level-high"></span></li>
                    <li class="threat-item"><i class="fas fa-ban threat-icon"></i> Comunicaciones no autorizadas (exfiltración) <span class="level-indicator level-high"></span></li>
                    <li class="threat-item"><i class="fas fa-hand-fist threat-icon"></i> Interdicción física antes del lanzamiento <span class="level-indicator level-high"></span></li>
                    <li class="threat-item"><i class="fas fa-unlink threat-icon"></i> Pérdida de control del satélite <span class="level-indicator level-high"></span></li>
                    <li class="threat-item"><i class="fas fa-lock-open threat-icon"></i> Compromiso criptográfico de datos <span class="level-indicator level-high"></span></li>
                </ul>
            </div>
            <div class="flex items-center">
                <span class="level-indicator level-high"></span> Alto Impacto
            </div>
            <div class="flex items-center">
                <span class="level-indicator level-medium"></span> Medio Impacto
            </div>
        </div>

        <div class="segment-card">
            <h2 class="text-2xl font-bold mb-4 text-indigo-700"><i class="fas fa-link component-icon"></i> Transmisión de datos</h2>
            <p class="text-lg mb-4 text-gray-700">Enlaces y comunicaciones:</p>
            <ul class="list-none pl-0 mb-6">
                <li class="flex items-center mb-2"><i class="fas fa-exchange-alt component-icon"></i> Space-space</li>
                <li class="flex items-center mb-2"><i class="fas fa-arrow-down component-icon"></i> Space-ground</li>
                <li class="flex items-center mb-2"><i class="fas fa-arrow-right component-icon"></i> Ground-user</li>
                <li class="flex items-center mb-2"><i class="fas fa-user-astronaut component-icon"></i> Space-user</li>
            </ul>

            <div>
                <h3 class="text-xl font-semibold mb-2 text-gray-800">Amenazas:</h3>
                <ul class="list-none pl-0">
                    <li class="threat-item"><i class="fas fa-wave-square threat-icon"></i> Interferencia (Jamming) <span class="level-indicator level-high"></span></li>
                    <li class="threat-item"><i class="fas fa-mask threat-icon"></i> Suplantación (Spoofing) <span class="level-indicator level-high"></span></li>
                    <li class="threat-item"><i class="fas fa-database threat-icon"></i> Robo e intercepción de datos <span class="level-indicator level-high"></span></li>
                    <li class="threat-item"><i class="fas fa-server threat-icon"></i> Denegación de Servicio (DoS) <span class="level-indicator level-high"></span></li>
                    <li class="threat-item"><i class="fas fa-clone duplication-icon"></i>  Interceptación y Repetición (Meaconing) <span class="level-indicator level-medium"></span></li>
                </ul>
            </div>
            <div class="flex items-center">
                <span class="level-indicator level-high"></span> Alto Impacto
            </div>
            <div class="flex items-center">
                <span class="level-indicator level-medium"></span> Medio Impacto
            </div>
        </div>

        <div class="transversal-threats">
            <i class="fas fa-arrow-up-left arrow-up-left"></i>
            <i class="fas fa-arrow-up-right arrow-up-right"></i>
            <i class="fas fa-arrow-down-left arrow-down-left"></i>
            <i class="fas fa-arrow-down-right arrow-down-right"></i>
            <h2 class="text-2xl font-bold mb-4 text-orange-700"><i class="fas fa-arrows-alt component-icon"></i> Amenazas Transversales y Contextuales</h2>
            <p class="text-lg mb-4 text-gray-700">Estas amenazas cruzan y afectan múltiples segmentos:</p>
            <ul class="list-none pl-0 text-left mx-auto max-w-md">
                <li class="threat-item"><i class="fas fa-exclamation-triangle threat-icon"></i> Riesgos Técnicos y Operacionales <span class="level-indicator level-high"></span></li>
                <li class="threat-item"><i class="fas fa-eye-slash threat-icon"></i> Gestión de Seguridad de Operaciones (OPSEC) <span class="level-indicator level-medium"></span></li>
                <li class="threat-item"><i class="fas fa-truck-loading threat-icon"></i> Riesgos en la Cadena de Suministro <span class="level-indicator level-high"></span></li>
                <li class="threat-item"><i class="fas fa-wave-square threat-icon"></i> Interferencia (Jamming) <span class="level-indicator level-high"></span></li>
                <li class="threat-item"><i class="fas fa-mask threat-icon"></i> Suplantación (Spoofing) <span class="level-indicator level-high"></span></li>
                <li class="threat-item"><i class="fas fa-clone duplication-icon"></i> Interceptación y Repetición (Meaconing) <span class="level-indicator level-high"></span></li>
                <li class="threat-item"><i class="fas fa-handshake-slash threat-icon"></i> Dependencia de proveedores externos (pérdida de soberanía) <span class="level-indicator level-medium"></span></li>
                <li class="threat-item"><i class="fas fa-fighter-jet threat-icon"></i> Militarización del Espacio <span class="level-indicator level-high"></span></li>
                <li class="threat-item"><i class="fas fa-info-circle threat-icon"></i> Falta estructural de información estratégica espacial <span class="level-indicator level-medium"></span></li>
            </ul>
            <div class="flex items-center">
                <span class="level-indicator level-high"></span> Alto Impacto
            </div>
            <div class="flex items-center">
                <span class="level-indicator level-medium"></span> Medio Impacto
            </div>
        </div>

        <div class="segment-card">
            <h2 class="text-2xl font-bold mb-4 text-indigo-700"><i class="fas fa-user component-icon"></i> Segmento de Usuario</h2>
            <p class="text-lg mb-4 text-gray-700">Dispositivos y terminales:</p>
            <ul class="list-none pl-0 mb-6">
                <li class="flex items-center mb-2"><i class="fas fa-mobile-alt component-icon"></i> Equipos personales (smartphones, tablets, smartwaches, receptores GPS comerciales)</li>
                <li class="flex items-center mb-2"><i class="fas fa-satellite-dish component-icon"></i> Equipos de navegación usados en aeronaves</li>
            </ul>

            <div>
                <h3 class="text-xl font-semibold mb-2 text-gray-800">Amenazas:</h3>
                <ul class="list-none pl-0">
                    <li class="threat-item"><i class="fas fa-skull-crossbones threat-icon"></i> Compromiso o degradación de dispositivos <span class="level-indicator level-high"></span></li>
                    <li class="threat-item"><i class="fas fa-mobile-alt threat-icon"></i> Vulnerabilidades en dispositivos personales <span class="level-indicator level-medium"></span></li>
                    <li class="threat-item"><i class="fas fa-eye-slash threat-icon"></i> Riesgos para seguridad operacional (Jamming, Spoofing, Meaconing) <span class="level-indicator level-medium"></span></li>
                    <li class="threat-item"><i class="fas fa-house-damage threat-icon"></i> Ataques desde infraestructura de usuario <span class="level-indicator level-high"></span></li>
                </ul>
            </div>
            <div class="flex items-center">
                <span class="level-indicator level-high"></span> Alto Impacto
            </div>
            <div class="flex items-center">
                <span class="level-indicator level-medium"></span> Medio Impacto
            </div>
        </div>

        <div class="segment-card">
            <h2 class="text-2xl font-bold mb-4 text-indigo-700"><i class="fas fa-building component-icon"></i> Segmento de Control</h2>
            <p class="text-lg mb-4 text-gray-700">Infraestructura terrestre:</p>
            <ul class="list-none pl-0 mb-6">
                <li class="flex items-center mb-2"><i class="fas fa-server component-icon"></i> Centro de Procesamiento de Datos</li>
                <li class="flex items-center mb-2"><i class="fas fa-cogs component-icon"></i> Terminales remotos y estaciones de control</li>
            </ul>

            <div>
                <h3 class="text-xl font-semibold mb-2 text-gray-800">Amenazas:</h3>
                <ul class="list-none pl-0">
                    <li class="threat-item"><i class="fas fa-door-closed threat-icon"></i> Compromiso físico (Destrucción física, Acceso y distribución de Malware)<span class="level-indicator level-high"></span></li>
                    <li class="threat-item"><i class="fas fa-industry threat-icon"></i> Sistemas industriales y dispositivos IoT comprometidos <span class="level-indicator level-high"></span></li>
                    <li class="threat-item"><i class="fas fa-wrench threat-icon"></i> Dificultades en actualización y mantenimiento <span class="level-indicator level-medium"></span></li>
                    <li class="threat-item"><i class="fas fa-clipboard-list threat-icon"></i> Protección insuficiente de registros (logs) y auditoría <span class="level-indicator level-medium"></span></li>
                </ul>
            </div>
            <div class="flex items-center">
                <span class="level-indicator level-high"></span> Alto Impacto
            </div>
            <div class="flex items-center">
                <span class="level-indicator level-medium"></span> Medio Impacto
            </div>
        </div>

        <div class="mt-10 text-center text-gray-600">
            <p class="text-lg">Indicadores gráficos:</p>
            <div class="flex justify-center items-center mt-4 space-x-4">
                <div class="flex items-center">
                    <i class="fas fa-lock text-green-500 text-2xl mr-2"></i> Seguridad
                </div>
                <div class="flex items-center">
                    <i class="fas fa-lock-open text-red-500 text-2xl mr-2"></i> Vulnerabilidad
                </div>
                <div class="flex items-center">
                    <span class="level-indicator level-high"></span> Alto Impacto
                </div>
                <div class="flex items-center">
                    <span class="level-indicator level-medium"></span> Medio Impacto
                </div>
                <div class="flex items-center">
                    <span class="level-indicator level-low"></span> Bajo Impacto
                </div>
            </div>
        </div>

    </div>

</body>
</html>
```

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
