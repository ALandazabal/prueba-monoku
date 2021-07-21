# Prueba Monoku
En las siguientes secciones se detalla los diferentes aspectos a seguir para la ejecución de la aplicación.  Se informa que el siguiente proyecto está realizado sobre el sistema operativo(SO) **Windows 10**.

## Requerimientos
* Python 3.7
* PIP -> Para instalarlo puede seguir las instrucciones del siguiente link <https://pip.pypa.io/en/stable/installing/>
* PostgreSQL -> Puede seguir los pasos de instalación en el siguiente blog <https://paggyru.medium.com/install-postgresql-12-on-windows-10-for-beginners-5e8fce387dc7>
* virtualenv -> Luego de tener **pip** en su máquina, puede usar el siguiente comando para instalarlo:
```bash
pip install virtualenv
```


## Instalación
Luego de descargar el repositorio, se debe de crear un entorno virtual y la base de datos en la que correra el proyecto:

### Entorno virtual
Para crear el entorno virtual, se procede con el siguiente comando:

```bash
virtualenv env
```

Con el SO Windows, se activa el ambiente con el comando:

```bash
\env\Scripts\activate
```

Luego de activado el ambiente, se procede a instalar las dependencias:

```bash
pip install -r requirements.txt
```

### Base de datos (DB)
Luego de tener Postgres en su máquina siga los siguientes pasos:
* Cree una nueva DB.
* Obtenga los datos de conexión como el host, puerto, nombre de la DB, usuario y contraseña.
* En la carpeta raíz del proyecto, modifique el nombre del archivo **configExample.py** a **config.py**.
* Dentro del archivo **config.py**, coloque los datos de conexión correspondientes que allí se le solicitan.
* Guarde los cambios.

## Ejecución
Para ejecutar django, ubiquese dentro de la carpeta llamada **pruebaMonoku** y luego debe de ejecutar los comandos de los siguientes pasos:

* Verifique que todas las migraciones estén creadas en el proyecto:
```bash
python manage.py makemigrations
```
* Aplique las migraciones relacionadas al proyecto
```bash
python manage.py migrate
```
* Sí los pasos anteriores fueron ejecutados con éxito, corra la aplicación con:
```bash
python manage.py runserver
```

## Cargar Datos
Ubíquese en la carpeta raíz del repositorio y ejecute el siguiente comando :
```bash
loadData.py
```

## Guía de estilos 
Si deseas comprobar la guía de estilos utilizada en el código, ejecuta el siguiente comando:
```bash
flake8
```
Flake8 es una herramienta diseñada para la aplicación de la guía de estilos. Muestra por consola las advertencias de la falta estilos regido por PEP8 contra tú código. Sí deseas conocer más, te puedes guiar por su documentación <https://flake8.pycqa.org/en/latest/>