**<p align="center">Proyecto de Data-BI de No Country . s17-18-m-data-bi</p>**

<img src="Imagenes\SP500.jpg" width="1010" height="400">

#  **<p align="center">INVERSIÓN EN EL SPY</p>** 
##  **<p align="center">COMO ALTERNATIVA PARA UN FONDO DE RETIRO</p>**

## Introducción
Las pensiones públicas suelen ser bajas e insuficientes para cubrir todos los gastos de necesidades básicas, como vivienda, alimentación y atención médica. La falta de fondos también puede limitar la capacidad de disfrutar de actividades recreativas y de mantener un estilo de vida activo y saludable.

El **objetivo de este proyecto** es desarrollar una herramienta de análisis de inversiones basados en el SPY, para personas de 25 a 50 años que buscan alternativas a su jubilación, plazo fijo o caja de ahorro. Con un perido de invesión a largo plazo a partir de 15 a 20 años.

## Descripción del proyecto
Nuestro proyecto se basa en el análisis del fondo **SPDR S&P 500 ETF Trust** creado en 1993, ofrece resultados según el índice S&P 500, que incluye empresas de gran capitalización de los 11 sectores (Consumo Discrecional, Consumo Básico, Energía, Financiero, Salud, Industria, Tecnología de la Información, Materiales, Inmobiliario, Servicios de Comunicación y Servicios Públicos). Su divisa base es el dólar y lo gestiona SSGA Funds Management, Inc. Las acciones del fondo se cotizan en la **Bolsa de Valores de Nueva York** bajo el **símbolo bursátil SPY**.

Este índice es ampliamente considerado como un indicador clave de la salud económica y del mercado de valores estadounidense.


Se realizó como **Producto Minimo Viable** un análisis historico del SPY desde el año 1995 al 2023, Bot de recomendación de inveresión y un modelo de machine learning del rendimiento a futuro.

**Análisis historico del Indice SPY**
- Rendimiento del SPY desde el año 1995 al 2023.
<img src="Imagenes\spy95_23.jpg" width="1010" height="400">

**Bot de recomendacion de compra y venta del SYP**
- Es un aplicativo desarrollado con Python y desplegado en Streamlit que brinda recomendaciones de compra/venta del ETF tanto del índice SP500 como de las 7 compañías que tienen mayor peso en la ponderación de dicho índice, la información de los activos se obtiene del portal [`Yahoo Finance`](https://finance.yahoo.com/)
- [Bot trading](https://robot-trading.streamlit.app/)
 
**Modelo de Machine learning**
- Un modelo de redes neuronales es crucial para predecir el precio del S&P 500 en los próximos 15 años, ya que permite captar patrones no lineales complejos en los datos históricos y proyectar tendencias futuras. Su capacidad de adaptación y aprendizaje continuo lo convierte en una herramienta poderosa para la toma de decisiones financieras a largo plazo.

## Colaboradores

**Grupo s17-18-m-data-bi:**
  - **Gloria Nabor:**  Project Manager [`Linkedin`](https://www.linkedin.com/in/gloria-nabor/), [`Github`](http://github.com/Gloria-Nabor)
  - **Angel Troncoso:** Data analyst [`Linkedin`](www.linkedin.com/in/angeltroncoso), [`Github`](https://github.com/AngelTroncoso)
  - **Juan Campos Quintana:** Data analyst [`Linkedin`](https://www.linkedin.com/in/jumacaq/), [`Github`](http://github.com/jumacaq)
  - **Cecilia Aponte:** Data science [`Linkedin`](https://www.linkedin.com/in/ceci-aponte-data/), [`Github`](https://github.com/CCAponte)
  - **Raul Almao:** Data science [`Linkedin`](https://www.linkedin.com/in/ralmao/),[`Github`](https://github.com/Ralmao)
  - **Arelys Acevedo:**  Data analyst [`Linkedin`](https://www.linkedin.com/in/arelys-acevedo/), [`Github`](http://github.com/acad2018)
  - **Fabio Maculus:** Data Analyst [`Linkedin`](https://www.linkedin.com/in/fabio-maculus-data-analyst/),[`Github`](https://github.com/Macu-Data)
  - **Hernán Pizarro:** Business Intelligence [`Linkedin`](https://www.linkedin.com/in/hern%C3%A1n-pizarro-683679268/), [`Github`](http://github.com/Hern4nOckham) 

**No Country:**
 - **Alan Rojas:** Team Leader [`Linkedin`](https://www.linkedin.com/in/alan-rojas-polanco-97a4b5291/)


## Tecnologías
- **Python:** Lenguaje de programación utilizado para análisis de datos y desarrollo de aplicaciones.
- **Power BI:** Visualización de Datos. [![Power BI](https://img.shields.io/badge/Power_BI-F2C811?logo=power-bi&logoColor=white)](https://app.powerbi.com/view?r=eyJrIjoiYTIwYTRiYTEtNTgyMi00ZGVhLThlMzEtYmI4NDk5MzQ1ZDI1IiwidCI6IjEwYWE5MTJkLTJjNzYtNGI5YS1iZmI2LWJkNGQ0Nzk5MTUwNiIsImMiOjR9&pageName=9a9665ed52580701a34c)
- **Streamlit:**  Plataforma para la creación de aplicaciones web interactivas a partir de scripts de Python. [Streamlit](https://robot-trading.streamlit.app/)
- **Trello:** Herramienta de Gestión de Proyectos: [Trello](https://trello.com/invite/b/66cd3c02fac81073b6752532/ATTI1258aad3b3bb787408fc3314244223832BFE00CD/s17-18-m-data-bi)
- **GitHub y Colab:** Desarrollo Colaborativo y Control de Versiones. 
- **Slack:** Comunicación diaria del equipo y colaboración en tiempo real.
- **Google Meet:** Reuniones diarias, planificación de sprint y coordinación de trabajo.
- **WhatsApp:** Comunicación instantánea para cuestiones urgentes.
- **Google Drive:** Almacenamiento y sincronización de documentación.


## Enlaces del Proyecto
- Dashboard: [`Power BI`](https://app.powerbi.com/view?r=eyJrIjoiYTIwYTRiYTEtNTgyMi00ZGVhLThlMzEtYmI4NDk5MzQ1ZDI1IiwidCI6IjEwYWE5MTJkLTJjNzYtNGI5YS1iZmI2LWJkNGQ0Nzk5MTUwNiIsImMiOjR9&pageName=9a9665ed52580701a34c)
- Datasets: [`SPY 500, VIX y las 503 empresas`](https://finance.yahoo.com/)
- Requisitos del proyecto: [`No Country`](https://drive.google.com/drive/folders/1kH9YZNrl84T8EldJYO_1q81jJXVeh6aq)

##  Disclaimer

La información y los datos presentados en este **documento tienen fines informativos y educativos** únicamente. No constituyen una recomendación de inversión, asesoría financiera, o sugerencia para la compra o venta de cualquier activo financiero. 

Antes de tomar cualquier decisión de inversión, se recomienda **consultar con un asesor financiero profesional** que tenga en cuenta su situación financiera particular, objetivos de inversión y tolerancia al riesgo. Cualquier acción que realice basándose en la información contenida en este documento es bajo su propia responsabilidad.
