# # Conceptos GIT y GitHub y comandos GIT Bash # #

## ID: Federico Iacono


# ¿Qué es GitHub?

# GitHub es una plataforma de desarrollo colaborativo para alojar proyectos utilizando el sistema de control de versiones 1  Git. Permite a múltiples personas trabajar en un mismo proyecto de forma simultánea, facilitando la colaboración y el seguimiento de los cambios.


# ¿Cómo crear un repositorio en GitHub?

# Inicia sesión en GitHub: Si no hay una cuenta, crear una.
# Clic en "New repository"
# Elegir un nombre para el repositorio: Descriptivo y único.
# Añadir una descripción
# Seleccionar la visibilidad: Público o privado


# ¿Cómo crear una rama en Git?

# En la terminal Bash
# git branch <nombre-de-la-rama>


# ¿Cómo cambiar a una rama en Git?

# git checkout <nombre-de-la-rama>


# ¿Cómo fusionar ramas en Git?

# git checkout <rama-principal>


# Fusiona la otra rama:

# git merge <rama-a-fusionar>


# ¿Cómo crear un commit en Git?

# Añade los cambios al área de preparación:
# git add . 

# Crea el commit con un mensaje descriptivo:
# git commit -m "Mensaje del commit"


# ¿Cómo enviar un commit a GitHub?

# Añadir el repositorio remoto (si no se ha hecho):
# git remote add origin <URL-del-repositorio-remoto>

# Envía los commits a la rama remota:
# git push origin <nombre-de-la-rama>


# ¿Qué es un repositorio remoto?

# Un repositorio remoto es una versión del repositorio que se encuentra alojada en un servidor, como GitHub. Permite la colaboración entre múltiples personas y sirve como copia de seguridad del proyecto.


# ¿Cómo agregar un repositorio remoto a Git?

# git remote add origin <URL-del-repositorio-remoto>


# ¿Cómo empujar cambios a un repositorio remoto?

# git push origin <nombre-de-la-rama>


# ¿Cómo tirar de cambios de un repositorio remoto?

# git pull origin <nombre-de-la-rama>


# ¿Qué es un fork de repositorio?

# Un fork es una copia de un repositorio que se crea en tu propia cuenta de GitHub. Te permite modificar el código original sin afectar al repositorio original.


# ¿Cómo crear un fork de un repositorio?

# Ir al repositorio que se quiere forkar.
# Clic en el botón "Fork" que se encuentra en la esquina superior derecha de la página.
# Seleccionar la cuenta de GitHub donde  crear el fork.


# ¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?

# Haz un fork del repositorio: Si no tienes permisos de escritura en el repositorio original.
# Crea una rama con tus cambios: En tu fork o en tu repositorio local.
# Sube tus cambios a tu repositorio remoto: git push origin <nombre-de-la-rama>.
# Ve al repositorio original en GitHub: Y haz clic en "New pull request".
# Compara las ramas: Selecciona la rama de tu repositorio con los cambios y la rama del repositorio original donde quieres fusionarlos.
# Añade un título y una descripción
# Haz clic en "Create pull request"


# ¿Cómo aceptar una solicitud de extracción?

# Ve a la solicitud de extracción: En el repositorio original
# Revisa los cambios: Comprueba que todo esté correcto
# Aprueba la solicitud (opcional): Si eres el propietario del repositorio
# Haz clic en "Merge pull request": Para fusionar los cambios
# Confirma la fusión: Y borra la rama (opcional)


# ¿Qué es una etiqueta en Git?

# Una etiqueta (tag) en Git es un puntero estático a un commit específico. Se utiliza para marcar puntos importantes en la historia del proyecto, como versiones publicadas.


# ¿Cómo crear una etiqueta en Git?

# Cambia al commit donde quieres crear la etiqueta:
# git checkout <commit-hash>

# Crea la etiqueta:
# git tag -a <nombre-de-la-etiqueta> -m "Mensaje de la etiqueta"


# ¿Cómo enviar una etiqueta a GitHub?

# git push origin <nombre-de-la-etiqueta>


# ¿Qué es un historial de Git?

# El historial de Git es un registro de todos los commits realizados en un repositorio. Muestra quién hizo los cambios, cuándo y qué cambios se realizaron.


# ¿Cómo ver el historial de Git?

# git log


# ¿Cómo buscar en el historial de Git?

# git log --grep="palabra-clave"


# ¿Cómo borrar el historial de Git?

# Borrar el historial de Git es una operación peligrosa y generalmente no se recomienda. Si realmente necesitas hacerlo, puedes usar git reset --hard <commit-hash>


# ¿Qué es un repositorio privado en GitHub?

# Un repositorio privado es un repositorio que solo es visible para las personas a las que les has dado acceso.


# ¿Cómo crear un repositorio privado en GitHub?

# Sigue los mismos pasos que para crear un repositorio público.
# Selecciona la opción "Private" en la configuración de visibilidad.


# ¿Cómo invitar a alguien a un repositorio privado en GitHub?

# Ve a la página de configuración del repositorio
# Haz clic en "Manage access" y luego en "Invite a collaborator"
# Introduce el nombre de usuario o el correo electrónico de la persona
# Elige los permisos (lectura, escritura o administración)
# Haz clic en "Add collaborator"


# ¿Qué es un repositorio público en GitHub?

# Un repositorio público es un repositorio que es visible para todo el mundo en GitHub.


# ¿Cómo crear un repositorio público en GitHub?

# Sigue los mismos pasos que para crear un repositorio privado.
# Selecciona la opción "Public" en la configuración de visibilidad.


# ¿Cómo compartir un repositorio público en GitHub?

# Copia la URL del repositorio: De la barra de direcciones del navegador.
# Comparte la URL

# -------------------------