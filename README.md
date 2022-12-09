# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>
<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center>**`Data Engineering`**</h1>

## <h1 align=center>**`Mauro Emiliano Cadme`**</h1>

<hr>
<p align="center">
<img src="src\assets\programando.gif"  height=300>
</p>

#### <h1 align=center>**HOLA!**</h1> 

    Que gusto poder saludarte curioso del Data Science, como pudiste notarlo yo soy Mauro, un ser humano 
    en busca de comprender los datos.
    En este repositorio podrás encontrar mi primer proyecto de Data Engineering enfocado en el procesamientos
    de datos mediante ETL (Extraction, Transformation, Loading) y posteriormente la conexión de una API 
    (Application Programming Interface) con Docker.

# <h1 align=center> *`A continuación te presento la trabla de contenidos del repositorio...`* </h1>

    

<hr>

## **TABLA DE CONTENIDO**  
+ 1-Introducción  
+ 2-Objetivo   
+ 3-Tecnologías Utilizadas  
+ 4-Ejecución  
+ 5-Conclusiones 

<hr>

## Introducción  

    Los datos crecen exponencialmente y cada vez son más las empresas que buscan expertos que puedan ayudarles 
    a entender, analizar y utilizar el potencial de tal cantidad de información. El objetivo de la Data Engineering
    es construir y mantener las estructuras de datos y las arquitecturas tecnológicas necesarias para el 
    procesamiento, ingestión e implementación a gran escala de aplicaciones que usan datos de manera intensiva. 
      

<p align="center">
<img src="src\assets\data-engineering.webp"  height=300>
</p>
    
<hr>

## Objetivo 

* Realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que consideren
pertinentes.
* Disponibilizar los datos limpios para su consulta a través de una API construida en un entorno virtual dockerizado.

<hr>

## Tecnologías Utilizadas 

<p align="center">
<img src="src\assets\Python.svg.png"  height=100>
<img src="src\assets\mysql.png"  height=100>
<img src="src\assets\api.png"  height=100>
<img src="src\assets\docker.png"  height=100>
</p>

* Python
Es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código,
se utiliza para desarrollar aplicaciones de todo tipo.

    Se utilizaron las siguientes librerias:

    'anyio, charset-normalizer, click, colorama, docopt ,fastapi, greenlet, h11, idna, mysqlclient, pipreqs, pydantic,
    PyMySQL, requests, sniffio, SQLAlchemy, starlette, typing_extensions, urllib, uvicorn, wincertstore, yarg, numpy,
    pandas, chardet, pathlib, datefinder, datetime, openpyxl'.

    Librerías utilizadas para EDA(Exploratory data analysis), conexión con la base de datos en MySQL, implementación 
    de la API y conexión con Docker.

* MySQL
    MySQL es un sistema de gestión de bases de datos relacionales (RDBMS) desarrollado por Oracle que se basa en el 
    lenguaje de consulta estructurado (SQL).

* API
    La tecnología API, se trata de un conjunto de definiciones y protocolos que se utiliza para desarrollar e integrar
    el software de las aplicaciones, permitiendo la comunicación entre dos aplicaciones de software a través de un 
    conjunto de reglas.

*Docker
    Docker es una plataforma abierta para desarrollar, desplegar y ejecutar aplicaciones. Permite separar las aplicaciones
    de su infraestructura para que pueda desplegar rápidamente software en cualquier parte del mundo de una froma sencilla y eficaz 

<hr>

## Ejecución 

<p align="center">
<img src="src\assets\monkey.gif"  height=300>
</p>

*Extración de los datos*

    Los datos provistos en archivos de diferentes extensiones, como csv o json, fueron caragados en diferentes dataframes
    mediante Pandas para una mejor visualización. 

<p align="center">
<img src="src\assets\extraccion .png"  height=400>
</p>

    Se realizó un EDA para cada dataset y corrijeron los tipos de datos, valores nulos y duplicados. 
    Del analisis pertinente se obtuvo que:

    De acuero a lo solicitado, las columnas de interes son:

* platform (se va a crear esta columna)
* type (cambiar nombre a "category" para que no choque con mysql)
* duration
* listed_in(cambiar nombre a "genre")
* release_year
* cast

    Columnas que vamos a dejar para futuras consultas:

* title

    Al observar la cantidad de nulos de las siguientes columnas

* director: **35.91% nulos**
* date_added: **41.54% nulos**
* country: **50% nulos**

    Se concluye que seran eliminadas del dataframe, además las columnas siguientes se eliminaran por la falta 
    de relevancia en lo solicitado

* show_id
* rating
* description

*Tranformación de los datos*

    Se unieron los datos en un solo dataframe para facilitar el proceso de transformación de los datos.

    Se eliminaron aquellas columnas que no tenían relevancia en el estudio a realizar, los datos nulos fueron llenados
    con 'sin dato' en el caso de los datos tipo texto y en el caso de los datos numéricos se remplazó con 0.

    Se separaron en tablas independientes a los actores y el géenero de cada programa de televisión/película con el fin
    de acilitar el acceso por mySQL.

*Carga de los datos*

    En MySQL se creó una base de datos con las columnas correspondientes a cada dataframe creado

<p align="center">
<img src="src\assets\dabe de datos.png"  height=400>
</p>

*API*

El API se realizó con la librería de python Fast APi

Las consultas a realizar son:

* Máxima duración según tipo de film (película/serie), por plataforma y por año: 
El request debe ser: get_max_duration(año, plataforma, [min o season])

* Cantidad de películas y series (separado) por plataforma 
El request debe ser: get_count_plataform(plataforma)

* Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. 
El request debe ser: get_listedin('genero')
Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

* Actor que más se repite según plataforma y año. 
El request debe ser: get_actor(plataforma, año)

    El trabajo realizado lo podemos resumir a continuación

1- Se trabajó en un entorno virtual para lo cual se instala todo lo necesario para correr el API mediante un archivo .txt
2-Se utilizó un sistema de carpetas con todo lo necesario para el funcionamiento del API:  
  + **main:** archivo responsable de la creación de API. 
  + **config:** crea el engine para la conexión del API.  
  + **models:** contiene los modulos para las consultas del API, deberán ser iguales a los creados en el base de datos. 
  + **router:** aquí trabajamos en las funciones necesarias para realizar las consultas en nuestra API.

*Docker*  

Con la API lista, crearemos un archivo dockerfile contenido  en la carpeta de la API:

<code>
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
</code>

Finalmente nos posicionamosabrimos una terminal en la carpeta en la que se encuentra nuestro docker file y 
corremos las siguientes líneas de código .

<code> 
 docker build -t mycontainerfastapi .

 docker run -d --name mycontainer -p 80:80 mycontainerfastapi
 </code>

Con esto podemos verificar nuestra imagen en docker hub 

<p align="center">
<img src="src\assets\api-docker.png"  height=300>
</p>

*API corriendo en docker*

Finalmente observamos la API corriendo correctamente y haciendo las consultas pertinentes

<p align="center">
<img src="src\assets\api-docker.png"  height=200>
</p>

<hr>

## Conclusiones

* Se realizó una ingesta de datos desde diversas fuentes, posteriormente se aplicaron las transformaciones pertinentes.
* Se disponibilizó los datos limpios para su consulta a través de una API construida en un entorno virtual dockerizado.

En este arduo trabajo aprendí como extraer, limpiar y subir una base de datos para luego disponibilizar sus consultas en 
un API en un ambiente dockerizado.

Sin más que decir, te comparto un vídeo demostrativo de las consultas hechas en el API.
Link Video Demostrativo: https://youtu.be/kLck6Zn3OXg

# <h1 align=center> *`Gracias por acompañarme en este viaje a travées de mi proyecto...`* </h1>


