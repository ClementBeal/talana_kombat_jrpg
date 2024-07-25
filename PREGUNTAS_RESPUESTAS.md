# Preguntas generales

1. **Supongamos que haces un commit en un repositorio GIT y olvidas un archivo. Explica cómo lo solucionarías si ya hiciste push y cómo lo harías si aún no lo has hecho. Si es posible, que solo quede un commit con los cambios.**

En el caso de que aún no se haya hecho push del commit, es bastante sencillo si se desea modificar el último commit:

```bash
git add file_to_add && git commit --amend --no-edit
```

Este comando añadirá el archivo olvidado al último commit de la rama gracias al flag "amend". Si se quiere modificar el mensaje del commit, se elimina el flag "no-edit".

En el caso de un commit ya enviado (push), es un poco más delicado. Se puede usar el comando anterior añadiendo la orden `git push --force`. Este flag indica a Git que reemplace la rama remota con la rama local.
El problema de esta solución es que si un colaborador ya ha recuperado las modificaciones, tendrá problemas de fusión (merge). En general, muchas ramas como "master"/"main" tienen reglas para impedir el `git push --force`.

2. **Si has trabajado con control de versiones, ¿cuáles han sido los flujos de trabajo que has utilizado?**

He trabajado con diferentes flujos de trabajo.

En primer lugar, en open source en Github, cuando encuentro un error en un programa o una funcionalidad que me gustaría ver implementada, creo una nueva issue. En caso de que pueda hacerlo yo mismo, yo "fork" el repositorio, creo una nueva rama con un nombre explícito y, si es posible, con el número de la issue. Una vez escrito el código, subo mi rama y creo una "Pull Request" con un mensaje que describa el código y el trabajo realizado.

En la empresa, he trabajado con feature branches. Para cada story de un sprint, creábamos una nueva rama y, para cada tarea de la historia, creábamos una nueva rama. Una vez escrito el código, hacíamos una Pull Request y esperábamos a que uno o dos compañeros validaran el código para merge nuestra rama con la rama de funcionalidad. Una vez realizadas todas las tareas, fusionábamos la rama de funcionalidad.

En general, el flujo de trabajo siempre es el siguiente:

- fork el repositorio
- crear una nueva rama
- push el código
- hacer una Pull Request para merge las modificaciones
- esperar la validación de uno o dos colaboradores
- merge evitando los merge issues

3. **¿Cuál ha sido la situación más compleja que has tenido con el control de versiones?**

En general, la parte más complicada es la code review. Es la parte que requiere más atención porque hay que juzgar el código de otra persona y comprobar que no hay fallos. La discusión puede llevar varios días hasta ser resuelta.

4. **¿Qué experiencia has tenido con los microservicios?**

He tenido dos experiencias con los microservicios.

La primera fue en Société Générale, donde mi equipo y yo teníamos que seguir una arquitectura de microservicios con servicios escritos en Python+Flask. En ese caso, fue una mala elección. Los microservicios nos hacían perder más tiempo que otra cosa. Hacían que la arquitectura global de nuestros proyectos fuera compleja.

La segunda fue en Credit Suisse, pero esta vez me ocupaba de la parte de DevOps. Escribía los pipelines para compilar los microservicios, construir las imágenes de Docker y desplegarlas en la nube (OpenShift) usando Helm. No tenía que escribir el código de los microservicios. Esta vez, los microservicios fueron útiles porque muchos equipos trabajaban al mismo tiempo en ellos. Había un gran número de cambios cada día. Si hubiéramos tenido un servicio monolítico, seguramente habríamos tenido un servicio desplegándose continuamente.

5. **¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?**

Nunca he utilizado estos servicios en la nube. Probablemente mi servicio favorito sea AWS S3. Nunca lo he utilizado, pero he utilizado otras soluciones que reimplementaban la API de S3.

Las empresas para las que trabajaba eran bancos con su propia nube.
Podíamos desplegar directamente nuestras imágenes de Docker en el Kubernetes local. Estas infraestructuras de nube tenían sus propias soluciones para DNS, almacenamiento distribuido S3 e IAM.