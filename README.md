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

