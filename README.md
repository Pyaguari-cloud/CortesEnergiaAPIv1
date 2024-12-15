# API CortesEnergia

# Nota: es necesario tener instalado python 3.10.5 para un correcto funcionamiento de la API

pasos parar usar la Api:

1. Descargar o clonar el proyecto
2. Abrir la carpeta contenedora dentro del editor de codigo, seguido a esto creamos un entorno virtual el cual una vez creado se tiene que activar escribiendo en la consola del editor de codigo o cmd el comando " env/Scripts/active "
3. Ahora se instalan la libreria que necesita el proyecto escribiendo en el comando " pip install -r requirements.txt "
4. Entramos en la carpeta del Proyecto llamada "CortesEnergia", se abre el archivo settings.py y bajamos hasta encontrar el objeto DATABASES el cual esta de esta manera:
```bash
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cortesenergia_db',
        'USER': 'postgres',
        'PASSWORD': '240242',
        'HOST': 'localhost',
        'PORT': '5432',                                     
    }
}
```
puede modificar los atributos del objeto segun sus necesidades o segun su base de datos en PostgreSQL
5. Levantamos el proyecto con el comando " py manage.py runserver ", bajamos el servidor con Ctrl+c, se escribe el comando " py manage.py migrate " y se crearan las tablas en la base de datos
