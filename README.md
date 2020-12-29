# CRUD-Django

## Requisitos:
  - Instalar python:
  
    https://www.python.org/downloads/
  
  - Instalar Django: 
    
  En la teminal de comandos de windows:
    
    pip install Django==3.1.1
   
  - Instalar modulo de postgreSQL:
  
  En la terminal de comandos de windows:
    
    pip install psycopg2
   
  - Descargar e instalar postgresql:
  
    https://www.postgresql.org/
      
## Crear proyecto Django:
  
  #### 1.Creamos proyecto:
  
   En la terminal de comandos de windows:
  
    django-admin startproject crud_django
    
   #### 2.Crear primer app:
   
   En la terminal de comandos de windows:
    
    python manage.py startapp gestionRecursos
    
   #### 3.Editamos el archivo settings.py:
   
   Una vez creada la aplicacion, debemos registrarla para ello
   
   editamos la lista INTALLED_APPS, le agregamos el nuevo app creado.
   
   ```python
    INSTALLED_APPS = ['....',
                      '....',
                      'gestionRecursos']
   ```
    
   #### 4.Creamos el modelo o la tabla de la BBDD:
   
   Dentro de la carpeta gestionRecursos encontramos el archivo models.py
   
   ```python
      from django.db import models

      class Menus(models.Model):
          entrada = models.CharField(max_length=40)
          fondo = models.CharField(max_length=40)
          postre = models.CharField(max_length=40)
          precio = models.FloatField()
   ```
   
   
   #### 5.Creamos la base de datos en el servicio de PostgreSQL instalado en el sistema
   
   
   ```sql
    create database menusclientes
   ```
   
   #### 6.Editar el archivo settings.py:
   
   Editamos el diccionario DATABASES.
   
   ``` python
        
        DATABASES={
          "default":{
            'ENGINE':'django.db.backends.postgresql_psycopg2',
            'NAME':'insert the name', #Nombre de BBDD
            'USER':'postgres',
            'PASSWORD':'insert the password',
            'HOST':'insert the host',
            'DATABASE_PORT':5432 #Es el puerto por defecto cuando instalamos postgresql
          }
        }
    
   ```
   
   #### 7.Generamos las migraciones de la BBDD:
   
   En la teminal de comandos de windows:
    
   ```
    python manage.py makemigrations
   ```
   ```
    python manage.py migrate
   ```
   
   #### 8.Creamos las vistas, los templates configuramos las URLS para cada vista:
   
   - Dentro de la carpeta gestionsRecursos, creamos una carpeta templates.
   
   - En el caso de no estar el archivos views.py dentro de la carpeta gestionRecursos,
    
      la creamos en ella estarán todos las vistas, en otras palabras se definirán lo que se 
      
      hará en cada peticion http que solicitemos.
      
   - Por cada vista creada se definirá la url en el archivo urls.py:
   
     ```python
        from grstionRecursos.views import menus
        urlpatterns = [
            path('menu/',menus),
        ]
        
      ```
      
   
