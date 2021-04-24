# Prueba Monoku

En las siguientes secciones se detalla los diferentes aspectos a seguir para la ejecución de la aplicación

##Instalación
Luego de descargar el repositorio, se debe de crear un entorno virtual con la siguiente instrucción usando virtualenv:

```bash
virtualenv env
```

En caso de que use Windows como SO, activar el ambiente con el siguiente comando:

```bash
\\env\\Scripts\\activate
```

Luego de activado el ambiente, se procede a instalar las dependencias con el comando:

```bash
pip install -r requirements.txt
```

#Ejecución

Para ejecutar django, ubiquese dentro de la carpeta llamada 'pruebaMonoku' y luego debe de utilizar el siguiente comando:

```bash
python manage.py runserver
```

#Cargar Datos

Ubíquese en la carpeta raíz del repositorio y ejecute el siguiente comando :

```bash
loadData.py
```