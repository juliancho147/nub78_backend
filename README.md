# nub78_backend

Para la ejecucion del código se requiere de tener instalado docker en la maquina que se va a ejecuta

<h3>
El comando de inicio del conentenedor es:
</h3>  
  
_docker compose -f docker-compose-dev.yml up_

Una vez se descarguen todas las dependencias de el servidor y la base de datos, se puede hacer solicitudes al servidor usando el punto de enlace http://localhost:5001

Dentro del problema se encontraron tres objetos o clases que interacuntuan en el sistema, estos son susursal, elemento y tecnico, la forma en que estos interactuan se puede ver en la siguiente imagen 

<img src="https://github.com/juliancho147/nub78_backend/blob/main/diagramas/diagrama%20de%20clases.jpg?raw=true" alt="drawing" width="500"/>

Para el manejo de la base de datos se utlizo el motor MySql, dentro de esta se crearon las tablas con las llaves necesarias para el correcto funcionamiento del servidor, la informacion de la estructura se puede ver en la imagen 

<img src="https://github.com/juliancho147/nub78_backend/blob/main/diagramas/diagrama%20relacional.jpg?raw=true" alt="drawing" width="500"/>

<h3>EndPoints</h3>

Para poder editar todas las funcionalidades de los tecnicos en el sistema se crearon difenrentes rutas, las cuales son:

DELETE   /delete_tecnico

DELETE   /drop_element

POST     /get_elementos

GET      /get_sucursales

GET      /get_tecnicos

GET      /get_todos_los_elementos

POST     /insert_elemento_to_tecnico

POST     /insert_tecnico

PUT      /update_tecnico


<h3>FrontEnd</h3>

Se realizó un desarrollo en Angular para poder ver de forma mas facil el funcionamiento del sistme, para poder acceder a este se tiene que descargar el código del siguiente enlace https://github.com/juliancho147/nub78_frontend
