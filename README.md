# EasyBroker Postulación
## Cómo instalar
El proyecto está construido en Django por lo cuál se necesita python para poder ejecutarlo, se recomienda una versión igual o superior a python3.8.10 ya que en está fue construida.

Para instalar y correr la app siga los siguientes pasos:
1. Clone este repositorio
1. Instale las dependencias con el siguiente comando (Se recomienda iniciar un entorno virtual primero):
`pip install -r ./requirements.txt`

### Correr los tests
Para correr los tests, una vez instaladas las dependencias, haga uso del siguiente comando:
`python manage.py test properties`
 Se encontrará en el proceso de ejecución con algunos mensajes tipo
 ```bash
Error code: 401
Error details: Your API key is invalid
```
Tranquilo, son solo prints que coloqué para que el desarrollador tenga retroalimentación de en que está fallando la conexión a la API

Para sabes si los tests fallaron o fueron exitosos, una vvez terminen de ejecutarse, hasta abajo aparecerá un mensaje como el siguiente:

```bash
...
----------------------------------------------------------------------
Ran 15 tests in 5.962s

OK
```
Si aparece OK quiere decir que todos los tests fueron exitosos, en caso de que aparezca FAILED significa que alguno fallo.

### Correr el servidor
Para poder visualizar la app, tenemos que correr el servidor, para ello usamos el comando
`python manage.py runserver`
Nos mostrará la ip y puerto en la que está corriendo nuestra app, generalmente es:
`http://127.0.0.1:8000/`

### Páginas de la APP
La primera página que verás será la correspondiente al listado de las propiedades publicadas, mostrará un máximo de 15 por página
[![Listado1](blob:https://correoipn-my.sharepoint.com/d9daafba-6d9a-4b97-a362-4f175c658206 "Listado1")](https://correoipn-my.sharepoint.com/personal/lmaciela1500_alumno_ipn_mx/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker%2Flista%20%5Fpropiedades%2Epng&parent=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker "Listado1")
Hasta abajo aparece la paginación para poder navegar entre ellas
[![Listado paginación](blob:https://correoipn-my.sharepoint.com/5abc345b-7be7-4dba-8a84-a97ae1605df3 "Listado paginación")](https://correoipn-my.sharepoint.com/personal/lmaciela1500_alumno_ipn_mx/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker%2Flista%20%5Fpropiedades2%2Epng&parent=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker "Listado paginación")

La siguiente página que verás será la de la propiedad cuando des click en el título de alguna
[![Propiedad](blob:https://correoipn-my.sharepoint.com/eb36a654-e480-412f-b7cb-1a03b70252e4 "Propiedad")](https://correoipn-my.sharepoint.com/personal/lmaciela1500_alumno_ipn_mx/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker%2Fpropiedad1%2Epng&parent=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker "Propiedad")
Abajo aparecerá un mapa mostrando la localización en caso de que tenga latitud y longitud
[![Propiedad mapa](blob:https://correoipn-my.sharepoint.com/016acafa-5116-4ce5-aceb-e3fcc5354334 "Propiedad mapa")](https://correoipn-my.sharepoint.com/personal/lmaciela1500_alumno_ipn_mx/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker%2Fpropiedad2%2Epng&parent=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker "Propiedad mapa")

Cuando enviemos un mensaje, si los datos no están correctos nos mostrará en que nos equivocamos sin borrar los datos anteriores
[![message error](blob:https://correoipn-my.sharepoint.com/4072cb6f-b4c8-4eba-a204-a4dcb1f88b7d "message error")](https://correoipn-my.sharepoint.com/personal/lmaciela1500_alumno_ipn_mx/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Flmaciela1500_alumno_ipn_mx%2FDocuments%2Feasybroker%2Fpropiedad3%2Epng&parent=%2Fpersonal%2Flmaciela1500_alumno_ipn_mx%2FDocuments%2Feasybroker "message error")
Si el mensaje se logra enviar nos mostrara un alert diciendonos que se ha enviado
[![message success](blob:https://correoipn-my.sharepoint.com/a43cfec8-12e4-4a8c-8378-bca27b06d76a "message success")](https://correoipn-my.sharepoint.com/personal/lmaciela1500_alumno_ipn_mx/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker%2Fpropiedad4%2Epng&parent=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker "message success")

En caso de que no se encuentre el ID de la propiedad nos mostrará un template de error
[![error page](https://correoipn-my.sharepoint.com/personal/lmaciela1500_alumno_ipn_mx/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker%2Ferror%2Epng&parent=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker "error page")](https://correoipn-my.sharepoint.com/personal/lmaciela1500_alumno_ipn_mx/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker%2Ferror%2Epng&parent=%2Fpersonal%2Flmaciela1500%5Falumno%5Fipn%5Fmx%2FDocuments%2Feasybroker "error page")

## Notas
Una de las cosas que decidí implementear fue el guardar la API KEY en un archivo .env, para que no estuvieran directamente en el código y de esta forma dar un poco más de seguridad, ya que en producción este archivo no se sube y se almacenan en las variables del sistema.
También añadí un alert al momento de que el usuario hace contacto para que sepa que sí se envío su mensaje y tenga más confianza, de igual forma, si se equivoca me pareció buena idea dejar los datos que introdujo para que no tuviera que anotar todo de nuevo y solo lo corrija.

Igual me pareció un buen toque el colocar una imagen de "Image not found" si la propiedad no cuenta con imágenes. También colocar el mapa de la ubicación de la propiedad si es que tiene siento que da más profesionalismo al sitio.

Decidí poner una página/template de error en caso de que no se encuentre la propiedad para mejorar la experiencia de usuario, esta misma página es la que funcionará como template de error para todo el sitio si meten una url incorrecta. Para verla en funcionamiento como página de error 404, en el archivo `easybroker/settings.p`y la opción `DEBUG` debe de colocarse a `DEBUG = False` y al correr el servidor debe de hacerse con el comando `python manage.py runserver --insecure`. Decidí no implementar esa configuración en el código mandado ya que es para revisión.

En cuanto al diseño del código, decidí crear la clase MyPaginator para que pudiera reutilizar el código y paginar otras secciones u otros endpoints. También creé una clase llamada MyRequest que me permite realizar requests a cualquier API y endpoint y ver si fue exitoso o no, y en caso de que no lo sea mostrar al desarrollador porque no lo fue, de esta forma el código queda más limpio ya que no escribo lo mimo para cada petición que realizo.

Otra parte donde creo el código es eficiente, es en los templates, ya que al crear los partials del form y de la paginación, los puedo incluir en cualquier otra sección que la requiere, además, todos los templates se extienden de una base que es el diseño central del sitio.

Si hubiera contado con más tiempo, me hubiera gustado implementar un botón para cambiar de propiedad sin tener que regresar al inicio, o una sección donde aparecieran ya sea propiedades relacionadas a la que el usuario está viendo o propiedades destacadas. También me hubiera gusta tener el tiempo de dockerizar la app para facilitar su despliegue e incluso subirla a algún servidor de prueba.

La parte de mi código que creo es menos entendible es la sección en la que almaceno los datos del form pasado (cuando le muestro en que se equivocó al usuario) en una cookie para mostrarselo al usuario y no tenga que escribirlo de nuevo, creo que la parte de crear y elimiar esa variable de sesión no es muy limpia ni amigable, investigando encontre que hay un framework como livewire de Laravel que se llama Unicorn pero es para Django, este te permite unicamente refrescar ciertos componentes, creo que este hubiera sido mejor opción así solo se refresca el form y evito tener que almcenar los datos de este en sesión para mantenerlos al refrescar la página.

En cuanto a lo más dificil, creo que justamente fue eso,  la parte de mantener los datos anteriores del usuario, ya que no encontraba una forma que me convenciera.

La verdad estoy contento con lo que entrego, creo que cumple con todos los requisitos e incluso algunas cosas en el diseño dan un poco más.

PD. Los archivos que considero tienen la lógica que yo construí, quitando los archivos que genera Django, son:
- properties/views.py
- properties/forms.py
- properties/mypaginator.py
- properties/tests.py
- Toda la carpeta de templates, ya que creo que la modularidad de los templates para reutilizarse y no repetir código en ellos es importante