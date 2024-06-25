# TusDatos---PruebaTecnica

# Nombre del Proyecto
TuDatos Scraper

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Estructura](#Estructura)
- [Organización](#Organizacion)
- [Tecnologías](#Tecnologías)
- [Instalación](#Instalacion)
- [Contacto](#contacto)

## Descripción

Este proyecto es un scraper desarrollado como parte de una prueba técnica. Su objetivo es extraer datos estructurados de el sitio web especificado y almacenarlos en un JSON para su posterior análisis. El scraper está diseñado para ser simple y eficiente, demostrando habilidades básicas de web scraping y manipulación de datos.

## Características Clave

- Extracción de Datos Específicos: Recupera información relevante de la página web objetivo, como fechas, involucrados, id de cada proceso, descripciones de las acciones judiciarias, etc.
- Almacenamiento en JSON: Guarda los datos extraídos en un archivo JSON para facilitar su análisis y manipulación.
- Fácil de Usar: Implementación sencilla y directa que permite ejecutar el scraper con comandos mínimos, o incluso solo haciendo doble clcik en el archivo main.py.

## Estructura
TusDatos_PruebaTecnica/
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── logs/
│   │   ├── test/
│   │   │   └── test_scraper.log
│   │   └── production/
│   │       └── scraper.log
│   ├── test_data/
│   │   └── data.json
│   └── stored_data/
│       └── data.json
│
├── test/
│   ├── main.py
│   ├── scraper.py
│   └── server_response-test.py
│
├── utils/
│   ├── config_variables.py
│   ├── imports.py
│   └── selenium_functions.py
│
├── scripts/
│   ├── scraper.py
│   └── main.py
│
└── requirements.txt

## Descripción de Carpetas y Archivos
config/
  config.yaml: Archivo de configuración YAML que contiene variables de configuración para el proyecto.

data/
  logs/
  test/
    test_scraper.log: Archivo de registro para pruebas del scraper.
  production/
    scraper.log: Archivo de registro para el scraper en producción.
  test_data/
    data.json: Datos de prueba en formato JSON para pruebas del scraper.
  stored_data/
    data.json: Datos almacenados en formato JSON después de ser procesados por el scraper.

test/
  main.py: Archivo principal para pruebas generales del proyecto.
  scraper.py: Archivo de prueba específico para el scraper.
  server_response-test.py: Archivo de prueba para verificar respuestas del servidor.

utils/
  config_variables.py: Archivo que contiene variables globales de configuración utilizadas en el proyecto.
  imports.py: Archivo con las importaciones necesarias para los scripts del proyecto.
  selenium_functions.py: Archivo que contiene funciones relacionadas con Selenium para el proyecto.

scripts/
  scraper.py: Archivo principal del scraper que realiza la extracción de datos.
  main.py: Archivo principal para la ejecución principal del proyecto.
requirements.txt

Archivo que lista las dependencias de Python necesarias para el proyecto.

## Uso y Organización
Organización: La estructura está diseñada para separar claramente diferentes aspectos del proyecto, como configuración, datos, pruebas, utilidades y scripts principales.

Acceso a Datos: Los archivos de datos (data.json) se encuentran en carpetas específicas (test_data/ y stored_data/), mientras que los registros (*.log) están organizados dentro de la carpeta logs/ según el entorno de prueba y producción.

Pruebas y Utilidades: Los archivos en las carpetas test/ y utils/ proporcionan soporte para pruebas y funciones adicionales necesarias para el proyecto.


## Tecnologías
- Lenguaje: Python v3.10
- Librerías: BeautifulSoup, lxml, Selenium, yaml, webdriver-manager
  - estas librerias estan listas para ser instaladas, y se encuentran en el archivo requeriments.txt
  - Comando: pip install -r requeriments.txt
- Sistema: Any
- venv: opcional

## Instalación y Uso
1. Clona este repositorio:
git clone https://github.com/kevinHJ99/TusDatos---PruebaTecnica
cd scripts
2. ejecuta el script de scraping:
   python main.py
3. Los datos extraidos se almacenaran en un data.json en el siguiente directorio data/stored_data/data.json

## NOTA
NOTA: Se tomaron 10 registros (limite permitido) por cada paginacion, el scraper esta limitado a solo realizar 3 paginaciones, sin embargo esta restricion puede ser eliminada si al final del bucle while, dentro de la funcion find_results(), se cambia este fragmento de codigo:
  count+=1
        if count != 3: 
                sleep(1.5)
                af.do_clickByXpath(driver, '//button[@aria-label="Página siguiente"]')
        else: break

Y se deja de la siguiente manera:
    try:
       sleep(1.5)
       af.do_clickByXpath(driver, '//button[@aria-label="Página siguiente"]')
    except: break
    

## Contacto

Para preguntas o comentarios, puedes contactarme en:

Nombre: Kevin Hoyos
Email: kevinhj1099@gmail.com
GitHub: @kevinHJ99


