# <h1 style="text-align:center;font-weight:bold;">PROYECTO-BLOG-CODERHOUSE</h1>
---
### <h1 style="font-weight:bold;">Acerca del Blog</h1>

<p style="font-size:17px; font-weight:bold">
El proyecto trata de un blog dedicado a recomendaciones y experiencias sobre videojuegos y juegos que estan de moda.<br/>
Los usuarios podrán observar la lista de los juegos y un blog con publicaciones acerca de que juegos han jugado y como les parecio.<br/>
Cada POST consta de un título, contenido, autor y fecha de publicación (que se agrega automáticamente).
<br/>
Los posts se listan del más reciente al más antiguo.<br/>
Los datos se guardan en una base de datos de motor SQLite ya provisto por Django.<br/>
El usuario puede publicar un POST sobre como fue su experiencia con un videojuego.<br/>
En la parte de Games Solo pueden subir juegos los ADMIN
</p>
<h1 style="font-weight:bold;">Loyout</h1>
<p style="font-size:17px; font-weight:bold">
El blog cuenta con una barra de navegación a la cual se puede acceder a las distintas secciones del mismo. (Home, Blog,Games ,Crear Blog , About).
</p>

---

## <h1 style="text-align:center; text-transform:uppercase; font-weight:bold;">Instrucciones de uso</h1>

Recomendacion: Generar un entorno virtual

1.  Clonar el proyecto o descargar el archivo comprimido.

2.  Instalar las dependencias del proyecto:  
    +  ***Automaticamente:***
        -    *pip install -r requirements.txt*

3. Realizar las migraciones para generar la bd
    -    ***python manage.py makemigrations***
    -    ***python manage.py migrate***

4. Correr la aplicacion
    -    ***python manage.py runserver***

5. Ya puedes ingresar a web
    -    [http://localhost:8000/](http://localhost:8000/)
    *puedes especificar el puerto que prefieras utilizar, por defecto es el puerto 8000*

***